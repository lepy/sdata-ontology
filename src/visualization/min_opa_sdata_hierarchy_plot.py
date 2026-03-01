"""Create a class hierarchy plot spanning MIN -> OPA -> sdata-core."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL

MIN_PREFIX = "https://w3id.org/min"
OPA_PREFIX = "https://w3id.org/opa"
SDATA_CORE_PREFIX = "https://w3id.org/sdata/core/"


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "min" | "opa" | "sdata"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def _kind_from_iri(iri: URIRef) -> str | None:
    text = str(iri)
    if text.startswith(MIN_PREFIX):
        return "min"
    if text.startswith(OPA_PREFIX):
        return "opa"
    if text.startswith(SDATA_CORE_PREFIX):
        return "sdata"
    return None


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels = list(graph.objects(iri, RDFS.label))
    if not labels:
        text = str(iri)
        if "#" in text:
            return text.rsplit("#", 1)[1]
        return text.rsplit("/", 1)[-1]

    def score(label: Literal) -> tuple[int, str]:
        lang = (label.language or "").lower()
        if lang == "en":
            rank = 0
        elif not lang:
            rank = 1
        else:
            rank = 2
        return (rank, str(label))

    return str(sorted(labels, key=score)[0])


def _classes_from(graph: Graph) -> set[URIRef]:
    return {
        cls
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and _kind_from_iri(cls) is not None
    }


def load_graphs(min_path: Path, opa_path: Path, core_path: Path) -> tuple[Graph, Graph, Graph, Graph]:
    for path, label in ((min_path, "MIN ontology"), (opa_path, "OPA ontology"), (core_path, "sdata-core ontology")):
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {path}")

    min_graph = Graph()
    min_graph.parse(min_path, format="turtle")

    opa_graph = Graph()
    opa_graph.parse(opa_path, format="turtle")

    core_graph = Graph()
    core_graph.parse(core_path, format="turtle")

    merged = Graph()
    merged += min_graph
    merged += opa_graph
    merged += core_graph

    return min_graph, opa_graph, core_graph, merged


def extract_model(min_graph: Graph, opa_graph: Graph, core_graph: Graph, merged: Graph) -> Model:
    min_classes = _classes_from(min_graph)
    opa_classes = _classes_from(opa_graph)
    core_classes = _classes_from(core_graph)
    all_classes = min_classes | opa_classes | core_classes

    nodes = tuple(
        sorted(
            (
                Node(iri=cls, label=_best_label(merged, cls), kind=kind)
                for cls in all_classes
                for kind in [_kind_from_iri(cls)]
                if kind is not None
            ),
            key=lambda n: (n.kind, str(n.iri)),
        )
    )

    edges: set[Edge] = set()
    for child in all_classes:
        for parent in merged.objects(child, RDFS.subClassOf):
            if isinstance(parent, URIRef) and parent in all_classes:
                edges.add(Edge(parent=parent, child=child))

    return Model(nodes=nodes, edges=tuple(sorted(edges, key=lambda e: (str(e.parent), str(e.child)))))


def build_agraph(model: Model):
    try:
        import pygraphviz as pgv
    except ImportError as exc:
        raise RuntimeError(
            "pygraphviz is required to render diagrams. Install dev dependencies first."
        ) from exc

    graph = pgv.AGraph(strict=False, directed=True)
    graph.graph_attr.update(
        bgcolor="#FAFBFC",
        rankdir="TB",
        newrank="true",
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.55",
        fontname="Helvetica",
        fontsize="20",
        label="Class Hierarchy: MIN -> OPA -> sdata-core",
        labelloc="t",
        labeljust="c",
    )
    graph.node_attr.update(
        shape="box",
        style="filled,rounded",
        fontname="Helvetica",
        fontsize="12",
        penwidth="1.6",
        margin="0.14,0.08",
    )
    graph.edge_attr.update(
        color="#4A5568",
        penwidth="1.6",
        arrowsize="0.85",
        fontname="Helvetica",
    )

    min_cluster = graph.add_subgraph(name="cluster_min", label="MIN classes", color="#8FB7EA", style="rounded")
    opa_cluster = graph.add_subgraph(name="cluster_opa", label="OPA classes", color="#97D5BA", style="rounded")
    sdata_cluster = graph.add_subgraph(
        name="cluster_sdata", label="sdata-core classes", color="#D9B8F7", style="rounded"
    )

    style_map = {
        "min": {"fillcolor": "#E7F0FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "opa": {"fillcolor": "#E8FFF4", "color": "#2F855A", "fontcolor": "#1C4532"},
        "sdata": {"fillcolor": "#F8EEFF", "color": "#6B46C1", "fontcolor": "#44337A"},
    }

    for node in model.nodes:
        target = min_cluster if node.kind == "min" else opa_cluster if node.kind == "opa" else sdata_cluster
        target.add_node(str(node.iri), label=node.label, **style_map[node.kind])

    for edge in model.edges:
        graph.add_edge(str(edge.parent), str(edge.child), label="")

    ordered_min = sorted(str(node.iri) for node in model.nodes if node.kind == "min")
    ordered_opa = sorted(str(node.iri) for node in model.nodes if node.kind == "opa")
    ordered_sdata = sorted(str(node.iri) for node in model.nodes if node.kind == "sdata")
    if ordered_min and ordered_opa:
        graph.add_edge(ordered_min[0], ordered_opa[0], style="invis", color="#FFFFFF", weight="100")
    if ordered_opa and ordered_sdata:
        graph.add_edge(ordered_opa[0], ordered_sdata[0], style="invis", color="#FFFFFF", weight="100")

    return graph


def render(
    graph, out_svg: Path | None, out_png: Path | None, out_dot: Path | None, layout: str, dpi: int
) -> None:
    if out_dot:
        graph.write(out_dot)
    if out_svg:
        graph.draw(out_svg, format="svg", prog=layout)
    if out_png:
        graph.draw(out_png, format="png", prog=layout, args=f"-Gdpi={dpi}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min", dest="min_path", type=Path, default=Path("min-v1.0.0.ttl"))
    parser.add_argument("--opa", dest="opa_path", type=Path, default=Path("opa-v1.0.0.ttl"))
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-min-opa-core-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        min_g, opa_g, core_g, merged_g = load_graphs(args.min_path, args.opa_path, args.core)
        model = extract_model(min_g, opa_g, core_g, merged_g)
        if not model.nodes:
            print("No nodes found for visualization.", file=sys.stderr)
            return 4
        agraph = build_agraph(model)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_dot = args.out_dir / f"{args.name}.dot"
    out_svg = args.out_dir / f"{args.name}.svg" if args.format in ("svg", "both") else None
    out_png = args.out_dir / f"{args.name}.png" if args.format in ("png", "both") else None
    render(agraph, out_svg, out_png, out_dot, layout=args.layout, dpi=args.dpi)

    print(f"Generated {out_dot}")
    if out_svg:
        print(f"Generated {out_svg}")
    if out_png:
        print(f"Generated {out_png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

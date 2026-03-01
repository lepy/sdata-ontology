"""Create a styled class hierarchy plot from sdata-core Turtle files."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL

SDATA = Namespace("https://w3id.org/sdata/core/")


@dataclass(frozen=True)
class HierarchyNode:
    iri: URIRef
    label: str
    kind: str  # "sdata"


@dataclass(frozen=True)
class HierarchyEdge:
    child: URIRef
    parent: URIRef


@dataclass(frozen=True)
class HierarchyModel:
    nodes: tuple[HierarchyNode, ...]
    edges: tuple[HierarchyEdge, ...]


def load_graph(core_path: Path, alignment_path: Path | None = None) -> Graph:
    """Load core ontology and an optional overlay module into one RDF graph."""
    if not core_path.exists():
        raise FileNotFoundError(f"Core ontology not found: {core_path}")

    graph = Graph()
    graph.parse(core_path, format="turtle")
    if alignment_path:
        if not alignment_path.exists():
            raise FileNotFoundError(f"Alignment ontology not found: {alignment_path}")
        graph.parse(alignment_path, format="turtle")
    return graph


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


def extract_hierarchy(graph: Graph) -> HierarchyModel:
    """Extract sdata class hierarchy from asserted subclass relations."""
    sdata_classes = {
        cls
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and str(cls).startswith(str(SDATA))
    }

    edges: set[HierarchyEdge] = set()
    for child in sdata_classes:
        for parent in graph.objects(child, RDFS.subClassOf):
            if isinstance(parent, URIRef) and parent in sdata_classes:
                edges.add(HierarchyEdge(child=child, parent=parent))

    nodes = tuple(
        HierarchyNode(iri=cls, label=_best_label(graph, cls), kind="sdata")
        for cls in sorted(sdata_classes, key=str)
    )

    return HierarchyModel(
        nodes=nodes,
        edges=tuple(sorted(edges, key=lambda e: (str(e.child), str(e.parent)))),
    )


def build_agraph(model: HierarchyModel):
    """Build styled PyGraphviz graph from model."""
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
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.55",
        fontname="Helvetica",
        fontsize="20",
        label="sdata Class Hierarchy (core v0.8.0 / MIN+OPA based)",
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

    sdata_cluster = graph.add_subgraph(
        name="cluster_sdata", label="sdata classes", color="#90B5E8", style="rounded"
    )

    style = {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"}
    for node in model.nodes:
        sdata_cluster.add_node(str(node.iri), label=node.label, **style)

    for edge in model.edges:
        graph.add_edge(str(edge.parent), str(edge.child), label="")

    legend = graph.add_subgraph(name="cluster_legend", label="Legend", color="#CBD5E0", style="rounded")
    legend.add_node(
        "legend_sdata",
        label="sdata class",
        fillcolor="#E8F1FF",
        color="#2B6CB0",
        fontcolor="#1A365D",
    )
    legend.add_edge("legend_sdata", "legend_sdata", label="superclass -> subclass", color="#4A5568")

    return graph


def render(
    graph, out_svg: Path | None, out_png: Path | None, out_dot: Path | None, layout: str, dpi: int
) -> None:
    """Render graph as DOT and optional SVG/PNG."""
    if out_dot:
        graph.write(out_dot)
    if out_svg:
        graph.draw(out_svg, format="svg", prog=layout)
    if out_png:
        graph.draw(out_png, format="png", prog=layout, args=f"-Gdpi={dpi}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--alignment", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-class-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.core, args.alignment)
        model = extract_hierarchy(graph)
        if not model.nodes:
            print("No classes found for visualization.", file=sys.stderr)
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

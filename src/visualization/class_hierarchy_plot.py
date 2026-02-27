"""Create a styled class hierarchy plot from ontology Turtle files."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL

SDATA = Namespace("https://w3id.org/sdata/core#")
BFO_PREFIX = "http://purl.obolibrary.org/obo/BFO_"


@dataclass(frozen=True)
class HierarchyNode:
    iri: URIRef
    label: str
    kind: str  # "sdata" or "bfo"


@dataclass(frozen=True)
class HierarchyEdge:
    child: URIRef
    parent: URIRef


@dataclass(frozen=True)
class HierarchyModel:
    nodes: tuple[HierarchyNode, ...]
    edges: tuple[HierarchyEdge, ...]


def load_graph(core_path: Path, vendor_paths: Iterable[Path]) -> Graph:
    """Load core ontology and selected vendor ontologies into one RDF graph."""
    if not core_path.exists():
        raise FileNotFoundError(f"Core ontology not found: {core_path}")

    graph = Graph()
    graph.parse(core_path, format="turtle")
    for path in vendor_paths:
        if path.exists():
            graph.parse(path, format="turtle")
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
    """Extract sdata classes plus direct BFO parents from graph."""
    sdata_classes = {
        cls
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and str(cls).startswith(str(SDATA))
    }

    bfo_classes: set[URIRef] = set()
    edges: set[HierarchyEdge] = set()

    for child in sdata_classes:
        for parent in graph.objects(child, RDFS.subClassOf):
            if not isinstance(parent, URIRef):
                continue
            parent_str = str(parent)
            if parent in sdata_classes:
                edges.add(HierarchyEdge(child=child, parent=parent))
            elif parent_str.startswith(BFO_PREFIX):
                bfo_classes.add(parent)
                edges.add(HierarchyEdge(child=child, parent=parent))

    nodes: list[HierarchyNode] = []
    for cls in sorted(sdata_classes, key=str):
        nodes.append(HierarchyNode(iri=cls, label=_best_label(graph, cls), kind="sdata"))
    for cls in sorted(bfo_classes, key=str):
        nodes.append(HierarchyNode(iri=cls, label=_best_label(graph, cls), kind="bfo"))

    return HierarchyModel(
        nodes=tuple(nodes),
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
        label="sdata Class Hierarchy (with direct BFO parents)",
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
    bfo_cluster = graph.add_subgraph(
        name="cluster_bfo_context", label="BFO context", color="#F3C887", style="rounded"
    )

    style_map = {
        "sdata": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "bfo": {"fillcolor": "#FFF4E5", "color": "#B7791F", "fontcolor": "#7B341E"},
    }

    for node in model.nodes:
        attrs = style_map[node.kind]
        target = sdata_cluster if node.kind == "sdata" else bfo_cluster
        target.add_node(str(node.iri), label=node.label, **attrs)

    for edge in model.edges:
        graph.add_edge(str(edge.child), str(edge.parent), label="")

    legend = graph.add_subgraph(name="cluster_legend", label="Legend", color="#CBD5E0", style="rounded")
    legend.add_node(
        "legend_sdata",
        label="sdata class",
        fillcolor="#E8F1FF",
        color="#2B6CB0",
        fontcolor="#1A365D",
    )
    legend.add_node(
        "legend_bfo",
        label="BFO parent",
        fillcolor="#FFF4E5",
        color="#B7791F",
        fontcolor="#7B341E",
    )
    legend.add_edge("legend_sdata", "legend_bfo", label="rdfs:subClassOf", color="#4A5568")

    return graph


def render(graph, out_svg: Path | None, out_png: Path | None, layout: str, dpi: int) -> None:
    """Render graph as SVG and/or PNG."""
    graph.layout(prog=layout)
    if out_svg:
        graph.draw(out_svg, format="svg")
    if out_png:
        graph.draw(out_png, format="png", args=f"-Gdpi={dpi}")


def _default_vendor_files(vendor_dir: Path) -> list[Path]:
    return [
        vendor_dir / "bfo.ttl",
        vendor_dir / "prov-o.ttl",
        vendor_dir / "qudt.ttl",
        vendor_dir / "dtype.ttl",
        vendor_dir / "vaem.ttl",
        vendor_dir / "skos.ttl",
    ]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--vendor-dir", type=Path, default=Path("vendor/ontologies"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-class-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    # Vendor ontologies may contain malformed rdf:HTML literals; keep output clean.
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])
    vendor_paths = _default_vendor_files(args.vendor_dir)

    try:
        graph = load_graph(args.core, vendor_paths)
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
    out_svg = args.out_dir / f"{args.name}.svg" if args.format in ("svg", "both") else None
    out_png = args.out_dir / f"{args.name}.png" if args.format in ("png", "both") else None
    render(agraph, out_svg, out_png, layout=args.layout, dpi=args.dpi)

    if out_svg:
        print(f"Generated {out_svg}")
    if out_png:
        print(f"Generated {out_png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

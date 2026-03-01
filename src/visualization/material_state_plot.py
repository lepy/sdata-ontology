"""Create a hierarchy plot for the sdata-material-state extension ontology."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

SMS = Namespace("https://w3id.org/sdata/material-state/")


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "axis" | "scheme" | "concept"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef
    kind: str  # "subclass" | "scheme" | "top" | "broader"


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def load_graph(state_path: Path) -> Graph:
    if not state_path.exists():
        raise FileNotFoundError(f"Material-state ontology not found: {state_path}")
    graph = Graph()
    graph.parse(state_path, format="turtle")
    return graph


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels = list(graph.objects(iri, RDFS.label)) + list(graph.objects(iri, SKOS.prefLabel))
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


def _is_sms_uri(iri: URIRef) -> bool:
    return str(iri).startswith(str(SMS))


def extract_model(graph: Graph) -> Model:
    nodes: dict[URIRef, str] = {}
    edges: set[Edge] = set()

    state_axis = SMS.StateAxis
    if (state_axis, RDF.type, OWL.Class) in graph:
        nodes[state_axis] = "axis"

    axes = {
        cls
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and _is_sms_uri(cls) and cls != state_axis
    }
    for axis in axes:
        nodes[axis] = "axis"
        if (axis, RDFS.subClassOf, state_axis) in graph and state_axis in nodes:
            edges.add(Edge(parent=state_axis, child=axis, kind="subclass"))

    schemes = {
        scheme
        for scheme in graph.subjects(RDF.type, SKOS.ConceptScheme)
        if isinstance(scheme, URIRef) and _is_sms_uri(scheme)
    }
    for scheme in schemes:
        nodes[scheme] = "scheme"

    for axis in {state_axis} | axes:
        for scheme in graph.objects(axis, SMS.hasConceptScheme):
            if isinstance(scheme, URIRef) and scheme in schemes:
                edges.add(Edge(parent=axis, child=scheme, kind="scheme"))

    concepts: set[URIRef] = set()
    for scheme in schemes:
        scheme_concepts = {
            concept
            for concept in graph.subjects(SKOS.inScheme, scheme)
            if isinstance(concept, URIRef) and _is_sms_uri(concept)
        }
        concepts |= scheme_concepts

    for concept in concepts:
        nodes[concept] = "concept"

    for scheme in schemes:
        for concept in graph.objects(scheme, SKOS.hasTopConcept):
            if isinstance(concept, URIRef) and concept in concepts:
                edges.add(Edge(parent=scheme, child=concept, kind="top"))

    for concept in concepts:
        for parent in graph.objects(concept, SKOS.broader):
            if isinstance(parent, URIRef) and parent in concepts:
                edges.add(Edge(parent=parent, child=concept, kind="broader"))

    return Model(
        nodes=tuple(
            Node(iri=iri, label=_best_label(graph, iri), kind=kind)
            for iri, kind in sorted(nodes.items(), key=lambda item: str(item[0]))
        ),
        edges=tuple(sorted(edges, key=lambda e: (str(e.parent), str(e.child), e.kind))),
    )


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
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.55",
        fontname="Helvetica",
        fontsize="20",
        label="sdata Material State Space",
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
        penwidth="1.5",
        arrowsize="0.8",
        fontname="Helvetica",
        fontsize="10",
    )

    axis_cluster = graph.add_subgraph(
        name="cluster_sms_axes", label="state axes", color="#90B5E8", style="rounded"
    )
    scheme_cluster = graph.add_subgraph(
        name="cluster_sms_schemes", label="concept schemes", color="#9AD9BF", style="rounded"
    )
    concept_cluster = graph.add_subgraph(
        name="cluster_sms_concepts", label="state values (SKOS concepts)", color="#D6BCFA", style="rounded"
    )

    style_map = {
        "axis": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "scheme": {"fillcolor": "#E7FFF6", "color": "#2F855A", "fontcolor": "#1C4532"},
        "concept": {"fillcolor": "#F7EEFF", "color": "#6B46C1", "fontcolor": "#44337A"},
    }

    for node in model.nodes:
        target = axis_cluster if node.kind == "axis" else scheme_cluster if node.kind == "scheme" else concept_cluster
        target.add_node(str(node.iri), label=node.label, **style_map[node.kind])

    for edge in model.edges:
        attrs = {"label": ""}
        if edge.kind == "scheme":
            attrs.update({"style": "dashed", "color": "#2B6CB0", "label": "hasConceptScheme"})
        elif edge.kind == "top":
            attrs.update({"style": "dotted", "color": "#2F855A", "label": "top concept"})
        elif edge.kind == "broader":
            attrs.update({"style": "solid", "color": "#6B46C1", "label": "broader"})
        graph.add_edge(str(edge.parent), str(edge.child), **attrs)

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
    parser.add_argument("--material-state", type=Path, default=Path("sdata-material-state.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-material-state")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.material_state)
        model = extract_model(graph)
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

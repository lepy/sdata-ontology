"""Create a styled R-strategies plot from sdata-r-strategies.ttl."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import SKOS

SDATA = Namespace("https://w3id.org/sdata/core/")
SR = Namespace("https://w3id.org/sdata/r-strategies/")

MAPS_TO_VERB = SR.mapsToVerb
CIRCULARITY_RANK = SR.circularityRank


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "scheme" | "collection" | "concept" | "verb"


@dataclass(frozen=True)
class Edge:
    source: URIRef
    target: URIRef
    label: str
    kind: str  # "top" | "member" | "maps"


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def load_graph(strategies_path: Path) -> Graph:
    if not strategies_path.exists():
        raise FileNotFoundError(f"R-strategies ontology not found: {strategies_path}")
    graph = Graph()
    graph.parse(strategies_path, format="turtle")
    return graph


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels = list(graph.objects(iri, SKOS.prefLabel)) + list(graph.objects(iri, RDFS.label))
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


def extract_model(graph: Graph) -> Model:
    nodes: dict[URIRef, Node] = {}
    edges: set[Edge] = set()

    schemes = [
        s
        for s in graph.subjects(RDF.type, SKOS.ConceptScheme)
        if isinstance(s, URIRef) and str(s).startswith(str(SR))
    ]
    if not schemes:
        # fallback to known default
        schemes = [SR.RStrategyScheme]

    for scheme in schemes:
        nodes[scheme] = Node(iri=scheme, label=_best_label(graph, scheme), kind="scheme")

        top_concepts = [
            c for c in graph.objects(scheme, SKOS.hasTopConcept) if isinstance(c, URIRef)
        ]
        for concept in top_concepts:
            rank_values = [o for o in graph.objects(concept, CIRCULARITY_RANK) if isinstance(o, Literal)]
            rank_suffix = ""
            if rank_values:
                rank_suffix = f" [rank {rank_values[0]}]"
            label = f"{_best_label(graph, concept)}{rank_suffix}"
            nodes[concept] = Node(iri=concept, label=label, kind="concept")
            edges.add(Edge(source=scheme, target=concept, label="top concept", kind="top"))

    collections = [
        c
        for c in graph.subjects(RDF.type, SKOS.Collection)
        if isinstance(c, URIRef) and str(c).startswith(str(SR))
    ]
    for coll in collections:
        nodes[coll] = Node(iri=coll, label=_best_label(graph, coll), kind="collection")
        for member in graph.objects(coll, SKOS.member):
            if not isinstance(member, URIRef):
                continue
            if member not in nodes:
                rank_values = [o for o in graph.objects(member, CIRCULARITY_RANK) if isinstance(o, Literal)]
                rank_suffix = f" [rank {rank_values[0]}]" if rank_values else ""
                nodes[member] = Node(
                    iri=member, label=f"{_best_label(graph, member)}{rank_suffix}", kind="concept"
                )
            edges.add(Edge(source=coll, target=member, label="member", kind="member"))

    concepts = [
        c
        for c in graph.subjects(RDF.type, SKOS.Concept)
        if isinstance(c, URIRef) and str(c).startswith(str(SR))
    ]
    for concept in concepts:
        if concept not in nodes:
            rank_values = [o for o in graph.objects(concept, CIRCULARITY_RANK) if isinstance(o, Literal)]
            rank_suffix = f" [rank {rank_values[0]}]" if rank_values else ""
            nodes[concept] = Node(
                iri=concept, label=f"{_best_label(graph, concept)}{rank_suffix}", kind="concept"
            )
        for verb in graph.objects(concept, MAPS_TO_VERB):
            if not isinstance(verb, URIRef):
                continue
            if verb not in nodes:
                nodes[verb] = Node(iri=verb, label=_best_label(graph, verb), kind="verb")
            edges.add(Edge(source=concept, target=verb, label="mapsToVerb", kind="maps"))

    return Model(
        nodes=tuple(sorted(nodes.values(), key=lambda n: str(n.iri))),
        edges=tuple(sorted(edges, key=lambda e: (str(e.source), str(e.target), e.label))),
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
        rankdir="LR",
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.5",
        fontname="Helvetica",
        fontsize="20",
        label="sdata R-Strategies Map",
        labelloc="t",
        labeljust="c",
    )
    graph.node_attr.update(
        shape="box",
        style="filled,rounded",
        fontname="Helvetica",
        fontsize="11",
        penwidth="1.4",
        margin="0.14,0.08",
    )
    graph.edge_attr.update(
        color="#4A5568",
        penwidth="1.4",
        arrowsize="0.8",
        fontname="Helvetica",
        fontsize="10",
    )

    style_map = {
        "scheme": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "collection": {"fillcolor": "#F0FFF9", "color": "#2F855A", "fontcolor": "#1C4532"},
        "concept": {"fillcolor": "#FFF4E5", "color": "#B7791F", "fontcolor": "#7B341E"},
        "verb": {"fillcolor": "#F3E8FF", "color": "#805AD5", "fontcolor": "#44337A"},
    }
    edge_style = {
        "top": {"color": "#2B6CB0", "style": "solid"},
        "member": {"color": "#2F855A", "style": "dotted"},
        "maps": {"color": "#805AD5", "style": "dashed"},
    }

    scheme_cluster = graph.add_subgraph(
        name="cluster_scheme", label="R-Strategy Scheme", color="#90B5E8", style="rounded"
    )
    group_cluster = graph.add_subgraph(
        name="cluster_groups", label="Level Groups", color="#9AD9BF", style="rounded"
    )
    concept_cluster = graph.add_subgraph(
        name="cluster_concepts", label="R-Concepts", color="#F3C887", style="rounded"
    )
    verb_cluster = graph.add_subgraph(
        name="cluster_verbs", label="Lifecycle Verbs", color="#C3A7F2", style="rounded"
    )

    for node in model.nodes:
        attrs = style_map[node.kind]
        if node.kind == "scheme":
            target = scheme_cluster
        elif node.kind == "collection":
            target = group_cluster
        elif node.kind == "verb":
            target = verb_cluster
        else:
            target = concept_cluster
        target.add_node(str(node.iri), label=node.label, **attrs)

    for edge in model.edges:
        attrs = edge_style[edge.kind].copy()
        attrs["label"] = edge.label
        graph.add_edge(str(edge.source), str(edge.target), **attrs)

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
    parser.add_argument("--strategies", type=Path, default=Path("sdata-r-strategies.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-r-strategies-map")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.strategies)
        model = extract_model(graph)
        if not model.nodes:
            print("No R-strategy nodes found for visualization.", file=sys.stderr)
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

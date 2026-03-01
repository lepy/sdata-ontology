"""Create a styled agent classification hierarchy plot rooted at sdata agent classes."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

SDATA = Namespace("https://w3id.org/sdata/core/")
SAGENTS = Namespace("https://w3id.org/sdata/vocab/agents/")
SDATA_AGENT = SDATA.Agent
SDATA_HASH = "https://w3id.org/sdata/core#"
SAGENTS_HASH = "https://w3id.org/sdata/vocab/agents#"


@dataclass(frozen=True)
class HierarchyNode:
    iri: URIRef
    label: str
    kind: str  # "sdata" | "scheme" | "concept"


@dataclass(frozen=True)
class HierarchyEdge:
    parent: URIRef
    child: URIRef


@dataclass(frozen=True)
class HierarchyModel:
    nodes: tuple[HierarchyNode, ...]
    edges: tuple[HierarchyEdge, ...]


def _canon_core(iri: URIRef) -> URIRef:
    text = str(iri)
    if text.startswith(SDATA_HASH):
        return URIRef(str(SDATA) + text[len(SDATA_HASH) :])
    return iri


def _core_aliases(iri: URIRef) -> tuple[URIRef, ...]:
    text = str(iri)
    if text.startswith(str(SDATA)):
        return (iri, URIRef(SDATA_HASH + text[len(str(SDATA)) :]))
    if text.startswith(SDATA_HASH):
        return (_canon_core(iri), iri)
    return (iri,)


def _is_agents_uri(iri: URIRef) -> bool:
    text = str(iri)
    return text.startswith(str(SAGENTS)) or text.startswith(SAGENTS_HASH)


def load_graph(core_path: Path, agents_path: Path) -> Graph:
    if not core_path.exists():
        raise FileNotFoundError(f"Core ontology not found: {core_path}")
    if not agents_path.exists():
        raise FileNotFoundError(f"Agents ontology not found: {agents_path}")

    graph = Graph()
    graph.parse(core_path, format="turtle")
    graph.parse(agents_path, format="turtle")
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


def extract_hierarchy(graph: Graph) -> HierarchyModel:
    nodes: dict[URIRef, str] = {}
    edges: set[HierarchyEdge] = set()

    agent_roots: list[URIRef] = []
    for sdata_class in (SDATA_AGENT,):
        for alias in _core_aliases(sdata_class):
            if (alias, RDF.type, OWL.Class) in graph:
                nodes[sdata_class] = "sdata"
                if sdata_class not in agent_roots:
                    agent_roots.append(sdata_class)

    schemes = [
        scheme
        for scheme in graph.subjects(RDF.type, SKOS.ConceptScheme)
        if isinstance(scheme, URIRef) and _is_agents_uri(scheme)
    ]

    for scheme in schemes:
        nodes[scheme] = "scheme"
        for root in agent_roots:
            edges.add(HierarchyEdge(parent=root, child=scheme))

        concepts = {
            concept
            for concept in graph.subjects(SKOS.inScheme, scheme)
            if isinstance(concept, URIRef) and _is_agents_uri(concept)
        }

        for concept in concepts:
            nodes[concept] = "concept"

        has_unified_root = SDATA_AGENT in nodes
        for concept in concepts:
            broader_parents = {
                parent
                for parent in graph.objects(concept, SKOS.broader)
                if isinstance(parent, URIRef) and parent in concepts
            }

            if broader_parents:
                for parent in broader_parents:
                    edges.add(HierarchyEdge(parent=parent, child=concept))
                continue

            is_top = (
                (concept, SKOS.topConceptOf, scheme) in graph
                or (scheme, SKOS.hasTopConcept, concept) in graph
            )
            if is_top:
                edges.add(HierarchyEdge(parent=scheme, child=concept))
                if has_unified_root:
                    edges.add(HierarchyEdge(parent=SDATA_AGENT, child=concept))

    model_nodes = tuple(
        HierarchyNode(iri=iri, label=_best_label(graph, iri), kind=kind)
        for iri, kind in sorted(nodes.items(), key=lambda item: str(item[0]))
    )
    model_edges = tuple(sorted(edges, key=lambda e: (str(e.parent), str(e.child))))
    return HierarchyModel(nodes=model_nodes, edges=model_edges)


def build_agraph(model: HierarchyModel):
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
        label="sdata Agents Hierarchy (core agents -> SKOS classifications)",
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

    core_cluster = graph.add_subgraph(
        name="cluster_core", label="sdata-core ontology", color="#90B5E8", style="rounded"
    )
    agents_cluster = graph.add_subgraph(
        name="cluster_agents", label="sdata-agents ontology", color="#9AD9BF", style="rounded"
    )

    style_map = {
        "sdata": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "scheme": {"fillcolor": "#E7FFF6", "color": "#2F855A", "fontcolor": "#1C4532"},
        "concept": {"fillcolor": "#F0FFF9", "color": "#2F855A", "fontcolor": "#1C4532"},
    }

    for node in model.nodes:
        if node.kind == "sdata":
            target = core_cluster
        else:
            target = agents_cluster
        target.add_node(str(node.iri), label=node.label, **style_map[node.kind])

    for edge in model.edges:
        attrs = {"label": ""}
        if edge.parent in {SDATA_AGENT} and edge.child in {
            URIRef(str(SAGENTS) + "AgentTypeScheme"),
            URIRef(SAGENTS_HASH + "AgentTypeScheme"),
        }:
            attrs["label"] = "classification scheme"
        elif edge.parent in {SDATA_AGENT}:
            attrs["label"] = "also an"
        graph.add_edge(str(edge.parent), str(edge.child), **attrs)

    legend = graph.add_subgraph(name="cluster_legend", label="Legend", color="#CBD5E0", style="rounded")
    legend.add_node("legend_sdata", label="sdata agent class", **style_map["sdata"])
    legend.add_node("legend_scheme", label="SKOS ConceptScheme", **style_map["scheme"])
    legend.add_node("legend_concept", label="SKOS Concept", **style_map["concept"])
    legend.add_edge("legend_sdata", "legend_scheme", label="classification scheme", color="#4A5568")
    legend.add_edge("legend_scheme", "legend_concept", label="broader -> narrower", color="#4A5568")

    core_cluster.add_node("__anchor_core", style="invis", width="0", height="0", label="")
    agents_cluster.add_node("__anchor_agents", style="invis", width="0", height="0", label="")
    graph.add_edge("__anchor_core", "__anchor_agents", style="invis", weight="20")

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
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--agents", type=Path, default=Path("sdata-agents.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-agents-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.core, args.agents)
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

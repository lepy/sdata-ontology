"""Create a combined hierarchy plot for sdata-core, processtypes and agents."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

SDATA_SLASH = "https://w3id.org/sdata/core/"
SDATA_HASH = "https://w3id.org/sdata/core#"
SAGENTS_SLASH = "https://w3id.org/sdata/vocab/agents/"
SAGENTS_HASH = "https://w3id.org/sdata/vocab/agents#"


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "core" | "proc" | "agents_scheme" | "agents_concept"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef
    kind: str  # "subclass" | "top" | "broader" | "typed"
    label: str = ""


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def _canon(term: URIRef) -> URIRef:
    text = str(term)
    if text.startswith(SDATA_HASH):
        return URIRef(SDATA_SLASH + text[len(SDATA_HASH) :])
    return term


def _aliases(term: URIRef) -> tuple[URIRef, ...]:
    text = str(term)
    if text.startswith(SDATA_SLASH):
        return (term, URIRef(SDATA_HASH + text[len(SDATA_SLASH) :]))
    if text.startswith(SDATA_HASH):
        return (_canon(term), term)
    return (term,)


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels: list[Literal] = []
    for alias in _aliases(iri):
        labels.extend(list(graph.objects(alias, RDFS.label)))
        labels.extend(list(graph.objects(alias, SKOS.prefLabel)))
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


def _is_sdata_uri(iri: URIRef) -> bool:
    text = str(iri)
    return text.startswith(SDATA_SLASH) or text.startswith(SDATA_HASH)


def _classes_from(graph: Graph) -> set[URIRef]:
    return {
        _canon(cls)
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and _is_sdata_uri(cls)
    }


def _parents(graph: Graph, node: URIRef) -> set[URIRef]:
    found: set[URIRef] = set()
    for alias in _aliases(node):
        for parent in graph.objects(alias, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                found.add(_canon(parent))
    return found


def load_graphs(
    core_path: Path, processtypes_path: Path, agents_path: Path
) -> tuple[Graph, Graph, Graph, Graph]:
    for path, label in (
        (core_path, "Core ontology"),
        (processtypes_path, "Processtypes ontology"),
        (agents_path, "Agents ontology"),
    ):
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {path}")

    core_graph = Graph()
    core_graph.parse(core_path, format="turtle")

    proc_graph = Graph()
    proc_graph.parse(processtypes_path, format="turtle")

    agents_graph = Graph()
    agents_graph.parse(agents_path, format="turtle")

    merged = Graph()
    merged += core_graph
    merged += proc_graph
    merged += agents_graph

    return core_graph, proc_graph, agents_graph, merged


def extract_model(core_graph: Graph, proc_graph: Graph, agents_graph: Graph, merged: Graph) -> Model:
    core_classes = _classes_from(core_graph)
    proc_classes = _classes_from(proc_graph)
    all_sdata_classes = core_classes | proc_classes

    nodes: dict[URIRef, Node] = {}
    edges: set[Edge] = set()

    for cls in sorted(core_classes, key=str):
        nodes[cls] = Node(iri=cls, label=_best_label(merged, cls), kind="core")
    for cls in sorted(proc_classes, key=str):
        kind = "core" if cls in nodes else "proc"
        nodes[cls] = Node(iri=cls, label=_best_label(merged, cls), kind=kind)

    for child in all_sdata_classes:
        for parent in _parents(merged, child):
            if parent in all_sdata_classes:
                edges.add(Edge(parent=parent, child=child, kind="subclass"))

    schemes = [
        s
        for s in agents_graph.subjects(RDF.type, SKOS.ConceptScheme)
        if isinstance(s, URIRef) and (str(s).startswith(SAGENTS_SLASH) or str(s).startswith(SAGENTS_HASH))
    ]
    concepts = [
        c
        for c in agents_graph.subjects(RDF.type, SKOS.Concept)
        if isinstance(c, URIRef) and (str(c).startswith(SAGENTS_SLASH) or str(c).startswith(SAGENTS_HASH))
    ]

    for scheme in schemes:
        nodes[scheme] = Node(iri=scheme, label=_best_label(merged, scheme), kind="agents_scheme")
    for concept in concepts:
        nodes[concept] = Node(iri=concept, label=_best_label(merged, concept), kind="agents_concept")

    for scheme in schemes:
        for concept in agents_graph.objects(scheme, SKOS.hasTopConcept):
            if isinstance(concept, URIRef):
                edges.add(Edge(parent=scheme, child=concept, kind="top", label="top concept"))

    for concept in concepts:
        for broader in agents_graph.objects(concept, SKOS.broader):
            if isinstance(broader, URIRef):
                edges.add(Edge(parent=broader, child=concept, kind="broader", label="broader"))

    for scheme in schemes:
        for agent_cls in (URIRef(SDATA_SLASH + "MaterialAgent"), URIRef(SDATA_SLASH + "InformationAgent")):
            if agent_cls in nodes:
                edges.add(Edge(parent=agent_cls, child=scheme, kind="typed", label="typed via sdata:agentType"))

    return Model(
        nodes=tuple(sorted(nodes.values(), key=lambda n: (n.kind, str(n.iri)))),
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
        label="sdata Combined Hierarchy (autark core + processtypes + agents)",
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

    core_cluster = graph.add_subgraph(name="cluster_core", label="sdata-core classes", color="#90B5E8", style="rounded")
    proc_cluster = graph.add_subgraph(
        name="cluster_proc", label="sdata-processtypes verb classes", color="#B6D7A8", style="rounded"
    )
    agents_cluster = graph.add_subgraph(
        name="cluster_agents", label="sdata-agents vocabulary", color="#9AD9BF", style="rounded"
    )

    style_map = {
        "core": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "proc": {"fillcolor": "#EEF8E7", "color": "#4F8A10", "fontcolor": "#2F5D08"},
        "agents_scheme": {"fillcolor": "#E7FFF6", "color": "#2F855A", "fontcolor": "#1C4532"},
        "agents_concept": {"fillcolor": "#F0FFF9", "color": "#2F855A", "fontcolor": "#1C4532"},
    }

    for node in model.nodes:
        attrs = style_map[node.kind]
        if node.kind == "core":
            target = core_cluster
        elif node.kind == "proc":
            target = proc_cluster
        else:
            target = agents_cluster
        target.add_node(str(node.iri), label=node.label, **attrs)

    for edge in model.edges:
        attrs = {"label": edge.label}
        if edge.kind == "typed":
            attrs.update({"style": "dashed", "color": "#2F855A"})
        elif edge.kind in {"top", "broader"}:
            attrs.update({"style": "dotted", "color": "#2F855A"})
        graph.add_edge(str(edge.parent), str(edge.child), **attrs)

    dual_pairs = [
        (URIRef(SDATA_SLASH + "MaterialArtifact"), URIRef(SDATA_SLASH + "InformationArtifact")),
        (URIRef(SDATA_SLASH + "Material"), URIRef(SDATA_SLASH + "Information")),
        (URIRef(SDATA_SLASH + "MaterialAgent"), URIRef(SDATA_SLASH + "InformationAgent")),
        (URIRef(SDATA_SLASH + "MaterialProcess"), URIRef(SDATA_SLASH + "InformationProcess")),
        (URIRef(SDATA_SLASH + "MaterialSite"), URIRef(SDATA_SLASH + "InformationSite")),
    ]
    node_ids = {str(node.iri) for node in model.nodes}
    for left, right in dual_pairs:
        left_id, right_id = str(left), str(right)
        if left_id in node_ids and right_id in node_ids:
            pair_rank = core_cluster.add_subgraph(
                name=f"cluster_combined_dual_rank_{left_id.rsplit('/', 1)[-1]}",
                rank="same",
                style="invis",
            )
            pair_rank.add_node(left_id)
            pair_rank.add_node(right_id)
            graph.add_edge(
                left_id,
                right_id,
                dir="none",
                style="dashed",
                color="#6B7280",
                fontcolor="#6B7280",
                label="dual",
                constraint="false",
            )

    proc_nodes = [node for node in model.nodes if node.kind == "proc"]
    proc_node_ids = {str(node.iri) for node in proc_nodes}
    proc_pairs: list[tuple[str, str, str]] = []
    for node in proc_nodes:
        left_id = str(node.iri)
        local = left_id.rsplit("/", 1)[-1]
        if not local.startswith("Material"):
            continue
        suffix = local[len("Material") :]
        right_local = f"Information{suffix}"
        right_id = f"{SDATA_SLASH}{right_local}"
        if right_id in proc_node_ids:
            proc_pairs.append((left_id, right_id, local))

    for left_id, right_id, local in sorted(proc_pairs):
        pair_rank = proc_cluster.add_subgraph(
            name=f"cluster_proc_dual_rank_{local}",
            rank="same",
            style="invis",
        )
        pair_rank.add_node(left_id)
        pair_rank.add_node(right_id)
        graph.add_edge(
            left_id,
            right_id,
            dir="none",
            style="dashed",
            color="#6B7280",
            fontcolor="#6B7280",
            label="dual",
            constraint="false",
        )

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
    parser.add_argument("--processtypes", type=Path, default=Path("sdata-processtypes.ttl"))
    parser.add_argument("--agents", type=Path, default=Path("sdata-agents.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-combined-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        core_g, proc_g, agents_g, merged_g = load_graphs(
            args.core, args.processtypes, args.agents
        )
        model = extract_model(core_g, proc_g, agents_g, merged_g)
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

"""Create a class hierarchy plot spanning MIN -> sdata-core."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL

MIN_PREFIX = "https://w3id.org/min"
SDATA_CORE_PREFIX = "https://w3id.org/sdata/core/"
MIN_ENTITY = "https://w3id.org/min#Entity"
MIN_NEXUS = "https://w3id.org/min#Nexus"
MIN_FORMA = "https://w3id.org/min#Forma"
MIN_OBJECT = "https://w3id.org/min#Object"
MIN_PROCESS = "https://w3id.org/min#Process"
MIN_DATA = "https://w3id.org/min#Data"
MIN_AGENT = "https://w3id.org/min#Agent"
MIN_BOUNDARY = "https://w3id.org/min#Boundary"
SDATA_OBJECT_CHILDREN = (
    "https://w3id.org/sdata/core/Material",
    "https://w3id.org/sdata/core/Product",
    "https://w3id.org/sdata/core/Hardware",
    "https://w3id.org/sdata/core/Software",
)
SDATA_AGENT_CHILDREN = (
    "https://w3id.org/sdata/core/Person",
    "https://w3id.org/sdata/core/HardwareAgent",
    "https://w3id.org/sdata/core/SoftwareAgent",
    "https://w3id.org/sdata/core/Organization",
    "https://w3id.org/sdata/core/EnvironmentAgent",
)


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "min" | "sdata"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def _children_index(model: Model) -> dict[str, set[str]]:
    children: dict[str, set[str]] = {}
    for edge in model.edges:
        parent = str(edge.parent)
        child = str(edge.child)
        children.setdefault(parent, set()).add(child)
    return children


def _descendants(start: str, children: dict[str, set[str]]) -> set[str]:
    seen: set[str] = set()
    stack = list(children.get(start, set()))
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(children.get(node, set()))
    return seen


def _local_name(iri: str) -> str:
    if "#" in iri:
        return iri.rsplit("#", 1)[1]
    return iri.rsplit("/", 1)[-1]


def _kind_from_iri(iri: URIRef) -> str | None:
    text = str(iri)
    if text.startswith(MIN_PREFIX):
        return "min"
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


def load_graphs(min_path: Path, core_path: Path) -> tuple[Graph, Graph, Graph]:
    for path, label in ((min_path, "MIN ontology"), (core_path, "sdata-core ontology")):
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {path}")

    min_graph = Graph()
    min_graph.parse(min_path, format="turtle")

    core_graph = Graph()
    core_graph.parse(core_path, format="turtle")

    merged = Graph()
    merged += min_graph
    merged += core_graph

    return min_graph, core_graph, merged


def extract_model(min_graph: Graph, core_graph: Graph, merged: Graph) -> Model:
    min_classes = _classes_from(min_graph)
    core_classes = _classes_from(core_graph)
    all_classes = min_classes | core_classes

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
        compound="true",
        newrank="true",
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.55",
        fontname="Helvetica",
        fontsize="20",
        label="Class Hierarchy: MIN -> sdata-core",
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

    style_map = {
        "min": {"fillcolor": "#E7F0FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "sdata": {"fillcolor": "#F8EEFF", "color": "#6B46C1", "fontcolor": "#44337A"},
    }

    for node in model.nodes:
        graph.add_node(str(node.iri), label=node.label, **style_map[node.kind])

    node_ids = {str(node.iri) for node in model.nodes}
    children = _children_index(model)
    kind_by_id = {str(node.iri): node.kind for node in model.nodes}

    # Cluster each MIN class under Nexus/Forma together with all reachable sdata children.
    nexus_desc = _descendants(MIN_NEXUS, children) if MIN_NEXUS in node_ids else set()
    forma_desc = _descendants(MIN_FORMA, children) if MIN_FORMA in node_ids else set()
    branch_min_classes = sorted(
        iri
        for iri in (nexus_desc | forma_desc)
        if iri in node_ids and kind_by_id.get(iri) == "min"
    )
    for min_class in branch_min_classes:
        sdata_children = sorted(
            iri
            for iri in _descendants(min_class, children)
            if iri in node_ids and kind_by_id.get(iri) == "sdata"
        )
        members = [min_class] + sdata_children
        family = "Nexus" if min_class in nexus_desc else "Forma"
        family_style = (
            {"color": "#7AA2D6", "bgcolor": "#F2F8FF"}
            if family == "Nexus"
            else {"color": "#A48BC9", "bgcolor": "#FAF5FF"}
        )
        graph.add_subgraph(
            members,
            name=f"cluster_{_local_name(min_class).lower()}",
            label=f"{_local_name(min_class)} + sdata children",
            style="rounded,dashed",
            penwidth="1.2",
            rankdir="TB",
            **family_style,
        )

    # Keep only the global top anchor at Entity.
    if MIN_ENTITY in node_ids:
        graph.add_subgraph([MIN_ENTITY], name="rank_entity_top", rank="source", style="invis")

    # Stack direct Entity children vertically (tree TB root layering).
    entity_children = [iri for iri in children.get(MIN_ENTITY, set()) if iri in node_ids]
    ordered_entity_children = [iri for iri in (MIN_NEXUS, MIN_FORMA) if iri in entity_children]
    ordered_entity_children.extend(sorted(iri for iri in entity_children if iri not in ordered_entity_children))

    # Stagger branch nodes vertically, so branch subgraphs are not on one level.
    def _add_stagger_chain(ids: tuple[str, ...], prefix: str) -> None:
        present = [iri for iri in ids if iri in node_ids]
        for idx in range(len(present) - 1):
            graph.add_edge(
                present[idx],
                present[idx + 1],
                style="invis",
                color="#FFFFFF",
                weight="50",
                minlen="1",
                constraint="true",
                key=f"{prefix}_{idx}",
            )

    _add_stagger_chain(tuple(ordered_entity_children), "entity_children_stack")
    _add_stagger_chain((MIN_NEXUS, MIN_OBJECT, MIN_PROCESS, MIN_DATA, MIN_AGENT, MIN_BOUNDARY), "nexus_stack")
    _add_stagger_chain((MIN_FORMA, "https://w3id.org/min#Lex", "https://w3id.org/min#Structura", "https://w3id.org/min#Possibile", "https://w3id.org/min#Norma", "https://w3id.org/min#Institutio"), "forma_stack")

    for edge in model.edges:
        graph.add_edge(str(edge.parent), str(edge.child), label="")

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
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-min-core-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])

    try:
        min_g, core_g, merged_g = load_graphs(args.min_path, args.core)
        model = extract_model(min_g, core_g, merged_g)
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

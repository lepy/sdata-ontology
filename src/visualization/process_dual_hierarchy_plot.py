"""Visualize only MaterialProcess/InformationProcess and their subclasses."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

SDATA_SLASH = "https://w3id.org/sdata/core/"
SDATA_HASH = "https://w3id.org/sdata/core#"
MATERIAL_PROCESS = URIRef(SDATA_SLASH + "MaterialProcess")
INFORMATION_PROCESS = URIRef(SDATA_SLASH + "InformationProcess")


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "core" | "proc"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef


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


def load_graphs(core_path: Path, processtypes_path: Path) -> tuple[Graph, Graph, Graph]:
    for path, label in ((core_path, "Core ontology"), (processtypes_path, "Processtypes ontology")):
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {path}")

    core_graph = Graph()
    core_graph.parse(core_path, format="turtle")

    proc_graph = Graph()
    proc_graph.parse(processtypes_path, format="turtle")

    merged = Graph()
    merged += core_graph
    merged += proc_graph

    return core_graph, proc_graph, merged


def extract_model(core_graph: Graph, proc_graph: Graph, merged: Graph) -> Model:
    core_classes = _classes_from(core_graph)
    proc_classes = _classes_from(proc_graph)
    all_sdata_classes = core_classes | proc_classes

    child_map: dict[URIRef, set[URIRef]] = defaultdict(set)
    edges_all: set[Edge] = set()
    for child in all_sdata_classes:
        for parent in _parents(merged, child):
            if parent in all_sdata_classes:
                child_map[parent].add(child)
                edges_all.add(Edge(parent=parent, child=child))

    included: set[URIRef] = set()
    queue: deque[URIRef] = deque([MATERIAL_PROCESS, INFORMATION_PROCESS])
    while queue:
        current = queue.popleft()
        if current in included:
            continue
        included.add(current)
        for child in sorted(child_map.get(current, set()), key=str):
            queue.append(child)

    nodes: list[Node] = []
    for iri in sorted(included, key=str):
        kind = "core" if iri in core_classes else "proc"
        nodes.append(Node(iri=iri, label=_best_label(merged, iri), kind=kind))

    edges = [edge for edge in edges_all if edge.parent in included and edge.child in included]
    edges_sorted = sorted(edges, key=lambda e: (str(e.parent), str(e.child)))
    return Model(nodes=tuple(nodes), edges=tuple(edges_sorted))


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
        label="sdata Process Hierarchy (MaterialProcess/InformationProcess branches only)",
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
        "core": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "proc": {"fillcolor": "#EEF8E7", "color": "#4F8A10", "fontcolor": "#2F5D08"},
    }

    material_branch = graph.add_subgraph(
        name="cluster_material_branch",
        label="Material process branch",
        color="#9DC3E6",
        style="rounded",
        rankdir="TB",
    )
    information_branch = graph.add_subgraph(
        name="cluster_information_branch",
        label="Information process branch",
        color="#A9D18E",
        style="rounded",
        rankdir="TB",
    )
    root_branch = graph.add_subgraph(
        name="cluster_process_roots",
        label="Process roots",
        color="#D6D6D6",
        style="rounded",
        rank="source",
    )

    for node in model.nodes:
        node_id = str(node.iri)
        graph.add_node(node_id, label=node.label, **style_map[node.kind])
        local = node_id.rsplit("/", 1)[-1]
        if node_id == str(MATERIAL_PROCESS) or node_id == str(INFORMATION_PROCESS):
            root_branch.add_node(node_id)
            continue
        if local.startswith("Material"):
            material_branch.add_node(node_id)
        elif local.startswith("Information"):
            information_branch.add_node(node_id)

    for edge in model.edges:
        parent_id = str(edge.parent)
        child_id = str(edge.child)
        attrs = {"label": ""}
        # Keep TB flow primarily from the temporal sequence edges; root fan-out
        # edges should not force a wide same-rank spread of all child classes.
        if parent_id in (str(MATERIAL_PROCESS), str(INFORMATION_PROCESS)):
            attrs["constraint"] = "false"
        graph.add_edge(parent_id, child_id, **attrs)

    # Connect dual pairs (Material* <-> Information*) among the displayed nodes.
    node_ids = {str(node.iri) for node in model.nodes}
    pairs: list[tuple[str, str]] = []
    for node in model.nodes:
        left_id = str(node.iri)
        local = left_id.rsplit("/", 1)[-1]
        if not local.startswith("Material"):
            continue
        suffix = local[len("Material") :]
        right_id = f"{SDATA_SLASH}Information{suffix}"
        if right_id in node_ids:
            pairs.append((left_id, right_id))

    for left_id, right_id in sorted(pairs):
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

    # Keep the two root classes at the top while branches remain TB in their subgraphs.
    for root_id, first_child in (
        (str(INFORMATION_PROCESS), f"{SDATA_SLASH}InformationCreation"),
        (str(MATERIAL_PROCESS), f"{SDATA_SLASH}MaterialCreation"),
    ):
        if root_id in node_ids and first_child in node_ids:
            graph.add_edge(
                root_id,
                first_child,
                style="invis",
                color="#FFFFFF",
                constraint="true",
                weight="80",
                minlen="1",
            )

    # Add temporal sequence edges for process subclasses in each branch.
    sequence = [
        "Creation",
        "Transformation",
        "Transfer",
        "Observation",
        "Preservation",
        "Recovery",
        "Destruction",
    ]
    for prefix, color in (("Information", "#4F8A10"), ("Material", "#2B6CB0")):
        for left_suffix, right_suffix in zip(sequence, sequence[1:]):
            left_id = f"{SDATA_SLASH}{prefix}{left_suffix}"
            right_id = f"{SDATA_SLASH}{prefix}{right_suffix}"
            if left_id in node_ids and right_id in node_ids:
                graph.add_edge(
                    left_id,
                    right_id,
                    color=color,
                    penwidth="2.0",
                    style="bold",
                    label="next",
                    fontcolor=color,
                    constraint="true",
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
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-process-dual-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        core_g, proc_g, merged_g = load_graphs(args.core, args.processtypes)
        model = extract_model(core_g, proc_g, merged_g)
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

"""Create a hierarchy plot for sdata-core and sdata-processtypes (without agents)."""

from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL, SKOS

SDATA_SLASH = "https://w3id.org/sdata/core/"
SDATA_HASH = "https://w3id.org/sdata/core#"
BFO_PREFIX = "http://purl.obolibrary.org/obo/BFO_"
PROV_PREFIX = "http://www.w3.org/ns/prov#"
BFO_ENTITY = URIRef("http://purl.obolibrary.org/obo/BFO_0000001")


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "core" | "proc" | "bfo" | "prov"


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


def _is_external(iri: URIRef) -> bool:
    text = str(iri)
    return text.startswith(BFO_PREFIX) or text.startswith(PROV_PREFIX)


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


def load_graphs(core_path: Path, processtypes_path: Path, vendor_paths: Iterable[Path]) -> tuple[Graph, Graph, Graph]:
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
    for path in vendor_paths:
        if path.exists():
            merged.parse(path, format="turtle")

    return core_graph, proc_graph, merged


def extract_model(core_graph: Graph, proc_graph: Graph, merged: Graph) -> Model:
    core_classes = _classes_from(core_graph)
    proc_classes = _classes_from(proc_graph)
    all_sdata_classes = core_classes | proc_classes

    nodes: dict[URIRef, Node] = {}
    edges: set[Edge] = set()
    external: set[URIRef] = set()

    for cls in sorted(core_classes, key=str):
        nodes[cls] = Node(iri=cls, label=_best_label(merged, cls), kind="core")

    for cls in sorted(proc_classes, key=str):
        kind = "core" if cls in nodes else "proc"
        nodes[cls] = Node(iri=cls, label=_best_label(merged, cls), kind=kind)

    for child in all_sdata_classes:
        for parent in _parents(merged, child):
            if parent in all_sdata_classes:
                edges.add(Edge(parent=parent, child=child))
            elif _is_external(parent):
                external.add(parent)
                edges.add(Edge(parent=parent, child=child))

    stack = list(external)
    visited: set[URIRef] = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        for parent in _parents(merged, current):
            if _is_external(parent):
                external.add(parent)
                edges.add(Edge(parent=parent, child=current))
                stack.append(parent)

    if any(str(n).startswith(BFO_PREFIX) for n in external):
        external.add(BFO_ENTITY)

    for ext in sorted(external, key=str):
        kind = "bfo" if str(ext).startswith(BFO_PREFIX) else "prov"
        nodes[ext] = Node(iri=ext, label=_best_label(merged, ext), kind=kind)

    return Model(
        nodes=tuple(sorted(nodes.values(), key=lambda n: (n.kind, str(n.iri)))),
        edges=tuple(sorted(edges, key=lambda e: (str(e.parent), str(e.child)))),
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
        newrank="true",
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="1.0",
        nodesep="0.55",
        fontname="Helvetica",
        fontsize="20",
        label="sdata Core + Processtypes Hierarchy (without agents)",
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

    core_cluster = graph.add_subgraph(name="cluster_core", label="sdata-core classes", color="#90B5E8", style="rounded")
    proc_cluster = graph.add_subgraph(
        name="cluster_proc", label="sdata-processtypes classes", color="#B6D7A8", style="rounded"
    )
    bfo_cluster = graph.add_subgraph(name="cluster_bfo", label="BFO hierarchy", color="#F3C887", style="rounded")
    prov_cluster = graph.add_subgraph(name="cluster_prov", label="PROV hierarchy", color="#9AD9BF", style="rounded")

    style_map = {
        "core": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "proc": {"fillcolor": "#EEF8E7", "color": "#4F8A10", "fontcolor": "#2F5D08"},
        "bfo": {"fillcolor": "#FFF4E5", "color": "#B7791F", "fontcolor": "#7B341E"},
        "prov": {"fillcolor": "#E7FFF6", "color": "#2F855A", "fontcolor": "#1C4532"},
    }

    for node in model.nodes:
        attrs = style_map[node.kind]
        if node.kind == "core":
            target = core_cluster
        elif node.kind == "proc":
            target = proc_cluster
        elif node.kind == "bfo":
            target = bfo_cluster
        else:
            target = prov_cluster
        target.add_node(str(node.iri), label=node.label, **attrs)

    for edge in model.edges:
        graph.add_edge(str(edge.parent), str(edge.child), label="")

    # Group and connect dual core class pairs.
    core_dual_pairs = [
        (URIRef(SDATA_SLASH + "MaterialArtifact"), URIRef(SDATA_SLASH + "InformationArtifact")),
        (URIRef(SDATA_SLASH + "Material"), URIRef(SDATA_SLASH + "Information")),
        (URIRef(SDATA_SLASH + "MaterialAgent"), URIRef(SDATA_SLASH + "InformationAgent")),
        (URIRef(SDATA_SLASH + "MaterialProcess"), URIRef(SDATA_SLASH + "InformationProcess")),
        (URIRef(SDATA_SLASH + "MaterialSite"), URIRef(SDATA_SLASH + "InformationSite")),
    ]
    node_ids = {str(node.iri) for node in model.nodes}
    for left, right in core_dual_pairs:
        left_id, right_id = str(left), str(right)
        if left_id in node_ids and right_id in node_ids:
            pair_rank = core_cluster.add_subgraph(
                name=f"cluster_core_dual_rank_{left_id.rsplit('/', 1)[-1]}",
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

    # Group and connect dual processtype pairs (Material* <-> Information*).
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

    # Force the processtypes cluster below the core cluster in top-bottom layouts.
    core_nodes = sorted((str(node.iri) for node in model.nodes if node.kind == "core"))
    proc_nodes_ordered = sorted((str(node.iri) for node in model.nodes if node.kind == "proc"))
    if core_nodes and proc_nodes_ordered:
        graph.add_edge(
            core_nodes[0],
            proc_nodes_ordered[0],
            style="invis",
            color="#FFFFFF",
            weight="120",
            minlen="2",
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
    parser.add_argument("--processtypes", type=Path, default=Path("sdata-processtypes.ttl"))
    parser.add_argument("--vendor-dir", type=Path, default=Path("vendor/ontologies"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-core-processtypes-hierarchy")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    args = parse_args(argv or sys.argv[1:])
    vendor_paths = _default_vendor_files(args.vendor_dir)

    try:
        core_g, proc_g, merged_g = load_graphs(args.core, args.processtypes, vendor_paths)
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

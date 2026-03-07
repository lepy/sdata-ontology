#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS

MIN_PREFIX = "https://w3id.org/min"
SDATA_PREFIX = "https://w3id.org/sdata/core/"
MIN_ONTOLOGY_IRI = "https://w3id.org/min"
SDATA_ONTOLOGY_IRI = "https://w3id.org/sdata/core"


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


def _kind_from_iri(iri: URIRef) -> str | None:
    text = str(iri)
    if text.startswith(MIN_PREFIX):
        return "min"
    if text.startswith(SDATA_PREFIX):
        return "sdata"
    return None


def _local_name(iri: URIRef) -> str:
    text = str(iri)
    if "#" in text:
        return text.rsplit("#", 1)[1]
    return text.rsplit("/", 1)[-1]


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels = list(graph.objects(iri, RDFS.label))
    if not labels:
        return _local_name(iri)

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


def _ontology_version(graph: Graph, ontology_iri: str) -> str:
    subject = URIRef(ontology_iri)
    for lit in graph.objects(subject, OWL.versionInfo):
        return str(lit)

    for subj in graph.subjects(RDF.type, OWL.Ontology):
        for lit in graph.objects(subj, OWL.versionInfo):
            return str(lit)

    return "unknown"


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


def build_dot(model: Model, min_version: str, core_version: str) -> str:
    lines: list[str] = []
    lines.append("digraph MIN_SDATA {")
    lines.append("    rankdir=TB;")
    lines.append('    bgcolor="transparent";')
    lines.append("    pad=0.35;")
    lines.append("    nodesep=0.45;")
    lines.append("    ranksep=0.7;")
    lines.append("    splines=true;")
    lines.append('    graph [fontname="Helvetica,Arial,sans-serif"];')
    lines.append('    node  [fontname="Helvetica,Arial,sans-serif"];')
    lines.append('    edge  [fontname="Helvetica,Arial,sans-serif"];')
    lines.append("    node [shape=box, style=\"rounded,filled\", penwidth=1.5, fontsize=11];")
    lines.append("    edge [penwidth=1.25, arrowsize=0.55];")
    lines.append("")

    lines.append('    subgraph cluster_min {')
    lines.append('        label="MIN";')
    lines.append('        style="rounded"; color="#8FB7EA"; bgcolor="#F2F8FF";')
    for node in model.nodes:
        if node.kind != "min":
            continue
        lines.append(
            f'        "{node.iri}" [label="{node.label}", fillcolor="#E7F0FF", color="#2B6CB0", fontcolor="#1A365D"];'
        )
    lines.append("    }")
    lines.append("")

    lines.append('    subgraph cluster_sdata {')
    lines.append('        label="sdata-core";')
    lines.append('        style="rounded"; color="#B39DDB"; bgcolor="#FAF5FF";')
    for node in model.nodes:
        if node.kind != "sdata":
            continue
        lines.append(
            f'        "{node.iri}" [label="{node.label}", fillcolor="#F1E8FF", color="#6B46C1", fontcolor="#44337A"];'
        )
    lines.append("    }")
    lines.append("")

    kind_by_iri = {node.iri: node.kind for node in model.nodes}
    for edge in model.edges:
        pk = kind_by_iri.get(edge.parent)
        ck = kind_by_iri.get(edge.child)
        if pk != ck:
            color = "#D97706"
            style = "bold"
        elif pk == "min":
            color = "#2B6CB0"
            style = "solid"
        else:
            color = "#6B46C1"
            style = "solid"
        lines.append(
            f'    "{edge.parent}" -> "{edge.child}" [color="{color}", style="{style}"];'
        )

    lines.append("")
    lines.append("    labelloc=t;")
    lines.append(
        '    label=<<FONT POINT-SIZE="16"><B>Class Hierarchy: MIN + sdata-core</B></FONT><BR/><FONT POINT-SIZE="10" COLOR="#666666">'
        f'MIN version: {min_version}  |  sdata-core version: {core_version}'
        "</FONT>>;"
    )
    lines.append("}")
    return "\n".join(lines) + "\n"


def build_mermaid(model: Model) -> str:
    lines: list[str] = []
    lines.append("```mermaid")
    lines.append("graph TD")

    ids: dict[URIRef, str] = {}
    for idx, node in enumerate(sorted(model.nodes, key=lambda n: str(n.iri))):
        ids[node.iri] = f"N{idx}"

    lines.append("    subgraph MIN")
    for node in sorted((n for n in model.nodes if n.kind == "min"), key=lambda n: str(n.iri)):
        nid = ids[node.iri]
        lines.append(f'        {nid}["{node.label}"]')
    lines.append("    end")
    lines.append("")

    lines.append("    subgraph sdata_core")
    for node in sorted((n for n in model.nodes if n.kind == "sdata"), key=lambda n: str(n.iri)):
        nid = ids[node.iri]
        lines.append(f'        {nid}["{node.label}"]')
    lines.append("    end")
    lines.append("")

    for edge in model.edges:
        lines.append(f"    {ids[edge.parent]} --> {ids[edge.child]}")

    lines.append("")
    lines.append("    classDef minNode fill:#E7F0FF,stroke:#2B6CB0,color:#1A365D")
    lines.append("    classDef sdataNode fill:#F1E8FF,stroke:#6B46C1,color:#44337A")

    if any(node.kind == "min" for node in model.nodes):
        min_ids = ",".join(ids[node.iri] for node in model.nodes if node.kind == "min")
        lines.append(f"    class {min_ids} minNode")
    if any(node.kind == "sdata" for node in model.nodes):
        sdata_ids = ",".join(ids[node.iri] for node in model.nodes if node.kind == "sdata")
        lines.append(f"    class {sdata_ids} sdataNode")

    lines.append("```")
    lines.append("")
    lines.append("Bridge edges (MIN -> sdata-core) are inferred from rdfs:subClassOf links.")
    lines.append("")
    return "\n".join(lines)


def render_svg(dot_path: Path, svg_path: Path) -> None:
    if shutil.which("dot") is None:
        raise RuntimeError("Graphviz 'dot' command not found. Install graphviz to render SVG.")
    subprocess.run(["dot", "-Tsvg", str(dot_path), "-o", str(svg_path)], check=True)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate combined MIN + sdata-core hierarchy (DOT/Mermaid/SVG)."
    )
    parser.add_argument("--min", default="min-v3.7.1.ttl", help="Input MIN ontology Turtle file")
    parser.add_argument("--core", default="sdata-core.ttl", help="Input sdata-core Turtle file")
    parser.add_argument(
        "--dot",
        default="docs/diagrams/sdata-min-core-hierarchy.dot",
        help="Output DOT file",
    )
    parser.add_argument(
        "--mmd",
        default="docs/diagrams/sdata-min-core-hierarchy.mmd",
        help="Output Mermaid file",
    )
    parser.add_argument(
        "--svg",
        default="docs/diagrams/sdata-min-core-hierarchy.svg",
        help="Output SVG file",
    )
    parser.add_argument(
        "--skip-svg", action="store_true", help="Only write DOT/Mermaid, do not render SVG"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    min_path = Path(args.min)
    core_path = Path(args.core)
    dot_path = Path(args.dot)
    mmd_path = Path(args.mmd)
    svg_path = Path(args.svg)

    try:
        min_graph, core_graph, merged_graph = load_graphs(min_path, core_path)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    model = extract_model(min_graph, core_graph, merged_graph)
    if not model.nodes:
        print("No MIN/sdata classes found for visualization.", file=sys.stderr)
        return 1

    min_version = _ontology_version(min_graph, MIN_ONTOLOGY_IRI)
    core_version = _ontology_version(core_graph, SDATA_ONTOLOGY_IRI)

    dot_path.parent.mkdir(parents=True, exist_ok=True)
    mmd_path.parent.mkdir(parents=True, exist_ok=True)

    dot_path.write_text(build_dot(model, min_version=min_version, core_version=core_version), encoding="utf-8")
    mmd_path.write_text(build_mermaid(model), encoding="utf-8")

    if not args.skip_svg:
        try:
            render_svg(dot_path, svg_path)
        except RuntimeError as exc:
            print(str(exc), file=sys.stderr)
            return 2

    print(f"Wrote {dot_path}")
    print(f"Wrote {mmd_path}")
    if not args.skip_svg:
        print(f"Wrote {svg_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

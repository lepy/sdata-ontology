"""Create a styled lifecycle flow plot from sdata-lifecycle.ttl."""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import OWL

SDATA = Namespace("https://w3id.org/sdata/core/")
SLC = Namespace("https://w3id.org/sdata/lifecycle#")

STAGE_CREATION = SDATA.Creation
STAGE_TRANSFORMATION = SDATA.Transformation
STAGE_TRANSFER = SDATA.Transfer
STAGE_PRESERVATION = SDATA.Preservation
STAGE_RECOVERY = SDATA.Recovery
STAGE_OBSERVATION = SDATA.Observation
STAGE_DESTRUCTION = SDATA.Destruction

CIRCULAR_STAGES = (
    STAGE_CREATION,
    STAGE_TRANSFORMATION,
    STAGE_TRANSFER,
    STAGE_PRESERVATION,
    STAGE_RECOVERY,
)


@dataclass(frozen=True)
class LifecycleNode:
    iri: URIRef
    label: str
    kind: str  # "circular" | "cross" | "terminal"


@dataclass(frozen=True)
class LifecycleEdge:
    source: URIRef
    target: URIRef
    kind: str  # "circular" | "cross" | "terminal"


@dataclass(frozen=True)
class LifecycleModel:
    nodes: tuple[LifecycleNode, ...]
    edges: tuple[LifecycleEdge, ...]


def load_graph(lifecycle_path: Path) -> Graph:
    if not lifecycle_path.exists():
        raise FileNotFoundError(f"Lifecycle ontology not found: {lifecycle_path}")
    graph = Graph()
    graph.parse(lifecycle_path, format="turtle")
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


def extract_lifecycle(graph: Graph) -> LifecycleModel:
    stages: list[URIRef] = [
        stage
        for stage in graph.objects(SLC.UniversalLifecycle, SLC.hasStage)
        if isinstance(stage, URIRef)
    ]
    if not stages:
        stages = list(CIRCULAR_STAGES)

    cross = next(
        (node for node in graph.objects(SLC.UniversalLifecycle, SLC.crossCutting) if isinstance(node, URIRef)),
        STAGE_OBSERVATION,
    )
    terminal = next(
        (node for node in graph.objects(SLC.UniversalLifecycle, SLC.terminalExit) if isinstance(node, URIRef)),
        STAGE_DESTRUCTION,
    )

    node_kind: dict[URIRef, str] = {stage: "circular" for stage in stages}
    node_kind[cross] = "cross"
    node_kind[terminal] = "terminal"

    edges: set[LifecycleEdge] = set()
    for source, target in graph.subject_objects(SLC.typicallyFollowedBy):
        if isinstance(source, URIRef) and isinstance(target, URIRef):
            edges.add(LifecycleEdge(source=source, target=target, kind="circular"))

    if not edges:
        fallback = list(CIRCULAR_STAGES)
        for idx, source in enumerate(fallback):
            target = fallback[(idx + 1) % len(fallback)]
            edges.add(LifecycleEdge(source=source, target=target, kind="circular"))

    for stage in stages:
        edges.add(LifecycleEdge(source=cross, target=stage, kind="cross"))
        edges.add(LifecycleEdge(source=stage, target=terminal, kind="terminal"))
    edges.add(LifecycleEdge(source=cross, target=terminal, kind="terminal"))

    nodes = tuple(
        LifecycleNode(iri=iri, label=_best_label(graph, iri), kind=kind)
        for iri, kind in sorted(node_kind.items(), key=lambda item: str(item[0]))
    )
    model_edges = tuple(sorted(edges, key=lambda e: (str(e.source), str(e.target), e.kind)))
    return LifecycleModel(nodes=nodes, edges=model_edges)


def build_agraph(model: LifecycleModel):
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
        ranksep="0.8",
        nodesep="0.45",
        fontname="Helvetica",
        fontsize="20",
        label="sdata Lifecycle Flow",
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
        "circular": {"fillcolor": "#E8F1FF", "color": "#2B6CB0", "fontcolor": "#1A365D"},
        "cross": {"fillcolor": "#E7FFF6", "color": "#2F855A", "fontcolor": "#1C4532"},
        "terminal": {"fillcolor": "#FFF4E5", "color": "#B7791F", "fontcolor": "#7B341E"},
    }
    edge_style = {
        "circular": {"color": "#2B6CB0", "style": "solid", "label": ""},
        "cross": {"color": "#2F855A", "style": "dashed", "label": "observes"},
        "terminal": {"color": "#B7791F", "style": "dashed", "label": "terminal exit"},
    }

    for node in model.nodes:
        graph.add_node(str(node.iri), label=node.label, **style_map[node.kind])

    for edge in model.edges:
        graph.add_edge(str(edge.source), str(edge.target), **edge_style[edge.kind])

    legend = graph.add_subgraph(name="cluster_legend", label="Legend", color="#CBD5E0", style="rounded")
    legend.add_node("legend_circular", label="circular stage", **style_map["circular"])
    legend.add_node("legend_cross", label="cross-cutting stage", **style_map["cross"])
    legend.add_node("legend_terminal", label="terminal stage", **style_map["terminal"])
    legend.add_edge("legend_circular", "legend_circular", color="#2B6CB0", label="typicallyFollowedBy")
    legend.add_edge("legend_cross", "legend_circular", color="#2F855A", style="dashed", label="observes")
    legend.add_edge("legend_circular", "legend_terminal", color="#B7791F", style="dashed", label="terminal exit")

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
    parser.add_argument("--lifecycle", type=Path, default=Path("sdata-lifecycle.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-lifecycle-flow")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.lifecycle)
        model = extract_lifecycle(graph)
        if not model.nodes:
            print("No lifecycle nodes found for visualization.", file=sys.stderr)
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

"""Render any example TTL graph to DOT/SVG/PNG with pygraphviz."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import BNode, Graph, Literal, RDF, URIRef


def load_graph(ttl_path: Path) -> Graph:
    if not ttl_path.exists():
        raise FileNotFoundError(f"TTL file not found: {ttl_path}")
    graph = Graph()
    graph.parse(ttl_path, format="turtle")
    return graph


def _safe_node_id(term) -> str:
    if isinstance(term, URIRef):
        return f"uri::{str(term)}"
    if isinstance(term, BNode):
        return f"bnode::{str(term)}"
    if isinstance(term, Literal):
        return f"lit::{str(term)}::{str(term.datatype) if term.datatype else ''}::{term.language or ''}"
    return f"other::{str(term)}"


def _term_label(graph: Graph, term) -> str:
    if isinstance(term, URIRef):
        try:
            return graph.namespace_manager.normalizeUri(term)
        except Exception:
            text = str(term)
            if "#" in text:
                return text.rsplit("#", 1)[1]
            return text.rsplit("/", 1)[-1]
    if isinstance(term, BNode):
        return f"_:{term}"
    if isinstance(term, Literal):
        text = str(term)
        if len(text) > 50:
            text = text[:47] + "..."
        return text
    return str(term)


def build_agraph(graph: Graph, title: str):
    try:
        import pygraphviz as pgv
    except ImportError as exc:
        raise RuntimeError(
            "pygraphviz is required to render diagrams. Install dev dependencies first."
        ) from exc

    instances = {s for s, _, _ in graph.triples((None, RDF.type, None))}
    classes = {o for _, _, o in graph.triples((None, RDF.type, None)) if isinstance(o, URIRef)}

    agraph = pgv.AGraph(strict=False, directed=True)
    agraph.graph_attr.update(
        bgcolor="#FAFBFC",
        rankdir="LR",
        splines="true",
        overlap="false",
        pad="0.35",
        ranksep="0.9",
        nodesep="0.4",
        fontname="Helvetica",
        fontsize="18",
        label=title,
        labelloc="t",
        labeljust="c",
    )
    agraph.node_attr.update(
        shape="box",
        style="filled,rounded",
        fontname="Helvetica",
        fontsize="10",
        penwidth="1.2",
        margin="0.12,0.06",
    )
    agraph.edge_attr.update(
        color="#4A5568",
        penwidth="1.2",
        arrowsize="0.75",
        fontname="Helvetica",
        fontsize="9",
    )

    for s, p, o in graph:
        s_id = _safe_node_id(s)
        s_label = _term_label(graph, s)
        if isinstance(s, Literal):
            s_style = {"fillcolor": "#FFF9DB", "color": "#B08900", "fontcolor": "#5C4500", "shape": "note"}
        elif isinstance(s, BNode):
            s_style = {"fillcolor": "#ECEFF1", "color": "#607D8B", "fontcolor": "#263238"}
        elif s in classes:
            s_style = {"fillcolor": "#F3E8FF", "color": "#7E57C2", "fontcolor": "#4527A0"}
        elif s in instances:
            s_style = {"fillcolor": "#E3F2FD", "color": "#1976D2", "fontcolor": "#0D47A1"}
        else:
            s_style = {"fillcolor": "#FFFFFF", "color": "#78909C", "fontcolor": "#37474F"}
        agraph.add_node(s_id, label=s_label, **s_style)

        o_id = _safe_node_id(o)
        o_label = _term_label(graph, o)
        if isinstance(o, Literal):
            o_style = {"fillcolor": "#FFF9DB", "color": "#B08900", "fontcolor": "#5C4500", "shape": "note"}
        elif isinstance(o, BNode):
            o_style = {"fillcolor": "#ECEFF1", "color": "#607D8B", "fontcolor": "#263238"}
        elif o in classes:
            o_style = {"fillcolor": "#F3E8FF", "color": "#7E57C2", "fontcolor": "#4527A0"}
        elif o in instances:
            o_style = {"fillcolor": "#E3F2FD", "color": "#1976D2", "fontcolor": "#0D47A1"}
        else:
            o_style = {"fillcolor": "#FFFFFF", "color": "#78909C", "fontcolor": "#37474F"}
        agraph.add_node(o_id, label=o_label, **o_style)

        pred_label = _term_label(graph, p)
        agraph.add_edge(s_id, o_id, label=pred_label)

    return agraph


def render(
    agraph,
    out_dot: Path,
    out_svg: Path | None,
    out_png: Path | None,
    layout: str,
    dpi: int,
) -> None:
    agraph.write(out_dot)
    if out_svg:
        agraph.draw(out_svg, format="svg", prog=layout)
    if out_png:
        agraph.draw(out_png, format="png", prog=layout, args=f"-Gdpi={dpi}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Path to TTL file")
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default=None, help="Base output file name (without extension)")
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    base_name = args.name or f"{args.input.stem}-graph"
    title = f"TTL Graph: {args.input.name}"

    try:
        graph = load_graph(args.input)
        agraph = build_agraph(graph, title=title)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_dot = args.out_dir / f"{base_name}.dot"
    out_svg = args.out_dir / f"{base_name}.svg" if args.format in ("svg", "both") else None
    out_png = args.out_dir / f"{base_name}.png" if args.format in ("png", "both") else None

    render(agraph, out_dot=out_dot, out_svg=out_svg, out_png=out_png, layout=args.layout, dpi=args.dpi)

    print(f"Generated {out_dot}")
    if out_svg:
        print(f"Generated {out_svg}")
    if out_png:
        print(f"Generated {out_png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

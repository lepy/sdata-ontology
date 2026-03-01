"""Render three category-modality plots for examples/min-opa-examples.ttl."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from rdflib import BNode, Graph, Namespace, RDF, URIRef

from src.visualization.example_ttl_plot import build_agraph, load_graph, render

EX = Namespace("https://example.org/instances#")
MIN = Namespace("https://w3id.org/min#")
MODALITIES: tuple[tuple[str, str, URIRef], ...] = (
    ("material-modal", "Object / material-dominant", URIRef("https://w3id.org/min#Object")),
    ("balanced-modal", "Process / balanced", URIRef("https://w3id.org/min#Process")),
    ("informational-modal", "Data / informational-dominant", URIRef("https://w3id.org/min#Data")),
)

DEFAULT_INPUT = Path("examples/min-opa-examples.ttl")
DEFAULT_OUT_DIR = Path("docs/diagrams")
DEFAULT_BASE = "min-opa-examples"


def _is_in_namespace(term, namespace: Namespace) -> bool:
    return isinstance(term, URIRef) and str(term).startswith(str(namespace))


def _empty_like(source: Graph) -> Graph:
    out = Graph()
    for prefix, ns in source.namespaces():
        out.bind(prefix, ns)
    return out


def extract_modality_view(source: Graph, modality: URIRef) -> Graph:
    view = _empty_like(source)
    roots = {s for s in source.subjects(RDF.type, modality) if isinstance(s, URIRef)}
    if not roots:
        return view

    queue: list[URIRef | BNode] = list(roots)
    visited: set[URIRef | BNode] = set()

    while queue:
        subject = queue.pop()
        if subject in visited:
            continue
        visited.add(subject)

        for pred, obj in source.predicate_objects(subject):
            view.add((subject, pred, obj))
            if isinstance(obj, URIRef) and _is_in_namespace(obj, EX):
                queue.append(obj)
            elif isinstance(obj, BNode):
                queue.append(obj)

    return view


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument("--base-name", default=DEFAULT_BASE)
    parser.add_argument("--format", choices=("svg", "png", "both"), default="both")
    parser.add_argument("--layout", default="dot")
    parser.add_argument("--dpi", type=int, default=220)
    return parser.parse_args(argv)


def _render_one(
    graph: Graph,
    out_dir: Path,
    name: str,
    title: str,
    fmt: str,
    layout: str,
    dpi: int,
) -> None:
    agraph = build_agraph(graph, title=title)
    out_dot = out_dir / f"{name}.dot"
    out_svg = out_dir / f"{name}.svg" if fmt in ("svg", "both") else None
    out_png = out_dir / f"{name}.png" if fmt in ("png", "both") else None
    render(agraph, out_dot=out_dot, out_svg=out_svg, out_png=out_png, layout=layout, dpi=dpi)
    print(f"Generated {out_dot}")
    if out_svg:
        print(f"Generated {out_svg}")
    if out_png:
        print(f"Generated {out_png}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    try:
        graph = load_graph(args.input)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    args.out_dir.mkdir(parents=True, exist_ok=True)

    for slug, label, modality in MODALITIES:
        view = extract_modality_view(graph, modality)
        if not view:
            print(f"Warning: no data found for modality {label}", file=sys.stderr)
            continue
        _render_one(
            graph=view,
            out_dir=args.out_dir,
            name=f"{args.base_name}-{slug}",
            title=f"TTL Graph ({label}): {args.input.name}",
            fmt=args.format,
            layout=args.layout,
            dpi=args.dpi,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate MkDocs class reference pages from sdata-core.ttl."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL

SDATA_BASE = "https://w3id.org/sdata/core/"
MIN_BASE = "https://w3id.org/min#"


@dataclass(frozen=True)
class ClassInfo:
    iri: URIRef
    name: str
    labels: tuple[str, ...]
    comment: str | None
    examples: tuple[str, ...]
    superclasses: tuple[URIRef, ...]
    subclasses: tuple[URIRef, ...]
    domain_of: tuple[URIRef, ...]
    range_of: tuple[URIRef, ...]


def _local_name(iri: URIRef) -> str:
    text = str(iri)
    if "#" in text:
        return text.rsplit("#", 1)[1]
    return text.rsplit("/", 1)[-1]


def _is_sdata_iri(iri: URIRef) -> bool:
    return str(iri).startswith(SDATA_BASE)


def _best_literal(values: list[Literal]) -> str | None:
    if not values:
        return None

    def key(value: Literal) -> tuple[int, str]:
        lang = (value.language or "").lower()
        if lang == "en":
            rank = 0
        elif lang == "de":
            rank = 1
        elif not lang:
            rank = 2
        else:
            rank = 3
        return (rank, str(value))

    return str(sorted(values, key=key)[0])


def _format_class_ref(iri: URIRef) -> str:
    name = _local_name(iri)
    if _is_sdata_iri(iri):
        return f"[`sdata:{name}`](./{name}.md)"
    if str(iri).startswith(MIN_BASE):
        return f"`min:{name}`"
    return f"`{iri}`"


def _format_prop_ref(iri: URIRef) -> str:
    name = _local_name(iri)
    if _is_sdata_iri(iri):
        return f"`sdata:{name}`"
    if str(iri).startswith(MIN_BASE):
        return f"`min:{name}`"
    return f"`{iri}`"


def _collect_properties(graph: Graph) -> set[URIRef]:
    prop_types = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    props: set[URIRef] = set()
    for prop_type in prop_types:
        for subject in graph.subjects(RDF.type, prop_type):
            if isinstance(subject, URIRef) and _is_sdata_iri(subject):
                props.add(subject)
    return props


def build_class_infos(graph: Graph) -> tuple[list[ClassInfo], str | None]:
    ontology_uri = URIRef("https://w3id.org/sdata/core")
    version = _best_literal([obj for obj in graph.objects(ontology_uri, OWL.versionInfo) if isinstance(obj, Literal)])

    sdata_classes = sorted(
        {
            cls
            for cls in graph.subjects(RDF.type, OWL.Class)
            if isinstance(cls, URIRef) and _is_sdata_iri(cls)
        },
        key=lambda iri: _local_name(iri).lower(),
    )
    class_set = set(sdata_classes)

    super_by_class: dict[URIRef, list[URIRef]] = defaultdict(list)
    sub_by_class: dict[URIRef, list[URIRef]] = defaultdict(list)
    for cls in sdata_classes:
        for parent in graph.objects(cls, RDFS.subClassOf):
            if isinstance(parent, URIRef):
                super_by_class[cls].append(parent)
                if parent in class_set:
                    sub_by_class[parent].append(cls)

    props = _collect_properties(graph)
    domain_map: dict[URIRef, list[URIRef]] = defaultdict(list)
    range_map: dict[URIRef, list[URIRef]] = defaultdict(list)
    for prop in sorted(props, key=lambda iri: _local_name(iri).lower()):
        for domain in graph.objects(prop, RDFS.domain):
            if isinstance(domain, URIRef) and domain in class_set:
                domain_map[domain].append(prop)
        for range_ in graph.objects(prop, RDFS.range):
            if isinstance(range_, URIRef) and range_ in class_set:
                range_map[range_].append(prop)

    infos: list[ClassInfo] = []
    for cls in sdata_classes:
        labels = tuple(str(x) for x in sorted(graph.objects(cls, RDFS.label), key=lambda lit: str(lit)))
        comment = _best_literal([obj for obj in graph.objects(cls, RDFS.comment) if isinstance(obj, Literal)])
        examples = tuple(str(x) for x in sorted(graph.objects(cls, URIRef("http://www.w3.org/2004/02/skos/core#example")), key=lambda lit: str(lit)))

        infos.append(
            ClassInfo(
                iri=cls,
                name=_local_name(cls),
                labels=labels,
                comment=comment,
                examples=examples,
                superclasses=tuple(sorted(set(super_by_class.get(cls, [])), key=str)),
                subclasses=tuple(sorted(set(sub_by_class.get(cls, [])), key=str)),
                domain_of=tuple(sorted(set(domain_map.get(cls, [])), key=str)),
                range_of=tuple(sorted(set(range_map.get(cls, [])), key=str)),
            )
        )

    return infos, version


def _render_list(values: list[str]) -> str:
    if not values:
        return "- (none)\n"
    return "".join(f"- {value}\n" for value in values)


def write_class_page(path: Path, info: ClassInfo) -> None:
    super_lines = [_format_class_ref(iri) for iri in info.superclasses]
    sub_lines = [_format_class_ref(iri) for iri in info.subclasses]
    domain_lines = [_format_prop_ref(iri) for iri in info.domain_of]
    range_lines = [_format_prop_ref(iri) for iri in info.range_of]

    lines: list[str] = []
    lines.append(f"# sdata:{info.name}\n")
    lines.append("## IRI\n")
    lines.append(f"`{info.iri}`\n")
    lines.append("## Labels\n")
    lines.append(_render_list([f"`{label}`" for label in info.labels]))
    lines.append("## Direct Superclasses\n")
    lines.append(_render_list(super_lines))
    lines.append("## Direct Subclasses\n")
    lines.append(_render_list(sub_lines))
    lines.append("## Comment\n")
    lines.append((f"{info.comment}\n\n" if info.comment else "(none)\n\n"))
    lines.append("## Examples\n")
    lines.append(_render_list([f"`{example}`" for example in info.examples]))
    lines.append("## Used As Domain\n")
    lines.append(_render_list(domain_lines))
    lines.append("## Used As Range\n")
    lines.append(_render_list(range_lines))
    lines.append("## Minimal Turtle\n")
    lines.append("```turtle\n")
    lines.append("@prefix sdata: <https://w3id.org/sdata/core/> .\n")
    lines.append("@prefix ex:    <https://example.org/> .\n\n")
    lines.append(f"ex:example a sdata:{info.name} .\n")
    lines.append("```\n")

    path.write_text("".join(lines), encoding="utf-8")


def write_index(path: Path, infos: list[ClassInfo], version: str | None) -> None:
    version_text = version or "unknown"
    lines: list[str] = []
    lines.append("# sdata-core Class Reference\n\n")
    lines.append(f"Generated from `sdata-core.ttl` (version `{version_text}`).\n\n")
    lines.append(f"Total classes: **{len(infos)}**\n\n")
    lines.append("| Class | Superclass(es) | Subclasses |\n")
    lines.append("|---|---|---|\n")
    for info in infos:
        class_link = f"[`sdata:{info.name}`](./{info.name}.md)"
        supers = ", ".join(_format_class_ref(iri) for iri in info.superclasses) or "(none)"
        lines.append(f"| {class_link} | {supers} | {len(info.subclasses)} |\n")
    lines.append("\n")

    path.write_text("".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=Path, default=Path("sdata-core.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/ontologies/sdata-core/classes"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.core.exists():
        raise FileNotFoundError(f"Core ontology not found: {args.core}")

    graph = Graph()
    graph.parse(args.core, format="turtle")
    infos, version = build_class_infos(graph)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for info in infos:
        write_class_page(args.out_dir / f"{info.name}.md", info)
    write_index(args.out_dir / "index.md", infos, version)

    print(f"Generated {len(infos)} class pages in {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

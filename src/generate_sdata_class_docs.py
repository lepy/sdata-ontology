"""Generate MkDocs class reference pages from sdata-core.ttl."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL

SDATA_BASE = "https://w3id.org/sdata/core/"
MIN_BASE = "https://w3id.org/min#"

INDUSTRY_EXAMPLE_BY_CLASS: dict[str, str] = {
    "Accreditation": "DAkkS-Akkreditierung eines Prueflabors fuer Zugversuche nach DIN EN ISO 6892-1.",
    "BillOfMaterials": "Stueckliste eines Kupfer-Kabelsatzes mit Leitern, Isolierung, Steckern und Mengenanteilen.",
    "Boundary": "Bilanzgrenze eines CO2-Footprints von Rohkupfer bis auslieferbares Halbzeug.",
    "BoundaryType": "Typisierung einer Grenze als `Cradle-to-Gate` fuer ein DPP-LCA-Modell.",
    "Certification": "ISO-9001-Zertifikat eines Ziehwerks als Nachweis im Produktpass.",
    "CryptographicKey": "Oeffentlicher Schluessel zur Verifikation signierter DPP-Dokumente.",
    "Data": "Messdaten aus Inline-Wanddickenmessung in der Rohrfertigung.",
    "DataFormat": "Definition des Datenformats als OPC-UA-Export fuer Shopfloor-Integrationen.",
    "DigitalTwin": "Digitaler Zwilling einer Giesslinie mit Live-Parametern und Historie.",
    "EnvironmentAgent": "Korrosive Betriebsumgebung als wirksamer Agent auf Materialalterung.",
    "Hardware": "Zugpruefmaschine als physisches Betriebsmittel im Prueflabor.",
    "Identifier": "Chargennummer einer Kupferlegierung als rueckverfolgbare Kennung.",
    "Law": "EU-Batterieverordnung als rechtsverbindliche Grundlage fuer DPP-Pflichten.",
    "LegalEntity": "Rechtliche Einheit eines OEMs als Vertragspartner in der Lieferkette.",
    "LifecyclePhase": "Nutzungsphase eines Kabelbaums zwischen Inbetriebnahme und Austausch.",
    "Material": "Cu-ETP-Bandmaterial als Eingangsrohstoff fuer Stanz-Biege-Teile.",
    "MaterialGrade": "Werkstoffguete `Cu-OF` zur Typisierung hochreinen Kupfers.",
    "Model": "FEM-Modell einer Stromschiene zur thermomechanischen Auslegung.",
    "ModelType": "Typisierung als `Transientes Thermomodell` fuer Simulationsdaten.",
    "Organization": "Tier-1-Lieferant als organisatorischer Akteur im DPP-Netzwerk.",
    "Person": "Qualitaetsingenieurin, die einen Pruefbericht fachlich freigibt.",
    "Process": "Mehrstufiger Ziehprozess zur Reduktion des Leitungsquerschnitts.",
    "ProcessType": "Typisierung als `Kaltumformung` innerhalb der Prozessklassifikation.",
    "ProductPassport": "Digital Product Passport eines Hochvolt-Kabels mit Material- und Compliance-Daten.",
    "ProductType": "Typisierung von Hardware und Software als einheitlicher Produkttyp.",
    "Proof": "Hash-basierter Integritaetsnachweis fuer einen freigegebenen Messdatensatz.",
    "Registry": "Branchenregister zur Aufloesung verifizierbarer Hersteller-Identitaeten.",
    "Regulation": "REACH- oder RoHS-Regelwerk mit gebuendelten Anforderungen an Substanzen.",
    "Requirement": "Grenzwertanforderung `Leitfaehigkeit >= 58 MS/m` fuer Kupferkomponenten.",
    "Result": "Bestanden/Nicht-bestanden Ergebnis einer elektrischen End-of-Line-Pruefung.",
    "Scenario": "Szenario `30% Rezyklatanteil` zur Bewertung von CO2- und Kostenwirkungen.",
    "Site": "Produktionsstandort mit Giesserei, Walzwerk und Prueflabor.",
    "Software": "MES-System zur Erfassung von Prozessparametern und Chargenbezug.",
    "Specification": "DIN EN ISO 6892-1 als Spezifikation fuer Zugversuchsablauf und Auswertung.",
    "Specimen": "Normprobe aus einer Kupfercharge fuer mechanische Pruefungen.",
    "Substance": "Legierungselement Phosphor als enthaltene Substanz in einer Charge.",
    "TrustFramework": "EUDI-/VC-Vertrauensrahmen fuer interoperable Nachweise im DPP.",
    "Typus": "Domänentyp `Leiterklasse 5` zur standardisierten Einordnung von Produkten.",
    "VerifiableCredential": "Signiertes Hersteller-Zertifikat als maschinenpruefbarer Nachweis.",
    "VerifiablePresentation": "Gebuendelte Vorlage mehrerer Nachweise fuer Audit oder Behoerde.",
}

OBJECT_CLASSES = {
    "Object",
    "Site",
}

DATA_CLASSES = {
    "Data",
    "Identifier",
    "Result",
    "ProductPassport",
    "DigitalProductPassport",
    "VerifiableCredential",
    "VerifiablePresentation",
    "Proof",
    "CryptographicKey",
    "BillOfMaterials",
}

AGENT_OBJECT_CLASSES = {
    "Person",
    "Hardware",
    "Material",
    "Substance",
    "Specimen",
}

AGENT_DATA_CLASSES = {
    "Software",
    "DigitalTwin",
}

AGENT_INSTITUTIONAL_CLASSES = {
    "Organization",
}

AGENT_PROCESS_CLASSES = {
    "EnvironmentAgent",
}

TYPUS_CLASSES = {
    "Typus",
    "MaterialGrade",
    "ProcessType",
    "ProductType",
    "DataFormat",
    "BoundaryType",
    "ModelType",
}

INSTITUTIO_CLASSES = {
    "Institutio",
    "Certification",
    "Accreditation",
    "Registry",
    "TrustFramework",
    "Regulation",
    "Specification",
    "LifecyclePhase",
    "LegalEntity",
}


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


def _industry_example(name: str) -> str:
    example = INDUSTRY_EXAMPLE_BY_CLASS.get(name)
    if example:
        return example
    return f"Praxisfall aus der Industrie, in dem `sdata:{name}` zur semantischen Modellierung eingesetzt wird."


def _slug(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def _industry_ttl(name: str) -> str:
    example = _industry_example(name)
    slug = _slug(name)
    lines = [
        "@prefix sdata: <https://w3id.org/sdata/core/> .",
        "@prefix ex:    <https://example.org/industry/> .",
        "",
        f"# {example}",
    ]

    if name == "Process":
        lines.extend(
            [
                "ex:process_001 a sdata:Process ;",
                '  sdata:hasIdentifier "PROC-001" ;',
                '  sdata:hasName "Warmumformung Linie 3" ;',
                "  sdata:hasInput ex:material_001 ;",
                "  sdata:hasOutput ex:part_001 ;",
                "  sdata:performedBy ex:software_001 ;",
                "  sdata:generates ex:result_001 .",
                "",
                "ex:material_001 a sdata:Material .",
                "ex:part_001 a sdata:Hardware ;",
                "  sdata:hasMaterial ex:material_001 ;",
                "  sdata:typifiedBy ex:product_type_001 .",
                "ex:software_001 a sdata:Software ; sdata:performs ex:process_001 .",
                "ex:result_001 a sdata:Result ; sdata:producedBy ex:process_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name in DATA_CLASSES:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Datensatz" ;',
                "  sdata:describes ex:asset_001 ;",
                "  sdata:producedBy ex:process_001 .",
                "",
                "ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .",
                "ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name == "Agent":
        lines.extend(
            [
                "ex:agent_001 a sdata:Agent ;",
                '  sdata:hasIdentifier "AGENT-001" ;',
                '  sdata:hasName "Generischer Agent im Shopfloor" ;',
                "  sdata:performs ex:process_001 .",
                "",
                "ex:process_001 a sdata:Process .",
            ]
        )
    elif name in AGENT_OBJECT_CLASSES:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} als materieller Agent" ;',
                "  sdata:performs ex:process_001 ;",
                "  sdata:actsOn ex:asset_001 .",
                "",
                "ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .",
                "ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name in AGENT_DATA_CLASSES:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} als informationeller Agent" ;',
                "  sdata:performs ex:process_001 ;",
                "  sdata:describes ex:asset_001 .",
                "",
                "ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .",
                "ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name in AGENT_INSTITUTIONAL_CLASSES:
        lines.extend(
            [
                "ex:organization_001 a sdata:Organization ;",
                '  sdata:hasIdentifier "ORG-001" ;',
                '  sdata:hasName "Tier-1 Lieferant Nord" ;',
                "  sdata:performs ex:process_001 ;",
                "  sdata:owns ex:asset_001 .",
                "",
                "ex:process_001 a sdata:Process .",
                "ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name in AGENT_PROCESS_CLASSES:
        lines.extend(
            [
                "ex:environment_agent_001 a sdata:EnvironmentAgent ;",
                '  sdata:hasIdentifier "ENV-001" ;',
                '  sdata:hasName "Feuchte-korrosive Umgebung" ;',
                "  sdata:influences ex:process_001 ;",
                "  sdata:actsOn ex:material_001 .",
                "",
                "ex:process_001 a sdata:Process .",
                "ex:material_001 a sdata:Material .",
            ]
        )
    elif name == "Boundary":
        lines.extend(
            [
                "ex:boundary_001 a sdata:Boundary ;",
                '  sdata:hasIdentifier "BOUND-001" ;',
                '  sdata:hasName "Kontaktgrenze Werkzeug-Blech" ;',
                "  sdata:bounds ex:tool_001 ;",
                "  sdata:bounds ex:sheet_001 .",
                "",
                "ex:tool_001 a sdata:Hardware .",
                "ex:sheet_001 a sdata:Material .",
            ]
        )
    elif name == "ProductType":
        lines.extend(
            [
                "ex:universalpruefmaschine a sdata:ProductType ;",
                '  sdata:hasIdentifier "PT-001" ;',
                '  sdata:hasName "Universalpruefmaschine" .',
                "",
                "ex:fe_solver_typ a sdata:ProductType ;",
                '  sdata:hasIdentifier "PT-002" ;',
                '  sdata:hasName "FE-Solver" .',
                "",
                "ex:zwick_z250 a sdata:Hardware ;",
                "  sdata:typifiedBy ex:universalpruefmaschine .",
                "",
                "ex:ls_dyna_r14 a sdata:Software ;",
                "  sdata:typifiedBy ex:fe_solver_typ .",
            ]
        )
    elif name in TYPUS_CLASSES:
        target_map = {
            "MaterialGrade": "Material",
            "ProcessType": "Process",
            "DataFormat": "Data",
            "BoundaryType": "Boundary",
            "ModelType": "Model",
        }
        target = target_map.get(name, "Hardware")
        target_slug = _slug(target)
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Klassifikation" ;',
                f"  sdata:typifies ex:{target_slug}_001 .",
                "",
                f"ex:{target_slug}_001 a sdata:{target} .",
            ]
        )
    elif name in {"Structura", "Model"}:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} zur Prozessauslegung" ;',
                "  sdata:constrains ex:process_001 .",
                "",
                f"ex:model_data_001 a sdata:Data ; sdata:encodes ex:{slug}_001 .",
                "ex:process_001 a sdata:Process .",
            ]
        )
    elif name in {"Possibile", "Scenario"}:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} 30 Prozent Rezyklat" ;',
                "  sdata:concerns ex:asset_001 ;",
                f"  sdata:alternativeTo ex:{slug}_002 .",
                "",
                f"ex:{slug}_002 a sdata:{name} ; sdata:concerns ex:asset_001 .",
                "ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .",
                "ex:product_type_001 a sdata:ProductType .",
            ]
        )
    elif name in {"Norma", "Requirement"}:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Leitfaehigkeitsgrenze" ;',
                "  sdata:evaluates ex:result_001 .",
                "",
                "ex:result_001 a sdata:Result ; sdata:assessmentOutcome \"pass\" .",
            ]
        )
    elif name in {"Lex", "Law"}:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} fuer Produktpasspflicht" ;',
                "  sdata:governs ex:process_001 .",
                "",
                "ex:process_001 a sdata:Process .",
            ]
        )
    elif name in INSTITUTIO_CLASSES:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Branchenregel" ;',
                "  sdata:typifies ex:process_001 ;",
                "  sdata:comprises ex:req_001 .",
                "",
                "ex:req_001 a sdata:Requirement .",
                "ex:process_001 a sdata:Process .",
            ]
        )
    elif name in OBJECT_CLASSES:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Instanz" ;',
                "  sdata:describedBy ex:data_001 .",
                "",
                "ex:data_001 a sdata:Data ;",
                f"  sdata:describes ex:{slug}_001 ;",
                "  sdata:producedBy ex:process_001 .",
                "",
                "ex:process_001 a sdata:Process .",
            ]
        )
    else:
        lines.extend(
            [
                f"ex:{slug}_001 a sdata:{name} ;",
                f'  sdata:hasIdentifier "{name.upper()}-001" ;',
                f'  sdata:hasName "{name} Beispielinstanz" ;',
                "  sdata:nexusWith ex:context_001 .",
                "",
                "ex:context_001 a sdata:Data .",
            ]
        )

    return "\n".join(lines)


def _write_text(path: Path, content: str) -> None:
    try:
        path.write_text(content, encoding="utf-8")
    except PermissionError:
        # Generated docs may be present with restrictive file modes from another user.
        # Recreate file so regeneration still works when directory permissions allow it.
        if path.exists():
            path.unlink()
            path.write_text(content, encoding="utf-8")
            return
        raise


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
    lines.append("## Industriebeispiel (TTL)\n")
    lines.append("```turtle\n")
    lines.append(_industry_ttl(info.name))
    lines.append("\n```\n")
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

    _write_text(path, "".join(lines))


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

    _write_text(path, "".join(lines))


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
    generated_paths = {args.out_dir / f"{info.name}.md" for info in infos}
    generated_paths.add(args.out_dir / "index.md")
    for path in args.out_dir.glob("*.md"):
        if path not in generated_paths:
            path.unlink()

    for info in infos:
        write_class_page(args.out_dir / f"{info.name}.md", info)
    write_index(args.out_dir / "index.md", infos, version)

    print(f"Generated {len(infos)} class pages in {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

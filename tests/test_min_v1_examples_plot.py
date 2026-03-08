from pathlib import Path

from rdflib import BNode, Graph, Namespace, RDF, URIRef

from src.visualization.example_ttl_plot import load_graph

ROOT = Path(__file__).resolve().parent.parent
EX = Namespace("https://example.org/zugversuch/")
MIN = Namespace("https://w3id.org/min#")
SDATA = Namespace("https://w3id.org/sdata/core/")


def extract_modality_view(source: Graph, modality: URIRef) -> Graph:
    view = Graph()
    for prefix, ns in source.namespaces():
        view.bind(prefix, ns)

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
            if isinstance(obj, BNode):
                queue.append(obj)
            elif isinstance(obj, URIRef) and str(obj).startswith(str(EX)):
                queue.append(obj)
    return view


def _source_graph():
    return load_graph(ROOT / "examples" / "specimen_tensiontest_data.ttl")


def test_extract_material_modal_view_contains_material_modal_instance():
    graph = _source_graph()
    material_view = extract_modality_view(graph, SDATA.Material)

    assert (EX.dc04, MIN.hasIdentifier, None) in material_view
    assert list(material_view.triples((EX.dc04, SDATA.hasQuantity, None)))


def test_extract_balanced_view_contains_process_flow():
    graph = _source_graph()
    balanced_view = extract_modality_view(graph, SDATA.Process)

    assert (EX.probenfertigung, MIN.hasInput, EX.coil) in balanced_view
    assert (EX.probenfertigung, MIN.hasOutput, EX.probe) in balanced_view
    assert (EX.zugversuch, MIN.generates, EX.ergebnis) in balanced_view


def test_all_modality_views_are_non_empty():
    graph = _source_graph()
    assert len(extract_modality_view(graph, SDATA.Material)) > 0
    assert len(extract_modality_view(graph, SDATA.Process)) > 0
    assert len(extract_modality_view(graph, SDATA.Data)) > 0

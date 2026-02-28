from pathlib import Path

from rdflib import Namespace

from src.visualization.class_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core/")


def _model():
    graph = load_graph(ROOT / "sdata-core.ttl")
    return extract_hierarchy(graph)


def test_extract_contains_all_expected_sdata_classes():
    model = _model()
    classes = {str(node.iri) for node in model.nodes if node.kind == "sdata"}
    expected = {
        str(SDATA.Tangible),
        str(SDATA.Intangible),
        str(SDATA.Artifact),
        str(SDATA.Substance),
        str(SDATA.Agent),
        str(SDATA.Process),
        str(SDATA.Site),
        str(SDATA.MaterialArtifact),
        str(SDATA.Material),
        str(SDATA.MaterialAgent),
        str(SDATA.MaterialProcess),
        str(SDATA.MaterialSite),
        str(SDATA.InformationArtifact),
        str(SDATA.Information),
        str(SDATA.Role),
        str(SDATA.Identifier),
        str(SDATA.InformationAgent),
        str(SDATA.InformationProcess),
        str(SDATA.InformationSite),
    }
    assert expected.issubset(classes)


def test_extract_is_sdata_only_for_autark_core():
    model = _model()
    assert {node.kind for node in model.nodes} == {"sdata"}


def test_edges_only_target_sdata_nodes():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    for edge in model.edges:
        assert str(edge.child) in kinds
        assert str(edge.parent) in kinds
        assert kinds[str(edge.child)] == "sdata"
        assert kinds[str(edge.parent)] == "sdata"


def test_leaf_classes_are_linked_to_domain_classes():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}
    assert (str(SDATA.MaterialAgent), str(SDATA.Tangible)) in edges
    assert (str(SDATA.InformationAgent), str(SDATA.Intangible)) in edges

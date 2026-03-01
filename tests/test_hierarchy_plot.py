from pathlib import Path

from rdflib import Namespace

from src.visualization.class_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core/")


def _model():
    graph = load_graph(ROOT / "sdata-core.ttl")
    return extract_hierarchy(graph)


def test_extract_contains_expected_v091_classes():
    model = _model()
    classes = {str(node.iri) for node in model.nodes if node.kind == "sdata"}
    expected = {
        str(SDATA.Object),
        str(SDATA.Material),
        str(SDATA.Product),
        str(SDATA.Hardware),
        str(SDATA.Software),
        str(SDATA.Data),
        str(SDATA.Process),
        str(SDATA.Agent),
        str(SDATA.Person),
        str(SDATA.HardwareAgent),
        str(SDATA.SoftwareAgent),
        str(SDATA.Organization),
        str(SDATA.AttributeQuantityValue),
        str(SDATA.ValueDomain),
    }
    assert expected.issubset(classes)


def test_extract_is_sdata_only():
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


def test_expected_subclass_edges_exist():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}
    assert (str(SDATA.Product), str(SDATA.Object)) in edges
    assert (str(SDATA.Hardware), str(SDATA.Object)) in edges
    assert (str(SDATA.Software), str(SDATA.Object)) in edges
    assert (str(SDATA.Data), str(SDATA.Object)) in edges
    assert (str(SDATA.Person), str(SDATA.Agent)) in edges
    assert (str(SDATA.HardwareAgent), str(SDATA.Agent)) in edges

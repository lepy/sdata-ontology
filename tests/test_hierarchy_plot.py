from pathlib import Path

from rdflib import Namespace

from src.visualization.class_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core/")
MIN = Namespace("https://w3id.org/min#")


def _model():
    graph = load_graph(ROOT / "sdata-core.ttl")
    return extract_hierarchy(graph)


def test_extract_contains_expected_v110_classes():
    model = _model()
    classes = {str(node.iri) for node in model.nodes}
    expected = {
        str(SDATA.Material),
        str(SDATA.Product),
        str(SDATA.Hardware),
        str(SDATA.Software),
        str(SDATA.Data),
        str(SDATA.Person),
        str(SDATA.HardwareAgent),
        str(SDATA.SoftwareAgent),
        str(SDATA.Organization),
        str(SDATA.EnvironmentAgent),
        str(MIN.Object),
        str(MIN.Data),
        str(MIN.Agent),
    }
    assert expected.issubset(classes)


def test_extract_is_sdata_and_min_only():
    model = _model()
    assert {node.kind for node in model.nodes} == {"sdata", "min"}


def test_edges_only_target_known_nodes():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    for edge in model.edges:
        assert str(edge.child) in kinds
        assert str(edge.parent) in kinds


def test_expected_subclass_edges_exist():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}
    assert (str(SDATA.Product), str(MIN.Object)) in edges
    assert (str(SDATA.Hardware), str(MIN.Object)) in edges
    assert (str(SDATA.Software), str(MIN.Object)) in edges
    assert (str(SDATA.Data), str(MIN.Data)) in edges
    assert (str(SDATA.Person), str(MIN.Agent)) in edges
    assert (str(SDATA.HardwareAgent), str(MIN.Agent)) in edges
    assert (str(SDATA.EnvironmentAgent), str(MIN.Agent)) in edges

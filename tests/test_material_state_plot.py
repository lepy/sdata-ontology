from pathlib import Path

from rdflib import Namespace

from src.visualization.material_state_plot import extract_model, load_graph

ROOT = Path(__file__).resolve().parent.parent
SMS = Namespace("https://w3id.org/sdata/material-state/")


def _model():
    graph = load_graph(ROOT / "sdata-material-state.ttl")
    return extract_model(graph)


def test_extract_contains_axes_and_schemes():
    model = _model()
    nodes = {str(node.iri): node.kind for node in model.nodes}
    assert str(SMS.StateAxis) in nodes
    assert str(SMS.OriginAxis) in nodes
    assert str(SMS.LifecyclePhaseAxis) in nodes
    assert str(SMS.StructureAxis) in nodes
    assert str(SMS.RoleAxis) in nodes
    assert str(SMS.MethodAxis) in nodes
    assert str(SMS.DomainAxis) in nodes
    assert str(SMS.DataTypeAxis) in nodes
    assert str(SMS["origin-values"]) in nodes
    assert str(SMS["phase-values"]) in nodes
    assert str(SMS["structure-values"]) in nodes
    assert str(SMS["role-values"]) in nodes
    assert str(SMS["method-values"]) in nodes
    assert str(SMS["domain-values"]) in nodes
    assert str(SMS["datatype-values"]) in nodes


def test_extract_contains_expected_value_concepts():
    model = _model()
    concepts = {str(node.iri) for node in model.nodes if node.kind == "concept"}
    expected = {
        str(SMS["origin.Virgin"]),
        str(SMS["origin.Recycled"]),
        str(SMS["processing.Raw"]),
        str(SMS["phase.Production"]),
        str(SMS["phase.Recycling"]),
        str(SMS["structure.SinglePart"]),
        str(SMS["role.Specimen"]),
        str(SMS["method.TensileTest"]),
        str(SMS["method.Degradation"]),
        str(SMS["method.Corrosion"]),
        str(SMS["method.Administrative"]),
        str(SMS["method.Creative"]),
        str(SMS["domain.Structural"]),
        str(SMS["datatype.DigitalProductPass"]),
    }
    assert expected.issubset(concepts)


def test_extract_contains_expected_edges():
    model = _model()
    edges = {(str(edge.parent), str(edge.child), edge.kind) for edge in model.edges}
    assert (str(SMS.StateAxis), str(SMS.OriginAxis), "subclass") in edges
    assert (str(SMS.StateAxis), str(SMS.StructureAxis), "subclass") in edges
    assert (str(SMS.StateAxis), str(SMS.RoleAxis), "subclass") in edges
    assert (str(SMS.StateAxis), str(SMS.MethodAxis), "subclass") in edges
    assert (str(SMS.StateAxis), str(SMS.DomainAxis), "subclass") in edges
    assert (str(SMS.StateAxis), str(SMS.DataTypeAxis), "subclass") in edges
    assert (str(SMS.OriginAxis), str(SMS["origin-values"]), "scheme") in edges
    assert (str(SMS.MethodAxis), str(SMS["method-values"]), "scheme") in edges
    assert (str(SMS.DomainAxis), str(SMS["domain-values"]), "scheme") in edges
    assert (str(SMS.DataTypeAxis), str(SMS["datatype-values"]), "scheme") in edges
    assert (str(SMS["origin-values"]), str(SMS["origin.Virgin"]), "top") in edges
    assert (str(SMS["method.Transformative"]), str(SMS["method.Degradation"]), "broader") in edges
    assert (str(SMS["method.Degradation"]), str(SMS["method.Corrosion"]), "broader") in edges
    assert (str(SMS["phase.Production"]), str(SMS["phase.Processing"]), "broader") in edges

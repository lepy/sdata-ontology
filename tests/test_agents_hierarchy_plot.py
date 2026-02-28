from pathlib import Path

from rdflib import Namespace

from src.visualization.agents_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core/")
SAGENTS = Namespace("https://w3id.org/sdata/vocab/agents/")


def _model():
    graph = load_graph(ROOT / "sdata-core.ttl", ROOT / "sdata-agents.ttl")
    return extract_hierarchy(graph)


def test_extract_contains_root_nodes():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    assert str(SDATA.MaterialAgent) in kinds
    assert str(SDATA.InformationAgent) in kinds
    assert str(SAGENTS.AgentTypeScheme) in kinds


def test_extract_contains_expected_agent_concepts():
    model = _model()
    concepts = {str(node.iri) for node in model.nodes if node.kind == "concept"}
    expected = {
        str(SAGENTS.Person),
        str(SAGENTS.Organization),
        str(SAGENTS.Hardware),
        str(SAGENTS.Software),
        str(SAGENTS.Sensor),
        str(SAGENTS.Solver),
        str(SAGENTS.Service),
    }
    assert expected.issubset(concepts)


def test_extract_contains_expected_hierarchy_edges():
    model = _model()
    edges = {(str(edge.parent), str(edge.child)) for edge in model.edges}
    assert (str(SDATA.MaterialAgent), str(SAGENTS.AgentTypeScheme)) in edges
    assert (str(SDATA.InformationAgent), str(SAGENTS.AgentTypeScheme)) in edges
    assert (str(SDATA.MaterialAgent), str(SAGENTS.Person)) in edges
    assert (str(SDATA.MaterialAgent), str(SAGENTS.Hardware)) in edges
    assert (str(SDATA.InformationAgent), str(SAGENTS.Software)) in edges
    assert (str(SAGENTS.AgentTypeScheme), str(SAGENTS.Hardware)) in edges

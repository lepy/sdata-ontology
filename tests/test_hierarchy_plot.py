from pathlib import Path

from rdflib import Namespace

from src.visualization.class_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core/")
BFO_ENTITY = "http://purl.obolibrary.org/obo/BFO_0000001"
PROV_AGENT = "http://www.w3.org/ns/prov#Agent"


def _model():
    graph = load_graph(
        ROOT / "sdata-core.ttl",
        [
            ROOT / "vendor/ontologies/bfo.ttl",
            ROOT / "vendor/ontologies/prov-o.ttl",
            ROOT / "vendor/ontologies/qudt.ttl",
            ROOT / "vendor/ontologies/dtype.ttl",
            ROOT / "vendor/ontologies/vaem.ttl",
            ROOT / "vendor/ontologies/skos.ttl",
        ],
    )
    return extract_hierarchy(graph)


def test_extract_contains_all_expected_sdata_classes():
    model = _model()
    classes = {str(node.iri) for node in model.nodes if node.kind == "sdata"}
    expected = {
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


def test_extract_adds_bfo_context_nodes():
    model = _model()
    bfo_nodes = [node for node in model.nodes if node.kind == "bfo"]
    assert bfo_nodes
    assert any(str(node.iri).startswith("http://purl.obolibrary.org/obo/BFO_") for node in bfo_nodes)
    assert any(str(node.iri) == BFO_ENTITY for node in bfo_nodes)


def test_edges_only_target_sdata_or_external_and_bfo_reaches_entity():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    parents_of: dict[str, set[str]] = {}
    for edge in model.edges:
        assert str(edge.child) in kinds
        assert str(edge.parent) in kinds
        assert kinds[str(edge.child)] in {"sdata", "bfo", "prov"}
        assert kinds[str(edge.parent)] in {"sdata", "bfo", "prov"}
        parents_of.setdefault(str(edge.child), set()).add(str(edge.parent))

    def reaches_entity(node: str, visited: set[str] | None = None) -> bool:
        visited = visited or set()
        if node == BFO_ENTITY:
            return True
        if node in visited:
            return False
        visited.add(node)
        return any(reaches_entity(parent, visited) for parent in parents_of.get(node, set()))

    bfo_nodes = [iri for iri, kind in kinds.items() if kind == "bfo"]
    for node in bfo_nodes:
        if node == BFO_ENTITY:
            continue
        assert reaches_entity(node), f"BFO node {node} does not connect to BFO entity"


def test_agent_chains_include_prov_agent():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    assert PROV_AGENT in kinds

    agent_parent_edges = {
        (str(edge.child), str(edge.parent))
        for edge in model.edges
        if str(edge.child) in {str(SDATA.MaterialAgent), str(SDATA.InformationAgent)}
    }
    assert (str(SDATA.MaterialAgent), PROV_AGENT) in agent_parent_edges
    assert (str(SDATA.InformationAgent), PROV_AGENT) in agent_parent_edges

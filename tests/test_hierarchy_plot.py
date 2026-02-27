from pathlib import Path

from rdflib import Namespace

from src.visualization.class_hierarchy_plot import extract_hierarchy, load_graph

ROOT = Path(__file__).resolve().parent.parent
SDATA = Namespace("https://w3id.org/sdata/core#")


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
        str(SDATA.Agent),
        str(SDATA.PhysicalArtifact),
        str(SDATA.Material),
        str(SDATA.Site),
        str(SDATA.DigitalArtifact),
        str(SDATA.Process),
        str(SDATA.Role),
        str(SDATA.Identifier),
    }
    assert expected.issubset(classes)


def test_extract_adds_bfo_context_nodes():
    model = _model()
    bfo_nodes = [node for node in model.nodes if node.kind == "bfo"]
    assert bfo_nodes
    assert any(str(node.iri).startswith("http://purl.obolibrary.org/obo/BFO_") for node in bfo_nodes)


def test_edges_only_target_sdata_or_bfo():
    model = _model()
    kinds = {str(node.iri): node.kind for node in model.nodes}
    for edge in model.edges:
        assert str(edge.child) in kinds
        assert str(edge.parent) in kinds
        assert kinds[str(edge.child)] == "sdata"
        assert kinds[str(edge.parent)] in {"sdata", "bfo"}


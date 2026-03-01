from pathlib import Path

from rdflib import Namespace

from src.visualization.min_opa_sdata_hierarchy_plot import extract_model, load_graphs

ROOT = Path(__file__).resolve().parent.parent
MIN = Namespace("https://w3id.org/min#")
OPA = Namespace("https://w3id.org/opa#")
SDATA = Namespace("https://w3id.org/sdata/core/")


def _model():
    min_g, opa_g, core_g, merged_g = load_graphs(
        ROOT / "min-v1.0.0.ttl",
        ROOT / "opa-v1.0.0.ttl",
        ROOT / "sdata-core.ttl",
    )
    return extract_model(min_g, opa_g, core_g, merged_g)


def test_extract_contains_nodes_per_ontology():
    model = _model()
    kinds = {node.kind for node in model.nodes}
    assert kinds == {"min", "opa", "sdata"}


def test_extract_contains_expected_bridge_edges():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}

    assert (str(OPA.Object), str(MIN.Nexus)) in edges
    assert (str(OPA.Process), str(MIN.Nexus)) in edges
    assert (str(OPA.Agent), str(MIN.Nexus)) in edges

    assert (str(SDATA.Object), str(OPA.Object)) in edges
    assert (str(SDATA.Process), str(OPA.Process)) in edges
    assert (str(SDATA.Agent), str(OPA.Agent)) in edges


def test_extract_contains_expected_intra_core_edges():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}

    assert (str(SDATA.Product), str(SDATA.Object)) in edges
    assert (str(SDATA.Hardware), str(SDATA.Object)) in edges
    assert (str(SDATA.Software), str(SDATA.Object)) in edges

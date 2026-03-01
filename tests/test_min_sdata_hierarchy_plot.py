from pathlib import Path

from rdflib import Namespace

from src.visualization.min_sdata_hierarchy_plot import extract_model, load_graphs

ROOT = Path(__file__).resolve().parent.parent
MIN = Namespace("https://w3id.org/min#")
SDATA = Namespace("https://w3id.org/sdata/core/")


def _model():
    min_g, core_g, merged_g = load_graphs(
        ROOT / "min-v2.0.0.ttl",
        ROOT / "sdata-core.ttl",
    )
    return extract_model(min_g, core_g, merged_g)


def test_extract_contains_nodes_per_ontology():
    model = _model()
    kinds = {node.kind for node in model.nodes}
    assert kinds == {"min", "sdata"}


def test_extract_contains_expected_bridge_edges():
    model = _model()
    edges = {(str(edge.child), str(edge.parent)) for edge in model.edges}

    assert (str(SDATA.Material), str(MIN.Object)) in edges
    assert (str(SDATA.Product), str(MIN.Object)) in edges
    assert (str(SDATA.Hardware), str(MIN.Object)) in edges
    assert (str(SDATA.Software), str(MIN.Object)) in edges
    assert (str(SDATA.Data), str(MIN.Data)) in edges
    assert (str(SDATA.Process), str(MIN.Process)) in edges

    assert (str(SDATA.Person), str(MIN.Agent)) in edges
    assert (str(SDATA.HardwareAgent), str(MIN.Agent)) in edges
    assert (str(SDATA.SoftwareAgent), str(MIN.Agent)) in edges
    assert (str(SDATA.Organization), str(MIN.Agent)) in edges
    assert (str(SDATA.EnvironmentAgent), str(MIN.Agent)) in edges

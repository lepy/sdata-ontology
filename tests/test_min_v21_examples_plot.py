from pathlib import Path

from rdflib import Namespace

from src.visualization.min_v21_examples_plot import extract_modality_view, load_graph

ROOT = Path(__file__).resolve().parent.parent
EX = Namespace("https://example.org/")
MIN = Namespace("https://w3id.org/min#")
SDATA = Namespace("https://w3id.org/sdata/core/")
QUDT = Namespace("http://qudt.org/schema/qudt/")


def _source_graph():
    return load_graph(ROOT / "examples" / "min-v3.7.1-examples.ttl")


def test_extract_material_modal_view_contains_material_modal_instance():
    graph = _source_graph()
    material_view = extract_modality_view(graph, MIN.Object)

    assert (EX.Stahlcoil_2026_001, MIN.hasIdentifier, None) in material_view
    assert (
        EX.Stahlcoil_2026_001,
        SDATA.hasQuantity,
        EX.Stahlcoil_2026_001_Masse_AQV,
    ) in material_view
    assert (EX.Stahlcoil_2026_001_Masse_AQV, QUDT.numericValue, None) in material_view


def test_extract_balanced_view_contains_process_flow():
    graph = _source_graph()
    balanced_view = extract_modality_view(graph, MIN.Process)

    assert (EX.Tiefziehen_2026_017, MIN.hasInput, EX.Stahlcoil_2026_001) in balanced_view
    assert (EX.Tiefziehen_2026_017, MIN.hasOutput, EX.Bauteil_2026_042) in balanced_view
    assert (EX.Tiefziehen_2026_017, MIN.generates, EX.Zugversuchsdaten_2026_042) in balanced_view


def test_all_modality_views_are_non_empty():
    graph = _source_graph()
    assert len(extract_modality_view(graph, MIN.Object)) > 0
    assert len(extract_modality_view(graph, MIN.Process)) > 0
    assert len(extract_modality_view(graph, MIN.Data)) > 0

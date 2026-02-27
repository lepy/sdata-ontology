"""Tests for sdata-core ontology and instance data."""

from pathlib import Path

import pytest
from rdflib import Graph, Namespace, URIRef, RDF

SDATA = Namespace("https://w3id.org/sdata/core/")
ROOT = Path(__file__).resolve().parent.parent


# ─── Fixture: load graphs ────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def core_graph():
    g = Graph()
    g.parse(ROOT / "sdata-core.ttl", format="turtle")
    return g


@pytest.fixture(scope="session")
def example_graph():
    g = Graph()
    g.parse(ROOT / "examples" / "battery-passport.ttl", format="turtle")
    return g


# ─── TTL Syntax ──────────────────────────────────────────────────────────────

@pytest.mark.parametrize("ttl_file", sorted(ROOT.glob("**/*.ttl")))
def test_turtle_syntax(ttl_file):
    """All .ttl files must parse without error."""
    g = Graph()
    g.parse(ttl_file, format="turtle")
    assert len(g) > 0, f"{ttl_file.name} contains no triples"


# ─── Core Ontology Structure ─────────────────────────────────────────────────

EXPECTED_CLASSES = [
    "MaterialArtifact", "Material", "MaterialAgent", "MaterialProcess", "MaterialSite",
    "InformationArtifact", "Information", "Identifier", "InformationAgent", "InformationProcess",
    "InformationSite", "Role",
]


@pytest.mark.parametrize("class_name", EXPECTED_CLASSES)
def test_core_classes_exist(core_graph, class_name):
    """All 8 core classes must be declared."""
    uri = SDATA[class_name]
    assert (uri, RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")) in core_graph, \
        f"sdata:{class_name} not declared as owl:Class"


EXPECTED_OBJECT_PROPERTIES = [
    "realizes", "isRealizedBy", "represents", "isRepresentedBy",
    "consistsOf", "hasPart", "consumes", "generates", "isGeneratedBy",
    "wasPerformedBy", "hasIdentifier", "locatedAt", "isLocationOf",
    "hostedAt", "isHostOf", "hostedOn", "hosts", "containsSite", "recoveredFrom",
    "derivedFrom",
]


@pytest.mark.parametrize("prop_name", EXPECTED_OBJECT_PROPERTIES)
def test_object_properties_exist(core_graph, prop_name):
    """All object properties must be declared."""
    uri = SDATA[prop_name]
    assert (uri, RDF.type, URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")) in core_graph, \
        f"sdata:{prop_name} not declared as owl:ObjectProperty"


EXPECTED_DATATYPE_PROPERTIES = [
    "agentType", "roleType", "identifierType", "identifierValue",
    "processType",
    "validFrom", "validUntil", "name", "description", "version",
    "hasGeometry", "geoCoordinates", "address", "endpoint",
]


@pytest.mark.parametrize("prop_name", EXPECTED_DATATYPE_PROPERTIES)
def test_datatype_properties_exist(core_graph, prop_name):
    """All 12 datatype properties must be declared."""
    uri = SDATA[prop_name]
    assert (uri, RDF.type, URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")) in core_graph, \
        f"sdata:{prop_name} not declared as owl:DatatypeProperty"


def test_core_class_count(core_graph):
    """Core must have exactly 12 classes."""
    classes = set(core_graph.subjects(RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")))
    sdata_classes = {c for c in classes if str(c).startswith(str(SDATA))}
    assert len(sdata_classes) == 12, f"Expected 12 classes, found {len(sdata_classes)}: {sdata_classes}"


# ─── SHACL Validation ────────────────────────────────────────────────────────

def test_shacl_battery_passport():
    """Example data must conform to SHACL shapes."""
    pyshacl = pytest.importorskip("pyshacl")

    data_graph = Graph()
    data_graph.parse(ROOT / "examples" / "battery-passport.ttl", format="turtle")

    shapes_graph = Graph()
    shapes_graph.parse(ROOT / "shapes" / "sdata-core-shapes.ttl", format="turtle")

    conforms, results_graph, results_text = pyshacl.validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference="none",
    )
    assert conforms, f"SHACL validation failed:\n{results_text}"


# ─── Example Data Completeness ───────────────────────────────────────────────

def test_example_uses_all_classes(example_graph):
    """Battery passport example should instantiate all 12 core classes."""
    for class_name in EXPECTED_CLASSES:
        uri = SDATA[class_name]
        instances = list(example_graph.subjects(RDF.type, uri))
        assert len(instances) > 0, f"No instances of sdata:{class_name} in example"

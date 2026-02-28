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
    # Dimension layer (v0.4.0)
    "Artifact", "Substance", "Agent", "Process", "Site",
    # Leaf layer
    "MaterialArtifact", "Material", "MaterialAgent", "MaterialProcess", "MaterialSite",
    "InformationArtifact", "Information", "InformationAgent", "InformationProcess", "InformationSite",
    # Orthogonal layer
    "Identifier", "Role",
]


@pytest.mark.parametrize("class_name", EXPECTED_CLASSES)
def test_core_classes_exist(core_graph, class_name):
    """All core classes must be declared."""
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
    """All datatype properties must be declared."""
    uri = SDATA[prop_name]
    assert (uri, RDF.type, URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")) in core_graph, \
        f"sdata:{prop_name} not declared as owl:DatatypeProperty"


def test_core_class_count(core_graph):
    """Core must have exactly 17 classes."""
    classes = set(core_graph.subjects(RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")))
    sdata_classes = {c for c in classes if str(c).startswith(str(SDATA))}
    assert len(sdata_classes) == 17, f"Expected 17 classes, found {len(sdata_classes)}: {sdata_classes}"


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

def test_example_uses_leaf_and_orthogonal_classes(example_graph):
    """Battery passport example should instantiate all 12 leaf/orthogonal classes."""
    for class_name in [
        "MaterialArtifact", "Material", "MaterialAgent", "MaterialProcess", "MaterialSite",
        "InformationArtifact", "Information", "InformationAgent", "InformationProcess",
        "InformationSite", "Identifier", "Role",
    ]:
        uri = SDATA[class_name]
        instances = list(example_graph.subjects(RDF.type, uri))
        assert len(instances) > 0, f"No instances of sdata:{class_name} in example"


def test_example_covers_dimension_classes_via_leafs(example_graph):
    """Dimension classes must be covered by corresponding leaf instances in the example."""
    dimension_to_leafs = {
        "Artifact": ("MaterialArtifact", "InformationArtifact"),
        "Substance": ("Material", "Information"),
        "Agent": ("MaterialAgent", "InformationAgent"),
        "Process": ("MaterialProcess", "InformationProcess"),
        "Site": ("MaterialSite", "InformationSite"),
    }
    for dimension, leafs in dimension_to_leafs.items():
        covered = any(list(example_graph.subjects(RDF.type, SDATA[leaf])) for leaf in leafs)
        assert covered, f"sdata:{dimension} is not covered by any leaf instance in example"

"""Tests for sdata-core ontology and instance data (v0.6.0)."""

from pathlib import Path

import pytest
from rdflib import Graph, Namespace, RDF, URIRef

SDATA = Namespace("https://w3id.org/sdata/core/")
ROOT = Path(__file__).resolve().parent.parent
OWL_CLASS = URIRef("http://www.w3.org/2002/07/owl#Class")
OWL_OBJ_PROP = URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")
OWL_DATA_PROP = URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")


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


@pytest.mark.parametrize("ttl_file", sorted(ROOT.glob("**/*.ttl")))
def test_turtle_syntax(ttl_file):
    """All .ttl files must parse without error."""
    g = Graph()
    g.parse(ttl_file, format="turtle")
    assert len(g) > 0, f"{ttl_file.name} contains no triples"


EXPECTED_CLASSES = [
    "Activity",
    "Agent",
    "Assembly",
    "AssemblyProcess",
    "AttributeQuantityValue",
    "Certificate",
    "ChemicalAnalysis",
    "CoatingProcess",
    "Component",
    "CrashSimulation",
    "Data",
    "Experiment",
    "FormingProcess",
    "HeatTreatment",
    "HumanAgent",
    "JoiningProcess",
    "MachineAgent",
    "ManufacturingProcess",
    "Material",
    "MaterialProperty",
    "MeasurementData",
    "MechanicalTest",
    "Metadata",
    "MetallographicExamination",
    "Model",
    "Object",
    "Organization",
    "Passport",
    "ProcessData",
    "Product",
    "RawMaterial",
    "Recyclate",
    "RecyclingProcess",
    "SemiFinishedProduct",
    "Simulation",
    "SimulationResult",
    "SoftwareAgent",
    "Specimen",
    "Table",
    "Tool",
    "Transport",
    "ValueDomain",
]


@pytest.mark.parametrize("class_name", EXPECTED_CLASSES)
def test_core_classes_exist(core_graph, class_name):
    uri = SDATA[class_name]
    assert (uri, RDF.type, OWL_CLASS) in core_graph, f"sdata:{class_name} not declared as owl:Class"


EXPECTED_OBJECT_PROPERTIES = [
    "certifiedBy",
    "describes",
    "hasData",
    "hasInput",
    "hasOutput",
    "hasPassport",
    "hasQuantity",
    "hasValueDomain",
    "isQuantityOf",
    "isValueDomainOf",
    "performedBy",
    "performs",
    "producedBy",
    "producesData",
    "resultOf",
    "undergoes",
    "usesTool",
]


@pytest.mark.parametrize("prop_name", EXPECTED_OBJECT_PROPERTIES)
def test_object_properties_exist(core_graph, prop_name):
    uri = SDATA[prop_name]
    assert (uri, RDF.type, OWL_OBJ_PROP) in core_graph, (
        f"sdata:{prop_name} not declared as owl:ObjectProperty"
    )


EXPECTED_DATATYPE_PROPERTIES = [
    "domainDescription",
    "dtype",
    "hasIdentifier",
    "hasStandard",
    "hasUnit",
    "hasValue",
    "hasVersion",
    "unitSymbol",
]


@pytest.mark.parametrize("prop_name", EXPECTED_DATATYPE_PROPERTIES)
def test_datatype_properties_exist(core_graph, prop_name):
    uri = SDATA[prop_name]
    assert (uri, RDF.type, OWL_DATA_PROP) in core_graph, (
        f"sdata:{prop_name} not declared as owl:DatatypeProperty"
    )


def test_core_class_count(core_graph):
    classes = set(core_graph.subjects(RDF.type, OWL_CLASS))
    sdata_classes = {c for c in classes if str(c).startswith(str(SDATA))}
    assert len(sdata_classes) == 42, f"Expected 42 classes, found {len(sdata_classes)}"


def test_example_uses_core_categories(example_graph):
    for class_name in ["Object", "Activity", "Data", "Agent"]:
        instances = list(example_graph.subjects(RDF.type, SDATA[class_name]))
        assert instances, f"No instances of sdata:{class_name} in example"


def test_example_uses_representative_domain_classes(example_graph):
    for class_name in [
        "Product",
        "Component",
        "FormingProcess",
        "MechanicalTest",
        "Simulation",
        "Passport",
        "Certificate",
        "HumanAgent",
        "MachineAgent",
        "SoftwareAgent",
        "Organization",
        "AttributeQuantityValue",
        "ValueDomain",
    ]:
        instances = list(example_graph.subjects(RDF.type, SDATA[class_name]))
        assert instances, f"No instances of sdata:{class_name} in example"


def test_example_uses_core_lifecycle_relations(example_graph):
    relation_names = [
        "hasInput",
        "hasOutput",
        "producesData",
        "describes",
        "performedBy",
        "hasPassport",
        "hasData",
    ]
    for relation in relation_names:
        predicate = SDATA[relation]
        triples = list(example_graph.triples((None, predicate, None)))
        assert triples, f"No triples using sdata:{relation} in example"

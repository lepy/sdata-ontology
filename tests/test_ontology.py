"""Tests for sdata-core ontology and instance data (v0.9.2)."""

from pathlib import Path

import pytest
from rdflib import Graph, Namespace, RDF, RDFS, URIRef

SDATA = Namespace("https://w3id.org/sdata/core/")
SMS = Namespace("https://w3id.org/sdata/material-state/")
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


@pytest.fixture(scope="session")
def material_state_graph():
    g = Graph()
    g.parse(ROOT / "sdata-material-state.ttl", format="turtle")
    return g


@pytest.mark.parametrize("ttl_file", sorted(ROOT.glob("**/*.ttl")))
def test_turtle_syntax(ttl_file):
    """All .ttl files must parse without error."""
    g = Graph()
    g.parse(ttl_file, format="turtle")
    assert len(g) > 0, f"{ttl_file.name} contains no triples"


EXPECTED_CLASSES = [
    "Object",
    "Material",
    "Product",
    "Hardware",
    "Software",
    "Data",
    "Process",
    "Agent",
    "Person",
    "HardwareAgent",
    "SoftwareAgent",
    "Organization",
    "AttributeQuantityValue",
    "ValueDomain",
]


@pytest.mark.parametrize("class_name", EXPECTED_CLASSES)
def test_core_classes_exist(core_graph, class_name):
    uri = SDATA[class_name]
    assert (uri, RDF.type, OWL_CLASS) in core_graph, f"sdata:{class_name} not declared as owl:Class"


EXPECTED_OBJECT_PROPERTIES = [
    "hasInput",
    "hasOutput",
    "undergoes",
    "resultOf",
    "madeOf",
    "producesData",
    "producedBy",
    "describes",
    "hasData",
    "hasDPP",
    "performedBy",
    "performs",
    "certifiedBy",
    "usesHardware",
    "usesSoftware",
    "hasQuantity",
    "isQuantityOf",
    "hasValueDomain",
    "isValueDomainOf",
]


@pytest.mark.parametrize("prop_name", EXPECTED_OBJECT_PROPERTIES)
def test_object_properties_exist(core_graph, prop_name):
    uri = SDATA[prop_name]
    assert (uri, RDF.type, OWL_OBJ_PROP) in core_graph, (
        f"sdata:{prop_name} not declared as owl:ObjectProperty"
    )


EXPECTED_DATATYPE_PROPERTIES = [
    "hasIdentifier",
    "hasStandard",
    "hasVersion",
    "unitSymbol",
    "dtype",
    "domainDescription",
    "hasValue",
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
    assert len(sdata_classes) == 14, f"Expected 14 classes, found {len(sdata_classes)}"


def _instances_of_class_or_subclass(example_graph: Graph, core_graph: Graph, class_uri: URIRef) -> set[URIRef]:
    candidate_classes: set[URIRef] = {class_uri}
    queue = [class_uri]
    while queue:
        parent = queue.pop()
        for child in core_graph.subjects(RDFS.subClassOf, parent):
            if isinstance(child, URIRef) and child not in candidate_classes:
                candidate_classes.add(child)
                queue.append(child)

    instances: set[URIRef] = set()
    for candidate in candidate_classes:
        instances.update(
            instance
            for instance in example_graph.subjects(RDF.type, candidate)
            if isinstance(instance, URIRef)
        )
    return instances


def test_example_uses_core_categories(example_graph, core_graph):
    for class_name in ["Object", "Process", "Data", "Agent"]:
        instances = _instances_of_class_or_subclass(example_graph, core_graph, SDATA[class_name])
        assert instances, f"No instances of sdata:{class_name} in example"


def test_example_uses_representative_domain_classes(example_graph, core_graph):
    for class_name in [
        "Material",
        "Product",
        "Hardware",
        "Software",
        "Data",
        "Process",
        "Person",
        "HardwareAgent",
        "SoftwareAgent",
        "Organization",
        "AttributeQuantityValue",
        "ValueDomain",
    ]:
        instances = _instances_of_class_or_subclass(example_graph, core_graph, SDATA[class_name])
        assert instances, f"No instances of sdata:{class_name} in example"


def test_example_uses_core_lifecycle_relations(example_graph):
    relation_names = [
        "hasInput",
        "hasOutput",
        "producesData",
        "describes",
        "performedBy",
        "madeOf",
        "hasDPP",
        "hasData",
        "usesHardware",
        "usesSoftware",
    ]
    for relation in relation_names:
        predicate = SDATA[relation]
        triples = list(example_graph.triples((None, predicate, None)))
        assert triples, f"No triples using sdata:{relation} in example"


def test_material_state_module_core_terms_exist(material_state_graph):
    for class_name in [
        "StateAxis",
        "StateAssignment",
        "OriginAxis",
        "ProcessingAxis",
        "ConditionAxis",
        "FormAxis",
        "GradeAxis",
        "ComplianceAxis",
        "CompositionAxis",
        "LifecyclePhaseAxis",
        "StructureAxis",
        "RoleAxis",
        "MethodAxis",
        "DomainAxis",
        "DataTypeAxis",
    ]:
        assert (SMS[class_name], RDF.type, OWL_CLASS) in material_state_graph

    for prop_name in ["hasConceptScheme", "hasStateAssignment", "hasStateValue", "onAxis"]:
        assert (SMS[prop_name], RDF.type, OWL_OBJ_PROP) in material_state_graph


def test_example_uses_material_state_assignments(example_graph):
    assert list(example_graph.triples((None, SMS.hasStateAssignment, None)))
    assert list(example_graph.triples((None, SMS.onAxis, None)))
    assert list(example_graph.triples((None, SMS.hasStateValue, None)))

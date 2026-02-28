import rdflib
from rdflib import Graph, Literal, RDF, URIRef, Namespace, XSD
from rdflib.namespace import RDFS, OWL, DC, DCTERMS, PROV

# Define namespaces based on the sdata Core Ontology
SDATA = Namespace("https://w3id.org/sdata/core/")
BFO = Namespace("http://purl.obolibrary.org/obo/BFO_")
QUDT = Namespace("http://qudt.org/schema/qudt/")
SAGENTS = Namespace("https://w3id.org/sdata/vocab/agents#")

# Example namespace for instances (e.g., for a specific DPP)
EX = Namespace("https://example.org/dpp/battery/")


class DigitalProductPassport:
    """
    Python-Implementierung eines Digitalen Produktpasses (DPP) basierend auf der sdata Core Ontology.
    Diese Klasse modelliert einen DPP als InformationArtifact, das ein MaterialArtifact repräsentiert.
    Integriert Data Provenance (über PROV-O-Alignment) und digitale Identifikatoren (Identifier-Klasse).

    Funktionalitäten:
    - Erstellung von Instanzen für Produkte, Prozesse, Agenten, etc.
    - Hinzufügen von Provenance (z.B. Herstellungsprozess, Agenten).
    - Management multipler digitaler Identifikatoren (z.B. Serial, GTIN, DID).
    - Serialisierung des Graphs als Turtle oder JSON-LD.

    Verwendung:
    dpp = DigitalProductPassport()
    dpp.create_sample_dpp()
    print(dpp.serialize(format='turtle'))
    """

    def __init__(self):
        self.graph = Graph()
        # Bind namespaces for easier serialization
        self.graph.bind("rdf", RDF)
        self.graph.bind("rdfs", RDFS)
        self.graph.bind("owl", OWL)
        self.graph.bind("xsd", XSD)
        self.graph.bind("prov", PROV)
        self.graph.bind("bfo", BFO)
        self.graph.bind("qudt", QUDT)
        self.graph.bind("dc", DC)
        self.graph.bind("dcterms", DCTERMS)
        self.graph.bind("sdata", SDATA)
        self.graph.bind("sagents", SAGENTS)
        self.graph.bind("ex", EX)

        # Optional: Load the core ontology if provided as string (for validation, but skipped for simplicity)
        # self.graph.parse(data=ONTOLOGY_TTL, format='turtle')  # ONTOLOGY_TTL would be the provided Turtle string

    def add_physical_artifact(self, uri, name, description):
        """Erstellt ein MaterialArtifact (z.B. ein Produkt wie eine Batterie)."""
        self.graph.add((uri, RDF.type, SDATA.MaterialArtifact))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.description, Literal(description, lang="de")))
        return uri

    def add_digital_artifact(self, uri, name, version, represents=None, valid_from=None, valid_until=None):
        """Erstellt ein InformationArtifact (z.B. den DPP selbst)."""
        self.graph.add((uri, RDF.type, SDATA.InformationArtifact))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.version, Literal(version)))
        if represents:
            self.graph.add((uri, SDATA.represents, represents))
        if valid_from:
            self.graph.add((uri, SDATA.validFrom, Literal(valid_from, datatype=XSD.dateTimeStamp)))
        if valid_until:
            self.graph.add((uri, SDATA.validUntil, Literal(valid_until, datatype=XSD.dateTimeStamp)))
        return uri

    def add_identifier(self, uri, id_type, id_value, target_entity):
        """Fügt einen digitalen Identifikator hinzu (z.B. Serialnummer, GTIN)."""
        self.graph.add((uri, RDF.type, SDATA.Identifier))
        self.graph.add((uri, SDATA.identifierType, Literal(id_type)))
        self.graph.add((uri, SDATA.identifierValue, Literal(id_value)))
        self.graph.add((target_entity, SDATA.hasIdentifier, uri))
        return uri

    def add_agent(self, uri, name, agent_type, agent_class=SDATA.InformationAgent):
        """Erstellt einen Agenten mit expliziter Klassenwahl (MaterialAgent oder InformationAgent)."""
        self.graph.add((uri, RDF.type, agent_class))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.agentType, Literal(agent_type)))
        return uri

    def add_process(
        self,
        uri,
        name,
        description,
        performed_by=None,
        generates=None,
        consumes=None,
        started_at=None,
        ended_at=None,
        process_class=SDATA.MaterialProcess,
    ):
        """Erstellt einen Process mit Provenance (z.B. Herstellungsprozess).
        Nutzt PROV-O-Alignment für Data Provenance."""
        self.graph.add((uri, RDF.type, process_class))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.description, Literal(description, lang="de")))
        if performed_by:
            self.graph.add((uri, SDATA.wasPerformedBy, performed_by))
            # PROV-Alignment
            self.graph.add((uri, PROV.wasAssociatedWith, performed_by))
        if generates:
            self.graph.add((uri, SDATA.generates, generates))
            # PROV-Alignment
            self.graph.add((uri, PROV.generated, generates))
        if consumes:
            self.graph.add((uri, SDATA.consumes, consumes))
            # PROV-Alignment
            self.graph.add((uri, PROV.used, consumes))
        if started_at:
            self.graph.add((uri, PROV.startedAtTime, Literal(started_at, datatype=XSD.dateTimeStamp)))
        if ended_at:
            self.graph.add((uri, PROV.endedAtTime, Literal(ended_at, datatype=XSD.dateTimeStamp)))
        return uri

    def add_material(self, uri, name, description):
        """Erstellt ein Material (z.B. Lithium für die Batterie)."""
        self.graph.add((uri, RDF.type, SDATA.Material))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.description, Literal(description, lang="de")))
        return uri

    def add_site(self, uri, name, address, geo_coords=None):
        """Erstellt einen MaterialSite (z.B. Produktionsstandort)."""
        self.graph.add((uri, RDF.type, SDATA.MaterialSite))
        self.graph.add((uri, SDATA.name, Literal(name, lang="de")))
        self.graph.add((uri, SDATA.address, Literal(address)))
        if geo_coords:
            self.graph.add((uri, SDATA.geoCoordinates, Literal(geo_coords)))
        return uri

    def create_sample_dpp(self):
        """Beispiel: DPP für eine Batterie mit Provenance und Identifikatoren."""
        # MaterialArtifact: Die Batterie-Instanz
        battery = self.add_physical_artifact(EX.battery_instance, "Batterie XYZ",
                                             "Eine spezifische Lithium-Ionen-Batterie für Elektrofahrzeuge.")

        # Material: Lithium-Charge, aus der die Batterie besteht
        lithium = self.add_material(EX.lithium_material, "Lithium-Charge", "Recycelte Lithium-Charge für Batterien.")
        self.graph.add((battery, SDATA.consistsOf, lithium))

        # Site: Produktionsstandort
        factory_site = self.add_site(EX.factory_site, "Fabrik Berlin", "Berlin, Deutschland", "52.5200,13.4050")
        self.graph.add((battery, SDATA.locatedAt, factory_site))

        # Agent: Hersteller (Organisation)
        manufacturer = self.add_agent(
            EX.manufacturer_org,
            "BatteryCorp GmbH",
            "Organization",
            agent_class=SDATA.InformationAgent,  # Aus sdata-agents vocab
        )

        # Process: Herstellungsprozess (Provenance)
        manufacturing_process = self.add_process(
            EX.manufacturing_process,
            "Herstellungsprozess",
            "Produktion der Batterie aus Lithium-Material.",
            performed_by=manufacturer,
            consumes=lithium,
            generates=battery,
            started_at="2026-01-01T00:00:00Z",
            ended_at="2026-01-15T00:00:00Z",
            process_class=SDATA.MaterialProcess,
        )

        # InformationArtifact: Der DPP selbst
        dpp = self.add_digital_artifact(
            EX.dpp_document,
            "Digitaler Produktpass für Batterie XYZ",
            "1.0",
            represents=battery,
            valid_from="2026-02-26T00:00:00Z",
            valid_until="2036-02-26T00:00:00Z"
        )

        # Identifier: Mehrere digitale Identifikatoren für die Batterie
        self.add_identifier(EX.serial_id, "SerialNumber", "BAT-123456789", battery)
        self.add_identifier(EX.gtin_id, "GTIN", "0123456789012", battery)
        self.add_identifier(EX.did_id, "DID", "did:example:123456789abcdefghi", battery)

        # Provenance für den DPP: Generiert durch einen Software-Agent
        software_agent = self.add_agent(
            EX.dpp_generator,
            "DPP-Generator-Software",
            "Software",
            agent_class=SDATA.InformationAgent,  # Aus sdata-agents vocab
        )
        dpp_generation_process = self.add_process(
            EX.dpp_generation_process,
            "DPP-Generierungsprozess",
            "Erstellung des DPP basierend auf Produktionsdaten.",
            performed_by=software_agent,
            generates=dpp,
            started_at="2026-02-26T10:00:00Z",
            ended_at="2026-02-26T10:05:00Z",
            process_class=SDATA.InformationProcess,
        )

    def serialize(self, format='turtle'):
        """Serialisiert den Graph als String (Turtle, JSON-LD, etc.)."""
        return self.graph.serialize(format=format)


# Beispielnutzung
if __name__ == "__main__":
    dpp = DigitalProductPassport()
    dpp.create_sample_dpp()
    print(dpp.serialize(format='turtle'))

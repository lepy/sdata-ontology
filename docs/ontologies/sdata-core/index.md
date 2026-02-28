# sdata-core.ttl

Das Kernmodul definiert ein 17-Klassen-Modell:

- 5 Dimensionen: `Artifact`, `Substance`, `Agent`, `Process`, `Site`
- 10 Leaf-Klassen: Material-/Information-Duale
- 2 orthogonale Klassen: `Role`, `Identifier`

Zusätzlich enthält es die zentralen Objekt- und Datentyp-Properties für Instanzdaten und Provenance.

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix prov:  <http://www.w3.org/ns/prov#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Labor1 a sdata:MaterialSite ;
  sdata:name "Werkstofflabor 1" .

ex:Probe_A1 a sdata:MaterialArtifact ;
  sdata:name "Zugprobe A1" ;
  sdata:locatedAt ex:Labor1 .

ex:Messmaschine_Z100 a sdata:MaterialAgent ;
  sdata:name "Zwick Z100" ;
  sdata:agentType "Hardware" ;
  sdata:locatedAt ex:Labor1 .

ex:KraftWegKurve_A1 a sdata:InformationArtifact ;
  sdata:name "Kraft-Weg-Kurve A1" ;
  sdata:represents ex:Probe_A1 .

ex:Zugversuch_A1 a sdata:MaterialProcess ;
  sdata:name "Zugversuch Probe A1" ;
  sdata:consumes ex:Probe_A1 ;
  sdata:generates ex:KraftWegKurve_A1 ;
  sdata:wasPerformedBy ex:Messmaschine_Z100 ;
  sdata:locatedAt ex:Labor1 ;
  prov:startedAtTime "2026-02-20T09:15:00Z"^^xsd:dateTimeStamp ;
  prov:endedAtTime   "2026-02-20T09:45:00Z"^^xsd:dateTimeStamp .
```

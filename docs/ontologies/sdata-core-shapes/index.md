# shapes/sdata-core-shapes.ttl

SHACL-Validierungsregeln für Instanzdaten (z. B. Pflichtfelder, Datentypen, Konsistenzregeln).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix prov:  <http://www.w3.org/ns/prov#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

# Erfüllt MaterialProcessShape: name + wasPerformedBy + Zeitlogik
ex:Zugversuch_A1
  a sdata:MaterialProcess ;
  sdata:name "Zugversuch A1" ;
  sdata:wasPerformedBy ex:Messmaschine_Z100 ;
  prov:startedAtTime "2026-02-20T09:15:00Z"^^xsd:dateTimeStamp ;
  prov:endedAtTime   "2026-02-20T09:45:00Z"^^xsd:dateTimeStamp .
```

Validierung lokal:

```bash
pyshacl -s shapes/sdata-core-shapes.ttl -df turtle examples/tensiontest-crashsimulation.ttl
```

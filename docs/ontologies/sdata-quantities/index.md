# sdata-quantities.ttl

Fuehrt `sdata:AttributeQuantityValue` und `sdata:ValueDomain` ein, um Messgroessen
mit Einheit und Wertebereich zu modellieren.

Aktueller Stand: `v0.1.1`.

## Kernpunkte

- Importiert `sdata-core` und `MIN`.
- `sdata:AttributeQuantityValue` ist `subClassOf qudt:QuantityValue` und `sdata:Data`.
- `sdata:ValueDomain` ist `subClassOf sdata:Data`.
- `sdata:hasQuantity` ist auf `min:Nexus` definiert (Objekt, Prozess, Data, Agent).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix qudt:  <http://qudt.org/schema/qudt/> .
@prefix unit:  <http://qudt.org/vocab/unit/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Probe_A1 sdata:hasQuantity ex:Rm_A1 .

ex:Rm_A1 a sdata:AttributeQuantityValue ;
  min:hasIdentifier "AQV-RM-A1" ;
  sdata:dtype "float" ;
  qudt:numericValue "312.4"^^xsd:double ;
  qudt:unit unit:MegaPA ;
  sdata:unitSymbol "MPa" ;
  sdata:hasValueDomain ex:RmDomain .

ex:RmDomain a sdata:ValueDomain ;
  sdata:domainDescription "Zulässiger Wertebereich für Rm" .
```

# sdata-quantities.ttl

Führt `sdata:AttributeQuantityValue` und `sdata:ValueDomain` ein, um Messgrößen mit Einheit und Wertebereich zu modellieren.

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix qudt:  <http://qudt.org/schema/qudt/> .
@prefix unit:  <http://qudt.org/vocab/unit/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Probe_A1 sdata:hasQuantity ex:Rm_A1 .

ex:Rm_A1 a sdata:AttributeQuantityValue ;
  sdata:name "Rm" ;
  sdata:description "Zugfestigkeit" ;
  sdata:dtype "float" ;
  qudt:numericValue "312.4"^^xsd:double ;
  qudt:unit unit:MegaPA ;
  sdata:unitSymbol "MPa" ;
  sdata:hasValueDomain ex:RmDomain .

ex:RmDomain a sdata:ValueDomain ;
  sdata:domainDescription "Zulässiger Wertebereich für Rm" .
```

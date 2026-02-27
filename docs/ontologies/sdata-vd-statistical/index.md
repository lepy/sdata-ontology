# sdata-vd-statistical.ttl

Spezialisiert `ValueDomain` für statistische Verteilungen und optionale Abschneidung via `sdata:truncatedBy`.

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:RmNormalDomain
  a sdata:NormalDomain ;
  sdata:mu "305.0"^^xsd:double ;
  sdata:sigma "11.5"^^xsd:double ;
  sdata:truncatedBy ex:RmBounds ;
  sdata:domainDescription "Verteilung der Zugfestigkeit Rm" .

ex:RmBounds
  a sdata:IntervalDomain ;
  sdata:minValue "260.0"^^xsd:double ;
  sdata:maxValue "360.0"^^xsd:double .
```

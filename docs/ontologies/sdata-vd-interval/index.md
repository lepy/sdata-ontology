# sdata-vd-interval.ttl

Spezialisiert `ValueDomain` als Intervall mit expliziter Grenzsemantik (`minInclusive`, `maxInclusive`).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DehnungBisBruchDomain
  a sdata:IntervalDomain ;
  sdata:minValue "18.0"^^xsd:double ;
  sdata:maxValue "32.0"^^xsd:double ;
  sdata:minInclusive "true"^^xsd:boolean ;
  sdata:maxInclusive "false"^^xsd:boolean ;
  sdata:domainDescription "A80 in [18, 32) Prozent" .
```

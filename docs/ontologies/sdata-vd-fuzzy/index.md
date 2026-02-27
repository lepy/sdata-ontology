# sdata-vd-fuzzy.ttl

Spezialisiert `ValueDomain` für unscharfe Zahlen (triangular, trapezoidal, gaussian, L-R).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:RmFuzzyDomain
  a sdata:TriangularFuzzyDomain ;
  sdata:fuzzyLeft "285.0"^^xsd:double ;
  sdata:fuzzyPeak "303.0"^^xsd:double ;
  sdata:fuzzyRight "320.0"^^xsd:double ;
  sdata:alphaLevel "1.0"^^xsd:double ;
  sdata:domainDescription "Unscharfer Rm-Bereich bei Messrauschen" .
```

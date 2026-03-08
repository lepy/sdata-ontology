# sdata-vd-enum.ttl

Spezialisiert `ValueDomain` für endliche Wertelisten (`allowedValue`) oder SKOS-Schemata (`allowedScheme`).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:ProbenOrientierungDomain
  a sdata:EnumeratedDomain ;
  sdata:allowedValue "0" , "45" , "90" ;
  sdata:domainDescription "Walzrichtung in Grad" .
```

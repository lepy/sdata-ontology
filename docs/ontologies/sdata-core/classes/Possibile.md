# sdata:Possibile
## IRI
`https://w3id.org/sdata/core/Possibile`
## Labels
- `Possibile`
- `Possibile`
## Direct Superclasses
- `min:Possibile`
## Direct Subclasses
- [`sdata:Scenario`](./Scenario.md)
## Comment
Fassade für min:Possibile. Möglichkeitsraum.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Possibile` zur semantischen Modellierung eingesetzt wird.
ex:possibile_001 a sdata:Possibile ;
  sdata:hasIdentifier "POSSIBILE-001" ;
  sdata:hasName "Possibile 30 Prozent Rezyklat" ;
  sdata:concerns ex:asset_001 ;
  sdata:alternativeTo ex:possibile_002 .

ex:possibile_002 a sdata:Possibile ; sdata:concerns ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Possibile .
```

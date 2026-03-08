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
Fassade für min:Possibile. Das, was sein könnte.
    Möglichkeitsraum.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Possibile` zur semantischen Modellierung eingesetzt wird.
ex:possibile_001 a sdata:Possibile ;
  min:hasIdentifier "POSSIBILE-001" ;
  min:hasName "Possibile 30 Prozent Rezyklat" ;
  min:concerns ex:product_001 ;
  min:alternativeTo ex:possibile_002 .

ex:possibile_002 a sdata:Possibile ; min:concerns ex:product_001 .
ex:product_001 a sdata:Product .
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

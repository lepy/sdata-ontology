# sdata:Norma
## IRI
`https://w3id.org/sdata/core/Norma`
## Labels
- `Norma`
- `Norma`
## Direct Superclasses
- `min:Norma`
## Direct Subclasses
- [`sdata:Requirement`](./Requirement.md)
## Comment
Fassade für min:Norma. Das, was gelten soll.
    Anforderung.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Norma` zur semantischen Modellierung eingesetzt wird.
ex:norma_001 a sdata:Norma ;
  min:hasIdentifier "NORMA-001" ;
  min:hasName "Norma Leitfaehigkeitsgrenze" ;
  min:evaluates ex:result_001 .

ex:result_001 a sdata:Result ; sdata:assessmentOutcome "pass" .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Norma .
```

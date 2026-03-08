# sdata:ProcessType
## IRI
`https://w3id.org/sdata/core/ProcessType`
## Labels
- `Process Type`
- `Verfahrenstyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Verfahrens. Nicht Specification.

## Examples
- `Zugversuch nach ISO 6892-1, Tiefziehen, Crashsimulation.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung als `Kaltumformung` innerhalb der Prozessklassifikation.
ex:process_type_001 a sdata:ProcessType ;
  sdata:hasIdentifier "PROCESSTYPE-001" ;
  sdata:hasName "ProcessType Klassifikation" ;
  sdata:typifies ex:process_001 .

ex:process_001 a sdata:Process .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ProcessType .
```

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
(none)

## Examples
- `Zugversuch nach ISO 6892-1, Tiefziehen, Crashsimulation.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Zugversuchstyp nach ISO 6892-1.
ex:zugversuch_typ a sdata:ProcessType ;
    sdata:hasName "Zugversuch nach ISO 6892-1" ;
    sdata:typifies ex:zugversuch_001 .
ex:zugversuch_001 a sdata:Process .
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

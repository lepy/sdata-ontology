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
Fassade für min:Norma. Anforderung.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Norma ist eine Fassade — verwende sdata:Requirement.
ex:req_rm a sdata:Requirement ;
    sdata:hasName "Rm ≥ 340 MPa" ;
    sdata:evaluates ex:probe_42 .
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

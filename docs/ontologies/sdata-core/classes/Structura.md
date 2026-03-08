# sdata:Structura
## IRI
`https://w3id.org/sdata/core/Structura`
## Labels
- `Structura`
- `Structura`
## Direct Superclasses
- `min:Structura`
## Direct Subclasses
- [`sdata:Model`](./Model.md)
## Comment
Fassade für min:Structura. Formale Struktur.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Structura ist eine Fassade — verwende sdata:Model.
ex:von_mises a sdata:Model ;
    sdata:hasName "von-Mises-Fließkriterium" ;
    sdata:typifiedBy ex:materialmodell_typ .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Structura .
```

# sdata:BoundaryType
## IRI
`https://w3id.org/sdata/core/BoundaryType`
## Labels
- `Boundary Type`
- `Grenzflächentyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Coulomb-Reibung, Σ3-CSL-Korngrenze, thermischer Kontaktwiderstand.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Coulomb-Reibungsmodell als Grenzflächentyp.
ex:coulomb_reibung a sdata:BoundaryType ;
    sdata:hasName "Coulomb-Reibung" ;
    sdata:typifies ex:reibung_werkzeug_blech .
ex:reibung_werkzeug_blech a sdata:Boundary .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:BoundaryType .
```

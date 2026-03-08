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

# Typisierung einer Grenze als `Cradle-to-Gate` fuer ein DPP-LCA-Modell.
ex:boundary_type_001 a sdata:BoundaryType ;
  sdata:hasIdentifier "BOUNDARYTYPE-001" ;
  sdata:hasName "BoundaryType Klassifikation" ;
  sdata:typifies ex:boundary_001 .

ex:boundary_001 a sdata:Boundary .
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

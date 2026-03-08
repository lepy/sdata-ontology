# sdata:Boundary
## IRI
`https://w3id.org/sdata/core/Boundary`
## Labels
- `Boundary`
- `Grenze`
## Direct Superclasses
- `min:Boundary`
## Direct Subclasses
- (none)
## Comment
Typisierung über sdata:BoundaryType.

## Examples
- `Übergangswiderstand, Reibung, Adhäsion, Korngrenze.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Reibkontakt zwischen Werkzeug und Blech beim Tiefziehen.
ex:reibung_001 a sdata:Boundary ;
    sdata:hasName "Kontakt Werkzeug–Blech" ;
    sdata:bounds ex:werkzeug_001 ;
    sdata:bounds ex:blech_042 ;
    sdata:typifiedBy ex:coulomb_typ .
ex:werkzeug_001 a sdata:Hardware .
ex:blech_042 a sdata:Hardware .
ex:coulomb_typ a sdata:BoundaryType ;
    sdata:hasName "Coulomb-Reibung" .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Boundary .
```

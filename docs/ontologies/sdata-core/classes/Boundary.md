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

# Bilanzgrenze eines CO2-Footprints von Rohkupfer bis auslieferbares Halbzeug.
ex:boundary_001 a sdata:Boundary ;
  sdata:hasIdentifier "BOUND-001" ;
  sdata:hasName "Kontaktgrenze Werkzeug-Blech" ;
  sdata:bounds ex:tool_001 ;
  sdata:bounds ex:sheet_001 .

ex:tool_001 a sdata:Hardware .
ex:sheet_001 a sdata:Material .
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

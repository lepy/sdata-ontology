# sdata:MaterialGrade
## IRI
`https://w3id.org/sdata/core/MaterialGrade`
## Labels
- `Material Grade`
- `Werkstoffsorte`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Werkstoffs. DPP-Feld ‹Werkstoffbezeichnung›.

## Examples
- `DC04, HC340LA, AlSi10Mg, PP-GF30, X5CrNi18-10.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Werkstoffguete `Cu-OF` zur Typisierung hochreinen Kupfers.
ex:material_grade_001 a sdata:MaterialGrade ;
  min:hasIdentifier "MATERIALGRADE-001" ;
  min:hasName "MaterialGrade Klassifikation" ;
  min:typifies ex:material_001 .

ex:material_001 a sdata:Material .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:MaterialGrade .
```

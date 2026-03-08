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
(none)

## Examples
- `DC04, HC340LA, AlSi10Mg, PP-GF30, X5CrNi18-10.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# DC04 als Werkstoffsorte mit Requirements.
ex:DC04 a sdata:MaterialGrade ;
    sdata:hasName "DC04" ;
    sdata:typifies ex:blech_042 ;
    sdata:comprises ex:req_C_max , ex:req_Rm_270 .
ex:blech_042 a sdata:Hardware .
ex:req_C_max a sdata:Requirement ;
    sdata:hasName "C ≤ 0.08%" .
ex:req_Rm_270 a sdata:Requirement ;
    sdata:hasName "Rm 270–350 MPa" .
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

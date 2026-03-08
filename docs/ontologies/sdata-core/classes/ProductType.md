# sdata:ProductType
## IRI
`https://w3id.org/sdata/core/ProductType`
## Labels
- `Product Type`
- `Produkttyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Produkts, Geräts oder
    Software-Typs. Einheitlicher Typus für Hardware,
    Software und alle anderen typifizierbaren Nexus.
    Ersetzt die ehemaligen Klassen Product, HardwareType
    und SoftwareType.

## Examples
- `Seitenteil, B-Säule, Felge, Universalprüfmaschine, Hydraulische Presse, FE-Solver, CAD-System, LCA-Software.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Seitenteil als Produkttyp (ersetzt ehemalige Klasse Product).
ex:seitenteil_typ a sdata:ProductType ;
    sdata:hasName "Seitenteil" ;
    sdata:typifies ex:seitenteil_001 .
ex:seitenteil_001 a sdata:Hardware .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ProductType .
```

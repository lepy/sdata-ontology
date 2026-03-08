# sdata:Material
## IRI
`https://w3id.org/sdata/core/Material`
## Labels
- `Material`
- `Werkstoff`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Werkstoff als Agent. Wirkt selektiv:
    DC04 verfestigt unter Zug, HC340LA widersteht
    höherer Last, AlSi10Mg leitet Wärme anders als CFK.
    Agent ∩ Object. Identität: material.

    Material = werkstofftechnisch (Gefüge, Zusammensetzung,
    Verarbeitungsgeschichte).
    Substance = stofflich-regulatorisch (CAS, REACH).
    Dasselbe Blech HAT ein Material und ENTHÄLT Substances.

    Klassifizierung: sdata:MaterialGrade.

## Examples
- `HC340LA, PP-GF30, AlSi10Mg, CFK-Prepreg, Recyclat.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Cu-ETP-Bandmaterial als Eingangsrohstoff fuer Stanz-Biege-Teile.
ex:material_001 a sdata:Material ;
  sdata:hasIdentifier "MATERIAL-001" ;
  sdata:hasName "Material als materieller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:hasMaterial`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Material .
```

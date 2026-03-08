# sdata:Material
## IRI
`https://w3id.org/sdata/core/Material`
## Labels
- `Material`
- `Werkstoff`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Ein Werkstoff oder Rohstoff. Physische Substanz, die
    in Fertigungsprozessen verarbeitet wird. Identität über chemische
    Zusammensetzung und Gefügezustand.

## Examples
- `HC340LA, PP-GF30, AlSi10Mg, CFK-Prepreg, Recyclat.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Cu-ETP-Bandmaterial als Eingangsrohstoff fuer Stanz-Biege-Teile.
ex:material_001 a sdata:Material ;
  min:hasIdentifier "MATERIAL-001" ;
  min:hasName "Material Instanz" ;
  min:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
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

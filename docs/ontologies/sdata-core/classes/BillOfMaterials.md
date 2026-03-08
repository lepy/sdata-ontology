# sdata:BillOfMaterials
## IRI
`https://w3id.org/sdata/core/BillOfMaterials`
## Labels
- `Bill of Materials`
- `Stückliste`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Stückliste als Data. sdata:describes Product.
    Rekursiv via sdata:hasComponent. ESPR-Pflichtbestandteil.

## Examples
- `Fahrzeug-BOM, Batterie-BOM, Elektronik-BOM.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Stueckliste eines Kupfer-Kabelsatzes mit Leitern, Isolierung, Steckern und Mengenanteilen.
ex:bill_of_materials_001 a sdata:BillOfMaterials ;
  min:hasIdentifier "BILLOFMATERIALS-001" ;
  min:hasName "BillOfMaterials Datensatz" ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:generates ex:data_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:hasBOM`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:BillOfMaterials .
```

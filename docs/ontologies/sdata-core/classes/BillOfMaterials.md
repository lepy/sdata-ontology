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
Stückliste als Data. sdata:describes ein physisches Ding.
    Rekursiv via sdata:hasComponent.

## Examples
- `Fahrzeug-BOM, Batterie-BOM, Elektronik-BOM.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Stueckliste eines Kupfer-Kabelsatzes mit Leitern, Isolierung, Steckern und Mengenanteilen.
ex:bill_of_materials_001 a sdata:BillOfMaterials ;
  sdata:hasIdentifier "BILLOFMATERIALS-001" ;
  sdata:hasName "BillOfMaterials Datensatz" ;
  sdata:describes ex:asset_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
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

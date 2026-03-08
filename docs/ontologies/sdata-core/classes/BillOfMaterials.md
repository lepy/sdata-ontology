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

# Stückliste einer Karosserie-Baugruppe mit rekursiven Komponenten.
ex:bom_karosserie a sdata:BillOfMaterials ;
    sdata:describes ex:baugruppe_001 ;
    sdata:hasComponent ex:bom_entry_seitenteil ;
    sdata:hasComponent ex:bom_entry_bsaeule .
ex:baugruppe_001 a sdata:Hardware ;
    sdata:typifiedBy ex:baugruppe_typ .
ex:baugruppe_typ a sdata:ProductType ;
    sdata:hasName "Karosserie-Baugruppe" .
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

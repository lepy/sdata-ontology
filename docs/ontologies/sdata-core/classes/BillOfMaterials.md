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
## Industriebeispiel
- Stueckliste eines Kupfer-Kabelsatzes mit Leitern, Isolierung, Steckern und Mengenanteilen.
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

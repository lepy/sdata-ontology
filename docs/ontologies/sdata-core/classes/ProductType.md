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
Wesensbestimmung eines Produkts. Typisiert sdata:Product
    via sdata:typifies. v0.1.0: neu.

## Examples
- `Seitenteil, B-Säule, Felge, Platine, Baugruppe, Coil.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung als `HV-Kabelsatz` fuer Variantensteuerung im PLM.
ex:product_type_001 a sdata:ProductType ;
  sdata:hasIdentifier "PRODUCTTYPE-001" ;
  sdata:hasName "ProductType Klassifikation" ;
  sdata:typifies ex:product_001 .

ex:product_001 a sdata:Product .
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

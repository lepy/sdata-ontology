# sdata:Product
## IRI
`https://w3id.org/sdata/core/Product`
## Labels
- `Product`
- `Produkt`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Ein Erzeugnis, Bauteil oder Halbzeug. Resultat eines
    Fertigungsprozesses. Träger eines Produktpasses. Typisierung
    über sdata:ProductType (sdata:typifiedBy).

## Examples
- `Seitenteil, Motorblock, B-Säule, Felge, Baugruppe.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Kupfer-Stromschiene als Endprodukt fuer E-Mobilitaetsanwendungen.
ex:product_001 a sdata:Product ;
  sdata:hasIdentifier "PRODUCT-001" ;
  sdata:hasName "Product Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- `sdata:hasBOM`
## Used As Range
- `sdata:hasProduct`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Product .
```

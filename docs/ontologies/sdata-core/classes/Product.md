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
## Industriebeispiel
- Kupfer-Stromschiene als Endprodukt fuer E-Mobilitaetsanwendungen.
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

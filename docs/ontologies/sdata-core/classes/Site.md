# sdata:Site
## IRI
`https://w3id.org/sdata/core/Site`
## Labels
- `Site`
- `Standort`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Physischer Standort. Verortung via sdata:locatedAt.

## Examples
- `Werk Duisburg, Presswerk Leipzig, Recyclinganlage Hamburg.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Produktionsstandort mit Giesserei, Walzwerk und Prueflabor.
ex:site_001 a sdata:Site ;
  min:hasIdentifier "SITE-001" ;
  min:hasName "Site Instanz" ;
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
- `sdata:locatedAt`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Site .
```

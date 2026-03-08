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
    Besteht den Selektivitätstest nicht — verortet nur.
    Einziges direkt instanziierbares Object ohne Agency.

## Examples
- `Werk Duisburg, Presswerk Leipzig, Recyclinganlage Hamburg.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Produktionsstandort mit Giesserei, Walzwerk und Prueflabor.
ex:site_001 a sdata:Site ;
  sdata:hasIdentifier "SITE-001" ;
  sdata:hasName "Site Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:site_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process .
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

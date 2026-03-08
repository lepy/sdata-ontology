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

# Werk Duisburg als physischer Standort.
ex:werk_duisburg a sdata:Site ;
    sdata:hasName "Werk Duisburg" ;
    sdata:identifiedBy ex:did_werk .
ex:did_werk a sdata:Identifier .
ex:zwick_z250 a sdata:Hardware ;
    sdata:locatedAt ex:werk_duisburg .
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

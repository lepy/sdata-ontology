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
## Industriebeispiel
- Produktionsstandort mit Giesserei, Walzwerk und Prueflabor.
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

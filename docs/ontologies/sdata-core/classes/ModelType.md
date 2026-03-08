# sdata:ModelType
## IRI
`https://w3id.org/sdata/core/ModelType`
## Labels
- `Model Type`
- `Modelltyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Materialmodell, Kryptoalgorithmus, ML-Architektur, DB-Schema.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Materialmodell als Modelltyp.
ex:materialmodell_typ a sdata:ModelType ;
    sdata:hasName "Materialmodell" ;
    sdata:typifies ex:johnson_cook .
ex:johnson_cook a sdata:Model .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ModelType .
```

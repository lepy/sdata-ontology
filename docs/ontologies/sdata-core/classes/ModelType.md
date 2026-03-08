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

# Typisierung als `Transientes Thermomodell` fuer Simulationsdaten.
ex:model_type_001 a sdata:ModelType ;
  sdata:hasIdentifier "MODELTYPE-001" ;
  sdata:hasName "ModelType Klassifikation" ;
  sdata:typifies ex:model_001 .

ex:model_001 a sdata:Model .
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

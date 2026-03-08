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
Wesensbestimmung eines Modelltyps. Unterscheidet
    physikalische Modelle, kryptographische Verfahren,
    ML-Architekturen, Schemata. v0.1.0: neu.

## Examples
- `Materialmodell, Kryptoalgorithmus, ML-Architektur, DB-Schema.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung als `Transientes Thermomodell` fuer Simulationsdaten.
ex:model_type_001 a sdata:ModelType ;
  min:hasIdentifier "MODELTYPE-001" ;
  min:hasName "ModelType Klassifikation" ;
  min:typifies ex:model_001 .

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

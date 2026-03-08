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
## Industriebeispiel
- Typisierung als `Transientes Thermomodell` fuer Simulationsdaten.
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

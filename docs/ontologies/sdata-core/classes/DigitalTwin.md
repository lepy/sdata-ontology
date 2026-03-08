# sdata:DigitalTwin
## IRI
`https://w3id.org/sdata/core/DigitalTwin`
## Labels
- `Digital Twin`
- `Digitaler Zwilling`
## Direct Superclasses
- [`sdata:Software`](./Software.md)
## Direct Subclasses
- (none)
## Comment
Digitaler Zwilling — Software-Agent, der ein
    physisches Gegenstück beschreibt und dessen Verhalten
    vorhersagt. Spezialisierung von Software (Agent ∩ Data).
    Semantischer Unterschied: DigitalTwin sdata:describes
    immer ein physisches Ding.

## Examples
- `FEM-basierter DZ, Predictive-Maintenance-DZ, Prozess-DZ.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Digitaler Zwilling einer Giesslinie mit Live-Parametern und Historie.
ex:digital_twin_001 a sdata:DigitalTwin ;
  sdata:hasIdentifier "DIGITALTWIN-001" ;
  sdata:hasName "DigitalTwin als informationeller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:describes ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:DigitalTwin .
```

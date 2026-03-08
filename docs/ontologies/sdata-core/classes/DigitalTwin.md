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

# Predictive-Maintenance-Zwilling eines Presswerks.
ex:dz_presse a sdata:DigitalTwin ;
    sdata:describes ex:presse_001 ;
    sdata:encodes ex:johnson_cook ;
    sdata:typifiedBy ex:predictive_twin_typ ;
    sdata:selects ex:szenario_versagen ;
    sdata:hasStatus "running" .
ex:presse_001 a sdata:Hardware .
ex:johnson_cook a sdata:Model .
ex:predictive_twin_typ a sdata:ProductType ;
    sdata:hasName "Predictive Twin" .
ex:szenario_versagen a sdata:Scenario .
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

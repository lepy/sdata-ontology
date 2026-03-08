# sdata:DigitalTwin
## IRI
`https://w3id.org/sdata/core/DigitalTwin`
## Labels
- `Digital Twin`
- `Digitaler Zwilling`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Digitales Abbild. Wenn aktiv: zusätzlich SoftwareAgent.

## Examples
- `FEM-basierter DZ, Predictive-Maintenance-DZ.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Digitaler Zwilling einer Giesslinie mit Live-Parametern und Historie.
ex:digital_twin_001 a sdata:DigitalTwin ;
  min:hasIdentifier "DIGITALTWIN-001" ;
  min:hasName "DigitalTwin Datensatz" ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:generates ex:data_001 .
ex:product_001 a sdata:Product .
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

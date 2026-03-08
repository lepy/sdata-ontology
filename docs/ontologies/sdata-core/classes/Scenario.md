# sdata:Scenario
## IRI
`https://w3id.org/sdata/core/Scenario`
## Labels
- `Scenario`
- `Szenario`
## Direct Superclasses
- [`sdata:Possibile`](./Possibile.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Versagensszenario, FMEA-Zeile, Designalternative.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Szenario `30% Rezyklatanteil` zur Bewertung von CO2- und Kostenwirkungen.
ex:scenario_001 a sdata:Scenario ;
  min:hasIdentifier "SCENARIO-001" ;
  min:hasName "Scenario 30 Prozent Rezyklat" ;
  min:concerns ex:product_001 ;
  min:alternativeTo ex:scenario_002 .

ex:scenario_002 a sdata:Scenario ; min:concerns ex:product_001 .
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

ex:example a sdata:Scenario .
```

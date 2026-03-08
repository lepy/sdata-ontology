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
@prefix ex:    <https://example.org/industry/> .

# Szenario `30% Rezyklatanteil` zur Bewertung von CO2- und Kostenwirkungen.
ex:scenario_001 a sdata:Scenario ;
  sdata:hasIdentifier "SCENARIO-001" ;
  sdata:hasName "Scenario 30 Prozent Rezyklat" ;
  sdata:concerns ex:asset_001 ;
  sdata:alternativeTo ex:scenario_002 .

ex:scenario_002 a sdata:Scenario ; sdata:concerns ex:asset_001 .
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

ex:example a sdata:Scenario .
```

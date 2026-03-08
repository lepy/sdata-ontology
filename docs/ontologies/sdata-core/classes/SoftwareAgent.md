# sdata:SoftwareAgent
## IRI
`https://w3id.org/sdata/core/SoftwareAgent`
## Labels
- `Software Agent`
- `Software-Agent`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Software als handelnder Agent. Co-Typisierung:
    Agent ∩ Data. Identitätskriterium: informationale
    Identität. Neue Gewichte = neuer Agent.

## Examples
- `FE-Solver (rechnend), ML-Modell, DPP-Service.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Automatischer Regelalgorithmus, der Ziehgeschwindigkeit adaptiv anpasst.
ex:software_agent_001 a sdata:SoftwareAgent ;
  sdata:hasIdentifier "SOFTWAREAGENT-001" ;
  sdata:hasName "SoftwareAgent Akteur" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:product_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
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

ex:example a sdata:SoftwareAgent .
```

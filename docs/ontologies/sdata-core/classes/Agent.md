# sdata:Agent
## IRI
`https://w3id.org/sdata/core/Agent`
## Labels
- `Agent`
- `Agent`
## Direct Superclasses
- `min:Agent`
## Direct Subclasses
- [`sdata:EnvironmentAgent`](./EnvironmentAgent.md)
- [`sdata:HardwareAgent`](./HardwareAgent.md)
- [`sdata:Organization`](./Organization.md)
- [`sdata:Person`](./Person.md)
- [`sdata:SoftwareAgent`](./SoftwareAgent.md)
## Comment
Fassade für min:Agent. Das, was handelt.
    Selektive Handlungsfähigkeit. Querkategorie.
    Co-Typisierung Pflicht: Agent ⊑ Nexus ⊔ Forma.
    Alle sdata-Agent-Klassen erben von sdata:Agent.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Agent` zur semantischen Modellierung eingesetzt wird.
ex:agent_001 a sdata:Agent ;
  sdata:hasIdentifier "AGENT-001" ;
  sdata:hasName "Agent Akteur" ;
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

ex:example a sdata:Agent .
```

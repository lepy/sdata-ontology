# sdata:HardwareAgent
## IRI
`https://w3id.org/sdata/core/HardwareAgent`
## Labels
- `Hardware Agent`
- `Hardware-Agent`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Handlungsfähige Maschine. Co-Typisierung:
    Agent ∩ Object. Identitätskriterium: materiale
    Kontinuität. Doppeltypisierung mit Hardware.

## Examples
- `CNC-Fräse, Roboterarm, Prüfmaschine (im Betrieb).`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Autonomer Roboterarm, der Materialproben umspannt und zufuehrt.
ex:hardware_agent_001 a sdata:HardwareAgent ;
  sdata:hasIdentifier "HARDWAREAGENT-001" ;
  sdata:hasName "HardwareAgent Akteur" ;
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

ex:example a sdata:HardwareAgent .
```

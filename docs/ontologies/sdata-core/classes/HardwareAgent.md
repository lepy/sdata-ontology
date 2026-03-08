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
## Industriebeispiel
- Autonomer Roboterarm, der Materialproben umspannt und zufuehrt.
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

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
- [`sdata:Hardware`](./Hardware.md)
- [`sdata:Material`](./Material.md)
- [`sdata:Organization`](./Organization.md)
- [`sdata:Person`](./Person.md)
- [`sdata:Software`](./Software.md)
- [`sdata:Specimen`](./Specimen.md)
- [`sdata:Substance`](./Substance.md)
## Comment
Fassade für min:Agent. Das, was handelt.
    Selektive Handlungsfähigkeit. Querkategorie.
    Co-Typisierung Pflicht: Agent ⊑ Nexus ⊔ Forma.

    DESIGN-PRINZIP: Zustand ≠ Typ.
    Ob ein Agent gerade aktiv ist, gehört in
    sdata:hasStatus, nicht in die Klassenhierarchie.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Agent` zur semantischen Modellierung eingesetzt wird.
ex:agent_001 a sdata:Agent ;
  sdata:hasIdentifier "AGENT-001" ;
  sdata:hasName "Generischer Agent im Shopfloor" ;
  sdata:performs ex:process_001 .

ex:process_001 a sdata:Process .
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

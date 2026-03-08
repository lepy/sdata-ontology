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

# Agent ist abstrakt — nicht direkt instanziieren.
# Verwende stattdessen: Person, Hardware, Software, etc.
ex:laborant_mueller a sdata:Person ;
    sdata:hasName "Laborant Müller" ;
    sdata:performs ex:zugversuch_001 .
ex:zugversuch_001 a sdata:Process .
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

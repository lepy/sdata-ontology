# sdata:LifecyclePhase
## IRI
`https://w3id.org/sdata/core/LifecyclePhase`
## Labels
- `Lebenszyklusphase`
- `Lifecycle Phase`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Konventionelle Lebenszykluseinteilung.
    Existiert durch Anerkennung der LCA/ESPR-Community.

## Examples
- `Rohstoffgewinnung, Fertigung, Nutzung, End-of-Life.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Fertigungsphase im LCA/ESPR-Kontext.
ex:phase_production a sdata:LifecyclePhase ;
    sdata:hasName "Fertigung" .
ex:walzen a sdata:Process ;
    sdata:requiresPhase ex:phase_production .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:requiresPhase`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:LifecyclePhase .
```

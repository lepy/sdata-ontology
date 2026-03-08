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

# Nutzungsphase eines Kabelbaums zwischen Inbetriebnahme und Austausch.
ex:lifecycle_phase_001 a sdata:LifecyclePhase ;
  sdata:hasIdentifier "LIFECYCLEPHASE-001" ;
  sdata:hasName "LifecyclePhase Branchenregel" ;
  sdata:typifies ex:process_001 ;
  sdata:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
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

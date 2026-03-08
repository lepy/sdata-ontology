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
Konventionelle Lebenszykluseinteilung. Keine
    Soll-Aussage, sondern konventionelle Klassifikation der
    LCA/ESPR-Community. Existiert durch Anerkennung.
    v0.1.0: von Norma nach Institutio verschoben.

## Examples
- `Rohstoffgewinnung, Fertigung, Nutzung, End-of-Life.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Nutzungsphase eines Kabelbaums zwischen Inbetriebnahme und Austausch.
ex:lifecycle_phase_001 a sdata:LifecyclePhase ;
  min:hasIdentifier "LIFECYCLEPHASE-001" ;
  min:hasName "LifecyclePhase Branchenregel" ;
  min:typifies ex:process_001 ;
  min:comprises ex:req_001 .

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

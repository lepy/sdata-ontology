# sdata:LifecyclePhase
## IRI
`https://w3id.org/sdata/core/LifecyclePhase`
## Labels
- `Lebenszyklusphase`
- `Lifecycle Phase`
## Direct Superclasses
- `min:Institutio`
## Direct Subclasses
- (none)
## Comment
Konventionelle Lebenszykluseinteilung. Keine
    Soll-Aussage, sondern konventionelle Klassifikation der
    LCA/ESPR-Community. Existiert durch Anerkennung.
    v0.15.0: von Norma nach Institutio verschoben.

## Examples
- `Rohstoffgewinnung, Fertigung, Nutzung, End-of-Life.`
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

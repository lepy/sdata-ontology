# sdata:EnvironmentAgent
## IRI
`https://w3id.org/sdata/core/EnvironmentAgent`
## Labels
- `Environment Agent`
- `Umwelt-Agent`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Process`](./Process.md)
## Direct Subclasses
- (none)
## Comment
Natürlicher Prozess mit selektiver Wirkung.
    Co-Typisierung: Agent ∩ Process.
    Greift BESTIMMTE Phasen/Materialien an, nicht alles.
    Selektivitätstest: Korrosion greift bestimmte Korngrenzen
    an → Agent. Tornado transformiert alles → kein Agent.

## Examples
- `Korrosion, UV-Strahlung, Feuchtigkeit.`
## Industriebeispiel
- Korrosive Betriebsumgebung als wirksamer Agent auf Materialalterung.
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:EnvironmentAgent .
```

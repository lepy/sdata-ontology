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
    Agent ∩ Process. Selektivitätstest:
    Korrosion greift bestimmte Korngrenzen an → Agent.
    Tornado transformiert alles → kein Agent.

## Examples
- `Korrosion, UV-Strahlung, Feuchtigkeit.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Korrosion als natürlicher Prozess mit selektiver Wirkung.
ex:korrosion_001 a sdata:EnvironmentAgent ;
    sdata:hasName "Interkristalline Korrosion" ;
    sdata:actsOn ex:rohr_001 .
ex:rohr_001 a sdata:Hardware .
```
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

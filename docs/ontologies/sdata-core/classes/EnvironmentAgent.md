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

# Korrosive Betriebsumgebung als wirksamer Agent auf Materialalterung.
ex:environment_agent_001 a sdata:EnvironmentAgent ;
  sdata:hasIdentifier "ENV-001" ;
  sdata:hasName "Feuchte-korrosive Umgebung" ;
  sdata:influences ex:process_001 ;
  sdata:actsOn ex:material_001 .

ex:process_001 a sdata:Process .
ex:material_001 a sdata:Material .
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

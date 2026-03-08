# sdata:Possibile
## IRI
`https://w3id.org/sdata/core/Possibile`
## Labels
- `Possibile`
- `Possibile`
## Direct Superclasses
- `min:Possibile`
## Direct Subclasses
- [`sdata:Scenario`](./Scenario.md)
## Comment
Fassade für min:Possibile. Möglichkeitsraum.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Possibile ist eine Fassade — verwende sdata:Scenario.
ex:szenario_versagen a sdata:Scenario ;
    sdata:hasName "Versagen Seitenteil links" ;
    sdata:concerns ex:seitenteil_001 .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Possibile .
```

# sdata:Scenario
## IRI
`https://w3id.org/sdata/core/Scenario`
## Labels
- `Scenario`
- `Szenario`
## Direct Superclasses
- [`sdata:Possibile`](./Possibile.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Versagensszenario, FMEA-Zeile, Designalternative.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Versagensszenario für FMEA.
ex:szenario_versagen_links a sdata:Scenario ;
    sdata:hasName "Versagen Seitenteil links bei Seitencrash" ;
    sdata:concerns ex:seitenteil_001 .
ex:seitenteil_001 a sdata:Hardware .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Scenario .
```

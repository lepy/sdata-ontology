# sdata:Law
## IRI
`https://w3id.org/sdata/core/Law`
## Labels
- `Gesetz`
- `Law`
## Direct Superclasses
- [`sdata:Lex`](./Lex.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Energieerhaltung, Massenerhaltung, Ficksches Diffusionsgesetz.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# EU-Batterieverordnung als rechtsverbindliche Grundlage fuer DPP-Pflichten.
ex:law_001 a sdata:Law ;
  min:hasIdentifier "LAW-001" ;
  min:hasName "Law fuer Produktpasspflicht" ;
  min:governs ex:process_001 .

ex:process_001 a sdata:Process .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:governedBy`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Law .
```

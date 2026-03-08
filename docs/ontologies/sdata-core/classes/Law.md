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
@prefix ex:    <https://example.org/industry/> .

# EU-Batterieverordnung als rechtsverbindliche Grundlage fuer DPP-Pflichten.
ex:law_001 a sdata:Law ;
  sdata:hasIdentifier "LAW-001" ;
  sdata:hasName "Law fuer Produktpasspflicht" ;
  sdata:governs ex:process_001 .

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

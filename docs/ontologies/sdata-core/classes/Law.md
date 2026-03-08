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
Universelles Gesetz. Gilt ausnahmslos.
    Kein Gegenbeispiel möglich. Fundament für FPT.
    Dünn: nur Erhaltungssätze und Hauptsätze.
    Hooke, Fick, Fourier sind Modelle, nicht Gesetze.

## Examples
- `Energieerhaltung, Massenerhaltung, Entropiezunahme, Impulserhaltung.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Energieerhaltungssatz als universelles Gesetz.
ex:energieerhaltung a sdata:Law ;
    sdata:hasName "Energieerhaltung" ;
    sdata:governs ex:zugversuch_001 .
ex:zugversuch_001 a sdata:Process .
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

# sdata:Lex
## IRI
`https://w3id.org/sdata/core/Lex`
## Labels
- `Lex`
- `Lex`
## Direct Superclasses
- `min:Lex`
## Direct Subclasses
- [`sdata:Law`](./Law.md)
## Comment
Fassade für min:Lex. Das, was immer gilt.
    Universelle Gültigkeit. Erhaltungssätze,
    Hauptsätze der Thermodynamik. Dünn, aber
    strukturell tragend für First Principle Thinking.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Lex ist eine Fassade — verwende sdata:Law.
ex:massenerhaltung a sdata:Law ;
    sdata:hasName "Massenerhaltung" ;
    sdata:governs ex:walzprozess .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Lex .
```

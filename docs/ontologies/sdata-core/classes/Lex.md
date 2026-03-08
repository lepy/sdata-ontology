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
    Universelle Gültigkeit.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Lex` zur semantischen Modellierung eingesetzt wird.
ex:lex_001 a sdata:Lex ;
  sdata:hasIdentifier "LEX-001" ;
  sdata:hasName "Lex fuer Produktpasspflicht" ;
  sdata:governs ex:process_001 .

ex:process_001 a sdata:Process .
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

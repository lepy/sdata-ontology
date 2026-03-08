# sdata:Person
## IRI
`https://w3id.org/sdata/core/Person`
## Labels
- `Person`
- `Person`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Mensch als handelnder Agent. Co-Typisierung:
    Agent ∩ Object. Identitätskriterium: materiale
    Kontinuität.

## Examples
- `Prüfer, Konstrukteur, Werker, Laborant.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Qualitaetsingenieurin, die einen Pruefbericht fachlich freigibt.
ex:person_001 a sdata:Person ;
  min:hasIdentifier "PERSON-001" ;
  min:hasName "Person Akteur" ;
  min:performs ex:process_001 ;
  min:actsOn ex:product_001 .

ex:process_001 a sdata:Process ; min:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Person .
```

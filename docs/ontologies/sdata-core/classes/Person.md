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
@prefix ex:    <https://example.org/industry/> .

# Qualitaetsingenieurin, die einen Pruefbericht fachlich freigibt.
ex:person_001 a sdata:Person ;
  sdata:hasIdentifier "PERSON-001" ;
  sdata:hasName "Person Akteur" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:product_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
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

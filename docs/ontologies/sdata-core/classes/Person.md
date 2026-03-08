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
Mensch als handelnder Agent. Agent ∩ Object.
    Identitätskriterium: materiale Kontinuität.

## Examples
- `Prüfer, Konstrukteur, Werker, Laborant.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Laborant als handelnder Agent im Zugversuch.
ex:laborant_schmidt a sdata:Person ;
    sdata:hasName "Laborant Schmidt" ;
    sdata:performs ex:probenentnahme_42 ;
    sdata:locatedAt ex:labor_berlin .
ex:probenentnahme_42 a sdata:Process .
ex:labor_berlin a sdata:Site .
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

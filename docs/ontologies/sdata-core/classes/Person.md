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

# Qualitaetsingenieurin, die einen Pruefbericht fachlich freigibt.
ex:person_001 a sdata:Person ;
  sdata:hasIdentifier "PERSON-001" ;
  sdata:hasName "Person als materieller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
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

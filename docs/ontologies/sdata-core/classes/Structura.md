# sdata:Structura
## IRI
`https://w3id.org/sdata/core/Structura`
## Labels
- `Structura`
- `Structura`
## Direct Superclasses
- `min:Structura`
## Direct Subclasses
- [`sdata:Model`](./Model.md)
## Comment
Fassade für min:Structura. Das, was die
    Wirklichkeit formalisiert. Formale Struktur.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Structura` zur semantischen Modellierung eingesetzt wird.
ex:structura_001 a sdata:Structura ;
  sdata:hasIdentifier "STRUCTURA-001" ;
  sdata:hasName "Structura zur Prozessauslegung" ;
  sdata:constrains ex:process_001 .

ex:model_data_001 a sdata:Data ; sdata:encodes ex:model_001 .
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

ex:example a sdata:Structura .
```

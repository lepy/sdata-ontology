# sdata:Model
## IRI
`https://w3id.org/sdata/core/Model`
## Labels
- `Model`
- `Modell`
## Direct Superclasses
- [`sdata:Structura`](./Structura.md)
## Direct Subclasses
- (none)
## Comment
Mathematische/formale Struktur. Deckt beschreibende
    Strukturen (von-Mises) und berechenbare Verfahren (Newton-Raphson,
    Ed25519, LSTM) gleichermaßen ab. Typisierung über
    sdata:ModelType (sdata:typifiedBy).

## Examples
- `von-Mises, Johnson-Cook, ReCiPe, Ed25519,
    Newton-Raphson, Gradient Boosting, LSTM, DB-Schema.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# FEM-Modell einer Stromschiene zur thermomechanischen Auslegung.
ex:model_001 a sdata:Model ;
  min:hasIdentifier "MODEL-001" ;
  min:hasName "Model zur Prozessauslegung" ;
  min:constrains ex:process_001 .

ex:model_data_001 a sdata:Data ; min:encodes ex:model_001 .
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

ex:example a sdata:Model .
```

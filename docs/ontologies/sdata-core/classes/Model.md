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
## Industriebeispiel
- FEM-Modell einer Stromschiene zur thermomechanischen Auslegung.
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

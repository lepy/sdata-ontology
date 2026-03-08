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
Formale Approximation. Kann nützlich sein,
    muss nicht stimmen. Hat einen Gültigkeitsbereich.
    Typisierung über sdata:ModelType.

## Examples
- `Hooke, von-Mises, Johnson-Cook, Fick, Fourier, ReCiPe, Ed25519, LSTM.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Hookesches Modell als formale Approximation.
ex:hooke a sdata:Model ;
    sdata:hasName "Hookesches Modell" ;
    sdata:typifiedBy ex:materialmodell_typ ;
    sdata:realizes ex:energieerhaltung .
ex:materialmodell_typ a sdata:ModelType ;
    sdata:hasName "Materialmodell" .
ex:energieerhaltung a sdata:Law .
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

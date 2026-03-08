# sdata:ProductPassport
## IRI
`https://w3id.org/sdata/core/ProductPassport`
## Labels
- `Product Passport`
- `Produktpass`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- [`sdata:DigitalProductPassport`](./DigitalProductPassport.md)
## Comment
Produktpass als Data-Artefakt.
    Versionskette via sdata:supersedes.

## Examples
- `Materialzeugnis EN 10204, Batterie-Pass, EPD, Stahl-DPP.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Materialzeugnis EN 10204 als analoger Produktpass.
ex:zeugnis_001 a sdata:ProductPassport ;
    sdata:describes ex:coil_001 ;
    sdata:hasVersion "1.0.0" ;
    sdata:signedBy ex:stahlwerk_ag .
ex:coil_001 a sdata:Hardware .
ex:stahlwerk_ag a sdata:Organization .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ProductPassport .
```

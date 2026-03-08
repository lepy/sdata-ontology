# sdata:Proof
## IRI
`https://w3id.org/sdata/core/Proof`
## Labels
- `Beweis`
- `Proof`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Kryptographische Signatur.

## Examples
- `Ed25519-Signatur, ECDSA-Signatur.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Ed25519-Signatur eines DPP.
ex:proof_001 a sdata:Proof ;
    sdata:signedBy ex:oem_ag ;
    sdata:encodes ex:ed25519 .
ex:oem_ag a sdata:Organization .
ex:ed25519 a sdata:Model .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Proof .
```

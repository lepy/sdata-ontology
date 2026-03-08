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
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Hash-basierter Integritaetsnachweis fuer einen freigegebenen Messdatensatz.
ex:proof_001 a sdata:Proof ;
  min:hasIdentifier "PROOF-001" ;
  min:hasName "Proof Datensatz" ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:generates ex:data_001 .
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

ex:example a sdata:Proof .
```

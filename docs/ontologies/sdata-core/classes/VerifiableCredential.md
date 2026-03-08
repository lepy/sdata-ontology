# sdata:VerifiableCredential
## IRI
`https://w3id.org/sdata/core/VerifiableCredential`
## Labels
- `Verifiable Credential`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Signiertes Credential. W3C VC Data Model.

## Examples
- `Signiertes Materialzeugnis, DPP als VC.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Signiertes Hersteller-Zertifikat als maschinenpruefbarer Nachweis.
ex:verifiable_credential_001 a sdata:VerifiableCredential ;
  sdata:hasIdentifier "VERIFIABLECREDENTIAL-001" ;
  sdata:hasName "VerifiableCredential Datensatz" ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
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

ex:example a sdata:VerifiableCredential .
```

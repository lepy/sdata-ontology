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
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

# Signiertes Materialzeugnis als VC.
ex:vc_zeugnis a sdata:VerifiableCredential ;
    sdata:signedBy ex:pruefinstitut_ag ;
    sdata:validFrom "2026-01-15T00:00:00Z"^^xsd:dateTime ;
    sdata:validUntil "2028-01-15T00:00:00Z"^^xsd:dateTime .
ex:pruefinstitut_ag a sdata:Organization .
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

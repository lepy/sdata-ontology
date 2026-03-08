# sdata:VerifiablePresentation
## IRI
`https://w3id.org/sdata/core/VerifiablePresentation`
## Labels
- `Verifiable Presentation`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Bündel von VCs. Selektive Offenlegung.

## Examples
- `DPP-Präsentation an Recycler.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# DPP-Präsentation an einen Recycler.
ex:vp_recycler a sdata:VerifiablePresentation ;
    sdata:hasComponent ex:dpp_001 ;
    sdata:hasComponent ex:vc_zeugnis ;
    sdata:signedBy ex:oem_ag .
ex:dpp_001 a sdata:DigitalProductPassport .
ex:vc_zeugnis a sdata:VerifiableCredential .
ex:oem_ag a sdata:Organization .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:VerifiablePresentation .
```

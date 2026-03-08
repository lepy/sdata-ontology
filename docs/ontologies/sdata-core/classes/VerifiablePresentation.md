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

# Gebuendelte Vorlage mehrerer Nachweise fuer Audit oder Behoerde.
ex:verifiable_presentation_001 a sdata:VerifiablePresentation ;
  sdata:hasIdentifier "VERIFIABLEPRESENTATION-001" ;
  sdata:hasName "VerifiablePresentation Datensatz" ;
  sdata:describes ex:asset_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
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

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
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Gebuendelte Vorlage mehrerer Nachweise fuer Audit oder Behoerde.
ex:verifiable_presentation_001 a sdata:VerifiablePresentation ;
  min:hasIdentifier "VERIFIABLEPRESENTATION-001" ;
  min:hasName "VerifiablePresentation Datensatz" ;
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

ex:example a sdata:VerifiablePresentation .
```

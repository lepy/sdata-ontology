# sdata:Identifier
## IRI
`https://w3id.org/sdata/core/Identifier`
## Labels
- `Identifier`
- `Identifikator`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Reifizierter Identifier. Scheme, Value, Issuer, Registry.

## Examples
- `GTIN, DID (did:web), DOI, VDA-Teilenummer, UUID.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Chargennummer einer Kupferlegierung als rueckverfolgbare Kennung.
ex:identifier_001 a sdata:Identifier ;
  min:hasIdentifier "IDENTIFIER-001" ;
  min:hasName "Identifier Datensatz" ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:generates ex:data_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- `sdata:hasIssuer`
- `sdata:hasScheme`
- `sdata:hasValue`
- `sdata:registeredIn`
## Used As Range
- `sdata:identifiedBy`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Identifier .
```

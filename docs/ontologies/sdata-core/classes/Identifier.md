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
@prefix ex:    <https://example.org/industry/> .

# Chargennummer einer Kupferlegierung als rueckverfolgbare Kennung.
ex:identifier_001 a sdata:Identifier ;
  sdata:hasIdentifier "IDENTIFIER-001" ;
  sdata:hasName "Identifier Datensatz" ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
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

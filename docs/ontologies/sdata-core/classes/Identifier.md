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

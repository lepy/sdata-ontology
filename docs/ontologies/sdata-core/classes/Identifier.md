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

# DID-Identifier eines OEM, registriert in Catena-X.
ex:did_oem a sdata:Identifier ;
    sdata:hasScheme "W3C:DID" ;
    sdata:hasValue "did:web:oem.example.com" ;
    sdata:hasIssuer ex:oem_ag ;
    sdata:registeredIn ex:catena_x_registry .
ex:oem_ag a sdata:Organization .
ex:catena_x_registry a sdata:Registry .
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

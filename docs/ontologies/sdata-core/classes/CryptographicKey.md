# sdata:CryptographicKey
## IRI
`https://w3id.org/sdata/core/CryptographicKey`
## Labels
- `Cryptographic Key`
- `Kryptographischer Schlüssel`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Schlüsselmaterial. sdata:encodes ein Model.

## Examples
- `Ed25519 Public Key, ECDSA Private Key.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Oeffentlicher Schluessel zur Verifikation signierter DPP-Dokumente.
ex:cryptographic_key_001 a sdata:CryptographicKey ;
  sdata:hasIdentifier "CRYPTOGRAPHICKEY-001" ;
  sdata:hasName "CryptographicKey Datensatz" ;
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

ex:example a sdata:CryptographicKey .
```

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

# Öffentlicher Ed25519-Schlüssel zur DPP-Verifikation.
ex:pubkey_oem a sdata:CryptographicKey ;
    sdata:hasName "OEM Public Key" ;
    sdata:encodes ex:ed25519 .
ex:ed25519 a sdata:Model ;
    sdata:typifiedBy ex:krypto_typ .
ex:krypto_typ a sdata:ModelType ;
    sdata:hasName "Kryptographisches Verfahren" .
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

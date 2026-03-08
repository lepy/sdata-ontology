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
## Industriebeispiel
- Oeffentlicher Schluessel zur Verifikation signierter DPP-Dokumente.
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

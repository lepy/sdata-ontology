# sdata:DigitalProductPassport
## IRI
`https://w3id.org/sdata/core/DigitalProductPassport`
## Labels
- `Digital Product Passport`
- `Digitaler Produktpass`
## Direct Superclasses
- [`sdata:ProductPassport`](./ProductPassport.md)
## Direct Subclasses
- (none)
## Comment
ESPR-konformer digitaler Produktpass.
    Doppeltypisierung mit VerifiableCredential ist Regelfall.

## Examples
- `ESPR-DPP, Batterie-Pass (EU 2023/1542), Textil-Pass.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# ESPR-konformer Stahl-DPP mit Signatur.
ex:dpp_001 a sdata:DigitalProductPassport , sdata:VerifiableCredential ;
    sdata:describes ex:seitenteil_001 ;
    sdata:encodes ex:espr_spec ;
    sdata:typifiedBy ex:espr_spec ;
    sdata:signedBy ex:oem_ag ;
    sdata:identifiedBy ex:did_dpp_001 ;
    sdata:hasVersion "1.0.0" ;
    sdata:hasComponent ex:result_rm ;
    sdata:hasComponent ex:proof_001 .
ex:seitenteil_001 a sdata:Hardware ;
    sdata:typifiedBy ex:seitenteil_typ .
ex:seitenteil_typ a sdata:ProductType .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:DigitalProductPassport .
```

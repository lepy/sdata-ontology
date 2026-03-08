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
ESPR-konformer digitaler Produktpass. Maschinenlesbar,
    signierbar, versionierbar. Spezialisierung von ProductPassport
    für den digitalen Fall.

    Doppeltypisierung DigitalProductPassport ∩ VerifiableCredential
    ist der Regelfall: ein DPP ist typischerweise ein signiertes
    Credential.

    Provenienz: sdata:derivedFrom für Vorgänger-DPPs.
    Versionierung: sdata:supersedes für Versionsketten.

## Examples
- `ESPR-DPP, Batterie-Pass (EU 2023/1542), Textil-Pass, Stahl-DPP.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:DigitalProductPassport` zur semantischen Modellierung eingesetzt wird.
ex:digital_product_passport_001 a sdata:DigitalProductPassport ;
  sdata:hasIdentifier "DIGITALPRODUCTPASSPORT-001" ;
  sdata:hasName "DigitalProductPassport Datensatz" ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
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

ex:example a sdata:DigitalProductPassport .
```

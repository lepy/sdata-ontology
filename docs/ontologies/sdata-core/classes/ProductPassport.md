# sdata:ProductPassport
## IRI
`https://w3id.org/sdata/core/ProductPassport`
## Labels
- `Product Passport`
- `Produktpass`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- [`sdata:DigitalProductPassport`](./DigitalProductPassport.md)
## Comment
Produktpass als Data-Artefakt.
    Versionskette via sdata:supersedes.

## Examples
- `Materialzeugnis EN 10204, Batterie-Pass, EPD, Stahl-DPP.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Digital Product Passport eines Hochvolt-Kabels mit Material- und Compliance-Daten.
ex:product_passport_001 a sdata:ProductPassport ;
  sdata:hasIdentifier "PRODUCTPASSPORT-001" ;
  sdata:hasName "ProductPassport Datensatz" ;
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

ex:example a sdata:ProductPassport .
```

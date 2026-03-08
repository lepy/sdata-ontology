# sdata:Substance
## IRI
`https://w3id.org/sdata/core/Substance`
## Labels
- `Substance`
- `Substanz`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Chemischer Stoff als Agent. Wirkt selektiv:
    Mangan härtet, Chrom-VI schädigt.
    Agent ∩ Object. Identität: material.
    Regulatorisch: REACH/RoHS/ESPR.

## Examples
- `Mangan (CAS 7439-96-5), Chrom-VI (SVHC), Blei (RoHS).`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Legierungselement Phosphor als enthaltene Substanz in einer Charge.
ex:substance_001 a sdata:Substance ;
  sdata:hasIdentifier "SUBSTANCE-001" ;
  sdata:hasName "Substance als materieller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- `sdata:hasCASNumber`
- `sdata:hasConcentration`
- `sdata:hasRegulatoryStatus`
## Used As Range
- `sdata:containsSubstance`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Substance .
```

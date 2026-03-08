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

# Mangan als Legierungselement mit regulatorischem Status.
ex:mn_001 a sdata:Substance ;
    sdata:hasName "Mangan" ;
    sdata:hasCASNumber "7439-96-5" ;
    sdata:hasConcentration "0.0035"^^xsd:float ;
    sdata:hasRegulatoryStatus "nicht SVHC" .
ex:DC04_charge a sdata:Material ;
    sdata:containsSubstance ex:mn_001 .
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

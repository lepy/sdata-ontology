# sdata:Specimen
## IRI
`https://w3id.org/sdata/core/Specimen`
## Labels
- `Probe`
- `Specimen`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Prüfkörper als Agent. Wirkt selektiv:
    widersteht Last, versagt lokal, kann Messeinrichtung
    zerstören. Agent ∩ Object. Identität: material.
    Provenienz via sdata:sampledFrom.

## Examples
- `Flachzugprobe (DIN 50125 Typ H), Rundprobe, Kerbschlagprobe.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Normprobe aus einer Kupfercharge fuer mechanische Pruefungen.
ex:specimen_001 a sdata:Specimen ;
  sdata:hasIdentifier "SPECIMEN-001" ;
  sdata:hasName "Specimen als materieller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- `sdata:sampledFrom`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Specimen .
```

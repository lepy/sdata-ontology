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

# Flachzugprobe aus DC04-Coil.
ex:probe_42 a sdata:Specimen ;
    sdata:hasName "Probe 42" ;
    sdata:sampledFrom ex:coil_DC04_001 ;
    sdata:hasMaterial ex:DC04_charge_7814 ;
    sdata:typifiedBy ex:flachzugprobe_typ .
ex:coil_DC04_001 a sdata:Hardware .
ex:DC04_charge_7814 a sdata:Material .
ex:flachzugprobe_typ a sdata:ProductType ;
    sdata:hasName "Flachzugprobe DIN 50125 Typ H" .
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

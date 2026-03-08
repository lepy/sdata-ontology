# sdata:Specification
## IRI
`https://w3id.org/sdata/core/Specification`
## Labels
- `Specification`
- `Spezifikation`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Technische Spezifikation oder Norm. BÜNDELT atomare
    Anforderungen via sdata:comprises.

## Examples
- `EN 10025-2, DIN EN ISO 6892-1, ISO 14040.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# DIN EN ISO 6892-1 als technische Spezifikation.
ex:din_6892 a sdata:Specification ;
    sdata:hasIdentifier "DIN EN ISO 6892-1:2019" ;
    sdata:hasName "Metallic materials — Tensile testing" ;
    sdata:specifies ex:zugversuch_001 ;
    sdata:comprises ex:req_dehnrate , ex:req_probenform , ex:req_temperatur ;
    sdata:constitutedBy ex:iso_tc164 .
ex:zugversuch_001 a sdata:Process .
ex:req_dehnrate a sdata:Requirement .
ex:req_probenform a sdata:Requirement .
ex:req_temperatur a sdata:Requirement ;
    sdata:hasName "Prüftemperatur 23 ± 5 °C" .
ex:iso_tc164 a sdata:Organization .
```
## Used As Domain
- `sdata:specifies`
## Used As Range
- `sdata:specifiedBy`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Specification .
```

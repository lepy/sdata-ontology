# sdata:Regulation
## IRI
`https://w3id.org/sdata/core/Regulation`
## Labels
- `Regulation`
- `Verordnung`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Regulatorisches Rahmenwerk. BÜNDELT atomare
    Anforderungen via sdata:comprises.

## Examples
- `ESPR, CBAM, REACH, RoHS, EU-Taxonomie.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# ESPR-Verordnung bündelt atomare Anforderungen.
ex:espr a sdata:Regulation ;
    sdata:hasIdentifier "EU-2024/1781" ;
    sdata:hasName "Ecodesign for Sustainable Products Regulation" ;
    sdata:comprises ex:req_dpp_pflicht , ex:req_recyclatanteil ;
    sdata:constitutedBy ex:eu_kommission ;
    sdata:recognizedBy ex:eu_mitgliedstaaten ;
    sdata:regulates ex:seitenteil_001 .
ex:req_dpp_pflicht a sdata:Requirement .
ex:req_recyclatanteil a sdata:Requirement .
ex:eu_kommission a sdata:Organization .
ex:seitenteil_001 a sdata:Hardware .
```
## Used As Domain
- `sdata:regulates`
## Used As Range
- `sdata:regulatedBy`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Regulation .
```

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

# REACH- oder RoHS-Regelwerk mit gebuendelten Anforderungen an Substanzen.
ex:regulation_001 a sdata:Regulation ;
  sdata:hasIdentifier "REGULATION-001" ;
  sdata:hasName "Regulation Branchenregel" ;
  sdata:typifies ex:process_001 ;
  sdata:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
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

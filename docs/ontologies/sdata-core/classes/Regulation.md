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
    Anforderungen (sdata:Requirement) via sdata:comprises.
    Existiert durch kollektive Anerkennung (EU, nationale
    Gesetzgeber). Exakt Searles Kriterium.
    v0.1.0: von Norma nach Institutio verschoben.

## Examples
- `ESPR, CBAM, REACH, RoHS, EU-Taxonomie.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# REACH- oder RoHS-Regelwerk mit gebuendelten Anforderungen an Substanzen.
ex:regulation_001 a sdata:Regulation ;
  min:hasIdentifier "REGULATION-001" ;
  min:hasName "Regulation Branchenregel" ;
  min:typifies ex:process_001 ;
  min:comprises ex:req_001 .

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

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
## Industriebeispiel
- REACH- oder RoHS-Regelwerk mit gebuendelten Anforderungen an Substanzen.
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

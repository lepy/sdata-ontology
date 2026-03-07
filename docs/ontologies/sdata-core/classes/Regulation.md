# sdata:Regulation
## IRI
`https://w3id.org/sdata/core/Regulation`
## Labels
- `Regulation`
- `Verordnung`
## Direct Superclasses
- `min:Institutio`
## Direct Subclasses
- (none)
## Comment
Regulatorisches Rahmenwerk. BÜNDELT atomare
    Anforderungen (sdata:Requirement) via sdata:comprises.
    Existiert durch kollektive Anerkennung (EU, nationale
    Gesetzgeber). Exakt Searles Kriterium.
    v0.15.0: von Norma nach Institutio verschoben.

## Examples
- `ESPR, CBAM, REACH, RoHS, EU-Taxonomie.`
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

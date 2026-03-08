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
    Anforderungen (sdata:Requirement) via sdata:comprises.
    Existiert durch Anerkennung der Normungsgemeinschaft.
    v0.1.0: von Norma nach Institutio verschoben.

## Examples
- `EN 10025-2, DIN EN ISO 6892-1, ISO 14040.`
## Industriebeispiel
- DIN EN ISO 6892-1 als Spezifikation fuer Zugversuchsablauf und Auswertung.
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

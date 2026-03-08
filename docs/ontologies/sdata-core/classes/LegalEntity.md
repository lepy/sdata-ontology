# sdata:LegalEntity
## IRI
`https://w3id.org/sdata/core/LegalEntity`
## Labels
- `Juristische Person`
- `Legal Entity`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Juristische Person als reine Institutio — OHNE Agency.

    sdata:Organization ist Agent ∩ Institutio
    (ein Knoten). LegalEntity bleibt für Fälle, in denen
    KEINE Agency vorliegt:
    — Aufgelöste Firmen (keine Handlungsfähigkeit mehr)
    — Historische Institutionen
    — Rechtsformen als abstrakte Institutio

    Aktive Unternehmen: sdata:Organization (hat beides).
    Juristische Hülle ohne Agency: sdata:LegalEntity.

## Examples
- `Aufgelöste GmbH, historische Institution, Rechtsform als Muster.`
## Industriebeispiel
- Rechtliche Einheit eines OEMs als Vertragspartner in der Lieferkette.
## Used As Domain
- (none)
## Used As Range
- `sdata:hasLegalEntity`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:LegalEntity .
```

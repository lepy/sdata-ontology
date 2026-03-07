# sdata:LegalEntity
## IRI
`https://w3id.org/sdata/core/LegalEntity`
## Labels
- `Juristische Person`
- `Legal Entity`
## Direct Superclasses
- `min:Institutio`
## Direct Subclasses
- (none)
## Comment
Organisation als juristische Person oder anerkannte
    Institution. Gegenstück zu sdata:Organization (Agent).
    Doppeltypisierung: dasselbe Unternehmen kann zugleich
    Organization (Agent, handelt) und LegalEntity (Institutio,
    existiert durch rechtliche Anerkennung) sein.
    Searle: ‹X counts as Y in context C.›

## Examples
- `GmbH, AG, Universität, Normungsgremium, Behörde.`
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

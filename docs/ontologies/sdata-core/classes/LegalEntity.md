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
Juristische Person OHNE Agency.
    Aktive Unternehmen: sdata:Organization.

## Examples
- `Aufgelöste GmbH, historische Institution.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Aufgelöste GmbH ohne aktuelle Handlungsfähigkeit.
ex:altfirma_gmbh a sdata:LegalEntity ;
    sdata:hasName "Altfirma GmbH (aufgelöst)" .
```
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

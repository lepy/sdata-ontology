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

# Rechtliche Einheit eines OEMs als Vertragspartner in der Lieferkette.
ex:legal_entity_001 a sdata:LegalEntity ;
  sdata:hasIdentifier "LEGALENTITY-001" ;
  sdata:hasName "LegalEntity Branchenregel" ;
  sdata:typifies ex:process_001 ;
  sdata:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
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

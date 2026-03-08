# sdata:Software
## IRI
`https://w3id.org/sdata/core/Software`
## Labels
- `Software`
- `Software`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- [`sdata:DigitalTwin`](./DigitalTwin.md)
## Comment
Software — IMMER Agent. Agent ∩ Data.
    Identitätskriterium: informationale Identität.
    Neue Gewichte = neuer Agent.

    Reine Installationsdatei ohne Agency ist sdata:Data.

    Klassifizierung: sdata:ProductType.

## Examples
- `AutoForm R10, Abaqus 2024, LS-DYNA R14, PostgreSQL, openLCA.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# MES-System zur Erfassung von Prozessparametern und Chargenbezug.
ex:software_001 a sdata:Software ;
  sdata:hasIdentifier "SOFTWARE-001" ;
  sdata:hasName "Software als informationeller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:describes ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:usesSoftware`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Software .
```

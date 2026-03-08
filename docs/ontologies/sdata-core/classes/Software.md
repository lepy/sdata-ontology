# sdata:Software
## IRI
`https://w3id.org/sdata/core/Software`
## Labels
- `Software`
- `Software`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Softwareprodukt als PASSIVES Artefakt. Wenn aktiv:
    Doppeltypisierung mit SoftwareAgent. Klassifizierung über
    sdata:SoftwareType. Datenbanken, Solver, CAD: alles
    SoftwareType-Instanzen.

## Examples
- `AutoForm R10, Abaqus 2024, LS-DYNA R14, PostgreSQL, openLCA.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# MES-System zur Erfassung von Prozessparametern und Chargenbezug.
ex:software_001 a sdata:Software ;
  sdata:hasIdentifier "SOFTWARE-001" ;
  sdata:hasName "Software Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
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

# sdata:SoftwareType
## IRI
`https://w3id.org/sdata/core/SoftwareType`
## Labels
- `Software Type`
- `Softwaretyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Software-Typs. Ersetzt Software-Subklassen.

## Examples
- `FE-Solver, CAD-System, LCA-Software, RDBMS, Triplestore.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung einer Anwendung als `LCA-Tool` fuer Bilanzierung.
ex:software_type_001 a sdata:SoftwareType ;
  min:hasIdentifier "SOFTWARETYPE-001" ;
  min:hasName "SoftwareType Klassifikation" ;
  min:typifies ex:software_001 .

ex:software_001 a sdata:Software .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:SoftwareType .
```

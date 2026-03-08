# sdata:Process
## IRI
`https://w3id.org/sdata/core/Process`
## Labels
- `Process`
- `Prozess`
## Direct Superclasses
- `min:Process`
## Direct Subclasses
- [`sdata:EnvironmentAgent`](./EnvironmentAgent.md)
## Comment
Typisierung über sdata:ProcessType.

## Examples
- `Tiefziehen, Zugversuch, FEM-Simulation, LCA-Studie.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

# Zugversuch mit vollständiger Prozesskette.
ex:zugversuch_001 a sdata:Process ;
    sdata:typifiedBy ex:zugversuch_typ ;
    sdata:hasInput ex:probe_42 ;
    sdata:hasOutput ex:result_zv001 ;
    sdata:performedBy ex:zwick_z250 ;
    sdata:usesTool ex:zwick_z250 ;
    sdata:realizes ex:din_6892 ;
    sdata:requiresPhase ex:phase_production ;
    sdata:governedBy ex:energieerhaltung ;
    sdata:hasStartTime "2026-03-08T09:00:00Z"^^xsd:dateTime ;
    sdata:hasEndTime "2026-03-08T09:15:00Z"^^xsd:dateTime .
ex:zugversuch_typ a sdata:ProcessType .
ex:probe_42 a sdata:Specimen .
ex:result_zv001 a sdata:Result .
ex:zwick_z250 a sdata:Hardware .
ex:din_6892 a sdata:Specification .
ex:energieerhaltung a sdata:Law .
```
## Used As Domain
- `sdata:governedBy`
- `sdata:hasEndTime`
- `sdata:hasStartTime`
- `sdata:precedes`
- `sdata:requiresPhase`
- `sdata:succeeds`
- `sdata:usesSoftware`
- `sdata:usesTool`
## Used As Range
- `sdata:originatedIn`
- `sdata:precedes`
- `sdata:producedBy`
- `sdata:succeeds`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Process .
```

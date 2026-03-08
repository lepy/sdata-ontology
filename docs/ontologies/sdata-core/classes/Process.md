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
Typisierung über sdata:ProcessType (sdata:typifiedBy).

## Examples
- `Tiefziehen, Zugversuch, FEM-Simulation, LCA-Studie.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Mehrstufiger Ziehprozess zur Reduktion des Leitungsquerschnitts.
ex:process_001 a sdata:Process ;
  sdata:hasIdentifier "PROC-001" ;
  sdata:hasName "Warmumformung Linie 3" ;
  sdata:hasInput ex:material_001 ;
  sdata:hasOutput ex:product_001 ;
  sdata:performedBy ex:person_001 ;
  sdata:generates ex:data_001 .

ex:material_001 a sdata:Material .
ex:product_001 a sdata:Product ; sdata:hasMaterial ex:material_001 .
ex:person_001 a sdata:Person .
ex:data_001 a sdata:Data ; sdata:producedBy ex:process_001 .
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

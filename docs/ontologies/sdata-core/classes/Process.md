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

# Mehrstufiger Ziehprozess zur Reduktion des Leitungsquerschnitts.
ex:process_001 a sdata:Process ;
  sdata:hasIdentifier "PROC-001" ;
  sdata:hasName "Warmumformung Linie 3" ;
  sdata:hasInput ex:material_001 ;
  sdata:hasOutput ex:part_001 ;
  sdata:performedBy ex:software_001 ;
  sdata:generates ex:result_001 .

ex:material_001 a sdata:Material .
ex:part_001 a sdata:Hardware ;
  sdata:hasMaterial ex:material_001 ;
  sdata:typifiedBy ex:product_type_001 .
ex:software_001 a sdata:Software ; sdata:performs ex:process_001 .
ex:result_001 a sdata:Result ; sdata:producedBy ex:process_001 .
ex:product_type_001 a sdata:ProductType .
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

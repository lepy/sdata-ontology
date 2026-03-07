# sdata:Process
## IRI
`https://w3id.org/sdata/core/Process`
## Labels
- `Process`
- `Prozess`
## Direct Superclasses
- `min:Process`
## Direct Subclasses
- (none)
## Comment
Typisierung über sdata:ProcessType (sdata:typifiedBy).

## Examples
- `Tiefziehen, Zugversuch, FEM-Simulation, LCA-Studie.`
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

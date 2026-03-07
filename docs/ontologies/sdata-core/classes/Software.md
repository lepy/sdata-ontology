# sdata:Software
## IRI
`https://w3id.org/sdata/core/Software`
## Labels
- `Software`
- `Software`
## Direct Superclasses
- `min:Object`
## Direct Subclasses
- (none)
## Comment
Softwareprodukt als PASSIVES Artefakt. Wenn aktiv:
    Doppeltypisierung mit SoftwareAgent. Klassifizierung über
    sdata:SoftwareType. Datenbanken, Solver, CAD: alles
    SoftwareType-Instanzen.

## Examples
- `AutoForm R10, Abaqus 2024, LS-DYNA R14, PostgreSQL, openLCA.`
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

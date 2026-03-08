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

# LS-DYNA R14 als Software-Agent in der Crashsimulation.
ex:ls_dyna_r14 a sdata:Software ;
    sdata:hasName "LS-DYNA R14" ;
    sdata:typifiedBy ex:fe_solver_typ ;
    sdata:performs ex:crashsim_001 ;
    sdata:realizes ex:zentrale_differenzen ;
    sdata:hasStatus "running" .
ex:fe_solver_typ a sdata:ProductType ;
    sdata:hasName "Expliziter FE-Solver" .
ex:crashsim_001 a sdata:Process .
ex:zentrale_differenzen a sdata:Model .
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

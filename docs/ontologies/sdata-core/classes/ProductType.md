# sdata:ProductType
## IRI
`https://w3id.org/sdata/core/ProductType`
## Labels
- `Product Type`
- `Produkttyp`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Produkts, Geräts oder
    Software-Typs. Einheitlicher Typus für Hardware,
    Software und alle anderen typifizierbaren Nexus.
    Ersetzt die ehemaligen Klassen Product, HardwareType
    und SoftwareType.

## Examples
- `Seitenteil, B-Säule, Felge, Universalprüfmaschine, Hydraulische Presse, FE-Solver, CAD-System, LCA-Software.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung von Hardware und Software als einheitlicher Produkttyp.
ex:universalpruefmaschine a sdata:ProductType ;
  sdata:hasIdentifier "PT-001" ;
  sdata:hasName "Universalpruefmaschine" .

ex:fe_solver_typ a sdata:ProductType ;
  sdata:hasIdentifier "PT-002" ;
  sdata:hasName "FE-Solver" .

ex:zwick_z250 a sdata:Hardware ;
  sdata:typifiedBy ex:universalpruefmaschine .

ex:ls_dyna_r14 a sdata:Software ;
  sdata:typifiedBy ex:fe_solver_typ .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ProductType .
```

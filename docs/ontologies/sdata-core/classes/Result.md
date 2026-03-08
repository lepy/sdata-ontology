# sdata:Result
## IRI
`https://w3id.org/sdata/core/Result`
## Labels
- `Ergebnis`
- `Result`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Semantisches Ergebnis-Bündel. Eigenes Axiom:
    assessesRequirement + assessmentOutcome.
    Doppeltypisierung Result ∩ VerifiableCredential möglich.
    Persistierung über sdata:typifiedBy → DataFormat.

## Examples
- `Zugversuchsergebnis, FEM-Ergebnis, Compliance-Bewertung.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Bestanden/Nicht-bestanden Ergebnis einer elektrischen End-of-Line-Pruefung.
ex:result_001 a sdata:Result ;
  sdata:hasIdentifier "RESULT-001" ;
  sdata:hasName "Result Datensatz" ;
  sdata:describes ex:asset_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
```
## Used As Domain
- `sdata:assessesRequirement`
- `sdata:assessmentOutcome`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Result .
```

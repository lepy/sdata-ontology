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

# Zugversuchsergebnis mit Compliance-Bewertung.
ex:result_rm a sdata:Result , sdata:VerifiableCredential ;
    sdata:assessesRequirement ex:req_rm ;
    sdata:assessmentOutcome "pass" ;
    sdata:generatedBy ex:zugversuch_001 ;
    sdata:describes ex:probe_42 ;
    sdata:signedBy ex:pruefinstitut_ag .
ex:req_rm a sdata:Requirement .
ex:zugversuch_001 a sdata:Process .
ex:probe_42 a sdata:Specimen .
ex:pruefinstitut_ag a sdata:Organization .
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

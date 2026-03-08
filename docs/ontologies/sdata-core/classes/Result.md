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
Semantisches Ergebnis-Bündel. Assessment-Verhalten
    emergiert aus sdata:assessesRequirement + assessmentOutcome.
    Doppeltypisierung Result ∩ VerifiableCredential möglich.

## Examples
- `Zugversuchsergebnis, FEM-Ergebnis, Compliance-Bewertung.`
## Industriebeispiel
- Bestanden/Nicht-bestanden Ergebnis einer elektrischen End-of-Line-Pruefung.
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

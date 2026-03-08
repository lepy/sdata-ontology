# sdata:Requirement
## IRI
`https://w3id.org/sdata/core/Requirement`
## Labels
- `Anforderung`
- `Requirement`
## Direct Superclasses
- [`sdata:Norma`](./Norma.md)
## Direct Subclasses
- (none)
## Comment
ATOMARE Anforderung oder Grenzwert. Bündelung
    zu Specification oder Regulation via sdata:comprises.

## Examples
- `Rm ≥ 340 MPa, Ra ≤ 1.6 µm, FU: 1 kg Stahl ab Werk.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Atomare Zugfestigkeitsanforderung.
ex:req_rm a sdata:Requirement ;
    sdata:hasName "Rm ≥ 340 MPa" ;
    sdata:evaluates ex:probe_42 .
ex:probe_42 a sdata:Specimen .
ex:result_rm a sdata:Result ;
    sdata:assessesRequirement ex:req_rm ;
    sdata:assessmentOutcome "pass" .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:assessesRequirement`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Requirement .
```

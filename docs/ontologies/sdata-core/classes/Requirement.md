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
ATOMARE Anforderung oder Grenzwert. Jede einzelne
    Anforderung ist eine eigenständige Norma-Instanz. Bündelung
    mehrerer Requirements zu einer Specification oder Regulation
    ist Institutio (via sdata:comprises).

## Examples
- `Rm ≥ 340 MPa, Ra ≤ 1.6 µm, FU: 1 kg Stahl ab Werk.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Grenzwertanforderung `Leitfaehigkeit >= 58 MS/m` fuer Kupferkomponenten.
ex:requirement_001 a sdata:Requirement ;
  sdata:hasIdentifier "REQUIREMENT-001" ;
  sdata:hasName "Requirement Leitfaehigkeitsgrenze" ;
  sdata:evaluates ex:result_001 .

ex:result_001 a sdata:Result ; sdata:assessmentOutcome "pass" .
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

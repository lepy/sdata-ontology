# sdata:Requirement
## IRI
`https://w3id.org/sdata/core/Requirement`
## Labels
- `Anforderung`
- `Requirement`
## Direct Superclasses
- `min:Norma`
## Direct Subclasses
- (none)
## Comment
ATOMARE Anforderung oder Grenzwert. Jede einzelne
    Anforderung ist eine eigenständige Norma-Instanz. Bündelung
    mehrerer Requirements zu einer Specification oder Regulation
    ist Institutio (via sdata:comprises).

## Examples
- `Rm ≥ 340 MPa, Ra ≤ 1.6 µm, FU: 1 kg Stahl ab Werk.`
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

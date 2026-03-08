# sdata:Accreditation
## IRI
`https://w3id.org/sdata/core/Accreditation`
## Labels
- `Accreditation`
- `Akkreditierung`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `DAkkS-Akkreditierung, UKAS.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# DAkkS-Akkreditierung eines Prüflabors für Zugversuche.
ex:dakks_001 a sdata:Accreditation ;
    sdata:hasName "DAkkS-Akkreditierung DIN EN ISO/IEC 17025" ;
    sdata:constitutedBy ex:dakks .
ex:dakks a sdata:Organization ;
    sdata:hasName "Deutsche Akkreditierungsstelle" .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Accreditation .
```

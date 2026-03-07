# sdata:Organization
## IRI
`https://w3id.org/sdata/core/Organization`
## Labels
- `Organisation`
- `Organization`
## Direct Superclasses
- `min:Agent`
## Direct Subclasses
- (none)
## Comment
Organisation als HANDELNDER Agent. Wenn dasselbe
    Unternehmen als juristische Person oder anerkannte Institution
    modelliert werden soll, ZUSÄTZLICH Doppeltypisierung mit
    min:Institutio oder sdata:LegalEntity.
    Organisation als Handelnder: sdata:Organization (Agent).
    Organisation als juristische Person: + min:Institutio.

## Examples
- `Stahlwerk, Prüflabor, Zertifizierer, OEM, Recycler.`
## Used As Domain
- `sdata:hasLegalEntity`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Organization .
```

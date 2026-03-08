# sdata:Certification
## IRI
`https://w3id.org/sdata/core/Certification`
## Labels
- `Certification`
- `Zertifizierung`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `ISO 9001, EN 10204 3.1, CE-Kennzeichnung.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# ISO-9001-Zertifikat eines Stahlwerks.
ex:iso9001_stahlwerk a sdata:Certification ;
    sdata:hasName "ISO 9001:2015" ;
    sdata:constitutedBy ex:tuev_sued .
ex:tuev_sued a sdata:Organization ;
    sdata:hasName "TÜV SÜD" .
ex:stahlwerk_ag a sdata:Organization ;
    sdata:certifiedUnder ex:iso9001_stahlwerk .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:certifiedUnder`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Certification .
```

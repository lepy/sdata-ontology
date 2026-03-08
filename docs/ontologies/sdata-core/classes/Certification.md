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

# ISO-9001-Zertifikat eines Ziehwerks als Nachweis im Produktpass.
ex:certification_001 a sdata:Certification ;
  sdata:hasIdentifier "CERTIFICATION-001" ;
  sdata:hasName "Certification Branchenregel" ;
  sdata:typifies ex:process_001 ;
  sdata:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
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

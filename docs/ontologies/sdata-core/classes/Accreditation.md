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

# DAkkS-Akkreditierung eines Prueflabors fuer Zugversuche nach DIN EN ISO 6892-1.
ex:accreditation_001 a sdata:Accreditation ;
  sdata:hasIdentifier "ACCREDITATION-001" ;
  sdata:hasName "Accreditation Branchenregel" ;
  sdata:typifies ex:process_001 ;
  sdata:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
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

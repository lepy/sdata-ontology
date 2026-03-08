# sdata:TrustFramework
## IRI
`https://w3id.org/sdata/core/TrustFramework`
## Labels
- `Trust Framework`
- `Vertrauensrahmen`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Catena-X, GAIA-X, EBSI, IBU EPD-Programm.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# EUDI-/VC-Vertrauensrahmen fuer interoperable Nachweise im DPP.
ex:trust_framework_001 a sdata:TrustFramework ;
  sdata:hasIdentifier "TRUSTFRAMEWORK-001" ;
  sdata:hasName "TrustFramework Branchenregel" ;
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

ex:example a sdata:TrustFramework .
```

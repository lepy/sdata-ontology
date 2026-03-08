# sdata:Registry
## IRI
`https://w3id.org/sdata/core/Registry`
## Labels
- `Register`
- `Registry`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
(none)

## Examples
- `Catena-X Registry, GAIA-X Registry.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Branchenregister zur Aufloesung verifizierbarer Hersteller-Identitaeten.
ex:registry_001 a sdata:Registry ;
  min:hasIdentifier "REGISTRY-001" ;
  min:hasName "Registry Branchenregel" ;
  min:typifies ex:process_001 ;
  min:comprises ex:req_001 .

ex:req_001 a sdata:Requirement .
ex:process_001 a sdata:Process .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:registeredIn`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Registry .
```

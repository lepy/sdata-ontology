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
@prefix ex:    <https://example.org/industry/> .

# Catena-X DID-Registry.
ex:catena_x_registry a sdata:Registry ;
    sdata:hasName "Catena-X DID Registry" ;
    sdata:constitutedBy ex:catena_x_consortium .
ex:catena_x_consortium a sdata:Organization .
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

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

# Catena-X als Vertrauensrahmen.
ex:catena_x a sdata:TrustFramework ;
    sdata:hasName "Catena-X" ;
    sdata:constitutedBy ex:catena_x_consortium ;
    sdata:hasComponent ex:catena_x_registry .
ex:catena_x_consortium a sdata:Organization .
ex:catena_x_registry a sdata:Registry .
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

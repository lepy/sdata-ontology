# sdata:Typus
## IRI
`https://w3id.org/sdata/core/Typus`
## Labels
- `Typus`
- `Typus`
## Direct Superclasses
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- [`sdata:BoundaryType`](./BoundaryType.md)
- [`sdata:DataFormat`](./DataFormat.md)
- [`sdata:MaterialGrade`](./MaterialGrade.md)
- [`sdata:ModelType`](./ModelType.md)
- [`sdata:ProcessType`](./ProcessType.md)
- [`sdata:ProductType`](./ProductType.md)
## Comment
Konventionelle Wesensbestimmung. Bündelt Forma.
    Typifiziert Nexus via sdata:typifies.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Typus ist die Basisklasse — verwende Subklassen.
# MaterialGrade, ProcessType, ProductType, DataFormat, etc.
ex:DC04 a sdata:MaterialGrade ;
    sdata:hasName "DC04" ;
    sdata:typifies ex:blech_042 .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Typus .
```

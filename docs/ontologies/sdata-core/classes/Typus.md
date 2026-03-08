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
- [`sdata:HardwareType`](./HardwareType.md)
- [`sdata:MaterialGrade`](./MaterialGrade.md)
- [`sdata:ModelType`](./ModelType.md)
- [`sdata:ProcessType`](./ProcessType.md)
- [`sdata:ProductType`](./ProductType.md)
- [`sdata:SoftwareType`](./SoftwareType.md)
## Comment
Konventionelle Wesensbestimmung in der Domäne.
    Bündelt Norma, Structura, Lex zu einem benannten Typ.
    Spezialisierung von Institutio für technische Klassifikation.
    Typifiziert Nexus via sdata:typifies.
    Bündelt Forma via sdata:comprises.

## Examples
- (none)
## Industriebeispiel
- Domänentyp `Leiterklasse 5` zur standardisierten Einordnung von Produkten.
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

# sdata:Object
## IRI
`https://w3id.org/sdata/core/Object`
## Labels
- `Object`
- `Objekt`
## Direct Superclasses
- `min:Object`
## Direct Subclasses
- [`sdata:Hardware`](./Hardware.md)
- [`sdata:Material`](./Material.md)
- [`sdata:Person`](./Person.md)
- [`sdata:Site`](./Site.md)
- [`sdata:Specimen`](./Specimen.md)
- [`sdata:Substance`](./Substance.md)
## Comment
Fassade für min:Object. Das, was da ist.
    Materielle Persistenz.

    Direkte Instanziierung nur für Site.
    Alle anderen physischen Dinge sind Agents
    (Hardware, Material, Substance, Specimen, Person).

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Object ist fast immer abstrakt — verwende Subklassen.
# Einzige direkte Instanziierung: Site.
ex:werk_duisburg a sdata:Site ;
    sdata:hasName "Werk Duisburg" .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Object .
```

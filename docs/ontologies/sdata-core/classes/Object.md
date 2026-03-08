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

# Praxisfall aus der Industrie, in dem `sdata:Object` zur semantischen Modellierung eingesetzt wird.
ex:object_001 a sdata:Object ;
  sdata:hasIdentifier "OBJECT-001" ;
  sdata:hasName "Object Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:object_001 ;
  sdata:producedBy ex:process_001 .

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

ex:example a sdata:Object .
```

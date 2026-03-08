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
- [`sdata:HardwareAgent`](./HardwareAgent.md)
- [`sdata:Material`](./Material.md)
- [`sdata:Person`](./Person.md)
- [`sdata:Product`](./Product.md)
- [`sdata:Site`](./Site.md)
- [`sdata:Software`](./Software.md)
- [`sdata:Specimen`](./Specimen.md)
- [`sdata:Substance`](./Substance.md)
## Comment
Fassade für min:Object. Das, was da ist.
    Materielle Persistenz. Alle sdata-Object-Klassen
    erben von sdata:Object, nicht von min:Object.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Object` zur semantischen Modellierung eingesetzt wird.
ex:object_001 a sdata:Object ;
  min:hasIdentifier "OBJECT-001" ;
  min:hasName "Object Instanz" ;
  min:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
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

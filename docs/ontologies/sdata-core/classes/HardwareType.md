# sdata:HardwareType
## IRI
`https://w3id.org/sdata/core/HardwareType`
## Labels
- `Gerätetyp`
- `Hardware Type`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Hardware-Typs. Ersetzt Hardware-Subklassen.

## Examples
- `Universalprüfmaschine, Hydraulische Presse, Thermoelement Typ K.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Typisierung einer Ofenanlage als `Induktionsofen 2 MW`.
ex:hardware_type_001 a sdata:HardwareType ;
  min:hasIdentifier "HARDWARETYPE-001" ;
  min:hasName "HardwareType Klassifikation" ;
  min:typifies ex:hardware_001 .

ex:hardware_001 a sdata:Hardware .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:HardwareType .
```

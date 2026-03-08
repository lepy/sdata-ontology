# sdata:Institutio
## IRI
`https://w3id.org/sdata/core/Institutio`
## Labels
- `Institutio`
- `Institutio`
## Direct Superclasses
- `min:Institutio`
## Direct Subclasses
- [`sdata:Accreditation`](./Accreditation.md)
- [`sdata:Certification`](./Certification.md)
- [`sdata:LegalEntity`](./LegalEntity.md)
- [`sdata:LifecyclePhase`](./LifecyclePhase.md)
- [`sdata:Organization`](./Organization.md)
- [`sdata:Registry`](./Registry.md)
- [`sdata:Regulation`](./Regulation.md)
- [`sdata:Specification`](./Specification.md)
- [`sdata:TrustFramework`](./TrustFramework.md)
- [`sdata:Typus`](./Typus.md)
## Comment
Fassade für min:Institutio. Das, was anerkannt wird.
    Kollektive Anerkennung.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Praxisfall aus der Industrie, in dem `sdata:Institutio` zur semantischen Modellierung eingesetzt wird.
ex:institutio_001 a sdata:Institutio ;
  min:hasIdentifier "INSTITUTIO-001" ;
  min:hasName "Institutio Branchenregel" ;
  min:typifies ex:process_001 ;
  min:comprises ex:req_001 .

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

ex:example a sdata:Institutio .
```

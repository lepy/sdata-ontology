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
Fassade für min:Institutio. Kollektive Anerkennung.

## Examples
- (none)
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Institutio ist eine Fassade — verwende Subklassen.
# Regulation, Specification, Certification, etc.
ex:espr a sdata:Regulation ;
    sdata:hasName "ESPR" ;
    sdata:comprises ex:req_dpp_pflicht .
ex:req_dpp_pflicht a sdata:Requirement .
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

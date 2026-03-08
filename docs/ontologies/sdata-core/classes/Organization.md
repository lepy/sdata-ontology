# sdata:Organization
## IRI
`https://w3id.org/sdata/core/Organization`
## Labels
- `Organisation`
- `Organization`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Agent ∩ Institutio.
    Identitätskriterium: institutionelle Identität.
    sdata:LegalEntity bleibt für Fälle ohne Agency.

## Examples
- `Stahlwerk, Prüflabor, Zertifizierer, OEM, Recycler.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Stahlwerk als Agent ∩ Institutio.
ex:stahlwerk_ag a sdata:Organization ;
    sdata:hasName "Stahlwerk AG" ;
    sdata:identifiedBy ex:did_stahlwerk ;
    sdata:locatedAt ex:werk_duisburg ;
    sdata:hasLegalEntity ex:stahlwerk_gmbh .
ex:did_stahlwerk a sdata:Identifier .
ex:werk_duisburg a sdata:Site .
ex:stahlwerk_gmbh a sdata:LegalEntity .
```
## Used As Domain
- `sdata:hasLegalEntity`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Organization .
```

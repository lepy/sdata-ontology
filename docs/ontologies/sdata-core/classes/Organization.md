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

# Tier-1-Lieferant als organisatorischer Akteur im DPP-Netzwerk.
ex:organization_001 a sdata:Organization ;
  sdata:hasIdentifier "ORG-001" ;
  sdata:hasName "Tier-1 Lieferant Nord" ;
  sdata:performs ex:process_001 ;
  sdata:owns ex:asset_001 .

ex:process_001 a sdata:Process .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
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

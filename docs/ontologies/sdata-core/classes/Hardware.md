# sdata:Hardware
## IRI
`https://w3id.org/sdata/core/Hardware`
## Labels
- `Hardware`
- `Hardware`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Physisches Gerät, Maschine, Bauteil, Werkzeug —
    IMMER Agent. Agent ∩ Object.
    Identitätskriterium: materiale Kontinuität.

    Alles Physische, das handeln KANN, ist Hardware.
    "Ist ein Produkt" kommt über sdata:typifiedBy →
    sdata:ProductType.

    Ob aktiv: sdata:hasStatus.
    Klassifizierung: sdata:ProductType.

## Examples
- `Presse, Ofen, Prüfmaschine, Sensor, Werkzeug, Roboterarm, Seitenteil, Hammer, Felge.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Universalprüfmaschine Zwick Z250 im Zugversuch.
ex:zwick_z250 a sdata:Hardware ;
    sdata:hasName "Zwick Z250" ;
    sdata:typifiedBy ex:universalpruefmaschine ;
    sdata:performs ex:zugversuch_001 ;
    sdata:locatedAt ex:labor_berlin ;
    sdata:hasStatus "running" .
ex:universalpruefmaschine a sdata:ProductType ;
    sdata:hasName "Universalprüfmaschine" .
ex:zugversuch_001 a sdata:Process .
ex:labor_berlin a sdata:Site .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:usesTool`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Hardware .
```

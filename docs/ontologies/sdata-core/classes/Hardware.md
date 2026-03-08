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

# Zugpruefmaschine als physisches Betriebsmittel im Prueflabor.
ex:hardware_001 a sdata:Hardware ;
  sdata:hasIdentifier "HARDWARE-001" ;
  sdata:hasName "Hardware als materieller Agent" ;
  sdata:performs ex:process_001 ;
  sdata:actsOn ex:asset_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:asset_001 .
ex:asset_001 a sdata:Hardware ; sdata:typifiedBy ex:product_type_001 .
ex:product_type_001 a sdata:ProductType .
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

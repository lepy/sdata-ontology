# Rohstoffherkunft und Chain-of-Custody (Kupfer)

Dieses Muster deckt Herkunft, Besitzkette und Registereintrag von Kupferlosen ab.

## Kernentscheidung

- Physisches Los: `sdata:Material`
- Beteiligte Akteure: `sdata:Organization`
- Nachweis-/Trackingdaten: `sdata:Identifier`, `sdata:Data`
- Uebergabeschritt: `sdata:Process`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:erz_lot_001 a sdata:Material ;
    sdata:identifiedBy ex:id_erz_lot_001 ;
    sdata:hasCustodian ex:mine_operator ;
    sdata:locatedAt ex:site_mine_07 .

ex:id_erz_lot_001 a sdata:Identifier ;
    sdata:hasScheme "LOT-ID" ;
    sdata:hasValue "ORE-2026-0001" ;
    sdata:hasIssuer ex:mine_operator ;
    sdata:registeredIn ex:registry_raw_material .

ex:schmelzen_001 a sdata:Process ;
    sdata:hasInput ex:erz_lot_001 ;
    sdata:hasOutput ex:kathode_lot_001 ;
    sdata:performedBy ex:smelter_org .

ex:kathode_lot_001 a sdata:Material ;
    sdata:identifiedBy ex:id_kathode_lot_001 ;
    sdata:hasCustodian ex:smelter_org .
```

## Minimal notwendige Relationen

- `sdata:identifiedBy`
- `sdata:hasIssuer`
- `sdata:registeredIn`
- `sdata:hasCustodian`
- `sdata:hasInput`, `sdata:hasOutput`
- `sdata:performedBy`


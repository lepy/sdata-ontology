# Prozesskette (Kupferherstellung End-to-End)

Dieses Muster modelliert die durchgaengige Herstellungssequenz von Rohmaterial bis Halbzeug.

## Kernentscheidung

- Jeder Fertigungsschritt: `sdata:Process`
- Material-/Produktzustaende je Schritt: `sdata:Material`, `sdata:Product`
- Reihenfolge explizit: `sdata:succeeds` / `sdata:precedes`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:smelting_001 a sdata:Process ;
    sdata:hasInput ex:erz_lot_001 ;
    sdata:hasOutput ex:kathode_lot_001 .

ex:casting_001 a sdata:Process ;
    sdata:hasInput ex:kathode_lot_001 ;
    sdata:hasOutput ex:bramme_001 ;
    sdata:succeeds ex:smelting_001 .

ex:rolling_001 a sdata:Process ;
    sdata:hasInput ex:bramme_001 ;
    sdata:hasOutput ex:bandcoil_001 ;
    sdata:succeeds ex:casting_001 .

ex:annealing_001 a sdata:Process ;
    sdata:hasInput ex:bandcoil_001 ;
    sdata:hasOutput ex:bandcoil_001_geglueht ;
    sdata:succeeds ex:rolling_001 .
```

## Minimal notwendige Relationen

- `sdata:hasInput`
- `sdata:hasOutput`
- `sdata:succeeds` (optional inverse `sdata:precedes`)


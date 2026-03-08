# Ausschuss, Nacharbeit und Yield

Dieses Muster macht Gutteile, Ausschuss und Nacharbeit als eigene Prozesspfade sichtbar.

## Kernentscheidung

- Hauptprozess + Nacharbeit: jeweils `sdata:Process`
- Ausschuss-/Nacharbeitsdaten: `sdata:Result`
- Material-/Produktfluss: `sdata:hasInput`, `sdata:hasOutput`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:stamping_001 a sdata:Process ;
    sdata:hasInput ex:bandcoil_001 ;
    sdata:hasOutput ex:part_good_001 ;
    sdata:hasOutput ex:part_scrap_001 ;
    sdata:hasData ex:yield_report_001 .

ex:rework_001 a sdata:Process ;
    sdata:hasInput ex:part_scrap_001 ;
    sdata:hasOutput ex:part_reworked_001 ;
    sdata:succeeds ex:stamping_001 .

ex:yield_report_001 a sdata:Result ;
    sdata:producedBy ex:stamping_001 ;
    sdata:describes ex:part_good_001 ;
    sdata:hasSource "QMS-Line-7" .
```

## Minimal notwendige Relationen

- `sdata:hasInput`, `sdata:hasOutput`
- `sdata:succeeds`
- `sdata:hasData`
- `sdata:producedBy`


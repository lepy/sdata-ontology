# DPP (Digital Product Passport)

Ein DPP wird in sdata primaer als **`sdata:ProductPassport`** modelliert,
der ein Produkt beschreibt und versioniert vorliegt.

## Kernentscheidung

- DPP selbst: `sdata:ProductPassport`
- Referenziertes Produkt: `sdata:Product`
- Erzeugungs-/Aktualisierungsablauf: `sdata:Process`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/dpp/> .

ex:BatteryPack_001 a sdata:Product ;
    sdata:hasIdentifier "PROD-PACK-001" .

ex:DPP_Update_2026_03 a sdata:Process ;
    sdata:hasInput ex:BatteryPack_001 ;
    sdata:generates ex:DPP_001 .

ex:DPP_001 a sdata:ProductPassport ;
    sdata:describes ex:BatteryPack_001 ;
    sdata:producedBy ex:DPP_Update_2026_03 ;
    sdata:hasVersion "2026-03" .
```

## Erweiterungen in der Praxis

- Zertifikate, Reports und Messergebnisse als weitere `sdata:Data` verknuepfen.
- Nachfuehrung ueber Versionen/Zeitraeume explizit modellieren.
- DPP-Versionen ueber `sdata:supersedes` / `sdata:supersededBy` verketten.

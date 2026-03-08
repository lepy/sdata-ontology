# Reibung

Diese Seite beschreibt Reibung als sdata-Modellierungsmuster fuer industrielle Prozesse.

## Kernentscheidung

- Reibungsvorgang: `sdata:Process`
- Kontaktflaeche: `sdata:Boundary`
- Reibungstyp: `sdata:BoundaryType`
- Nachweisdaten: `sdata:Result`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/reibung/> .

ex:reibung_001 a sdata:Process ;
    sdata:hasInput ex:blech_001 ;
    sdata:hasInput ex:werkzeug_001 ;
    sdata:hasOutput ex:blech_001_geformt ;
    sdata:hasBoundary ex:kontaktzone_001 ;
    sdata:generates ex:reibung_result_001 .

ex:kontaktzone_001 a sdata:Boundary ;
    sdata:typifiedBy ex:coulomb_reibung_typ .

ex:coulomb_reibung_typ a sdata:BoundaryType ;
    sdata:typifies ex:kontaktzone_001 .

ex:reibung_result_001 a sdata:Result ;
    sdata:producedBy ex:reibung_001 ;
    sdata:describes ex:blech_001_geformt .
```

## Minimal notwendige Relationen

- `sdata:hasInput`, `sdata:hasOutput`
- `sdata:hasBoundary`
- `sdata:typifiedBy` / `sdata:typifies`
- `sdata:generates`
- `sdata:producedBy`, `sdata:describes`


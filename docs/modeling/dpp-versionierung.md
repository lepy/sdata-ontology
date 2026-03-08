# DPP-Datenmodell und Versionierung

Dieses Muster modelliert den Produktpass als versionierte Datenentitaet.

## Kernentscheidung

- Produktpass: `sdata:ProductPassport`
- Referenziertes Produkt: `sdata:Product`
- Versionskette: `sdata:supersedes` / `sdata:supersededBy`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

ex:product_001 a sdata:Product ;
    sdata:identifiedBy ex:product_id_001 .

ex:dpp_v1 a sdata:ProductPassport ;
    sdata:describes ex:product_001 ;
    sdata:hasVersion "1.0" ;
    sdata:validFrom "2026-01-01T00:00:00Z"^^xsd:dateTime .

ex:dpp_v2 a sdata:ProductPassport ;
    sdata:describes ex:product_001 ;
    sdata:hasVersion "2.0" ;
    sdata:supersedes ex:dpp_v1 ;
    sdata:validFrom "2026-04-01T00:00:00Z"^^xsd:dateTime ;
    sdata:signedBy ex:oem_org .
```

## Minimal notwendige Relationen

- `sdata:describes`
- `sdata:hasVersion`
- `sdata:supersedes`
- `sdata:validFrom`
- `sdata:signedBy`


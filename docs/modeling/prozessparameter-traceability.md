# Prozessparameter und Traceability

Dieses Muster haelt Prozessparameter, Quellen und Dateien revisionsfaehig fest.

## Kernentscheidung

- Prozessinstanz: `sdata:Process`
- Mess-/Protokolldaten: `sdata:Data`, `sdata:ResultFile`
- Rueckverknuepfung: `sdata:producedBy`, `sdata:hasData`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

ex:annealing_001 a sdata:Process ;
    sdata:hasStartTime "2026-03-07T08:10:00Z"^^xsd:dateTime ;
    sdata:hasEndTime "2026-03-07T08:55:00Z"^^xsd:dateTime ;
    sdata:hasData ex:param_log_annealing_001 .

ex:param_log_annealing_001 a sdata:ResultFile ;
    sdata:producedBy ex:annealing_001 ;
    sdata:hasFormat "text/csv" ;
    sdata:hasChecksum "sha256:9f7b..." ;
    sdata:hasSource "PLC-Line-3" .
```

## Minimal notwendige Relationen

- `sdata:hasData`
- `sdata:producedBy`
- `sdata:hasStartTime`, `sdata:hasEndTime`
- `sdata:hasFormat`, `sdata:hasChecksum`, `sdata:hasSource`


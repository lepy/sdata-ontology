# Qualitaet und Pruefmerkmale

Dieses Muster verbindet pruefbare Anforderungen mit Messergebnissen.

## Kernentscheidung

- Pruefling: `sdata:Specimen`
- Anforderung: `sdata:Requirement`
- Auswertung: `sdata:Result`
- Stammmaterial: `sdata:Material` oder `sdata:Product`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:specimen_001 a sdata:Specimen ;
    sdata:sampledFrom ex:bandcoil_001_geglueht .

ex:req_conductivity_min a sdata:Requirement .

ex:test_result_001 a sdata:Result ;
    sdata:describes ex:specimen_001 ;
    sdata:assessesRequirement ex:req_conductivity_min ;
    sdata:assessmentOutcome "pass" ;
    sdata:hasConfidence 0.98 .
```

## Minimal notwendige Relationen

- `sdata:sampledFrom`
- `sdata:describes`
- `sdata:assessesRequirement`
- `sdata:assessmentOutcome`


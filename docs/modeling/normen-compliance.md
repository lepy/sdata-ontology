# Normen und Compliance

Dieses Muster modelliert regulatorische Anforderungen, Spezifikationen und deren Nachweise.

## Kernentscheidung

- Regelwerke: `sdata:Regulation`, `sdata:Specification`, `sdata:Requirement`
- Bewertungsnachweis: `sdata:Result`
- Formale Bestaetigung: `sdata:Certification`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:rohs_rule a sdata:Regulation ;
    sdata:governs ex:part_good_001 .

ex:customer_spec_44 a sdata:Specification ;
    sdata:specifies ex:part_good_001 .

ex:req_pb_max a sdata:Requirement .

ex:compliance_result_001 a sdata:Result ;
    sdata:describes ex:part_good_001 ;
    sdata:assessesRequirement ex:req_pb_max ;
    sdata:assessmentOutcome "pass" .

ex:iso9001_cert_2026 a sdata:Certification .

ex:part_good_001 sdata:certifiedUnder ex:iso9001_cert_2026 .
```

## Minimal notwendige Relationen

- `sdata:governs`
- `sdata:specifies`
- `sdata:assessesRequirement`
- `sdata:assessmentOutcome`
- `sdata:certifiedUnder`

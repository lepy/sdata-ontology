# sdata-material-state.ttl

Material-State-Erweiterung (`v0.2.0`) für `sdata-core v0.8.0`.

Modellidee:

- Zustand wird als Vektor über Achsen modelliert (`sms:StateAxis`).
- Konkrete Werte kommen aus SKOS-ConceptSchemes.
- Zuordnung erfolgt über `sms:StateAssignment`.

## Enthaltene Achsen

- `OriginAxis`
- `ProcessingAxis`
- `ConditionAxis`
- `FormAxis`
- `GradeAxis`
- `ComplianceAxis`
- `CompositionAxis`
- `LifecyclePhaseAxis`
- `StructureAxis` (neu)
- `RoleAxis` (neu)

## Kernrelationen

- `sms:hasStateAssignment` (`Material`/`Product` -> `StateAssignment`)
- `sms:onAxis` (`StateAssignment` -> `StateAxis`)
- `sms:hasStateValue` (`StateAssignment` -> `skos:Concept`)
- `sms:hasConceptScheme` (`StateAxis` -> `skos:ConceptScheme`)

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DC04 a sdata:Material ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:OriginAxis ;
    sms:hasStateValue sms:origin.Virgin
  ] ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:FormAxis ;
    sms:hasStateValue sms:form.Sheet
  ] .

ex:Probe_A1 a sdata:Product ;
  sdata:madeOf ex:DC04 ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:StructureAxis ;
    sms:hasStateValue sms:structure.SinglePart
  ] ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:RoleAxis ;
    sms:hasStateValue sms:role.Specimen
  ] .
```

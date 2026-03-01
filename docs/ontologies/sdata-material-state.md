# sdata-material-state.ttl

State-Space-Erweiterung (`v0.4.0`) für `sdata-core v0.9.1`.

Modellidee:

- Zustand wird als Vektor über Achsen modelliert (`sms:StateAxis`).
- Konkrete Werte kommen aus SKOS-ConceptSchemes.
- Zuordnung erfolgt über `sms:StateAssignment`.

## Enthaltene Achsen (13)

- Material-Achsen: `OriginAxis`, `ProcessingAxis`, `ConditionAxis`, `FormAxis`, `GradeAxis`, `ComplianceAxis`, `CompositionAxis`, `LifecyclePhaseAxis`
- Product-Achsen: `StructureAxis`, `RoleAxis`
- Process-Achsen: `MethodAxis`, `DomainAxis`
- Data-Achse: `DataTypeAxis`

## Kernrelationen

- `sms:hasStateAssignment` (`Object`/`Process` -> `StateAssignment`)
- `sms:onAxis` (`StateAssignment` -> `StateAxis`)
- `sms:hasStateValue` (`StateAssignment` -> `skos:Concept`)
- `sms:hasConceptScheme` (`StateAxis` -> `skos:ConceptScheme`)

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Probe_A1 a sdata:Product ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:RoleAxis ;
    sms:hasStateValue sms:role.Specimen
  ] .

ex:Zugversuch_A1 a sdata:Process ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:MethodAxis ;
    sms:hasStateValue sms:method.TensileTest
  ] .

ex:Messdaten_A1 a sdata:Data ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:DataTypeAxis ;
    sms:hasStateValue sms:datatype.TestReport
  ] .
```

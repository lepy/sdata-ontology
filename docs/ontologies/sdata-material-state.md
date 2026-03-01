# sdata-material-state.ttl

State-Space-Erweiterung (`v0.5.0`) fuer `sdata-core v0.10.0`.

## Zweck

`sdata-core` bleibt bewusst klein. Fachliche Auspraegungen werden ueber Achsenwerte modelliert.

- `sms:StateAxis`
: beschreibt die Dimension.
- `sms:StateAssignment`
: verbindet Resource + Achse + Wert.
- `skos:Concept`
: konkreter Wert (hierarchisch erweiterbar).

## Achsen (13)

- Material:
  - `OriginAxis`, `ProcessingAxis`, `ConditionAxis`, `FormAxis`, `GradeAxis`, `ComplianceAxis`, `CompositionAxis`, `LifecyclePhaseAxis`
- Product:
  - `StructureAxis`, `RoleAxis`
- Process:
  - `MethodAxis`, `DomainAxis`
- Data:
  - `DataTypeAxis`

## Neu in v0.5.0

- `MethodAxis` hat nun 6 Top-Level-Kategorien:
  - `Transformative`, `Observational`, `Computational`, `Logistical`, `Administrative`, `Creative`
- Neue Method-Konzepte:
  - `Approval`, `Certification`, `QualityGate`, `Design`, `ProcessPlanning`, `MaterialSelection`
- Neue Umweltmethoden unter `Transformative`:
  - `Degradation` mit `Corrosion`, `Weathering`, `NaturalAging`, `BiologicalDecay`, `FatigueDamage`

## Kernrelationen

- `sms:hasStateAssignment` (`sdata:Object` oder `sdata:Process` -> `sms:StateAssignment`)
- `sms:onAxis` (`sms:StateAssignment` -> `sms:StateAxis`)
- `sms:hasStateValue` (`sms:StateAssignment` -> `skos:Concept`)
- `sms:hasConceptScheme` (`sms:StateAxis` -> `skos:ConceptScheme`)

## Praxisbeispiele

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/demo/> .

# Product-Rolle
ex:Specimen_A1 a sdata:Product ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:RoleAxis ;
    sms:hasStateValue sms:role.Specimen
  ] .

# Process-Methode
ex:TensileTest_A1 a sdata:Process ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:MethodAxis ;
    sms:hasStateValue sms:method.TensileTest
  ] ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:DomainAxis ;
    sms:hasStateValue sms:domain.Structural
  ] .

# Data-Typ
ex:Report_A1 a sdata:Data ;
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:DataTypeAxis ;
    sms:hasStateValue sms:datatype.TestReport
  ] .
```

## Modellierungshinweise

- Nutze Core-Klassen fuer Struktur.
- Nutze State-Achsen fuer Semantik und Fachdetail.
- Erweitere Werte als SKOS-Konzepte im passenden `*-values` Scheme.
- Erweitere Achsen nur, wenn bestehende Achsen fachlich nicht ausreichen.

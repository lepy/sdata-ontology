# Quickstart

Dieser Quickstart zeigt den typischen Workflow auf `MIN v3.2.0`.
Er funktioniert fuer beide Core-Profile:
- `sdata-core.ttl` (`v0.12.0`, lean profile)
- `sdata-core-v0.13.1.ttl` (extended profile mit Forma-Fassaden + DPP-Haertung)

## 1. Setup

```bash
make setup
```

## 2. Checks ausfuehren

```bash
make test
make validate
make lint
```

## 3. Minimales Datenmodell schreiben

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/demo/> .

ex:Steel_DC04 a sdata:Material ;
  min:hasIdentifier "MAT-DC04-001" .

ex:Specimen_42 a sdata:Product ;
  min:hasIdentifier "SPEC-42" ;
  sdata:hasMaterial ex:Steel_DC04 .

ex:TensileTest_42 a sdata:Process ;
  min:hasInput ex:Specimen_42 ;
  min:generates ex:TensileData_42 .

ex:TensileData_42 a sdata:Data ;
  min:describes ex:Specimen_42 ;
  sdata:producedBy ex:TensileTest_42 ;
  sdata:hasVersion "1.0.0" .
```

## 4. State Space nutzen (optional, empfohlen)

```turtle
ex:TensileTest_42
  sms:hasStateAssignment [
    a sms:StateAssignment ;
    sms:onAxis sms:MethodAxis ;
    sms:hasStateValue sms:method.TensileTest
  ] .
```

## 5. Diagramme erzeugen

```bash
make viz-all
make viz-examples
make viz-min-v3-examples
make viz-min-core-interactive
```

Wichtige Outputs:

- `docs/diagrams/sdata-min-core-hierarchy.svg`
- `docs/diagrams/sdata-min-core-hierarchy-interactive.html`
- `docs/diagrams/sdata-class-hierarchy.svg`
- `docs/diagrams/sdata-material-state.svg`

## 6. Migration aus v0.10/OPA

Nutze die Checklisten in:

- `docs/ontologies/MIGRATION-v0.10-to-v0.12.md`
- `docs/ontologies/MIGRATION-v0.12-to-v0.13.md`
- `docs/ontologies/MIGRATION-v0.13.0-to-v0.13.1.md`

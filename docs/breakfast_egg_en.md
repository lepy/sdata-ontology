# Breakfast Egg (EN)

This page contains a compact end-to-end modeling example for a "breakfast egg",
showing product, process, data, and result.

## Goal

- Minimal, readable example for `sdata:Product`, `sdata:Process`,
  `sdata:Data`, and `sdata:Result`.
- Provenance trace: which process generated which output?
- Reusable pattern for larger DPP and digital twin setups.

## Compact Turtle Example

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/breakfast/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

ex:egg_001 a sdata:Product ;
  sdata:label "Breakfast Egg #001" .

ex:boiling_001 a sdata:Process ;
  sdata:label "Boiling" ;
  sdata:hasInput ex:egg_001 ;
  sdata:startedAt "2026-03-08T07:00:00Z"^^xsd:dateTime .

ex:egg_state_001 a sdata:Result ;
  sdata:label "Soft-boiled" ;
  sdata:generatedBy ex:boiling_001 .

ex:temp_data_001 a sdata:Data ;
  sdata:label "Water temperature log" ;
  sdata:generatedBy ex:boiling_001 .
```

## Interpretation

- `ex:egg_001` is the product under observation.
- `ex:boiling_001` models the process step.
- `ex:temp_data_001` captures process data.
- `ex:egg_state_001` is the resulting process output.

See also the [German version](breakfast_egg_de.md).

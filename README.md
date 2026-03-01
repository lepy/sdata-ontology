# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core version: `sdata-core-v0.8.0.ttl`
- Core foundation: `MIN` + `OPA`
- Material-state extension: `sdata-material-state-v0.2.0.ttl`

## Main modules

- `sdata-core.ttl` / `sdata-core-v0.8.0.ttl`
: Core model with 30 classes, 19 object properties, 8 datatype properties.
- `sdata-material-state.ttl`
: Material state space extension (10 axes incl. `StructureAxis` + `RoleAxis`).
- `sdata-agents.ttl`
: Agent-type SKOS vocabulary.
- `sdata-processtypes.ttl`
: Process verb-axis extension.
- `sdata-lifecycle.ttl`
: Lifecycle flow model.
- `shapes/sdata-core-shapes.ttl`
: SHACL validation shapes.

## Namespaces

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
```

## Core categories (v0.8.0)

- `sdata:Object`
- `sdata:Process`
- `sdata:Data`
- `sdata:Agent`

Main object classes:

- `sdata:Material`
- `sdata:Product`
- `sdata:Hardware`
- `sdata:Software`

## Material state space

`sdata-material-state` adds:

- `sms:StateAxis`
- `sms:StateAssignment`
- 10 predefined axis classes (`OriginAxis`, `ProcessingAxis`, `ConditionAxis`, ..., `StructureAxis`, `RoleAxis`)
- SKOS concept schemes per axis (`sms:origin-values`, `sms:phase-values`, ...)

## Development

```bash
make setup
make test
make validate
make lint
```

## Visualizations

Generate all ontology diagrams:

```bash
make viz-all
```

Includes:

- class hierarchy
- agents hierarchy
- core + processtypes
- process hierarchy plot
- combined hierarchy
- lifecycle flow
- material state hierarchy

Generate example instance graphs:

```bash
make viz-examples
```

Dedicated specimen visualization:

```bash
make viz-specimen
```

## Docs

```bash
uv run mkdocs build
```

# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core version: `sdata-core-v0.9.1.ttl`
- Core foundation: `MIN` + `OPA`
- Material-state extension: `sdata-material-state-v0.4.0.ttl`

## Main modules

- `sdata-core.ttl` / `sdata-core-v0.9.1.ttl`
: Core model with 14 classes, 19 object properties, 7 datatype properties.
- `sdata-material-state.ttl`
: State space extension (13 axes incl. `MethodAxis`, `DomainAxis`, `DataTypeAxis`).
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

## Core categories (v0.9.1)

- `sdata:Object`
- `sdata:Process`
- `sdata:Agent`

Main object classes:

- `sdata:Material`
- `sdata:Product`
- `sdata:Hardware`
- `sdata:Software`
- `sdata:Data`

Main agent classes:

- `sdata:Person`
- `sdata:HardwareAgent`
- `sdata:SoftwareAgent`
- `sdata:Organization`

## Material state space

`sdata-material-state` adds:

- `sms:StateAxis`
- `sms:StateAssignment`
- 13 predefined axis classes (`OriginAxis`, `ProcessingAxis`, ..., `MethodAxis`, `DomainAxis`, `DataTypeAxis`)
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

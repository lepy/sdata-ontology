# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core: `sdata-core-v0.12.0.ttl`
- Foundation: `MIN v2.1.0` (`min-v2.1.0.ttl`)
- OPA: removed
- State Space: `sdata-material-state-v0.5.0.ttl`

## Module Overview

- `sdata-core.ttl` (`v0.12.0`)
: 11 classes, 10 object properties, 7 datatype properties.
- `sdata-material-state.ttl` (`v0.5.0`)
: 13 state axes including `MethodAxis`, `DomainAxis`, `DataTypeAxis`.
- `shapes/sdata-core-shapes.ttl`
: SHACL checks for example data.

## Core Model In 60 Seconds

- Base categories come from MIN:
  - `min:Object`
  - `min:Process`
  - `min:Data`
  - `min:Agent`
- sdata core classes:
  - Objects: `Material`, `Product`, `Hardware`, `Software`
  - Process: `Process`
  - Data: `Data`
  - Agents: `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`, `EnvironmentAgent`
- Process instances are modeled as `sdata:Process` (`subClassOf min:Process`).
: method/domain semantics are typed via `sms:MethodAxis` and `sms:DomainAxis`.

## Core Modeling Pattern

```text
Object + Data -> Process -> Object + Data
                  ^
               Agent(s)
           + optional Tool/Software
```

## Namespaces

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
```

## Quickstart

```bash
make setup
make test
make validate
make lint
```

## Start Reading

- `docs/quickstart.md`
- `docs/modeling-cheatsheet.md`
- `docs/ontologies/MIGRATION-v0.10-to-v0.12.md`

## Visualizations

Build all ontology plots:

```bash
make viz-all
```

Build cross-ontology class hierarchy (MIN -> sdata-core):

```bash
make viz-min-core
```

![Class hierarchy MIN to sdata-core](docs/diagrams/sdata-min-core-hierarchy.svg)

Build all example plots:

```bash
make viz-examples
```

Build specimen example with dedicated module:

```bash
make viz-specimen
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

Build `min-v2.1.0-examples.ttl` via dedicated 3-plot module
(`Object`, `Process`, `Data` modalities):

```bash
make viz-min-v21-examples
uv run python -m src.visualization.min_v21_examples_plot
```

## Migration Notes (v0.10.0 -> v0.12.0)

- OPA dependency removed.
- MIN upgraded to `v2.1.0`.
- `sdata:Data` is `subClassOf min:Data`.
- `sdata:Process` is available as domain class (`subClassOf min:Process`).
- MIN polarity is schema-level (`min:materialProperty`, `min:informationalProperty`), not instance blank-node aspects.

## Documentation

```bash
uv run --group docs mkdocs build
```

# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core: `sdata-core-v0.9.2.ttl`
- Foundation: `MIN` + `OPA`
- State Space: `sdata-material-state-v0.4.1.ttl`

## Module overview

- `sdata-core.ttl` (`v0.9.2`)
: 14 classes, 19 object properties, 7 datatype properties.
- `sdata-material-state.ttl` (`v0.4.1`)
: 13 state axes incl. `MethodAxis`, `DomainAxis`, `DataTypeAxis`.
- `sdata-agents.ttl`
: SKOS vocabulary for agent classifications.
- `sdata-processtypes.ttl`
: 7 orthogonal verb classes (`Creation` ... `Destruction`).
- `sdata-lifecycle.ttl`
: flow relations (`precedes`, `follows`, `observes`).
- `shapes/sdata-core-shapes.ttl`
: SHACL checks for example data.

## Core model in 60 seconds

- 3 categories:
  - `sdata:Object`
  - `sdata:Process`
  - `sdata:Agent`
- `sdata:Object` subtypes:
  - `Material`, `Product`, `Hardware`, `Software`, `Data`
- `sdata:Agent` subtypes:
  - `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`
- `sdata:Process` has no core subclasses in `v0.9.2`.
: method and domain are modeled via `sms:MethodAxis` and `sms:DomainAxis`.

## Core modeling pattern

```text
Product + Data -> Process -> Product + Data
                    ^
                 Agent(s)
             + optional Hardware/Software
```

## Namespaces

```turtle
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

## Visualizations

Build all ontology plots:

```bash
make viz-all
```

Build all example plots:

```bash
make viz-examples
```

Build specimen example with dedicated module:

```bash
make viz-specimen
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

## Migration notes (v0.8 -> v0.9.2)

- `Data` moved into `Object` hierarchy.
- Process subclasses removed from core.
: use `sms:MethodAxis` and `sms:DomainAxis` instead.
- `MachineAgent` renamed to `HardwareAgent`.
- `Certificate`/`DigitalProductPass` moved to `sms:DataTypeAxis` concepts.
- `sdata:hasUnit` removed from core datatype properties.

## Documentation

```bash
uv run --group docs mkdocs build
```

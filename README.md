# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core (default alias): `sdata-core.ttl` (`v0.1.0`)
- Foundation: `MIN v1.0.0` (`min-v1.0.0.ttl`)
- Foundation examples: `examples/specimen_tensiontest_data.ttl`
- State Space: `sdata-material-state.ttl` (`v0.1.0`)
- Quantities: `sdata-quantities.ttl` (`v0.1.0`)

## Module Overview

- `sdata-core.ttl` (`v0.1.0`, default profile)
: 54 classes, 31 object properties, 19 datatype properties
: plus 52 MIN facade properties (`owl:equivalentProperty` / `owl:equivalentAnnotationProperty`).
- `sdata-material-state.ttl` (`v0.1.0`)
: 13 state axes including `MethodAxis`, `DomainAxis`, `DataTypeAxis`.
- `sdata-quantities.ttl` (`v0.1.0`)
: AQV + ValueDomain extension on top of `sdata-core` and `MIN`.
- `shapes/sdata-core-shapes.ttl`
: SHACL checks for example data.

## Core Model In 60 Seconds

- Base categories come from MIN:
  - `min:Object`
  - `min:Process`
  - `min:Data`
  - `min:Agent`
  - `min:Forma` with subclasses:
    - `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`
- sdata core classes:
  - Objects: `Material`, `Product`, `Hardware`, `Software`
  - Process: `Process`
  - Data: `Data`
  - Agents: `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`, `EnvironmentAgent`
- `sdata-core v0.1.0` provides:
  - 54 classes with MIN facade classes (`sdata:Object`, `sdata:Agent`, `sdata:Lex`, ...)
  - `sdata:derivedFrom` as MIN facade (`owl:equivalentProperty min:derivedFrom`)
  - full one-namespace usage via `sdata:*` facade relations
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
- `sdata_classes.md` (text tree of MIN -> sdata class hierarchy)

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

Build interactive class hierarchy (HTML, MIN v1.0.0 + sdata-core):

```bash
make viz-min-core-interactive
```

Output:

- `docs/diagrams/sdata-min-core-hierarchy-interactive.html`

Build all example plots:

```bash
make viz-examples
```

Build specimen example with dedicated module:

```bash
make viz-specimen
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

Build specimen example graph:

```bash
make viz-min-v1-examples
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

## Version Baseline

- Current baseline: `sdata-core v0.1.0` on `MIN v1.0.0`.
- `sdata:Data` is `subClassOf min:Data`.
- MIN polarity is schema-level (`min:materialProperty`, `min:informationalProperty`), not instance blank-node aspects.

## Documentation

```bash
uv run --group docs mkdocs build
```

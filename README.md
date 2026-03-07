# sdata — Semantic Data Ontology

Ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Status

- Core (default alias): `sdata-core.ttl` (`v0.15.0`)
- Core (latest release): `sdata-core-v0.15.0.ttl`
- Foundation: `MIN v3.7.1` (`min-v3.7.1.ttl`)
- Foundation examples: `examples/min-v3.7.1-examples.ttl`
- State Space: `sdata-material-state-v0.5.0.ttl`
- Quantities: `sdata-quantities.ttl` (`v0.1.1`)

## Module Overview

- `sdata-core.ttl` (`v0.15.0`, default profile)
: 46 classes, 32 object properties, 19 datatype properties
: plus 51 MIN facade properties (`owl:equivalentProperty` / `owl:equivalentAnnotationProperty`).
- `sdata-core-v0.13.1.ttl` (`legacy extended profile`)
: 35 classes, 21 object properties, 16 datatype properties.
- `sdata-material-state.ttl` (`v0.5.0`)
: 13 state axes including `MethodAxis`, `DomainAxis`, `DataTypeAxis`.
- `sdata-quantities.ttl` (`v0.1.1`)
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
- `sdata-core-v0.15.0` adds:
  - full `sdata:*` facades for MIN relations (one-namespace workflow)
  - Typus facades (`typifiedBy` patterns across typable Nexus categories)
  - additional domain classes including `Specimen`, `BillOfMaterials`, `Substance`
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
- `docs/ontologies/MIGRATION-v0.10-to-v0.12.md`
- `docs/ontologies/MIGRATION-v0.12-to-v0.13.md`
- `docs/ontologies/MIGRATION-v0.13.0-to-v0.13.1.md`

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

Build interactive class hierarchy (HTML, MIN v3.7.1 + sdata-core):

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

Build `min-v3.7.1-examples.ttl` via dedicated 3-plot module
(`Object`, `Process`, `Data` modalities; file also contains FORMA examples):

```bash
make viz-min-v3-examples
uv run python -m src.visualization.min_v3_examples_plot
# canonical module:
uv run python -m src.visualization.min_v21_examples_plot
```

## Migration Notes

- `v0.10 -> v0.12`: OPA removed, migration to MIN categories.
- `v0.12 -> v0.13`: expanded sdata facade for MIN v3 (including Forma classes).
- `v0.13.0 -> v0.13.1`: adds custody, registry binding, DPP supersession, and validity/revocation fields.
- `v0.13.1 -> v0.14.0`: switches to one-namespace modeling (`sdata:*` facades for MIN) and Typus facades.
- `v0.14.0 -> v0.15.0`: MIN v3.7.1 conformance, facade completion, and Forma realignment (`Regulation`/`Specification`/`LifecyclePhase` to `Institutio`).
- `sdata:Data` is `subClassOf min:Data`.
- MIN polarity is schema-level (`min:materialProperty`, `min:informationalProperty`), not instance blank-node aspects.

## Documentation

```bash
uv run --group docs mkdocs build
```

# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy and Digital Twins.

## Start Here

1. [Quickstart](quickstart.md)
2. [Modeling Cheat Sheet](modeling-cheatsheet.md)
3. [Migration v0.10 -> v0.12](ontologies/MIGRATION-v0.10-to-v0.12.md)
4. [Migration v0.12 -> v0.13](ontologies/MIGRATION-v0.12-to-v0.13.md)
5. [Migration v0.13.0 -> v0.13.1](ontologies/MIGRATION-v0.13.0-to-v0.13.1.md)

## Included Modules

- `sdata-core.ttl`: default core profile (`v0.12.0`, MIN v3.3 based)
- `sdata-core-v0.13.1.ttl`: extended core profile (MIN v3.3 + Forma + decentralized DPP additions)
- `min-v3.3.0.ttl`: foundation ontology
- `sdata-material-state.ttl`: material state space extension
- `sdata-quantities.ttl`: AQV + ValueDomain extension
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

Core sizes:
- `sdata-core.ttl` (`v0.12.0`): **11 classes**, **10 object properties**, **7 datatype properties**
- `sdata-core-v0.13.1.ttl`: **35 classes**, **21 object properties**, **16 datatype properties**

## Read This First

1. Choose your core profile (`sdata-core.ttl` v0.12 or `sdata-core-v0.13.1.ttl`).
2. Use `sdata-material-state` for method/domain/datatype/value typing.
3. Add `sdata-quantities` for AQV and ValueDomain modeling.
4. Use `sdata-core-shapes` to validate your instance data.

## Ontology Docs

- [sdata-core](ontologies/sdata-core/index.md)
- [sdata-material-state](ontologies/sdata-material-state.md)
- [sdata-quantities](ontologies/sdata-quantities/index.md)
- [sdata-vd-interval](ontologies/sdata-vd-interval/index.md)
- [sdata-vd-enum](ontologies/sdata-vd-enum/index.md)
- [sdata-vd-statistical](ontologies/sdata-vd-statistical/index.md)
- [sdata-vd-fuzzy](ontologies/sdata-vd-fuzzy/index.md)
- [sdata-r-strategies](ontologies/sdata-r-strategies/index.md)
- [sdata-core-shapes](ontologies/sdata-core-shapes/index.md)
- [Migration v0.10 -> v0.12](ontologies/MIGRATION-v0.10-to-v0.12.md)
- [Migration v0.12 -> v0.13](ontologies/MIGRATION-v0.12-to-v0.13.md)
- [Migration v0.13.0 -> v0.13.1](ontologies/MIGRATION-v0.13.0-to-v0.13.1.md)

## Example Datasets

- [Examples](examples.md)

## Local Development

```bash
make setup
make validate
make test
make lint
```

## Visualizations

```bash
make viz-all
```

This generates ontology-level diagrams into `docs/diagrams/`.

Individual targets:

```bash
make viz-hierarchy
make viz-min-core
make viz-min-core-interactive
make viz-material-state
make viz-specimen
make viz-min-v3-examples
make viz-examples
```

`viz-examples` renders every Turtle file in `examples/`.

Key diagrams:

- `docs/diagrams/sdata-min-core-hierarchy.svg`
- `docs/diagrams/sdata-min-core-hierarchy-interactive.html`
- `docs/diagrams/sdata-class-hierarchy.svg`
- `docs/diagrams/sdata-material-state.svg`

## Build Docs

```bash
uv run mkdocs build
```

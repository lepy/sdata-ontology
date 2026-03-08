# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy and Digital Twins.

## Start Here

1. [Quickstart](quickstart.md)
2. [Modeling Cheat Sheet](modeling-cheatsheet.md)

## Included Modules

- `sdata-core.ttl`: default core profile (`v0.1.0`, MIN v1.0 based)
- `min-v1.0.0.ttl`: foundation ontology
- `sdata-material-state.ttl`: material state space extension
- `sdata-quantities.ttl`: AQV + ValueDomain extension
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

## Read This First

1. Use `sdata-core.ttl` (`v0.1.0`) as default profile.
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
make viz-min-v1-examples
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

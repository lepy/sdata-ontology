# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy and Digital Twins.

## Included modules

- `sdata-core.ttl` / `sdata-core-v0.9.2.ttl`: core ontology (MIN/OPA-based)
- `sdata-material-state.ttl`: material state space extension
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

Current core model: **14 classes**, **19 object properties**, **7 datatype properties**.

## Read this first

1. `sdata-core` for base classes and properties.
2. `sdata-material-state` for method/domain/datatype/value typing.
3. `sdata-core-shapes` to validate your instance data.

## Ontology docs

- [sdata-core](ontologies/sdata-core/index.md)
- [sdata-material-state](ontologies/sdata-material-state.md)
- [sdata-quantities](ontologies/sdata-quantities/index.md)
- [sdata-vd-interval](ontologies/sdata-vd-interval/index.md)
- [sdata-vd-enum](ontologies/sdata-vd-enum/index.md)
- [sdata-vd-statistical](ontologies/sdata-vd-statistical/index.md)
- [sdata-vd-fuzzy](ontologies/sdata-vd-fuzzy/index.md)
- [sdata-r-strategies](ontologies/sdata-r-strategies/index.md)
- [sdata-core-shapes](ontologies/sdata-core-shapes/index.md)

## Example datasets

- [Examples](examples.md)

## Local development

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
make viz-material-state
make viz-specimen
make viz-examples
```

`viz-examples` renders every Turtle file in `examples/`.

## Build docs

```bash
uv run mkdocs build
```

# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy and Digital Twins.

## Included modules

- `sdata-core.ttl` / `sdata-core-v0.8.0.ttl`: core ontology (MIN/OPA-based)
- `sdata-material-state.ttl`: material state space extension
- `sdata-agents.ttl`: SKOS vocabulary for agent typing
- `sdata-processtypes.ttl`: verb-axis process extension
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

Current core model: **30 classes**, **19 object properties**, **8 datatype properties**.

## Ontology docs

- [sdata-core](ontologies/sdata-core/index.md)
- [sdata-material-state](ontologies/sdata-material-state.md)
- [sdata-agents](ontologies/sdata-agents/index.md)
- [sdata-processtypes](ontologies/sdata-processtypes/index.md)
- [sdata-lifecycle](ontologies/sdata-lifecycle/index.md)
- [sdata-quantities](ontologies/sdata-quantities/index.md)
- [sdata-vd-interval](ontologies/sdata-vd-interval/index.md)
- [sdata-vd-enum](ontologies/sdata-vd-enum/index.md)
- [sdata-vd-statistical](ontologies/sdata-vd-statistical/index.md)
- [sdata-vd-fuzzy](ontologies/sdata-vd-fuzzy/index.md)
- [sdata-r-strategies](ontologies/sdata-r-strategies/index.md)
- [sdata-core-shapes](ontologies/sdata-core-shapes/index.md)

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

Individual targets:

```bash
make viz-hierarchy
make viz-agents
make viz-core-processtypes
make viz-core-processtypes-sdata-only
make viz-process-dual
make viz-combined
make viz-lifecycle
make viz-material-state
make viz-specimen
make viz-examples
```

## Build docs

```bash
uv run mkdocs build
```

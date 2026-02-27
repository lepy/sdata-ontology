# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Included modules

- `sdata-core.ttl`: core ontology classes and properties
- `sdata-agents.ttl`: SKOS vocabulary for agent typing
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

## Ontology docs with tensile test examples

- [sdata-core](ontologies/sdata-core/index.md)
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

## Visualize class hierarchy

```bash
uv run python -m src.visualization.class_hierarchy_plot --out-dir docs/diagrams --format both
```

## Visualize agents hierarchy (subgraph under sdata:MaterialAgent / sdata:InformationAgent)

```bash
uv run python -m src.visualization.agents_hierarchy_plot --out-dir docs/diagrams --format both
```

## Build docs

```bash
uv run mkdocs build
```

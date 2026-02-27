# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Included modules

- `sdata-core.ttl`: core ontology classes and properties
- `sdata-agents.ttl`: SKOS vocabulary for agent typing
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

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

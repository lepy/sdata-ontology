# sdata Documentation

sdata is a modular ontology suite for Product Passports, Circular Economy, and Digital Twins.

## Included modules

- `sdata-core.ttl`: core ontology classes and properties
- `sdata-core-v0.5.0-bfo-alignment.ttl`: optional BFO/PROV bridge axioms
- `sdata-agents.ttl`: SKOS vocabulary for agent typing
- `shapes/sdata-core-shapes.ttl`: SHACL constraints for instance validation

Current core model: **19 classes** (`2 domains + 5 dimensions + 10 leaf + 2 orthogonal`), fully autark (no ontology imports).

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

## Visualizations

```bash
uv run python -m src.visualization.class_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.agents_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.core_processtypes_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.core_processtypes_sdata_only_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.process_dual_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.combined_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.lifecycle_plot --out-dir docs/diagrams --format both
```

Optional (with alignment module):

```bash
uv run python -m src.visualization.class_hierarchy_plot \
  --core sdata-core-v0.5.0.ttl \
  --alignment sdata-core-v0.5.0-bfo-alignment.ttl \
  --out-dir docs/diagrams \
  --name sdata-class-hierarchy-aligned \
  --format both
```

Oder über Makefile:

```bash
make viz-hierarchy
make viz-agents
make viz-core-processtypes
make viz-core-processtypes-sdata-only
make viz-process-dual
make viz-combined
make viz-lifecycle
make viz-all
```

## Build docs

```bash
uv run mkdocs build
```

# Examples

This repository ships executable Turtle examples under `examples/`.

## Files

- `examples/specimen_tensiontest_data.ttl`
: end-to-end tensile test dataset with product, process, data, AQV, and state assignments.
- `examples/battery-passport.ttl`
: product-passport style chain with process records, test reports, simulation reports, certificate, and DPP.
- `examples/tensiontest-crashsimulation.ttl`
: compact testing + simulation flow for product/data provenance.
- `examples/AttributeQuantityValue_sheetthickness.ttl`
: focused AQV and value-domain modeling sample.

## Render all example graphs

```bash
make viz-examples
```

## Render only specimen example

```bash
make viz-specimen
```

Equivalent direct command:

```bash
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

## Typical output files

- `docs/diagrams/specimen_tensiontest_data-graph.svg`
- `docs/diagrams/battery-passport-graph.svg`
- `docs/diagrams/tensiontest-crashsimulation-graph.svg`
- `docs/diagrams/AttributeQuantityValue_sheetthickness-graph.svg`

## Validation

```bash
make validate
```

This validates `examples/battery-passport.ttl` against SHACL and parses all `.ttl` files.

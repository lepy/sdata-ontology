# Examples

This repository ships executable Turtle examples under `examples/`.

## Files

- `examples/specimen_tensiontest_data.ttl`
: end-to-end tensile-test dataset with product, process, data and state assignments.
- `examples/battery-passport.ttl`
: product-passport style chain with process records, test reports, simulation reports, certificate, and DPP.
- `examples/tensiontest-crashsimulation.ttl`
: compact testing + simulation flow for product/data provenance.
- `examples/AttributeQuantityValue_sheetthickness.ttl`
: focused AQV and value-domain modeling sample.
- `examples/min-v3.0.0-examples.ttl`
: three MIN modalities (`Object`, `Process`, `Data`) in separate example roots.

## Render All Example Graphs

```bash
make viz-examples
```

## Render Only Specimen Example

```bash
make viz-specimen
```

Equivalent direct command:

```bash
uv run python -m src.visualization.specimen_tensiontest_data_plot
```

## Render Modality Example (3 Dedicated Plots)

```bash
make viz-min-v3-examples
uv run python -m src.visualization.min_v3_examples_plot
```

This generates 3 filtered views:

- `Object / material-dominant`
- `Process / balanced`
- `Data / informational-dominant`

## Typical Output Files

- `docs/diagrams/specimen_tensiontest_data-graph.svg`
- `docs/diagrams/battery-passport-graph.svg`
- `docs/diagrams/tensiontest-crashsimulation-graph.svg`
- `docs/diagrams/AttributeQuantityValue_sheetthickness-graph.svg`
- `docs/diagrams/min-v3.0.0-examples-material-modal.svg`
- `docs/diagrams/min-v3.0.0-examples-balanced-modal.svg`
- `docs/diagrams/min-v3.0.0-examples-informational-modal.svg`

## Validation

```bash
make validate
```

This validates `examples/battery-passport.ttl` against SHACL and parses all `.ttl` files.

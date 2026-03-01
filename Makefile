.PHONY: check-uv setup setup-docs setup-pip validate test lint viz-hierarchy viz-min-core viz-min-opa-core viz-material-state viz-specimen viz-min-opa-examples viz-all viz-examples clean

UV ?= uv

check-uv:
	@command -v $(UV) >/dev/null 2>&1 || { \
		echo "Error: '$(UV)' is not installed. Install uv from https://docs.astral.sh/uv/getting-started/installation/"; \
		exit 1; \
	}

# ─── Setup ────────────────────────────────────────────────────────────────────
setup: check-uv
	$(UV) sync --only-group dev

setup-docs: check-uv
	$(UV) sync --group docs

setup-pip:
	python3 -m pip install -e ".[dev]"

# ─── Validate all TTL files with SHACL ────────────────────────────────────────
validate: check-uv
	@echo "── Validating battery-passport.ttl against core shapes..."
	$(UV) run pyshacl -s shapes/sdata-core-shapes.ttl -df turtle examples/battery-passport.ttl
	@echo ""
	@echo "── Parsing all TTL files..."
	$(UV) run python tests/parse_all.py
	@echo ""
	@echo "✓ All validations passed."

# ─── Run pytest ───────────────────────────────────────────────────────────────
test: check-uv
	$(UV) run pytest -v

# ─── Lint TTL (syntax check only) ────────────────────────────────────────────
lint: check-uv
	@for f in *.ttl shapes/*.ttl examples/*.ttl; do \
		echo "Parsing $$f..."; \
		$(UV) run python -c "from rdflib import Graph; g = Graph(); g.parse('$$f', format='turtle'); print(f'  ✓ {len(g)} triples')" || exit 1; \
	done
	@echo "✓ All files valid Turtle."

# ─── Visualize class hierarchy ───────────────────────────────────────────────
viz-hierarchy: check-uv
	$(UV) run python -m src.visualization.class_hierarchy_plot

# ─── Visualize cross-ontology class hierarchy (MIN -> sdata-core) ────────────
viz-min-core: check-uv
	$(UV) run python -m src.visualization.min_sdata_hierarchy_plot

# Backward-compatible alias
viz-min-opa-core: viz-min-core

# ─── Clean ────────────────────────────────────────────────────────────────────
clean:
	rm -rf .venv __pycache__ .pytest_cache dist build site

# ─── Visualize material-state hierarchy ──────────────────────────────────────
viz-material-state: check-uv
	$(UV) run python -m src.visualization.material_state_plot

# ─── Visualize specimen_tensiontest_data example via dedicated module ────────
viz-specimen: check-uv
	$(UV) run python -m src.visualization.specimen_tensiontest_data_plot

# ─── Visualize min-opa-examples with three dedicated views ───────────────────
viz-min-opa-examples: check-uv
	$(UV) run python -m src.visualization.min_opa_examples_plot

# ─── Generate all main ontology visualizations ───────────────────────────────
viz-all: viz-hierarchy viz-min-core viz-material-state

# ─── Visualize all example TTL graphs ───────────────────────────────────────
viz-examples: viz-specimen check-uv
	@for f in examples/*.ttl; do \
		base="$$(basename "$$f" .ttl)-graph"; \
		echo "Rendering $$f -> docs/diagrams/$${base}.{dot,svg,png}"; \
		$(UV) run python -m src.visualization.example_ttl_plot --input "$$f" --out-dir docs/diagrams --format both --name "$$base" || exit 1; \
	done

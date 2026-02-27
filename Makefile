.PHONY: check-uv setup setup-docs setup-pip validate test lint viz-hierarchy clean

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

# ─── Clean ────────────────────────────────────────────────────────────────────
clean:
	rm -rf .venv __pycache__ .pytest_cache dist build site

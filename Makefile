.PHONY: setup validate test lint clean

# ─── Setup ────────────────────────────────────────────────────────────────────
setup:
	uv sync --group dev

# ─── Validate all TTL files with SHACL ────────────────────────────────────────
validate:
	@echo "── Validating battery-passport.ttl against core shapes..."
	uv run pyshacl -s shapes/sdata-core-shapes.ttl -df turtle examples/battery-passport.ttl
	@echo ""
	@echo "── Parsing all TTL files..."
	uv run python tests/parse_all.py
	@echo ""
	@echo "✓ All validations passed."

# ─── Run pytest ───────────────────────────────────────────────────────────────
test:
	uv run pytest -v

# ─── Lint TTL (syntax check only) ────────────────────────────────────────────
lint:
	@for f in *.ttl shapes/*.ttl examples/*.ttl; do \
		echo "Parsing $$f..."; \
		uv run python -c "from rdflib import Graph; g = Graph(); g.parse('$$f', format='turtle'); print(f'  ✓ {len(g)} triples')" || exit 1; \
	done
	@echo "✓ All files valid Turtle."

# ─── Clean ────────────────────────────────────────────────────────────────────
clean:
	rm -rf .venv __pycache__ .pytest_cache dist build site

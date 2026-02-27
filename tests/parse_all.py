"""Parse all TTL files and report triple counts."""

import logging
from pathlib import Path
from rdflib import Graph


def parse_all():
    # Vendored ontologies may contain malformed rdf:HTML literals; keep output clean.
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)

    root = Path(__file__).resolve().parent.parent
    ttl_files = sorted(root.glob("**/*.ttl"))

    total = 0
    for f in ttl_files:
        g = Graph()
        g.parse(f, format="turtle")
        count = len(g)
        total += count
        print(f"  {f.relative_to(root)}: {count} triples")

    print(f"\n  Total: {total} triples across {len(ttl_files)} files")


if __name__ == "__main__":
    parse_all()

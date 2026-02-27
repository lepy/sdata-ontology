# sdata — Semantic Data Ontology

**Deployment-ready mid-level ontology for Product Passports, Circular Economy & Digital Twins.**

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![BFO: ISO/IEC 21838-2](https://img.shields.io/badge/BFO-ISO%2FIEC%2021838--2%3A2021-green.svg)](https://www.iso.org/standard/74572.html)
[![W3C PROV-O](https://img.shields.io/badge/W3C-PROV--O-orange.svg)](https://www.w3.org/TR/prov-o/)

---

## Overview

sdata is a modular ontology suite built on three orthogonal foundations:

| Foundation | Standard | Answers |
|---|---|---|
| **BFO** | ISO/IEC 21838-2:2021 | *What exists?* — categorical grounding |
| **PROV-O** | W3C Recommendation | *Who did what when?* — provenance tracking |
| **QUDT** | QUDT 3.1 | *How much?* — quantities, units, dimensions |

## Namespace

All IRIs resolve via [w3id.org](https://w3id.org):

```
@prefix sdata: <https://w3id.org/sdata/core/> .
```

| Module | IRI | Description |
|---|---|---|
| **Core** | `https://w3id.org/sdata/core` | 12 classes, 15 object properties, 14 datatype properties |
| **Agents** | `https://w3id.org/sdata/vocab/agents` | SKOS ConceptScheme for agent types |
| **Core Shapes** | `https://w3id.org/sdata/core/shapes` | SHACL constraints for core data validation |

## Repository Structure

```
sdata/
├── sdata-core.ttl              Core ontology (v0.3.0)
├── sdata-agents.ttl            SKOS: Agent types
├── shapes/
│   ├── sdata-core-shapes.ttl   SHACL shapes for core validation
├── examples/
│   └── battery-passport.ttl    Example: Battery Passport instance data
├── src/
│   ├── examples/
│   │   └── dpp_01.py           Python example graph builder
│   └── visualization/
│       ├── class_hierarchy_plot.py
│       └── agents_hierarchy_plot.py
├── vendor/ontologies/
│   ├── bfo.ttl                 Vendored BFO ontology (from official ISO BFO 2020 OWL)
│   ├── prov-o.ttl              Vendored PROV-O ontology
│   ├── qudt.ttl                Vendored QUDT ontology
│   ├── dtype.ttl               Vendored QUDT dependency
│   ├── vaem.ttl                Vendored QUDT dependency
│   └── skos.ttl                Vendored QUDT dependency
├── docs/
│   ├── index.md                MkDocs entry page
│   └── diagrams/
│       ├── sdata-class-hierarchy.svg
│       ├── sdata-class-hierarchy.png
│       ├── sdata-agents-hierarchy.svg
│       └── sdata-agents-hierarchy.png
├── tests/
│   ├── test_ontology.py
│   └── test_hierarchy_plot.py
├── mkdocs.yml                  MkDocs site configuration
├── uv.lock                     Locked dependency graph for uv
├── LICENSE
└── README.md
```

## SDATA Core Ontology at a Glance

### 12 Classes

| SDATA Class | BFO Superclass | Description |
|---|---|---|
| `MaterialArtifact` | MaterialEntity | Discrete physical artifact |
| `Material` | MaterialEntity | Homogeneous material substance |
| `MaterialAgent` | MaterialEntity + prov:Agent | Tangible acting entity |
| `MaterialProcess` | Process | Process in material domain |
| `MaterialSite` | Site | Spatial location for material domain |
| `InformationArtifact` | GenericallyDependentContinuant | Discrete information artifact |
| `Information` | GenericallyDependentContinuant | Homogeneous information substance |
| `InformationAgent` | GenericallyDependentContinuant + prov:Agent | Intangible acting entity |
| `InformationProcess` | Process | Process in information domain |
| `InformationSite` | GenericallyDependentContinuant | Logical location for information domain |
| `Role` | Role | Orthogonal context role |
| `Identifier` | GenericallyDependentContinuant | Orthogonal typed identifier token |

### Key Design Decisions

- **Flat class hierarchy** — subtype discrimination via SKOS ConceptSchemes, not OWL subclasses
- **PROV-O via property-mapping** — `generates ⊆ prov:generated`, `consumes ⊆ prov:used`, `wasPerformedBy ⊆ prov:wasAssociatedWith` (no dual inheritance)
- **consistsOf vs. hasPart** — material constitution vs. structural BOM hierarchy, strictly separated
- **Dual substance model** — `Material` and `Information` are domain-dual non-discrete substances
- **xsd:dateTimeStamp** — mandatory timezone for global supply chain interoperability
- **Identifier as orthogonal class** — domain-spanning identifier token

## Usage

### SPARQL — find all materials in a product

```sparql
PREFIX sdata: <https://w3id.org/sdata/core/>

SELECT ?product ?material ?materialName WHERE {
  ?product a sdata:MaterialArtifact ;
           sdata:consistsOf ?material .
  ?material sdata:name ?materialName .
}
```

### SPARQL — provenance chain (PROV-O compatible)

```sparql
PREFIX prov: <http://www.w3.org/ns/prov#>

SELECT ?entity ?activity ?agent WHERE {
  ?activity prov:generated ?entity ;
            prov:wasAssociatedWith ?agent .
}
```

## Versioning

Versions follow semantic versioning. Each release is tagged (`v0.3.0`, …).

- **Ontology IRI** (always current): `https://w3id.org/sdata/core`
- **Version IRI** (pinned): `https://w3id.org/sdata/core/0.3.0`

Import the unversioned IRI to track latest, or the versioned IRI to pin.

## Validation

```bash
# Validate instance data against SHACL shapes
pyshacl -s shapes/sdata-core-shapes.ttl -df turtle data.ttl
```

## Offline / Autark Imports

The core ontology imports are vendored in `vendor/ontologies/` so the repository is usable offline without fetching BFO/PROV-O/QUDT from the web.  
All runtime imports are in Turtle (`*.ttl`), including BFO.

## Development Setup

### Prerequisites

- Python 3.12+
- `uv` (recommended): https://docs.astral.sh/uv/getting-started/installation/

### Install dependencies

```bash
# Recommended
make setup

# Alternative (without uv)
make setup-pip

# Optional: install documentation dependencies
make setup-docs
```

### Run checks

```bash
make validate
make test
make lint
```

## Class Hierarchy Visualization

Generate a styled class hierarchy diagram (SVG + PNG) from `sdata-core.ttl`, including BFO and PROV base hierarchies down to the sdata base classes:

```bash
make viz-hierarchy
make viz-agents
```

Output files:

- `docs/diagrams/sdata-class-hierarchy.svg`
- `docs/diagrams/sdata-class-hierarchy.png`
- `docs/diagrams/sdata-agents-hierarchy.svg`
- `docs/diagrams/sdata-agents-hierarchy.png`

Direct CLI usage:

```bash
uv run python -m src.visualization.class_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.agents_hierarchy_plot --out-dir docs/diagrams --format both
```

## Documentation

```bash
# Build static docs site with MkDocs
uv run mkdocs build
```

Docs entrypoint:

- `docs/index.md`

## Contributing

1. Fork this repository
2. Create a feature branch
3. Ensure all SHACL shapes pass
4. Submit a pull request

## License

[CC0 1.0 — Public Domain](http://creativecommons.org/publicdomain/zero/1.0/)

## References

- [ISO/IEC 21838-2:2021 — Basic Formal Ontology (BFO)](https://www.iso.org/standard/74572.html)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [QUDT Ontologies](http://qudt.org/)
- [w3id.org Persistent Identifiers](https://w3id.org/)

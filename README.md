# sdata — Semantic Data Ontology

**Deployment-ready mid-level ontology for Product Passports, Circular Economy & Digital Twins.**

[![Version](https://img.shields.io/badge/version-latest-informational.svg)](https://w3id.org/sdata/core)
[![W3ID](https://img.shields.io/badge/W3ID-w3id.org%2Fsdata-blueviolet.svg)](https://w3id.org/sdata)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![OWL 2 DL](https://img.shields.io/badge/OWL-2%20DL-blue.svg)](https://www.w3.org/TR/owl2-overview/)
[![Core](https://img.shields.io/badge/core-v0.5.1%20autark-green.svg)](https://w3id.org/sdata/core/0.5.1)
[![Alignment](https://img.shields.io/badge/alignment-BFO%2FPROV%20optional-orange.svg)](https://w3id.org/sdata/alignment/bfo-prov/0.5.0)
[![Turtle](https://img.shields.io/badge/format-Turtle%20(.ttl)-brightgreen.svg)](https://www.w3.org/TR/turtle/)
![GitHub last commit](https://img.shields.io/github/last-commit/lepy/sdata-ontology)
![GitHub contributors](https://img.shields.io/github/contributors/lepy/sdata-ontology)

---

## Overview

sdata is a modular ontology suite with an autark core and optional alignment modules:

| Foundation | Standard | Answers |
|---|---|---|
| **sdata-core (autark)** | RDF/RDFS/OWL/XSD only | *What exists in sdata?* — without external ontology imports |
| **sdata-bfo-prov alignment (optional)** | BFO 2020 + PROV-O | *How does sdata map to external upper ontologies?* |
| **Extension modules** | sdata-processtypes, sdata-lifecycle, sdata-vd-* | *How is the domain specialized?* |

## Namespace

All IRIs resolve via [w3id.org](https://w3id.org):

```
@prefix sdata: <https://w3id.org/sdata/core/> .
```

| Module | IRI | Description |
|---|---|---|
| **Core** | `https://w3id.org/sdata/core` | 19 classes (2 domains + 5 dimensions + 10 leaf + 2 orthogonal), 20 object properties, 14 datatype properties |
| **BFO/PROV Alignment** | `https://w3id.org/sdata/alignment/bfo-prov` | Optional bridge axioms from sdata-core to BFO/PROV |
| **Agents** | `https://w3id.org/sdata/vocab/agents` | SKOS ConceptScheme for agent types |
| **Core Shapes** | `https://w3id.org/sdata/core/shapes` | SHACL constraints for core data validation |

## Repository Structure

```
sdata/
├── sdata-core.ttl              Core ontology (v0.5.1 autark)
├── sdata-core-v0.5.1.ttl       Versioned autark core snapshot
├── sdata-core-v0.5.0-bfo-alignment.ttl   Optional BFO/PROV bridge module
├── sdata-agents.ttl            SKOS: Agent types
├── sdata-*.ttl
├── shapes/
│   ├── sdata-core-shapes.ttl   SHACL shapes for core validation
├── examples/
│   └── battery-passport.ttl    Example: Battery Passport instance data
├── src/
│   ├── examples/
│   │   └── dpp_01.py           Python example graph builder
│   └── visualization/
│       ├── class_hierarchy_plot.py
│       └── ...
├── vendor/ontologies/          Optional vendor files (needed only for alignment workflows)
├── docs/
│   ├── index.md                MkDocs entry page
│   └── ...
├── tests/
│   ├── test_ontology.py
│   └── ...
├── mkdocs.yml                  MkDocs site configuration
├── uv.lock                     Locked dependency graph for uv
├── LICENSE
└── README.md
```

## SDATA Core Ontology at a Glance

### 19 Classes: 2 + 5 + 10 + 2

| SDATA Class | Layer | Description |
|---|---|---|
| `Tangible` | Domain | Union of all material-side leaf classes |
| `Intangible` | Domain | Union of all information-side leaf classes |
| `Artifact` | Dimension | Union of `MaterialArtifact` and `InformationArtifact` |
| `Substance` | Dimension | Union of `Material` and `Information` |
| `Agent` | Dimension | Union of `MaterialAgent` and `InformationAgent` |
| `Process` | Dimension | Union of `MaterialProcess` and `InformationProcess` |
| `Site` | Dimension | Union of `MaterialSite` and `InformationSite` |
| `MaterialArtifact` | Leaf | Discrete physical artifact |
| `InformationArtifact` | Leaf | Discrete information artifact |
| `Material` | Leaf | Homogeneous material substance |
| `Information` | Leaf | Homogeneous information substance |
| `MaterialAgent` | Leaf | Tangible acting entity |
| `InformationAgent` | Leaf | Intangible acting entity |
| `MaterialProcess` | Leaf | Process in material domain |
| `InformationProcess` | Leaf | Process in information domain |
| `MaterialSite` | Leaf | Spatial location for material domain |
| `InformationSite` | Leaf | Logical location for information domain |
| `Role` | Orthogonal | Context-dependent realizable role |
| `Identifier` | Orthogonal | Typed identifier token across both domains |

### Dual Principle

`sdata-core` v0.5.1 follows a layered model:

- **Domain layer**: `Tangible`, `Intangible`
- **Dimension layer**: `Artifact`, `Substance`, `Agent`, `Process`, `Site`
- **Leaf layer (dual, material side)**: `Material`, `MaterialArtifact`, `MaterialAgent`, `MaterialProcess`, `MaterialSite`
- **Leaf layer (dual, information side)**: `Information`, `InformationArtifact`, `InformationAgent`, `InformationProcess`, `InformationSite`
- **Orthogonal classes**: `Role`, `Identifier`

Each material class has a semantic dual on the information side. Domain and dimension classes are defined OWL unions over leaf classes.

### Key Design Decisions

- **Four-layer class architecture** — domains + dimensions + leaves + orthogonals
- **Autark core** — no ontology imports and no hard dependency on BFO/PROV/QUDT
- **Optional alignment module** — BFO/PROV mapping is moved to `sdata-core-v0.5.0-bfo-alignment.ttl`
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

### SPARQL — process chain

```sparql
PREFIX sdata: <https://w3id.org/sdata/core/>

SELECT ?entity ?activity ?agent WHERE {
  ?activity sdata:generates ?entity ;
            sdata:wasPerformedBy ?agent .
}
```

## Versioning

Versions follow semantic versioning. Each release is tagged (`v0.5.1`, …).

- **Ontology IRI** (always current): `https://w3id.org/sdata/core`
- **Version IRI** (pinned): `https://w3id.org/sdata/core/0.5.1`

Import the unversioned IRI to track latest, or the versioned IRI to pin.

## Validation

```bash
# Validate instance data against SHACL shapes
pyshacl -s shapes/sdata-core-shapes.ttl -df turtle data.ttl
```

## Autark Core and Optional Alignment

`sdata-core.ttl` is fully autark and does not import any ontology.  
If you need BFO/PROV interoperability, import `sdata-core-v0.5.0-bfo-alignment.ttl` additionally.

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

## Visualizations

Generate all main diagrams (DOT + SVG + PNG):

```bash
make viz-all
```

Individual targets:

```bash
make viz-hierarchy
make viz-agents
make viz-core-processtypes
make viz-core-processtypes-sdata-only
make viz-process-dual
make viz-combined
make viz-lifecycle
```

Direct CLI usage:

```bash
uv run python -m src.visualization.class_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.agents_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.core_processtypes_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.core_processtypes_sdata_only_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.process_dual_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.combined_hierarchy_plot --out-dir docs/diagrams --format both
uv run python -m src.visualization.lifecycle_plot --out-dir docs/diagrams --format both
```

Optional alignment overlay for class hierarchy:

```bash
uv run python -m src.visualization.class_hierarchy_plot \
  --core sdata-core-v0.5.1.ttl \
  --alignment sdata-core-v0.5.0-bfo-alignment.ttl \
  --out-dir docs/diagrams \
  --name sdata-class-hierarchy-aligned \
  --format both
```

Key output files:

- `docs/diagrams/sdata-class-hierarchy.{dot,svg,png}`
- `docs/diagrams/sdata-agents-hierarchy.{dot,svg,png}`
- `docs/diagrams/sdata-core-processtypes-hierarchy.{dot,svg,png}`
- `docs/diagrams/sdata-core-processtypes-sdata-only.{dot,svg,png}`
- `docs/diagrams/sdata-process-dual-hierarchy.{dot,svg,png}`
- `docs/diagrams/sdata-combined-hierarchy.{dot,svg,png}`
- `docs/diagrams/sdata-lifecycle-flow.{dot,svg,png}`

![sdata class hierarchy](docs/diagrams/sdata-class-hierarchy.png)

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

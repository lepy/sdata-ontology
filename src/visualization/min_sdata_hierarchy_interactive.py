"""Create an interactive HTML class hierarchy for MIN -> sdata-core."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from rdflib import Graph, Literal, RDF, RDFS, URIRef
from rdflib.namespace import OWL

MIN_PREFIX = "https://w3id.org/min"
SDATA_CORE_PREFIX = "https://w3id.org/sdata/core/"


@dataclass(frozen=True)
class Node:
    iri: URIRef
    label: str
    kind: str  # "min" | "sdata"


@dataclass(frozen=True)
class Edge:
    parent: URIRef
    child: URIRef


@dataclass(frozen=True)
class Model:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]


def _kind_from_iri(iri: URIRef) -> str | None:
    text = str(iri)
    if text.startswith(MIN_PREFIX):
        return "min"
    if text.startswith(SDATA_CORE_PREFIX):
        return "sdata"
    return None


def _best_label(graph: Graph, iri: URIRef) -> str:
    labels = list(graph.objects(iri, RDFS.label))
    if not labels:
        text = str(iri)
        if "#" in text:
            return text.rsplit("#", 1)[1]
        return text.rsplit("/", 1)[-1]

    def score(label: Literal) -> tuple[int, str]:
        lang = (label.language or "").lower()
        if lang == "en":
            rank = 0
        elif not lang:
            rank = 1
        else:
            rank = 2
        return (rank, str(label))

    return str(sorted(labels, key=score)[0])


def _classes_from(graph: Graph) -> set[URIRef]:
    return {
        cls
        for cls in graph.subjects(RDF.type, OWL.Class)
        if isinstance(cls, URIRef) and _kind_from_iri(cls) is not None
    }


def load_graphs(min_path: Path, core_path: Path) -> tuple[Graph, Graph, Graph]:
    for path, label in ((min_path, "MIN ontology"), (core_path, "sdata-core ontology")):
        if not path.exists():
            raise FileNotFoundError(f"{label} not found: {path}")

    min_graph = Graph()
    min_graph.parse(min_path, format="turtle")

    core_graph = Graph()
    core_graph.parse(core_path, format="turtle")

    merged = Graph()
    merged += min_graph
    merged += core_graph

    return min_graph, core_graph, merged


def extract_model(min_graph: Graph, core_graph: Graph, merged: Graph) -> Model:
    min_classes = _classes_from(min_graph)
    core_classes = _classes_from(core_graph)
    all_classes = min_classes | core_classes

    nodes = tuple(
        sorted(
            (
                Node(iri=cls, label=_best_label(merged, cls), kind=kind)
                for cls in all_classes
                for kind in [_kind_from_iri(cls)]
                if kind is not None
            ),
            key=lambda n: (n.kind, str(n.iri)),
        )
    )

    edges: set[Edge] = set()
    for child in all_classes:
        for parent in merged.objects(child, RDFS.subClassOf):
            if isinstance(parent, URIRef) and parent in all_classes:
                edges.add(Edge(parent=parent, child=child))

    return Model(nodes=nodes, edges=tuple(sorted(edges, key=lambda e: (str(e.parent), str(e.child)))))


def _to_vis_nodes(model: Model) -> list[dict[str, object]]:
    payload: list[dict[str, object]] = []
    for node in model.nodes:
        iri = str(node.iri)
        payload.append(
            {
                "id": iri,
                "label": node.label,
                "title": iri,
                "group": node.kind,
                "kind": node.kind,
                "shape": "box",
            }
        )
    return payload


def _to_vis_edges(model: Model) -> list[dict[str, object]]:
    return [
        {
            "from": str(edge.parent),
            "to": str(edge.child),
            "arrows": "to",
        }
        for edge in model.edges
    ]


def write_html(model: Model, out_html: Path, title: str) -> None:
    nodes_json = json.dumps(_to_vis_nodes(model), ensure_ascii=False, indent=2)
    edges_json = json.dumps(_to_vis_edges(model), ensure_ascii=False, indent=2)

    html = dedent(
        f"""\
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <title>{title}</title>
          <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
          <style>
            :root {{
              --bg: #f6f7fb;
              --panel: #ffffff;
              --text: #1f2937;
              --muted: #6b7280;
              --border: #d1d5db;
            }}
            body {{
              margin: 0;
              font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
              color: var(--text);
              background: linear-gradient(160deg, #eff6ff 0%, #f8fafc 45%, #fef7ff 100%);
            }}
            .layout {{
              display: grid;
              grid-template-columns: 320px minmax(0, 1fr);
              min-height: 100vh;
              gap: 0;
            }}
            .sidebar {{
              background: var(--panel);
              border-right: 1px solid var(--border);
              padding: 16px;
              box-sizing: border-box;
            }}
            h1 {{
              font-size: 18px;
              margin: 0 0 12px 0;
            }}
            .meta {{
              color: var(--muted);
              font-size: 13px;
              margin-bottom: 16px;
            }}
            .controls {{
              display: grid;
              gap: 12px;
            }}
            label {{
              font-size: 14px;
              display: block;
              margin-bottom: 4px;
            }}
            input[type="text"] {{
              width: 100%;
              padding: 8px 10px;
              border: 1px solid var(--border);
              border-radius: 8px;
              box-sizing: border-box;
            }}
            .check-row {{
              display: flex;
              gap: 12px;
              align-items: center;
              font-size: 14px;
            }}
            .btn-row {{
              display: flex;
              gap: 8px;
              flex-wrap: wrap;
            }}
            button {{
              border: 1px solid var(--border);
              background: #ffffff;
              border-radius: 8px;
              padding: 7px 10px;
              cursor: pointer;
              font-size: 13px;
            }}
            button:hover {{
              background: #f3f4f6;
            }}
            .details {{
              margin-top: 14px;
              padding-top: 12px;
              border-top: 1px solid var(--border);
              font-size: 13px;
              line-height: 1.35;
            }}
            .details .dim {{
              color: var(--muted);
            }}
            #network {{
              width: 100%;
              height: 100vh;
              background: transparent;
            }}
            @media (max-width: 980px) {{
              .layout {{
                grid-template-columns: 1fr;
                grid-template-rows: auto minmax(0, 1fr);
              }}
              .sidebar {{
                border-right: 0;
                border-bottom: 1px solid var(--border);
              }}
              #network {{
                height: calc(100vh - 280px);
                min-height: 520px;
              }}
            }}
          </style>
        </head>
        <body>
          <div class="layout">
            <aside class="sidebar">
              <h1>{title}</h1>
              <div class="meta">
                Interactive class hierarchy for MIN v3.4.0 and sdata-core.
              </div>
              <div class="controls">
                <div>
                  <label for="search">Search class</label>
                  <input id="search" type="text" placeholder="Type label or IRI fragment..." />
                </div>
                <div class="check-row">
                  <label><input id="toggle-min" type="checkbox" checked /> MIN</label>
                  <label><input id="toggle-sdata" type="checkbox" checked /> sdata</label>
                </div>
                <div class="btn-row">
                  <button id="fit-btn" type="button">Fit graph</button>
                  <button id="expand-btn" type="button">Show all</button>
                  <button id="collapse-btn" type="button">Show selected branch</button>
                </div>
              </div>
              <div class="details" id="details">
                <div class="dim">Click a node to inspect details.</div>
              </div>
            </aside>
            <main id="network" aria-label="Interactive hierarchy graph"></main>
          </div>

          <script>
            const allNodes = {nodes_json};
            const allEdges = {edges_json};

            const nodeById = new Map(allNodes.map(n => [n.id, n]));
            const parentsByChild = new Map();
            const childrenByParent = new Map();
            for (const edge of allEdges) {{
              if (!parentsByChild.has(edge.to)) parentsByChild.set(edge.to, []);
              if (!childrenByParent.has(edge.from)) childrenByParent.set(edge.from, []);
              parentsByChild.get(edge.to).push(edge.from);
              childrenByParent.get(edge.from).push(edge.to);
            }}

            const nodes = new vis.DataSet([]);
            const edges = new vis.DataSet([]);

            const container = document.getElementById("network");
            const details = document.getElementById("details");
            const search = document.getElementById("search");
            const toggleMin = document.getElementById("toggle-min");
            const toggleSdata = document.getElementById("toggle-sdata");

            const options = {{
              nodes: {{
                shape: "box",
                margin: 8,
                borderWidth: 1.6,
                font: {{ face: "Helvetica", size: 13 }},
              }},
              groups: {{
                min: {{
                  color: {{
                    background: "#E7F0FF",
                    border: "#2B6CB0",
                    highlight: {{ background: "#d3e6ff", border: "#2B6CB0" }},
                  }},
                }},
                sdata: {{
                  color: {{
                    background: "#F8EEFF",
                    border: "#6B46C1",
                    highlight: {{ background: "#efd8ff", border: "#6B46C1" }},
                  }},
                }},
              }},
              edges: {{
                arrows: {{ to: {{ enabled: true, scaleFactor: 0.75 }} }},
                color: {{ color: "#4A5568", highlight: "#111827" }},
                smooth: {{ enabled: true, type: "cubicBezier", roundness: 0.2 }},
              }},
              layout: {{
                hierarchical: {{
                  enabled: true,
                  direction: "UD",
                  sortMethod: "directed",
                  levelSeparation: 120,
                  nodeSpacing: 185,
                  treeSpacing: 240,
                }},
              }},
              interaction: {{
                hover: true,
                dragNodes: true,
                dragView: true,
                zoomView: true,
                navigationButtons: true,
                keyboard: true,
              }},
              physics: false,
            }};

            const network = new vis.Network(container, {{ nodes, edges }}, options);

            function filterNodes() {{
              const q = search.value.trim().toLowerCase();
              const allow = new Set();
              if (toggleMin.checked) allow.add("min");
              if (toggleSdata.checked) allow.add("sdata");

              return allNodes.filter(n => {{
                if (!allow.has(n.kind)) return false;
                if (!q) return true;
                return n.label.toLowerCase().includes(q) || n.id.toLowerCase().includes(q);
              }});
            }}

            function renderGraph(visibleNodes) {{
              const ids = new Set(visibleNodes.map(n => n.id));
              const visibleEdges = allEdges.filter(e => ids.has(e.from) && ids.has(e.to));
              nodes.clear();
              edges.clear();
              nodes.add(visibleNodes);
              edges.add(visibleEdges);
            }}

            function showAll() {{
              renderGraph(filterNodes());
              network.fit({{ animation: {{ duration: 250, easingFunction: "easeInOutQuad" }} }});
            }}

            function branchFrom(seedId) {{
              const allowedKinds = new Set();
              if (toggleMin.checked) allowedKinds.add("min");
              if (toggleSdata.checked) allowedKinds.add("sdata");

              const keep = new Set([seedId]);
              const queue = [seedId];
              while (queue.length) {{
                const id = queue.shift();
                for (const p of (parentsByChild.get(id) || [])) {{
                  const node = nodeById.get(p);
                  if (node && allowedKinds.has(node.kind) && !keep.has(p)) {{
                    keep.add(p);
                    queue.push(p);
                  }}
                }}
                for (const c of (childrenByParent.get(id) || [])) {{
                  const node = nodeById.get(c);
                  if (node && allowedKinds.has(node.kind) && !keep.has(c)) {{
                    keep.add(c);
                    queue.push(c);
                  }}
                }}
              }}

              const q = search.value.trim().toLowerCase();
              const nodesFiltered = allNodes.filter(n => {{
                if (!keep.has(n.id)) return false;
                if (!allowedKinds.has(n.kind)) return false;
                if (!q) return true;
                return n.label.toLowerCase().includes(q) || n.id.toLowerCase().includes(q);
              }});
              renderGraph(nodesFiltered);
              network.fit({{ animation: {{ duration: 250, easingFunction: "easeInOutQuad" }} }});
            }}

            function updateDetails(nodeId) {{
              if (!nodeId) {{
                details.innerHTML = '<div class="dim">Click a node to inspect details.</div>';
                return;
              }}
              const node = nodeById.get(nodeId);
              const parents = parentsByChild.get(nodeId) || [];
              const children = childrenByParent.get(nodeId) || [];
              details.innerHTML = `
                <div><strong>${{node.label}}</strong></div>
                <div class="dim">${{node.id}}</div>
                <div style="margin-top:8px"><strong>Group:</strong> ${{node.kind}}</div>
                <div><strong>Parents:</strong> ${{parents.length}}</div>
                <div><strong>Children:</strong> ${{children.length}}</div>
              `;
            }}

            document.getElementById("fit-btn").addEventListener("click", () => {{
              network.fit({{ animation: {{ duration: 250, easingFunction: "easeInOutQuad" }} }});
            }});
            document.getElementById("expand-btn").addEventListener("click", showAll);
            document.getElementById("collapse-btn").addEventListener("click", () => {{
              const selected = network.getSelectedNodes();
              if (!selected.length) return;
              branchFrom(selected[0]);
            }});

            search.addEventListener("input", showAll);
            toggleMin.addEventListener("change", showAll);
            toggleSdata.addEventListener("change", showAll);

            network.on("click", params => {{
              const nodeId = params.nodes.length ? params.nodes[0] : null;
              updateDetails(nodeId);
            }});

            showAll();
          </script>
        </body>
        </html>
        """
    )

    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(html, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min", dest="min_path", type=Path, default=Path("min-v3.4.0.ttl"))
    parser.add_argument("--core", type=Path, default=Path("sdata-core-v0.13.1.ttl"))
    parser.add_argument("--out-dir", type=Path, default=Path("docs/diagrams"))
    parser.add_argument("--name", default="sdata-min-core-hierarchy-interactive")
    parser.add_argument("--title", default="Interactive Class Hierarchy: MIN v3.4.0 -> sdata-core")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    logging.getLogger("rdflib.term").setLevel(logging.CRITICAL)
    args = parse_args(argv or sys.argv[1:])

    try:
        min_g, core_g, merged_g = load_graphs(args.min_path, args.core)
        model = extract_model(min_g, core_g, merged_g)
        if not model.nodes:
            print("No classes found for visualization.", file=sys.stderr)
            return 4
        out_html = args.out_dir / f"{args.name}.html"
        write_html(model, out_html, title=args.title)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except Exception as exc:  # pragma: no cover - CLI fallback
        print(f"Failed to build interactive hierarchy: {exc}", file=sys.stderr)
        return 3

    print(f"Generated {out_html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


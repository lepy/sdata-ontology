# Migration Guide: sdata-core v0.10.0 → v0.12.0

## Übersicht

v0.12.0 migriert auf MIN v2.1.0. Die OPA-Zwischenschicht entfällt.
Blank-Node-Aspekte (v2.0) sind durch flache Properties ersetzt.

```
VORHER (3 Schichten):     NACHHER (2 Schichten):
  MIN  ←  OPA  ←  sdata      MIN  ←  sdata
```

## Breaking Changes

### 1. OPA-Import entfällt

```diff
- owl:imports <https://w3id.org/opa> .
  owl:imports <https://w3id.org/min> .
```

### 2. Namespace-Migration (opa: → min:)

| v0.10.0 (opa:)          | v0.12.0 (min:)          |
|--------------------------|-------------------------|
| `opa:Object`             | `min:Object`            |
| `opa:Process`            | `min:Process`           |
| `opa:Agent`              | `min:Agent`             |
| `opa:hasInput`           | `min:hasInput`          |
| `opa:hasOutput`          | `min:hasOutput`         |
| `opa:performs`           | `min:performs`          |
| `opa:performedBy`        | `min:performedBy`       |
| `opa:controls`           | `min:controls`          |
| `opa:actsOn`             | `min:actsOn`            |
| `opa:affectedBy`         | `min:affectedBy`        |
| `opa:owns`               | `min:owns`              |
| `opa:undergoes`          | `min:undergoes`         |
| `opa:resultOf`           | `min:resultOf`          |
| `opa:produces`           | `min:produces`          |
| `opa:hasIdentifier`      | `min:hasIdentifier`     |
| `opa:hasName`            | `min:hasName`           |
| `opa:hasTimestamp`        | `min:hasTimestamp`       |
| `opa:hasDescription`      | `min:hasDescription`     |
| `opa:hasStatus`           | `min:hasStatus`          |

### 3. Data verschoben

```diff
- sdata:Data rdfs:subClassOf sdata:Object .   # material-dominant
+ sdata:Data rdfs:subClassOf min:Data .        # informational-dominant
```

**Konsequenz:** `sdata:Data` ist nicht mehr unter `min:Object`.
SPARQL-Queries wie `?x a min:Object` liefern keine Data-Instanzen mehr.

### 4. Entfernte MIN/OPA-Konzepte

| Konzept                         | Ersatz                          |
|---------------------------------|---------------------------------|
| `min:Material` (Klasse)         | Blank Node via `min:materialAspect` |
| `min:Information` (Klasse)      | Blank Node via `min:informationalAspect` |
| `min:Modality`                  | Klasse IST Modalität            |
| `min:hasModality`               | entfällt                        |
| `min:hasMaterialAspect`         | `min:materialAspect`            |
| `min:hasInformationalAspect`    | `min:informationalAspect`       |
| `min:isAspectOf`                | entfällt (Blank Nodes)          |
| `min:isMaterialAspectOf`        | entfällt (Blank Nodes)          |
| `min:isInformationalAspectOf`   | entfällt (Blank Nodes)          |

### 5. Neue MIN-Konzepte

| Konzept                | Bedeutung                              |
|------------------------|----------------------------------------|
| `min:Data`             | Erstklassige Kategorie für Daten       |
| `min:describes`        | Data beschreibt Nexus                  |
| `min:describedBy`      | Nexus wird beschrieben durch Data      |
| `min:generates`        | Process erzeugt Data                   |
| `min:generatedBy`      | Data wird erzeugt durch Process        |
| `min:materialAspect`   | Blank-Node-Pol (ersetzt hasMaterialAspect) |
| `min:informationalAspect` | Blank-Node-Pol (ersetzt hasInformationalAspect) |

### 6. Neue sdata-core Properties (v0.12.0)

| Konzept                | Bedeutung                              |
|------------------------|----------------------------------------|
| `sdata:hasData`        | Nexus hat zugehörige Data (subProp von min:describedBy) |
| `sdata:producedBy`     | Data wurde durch Process erzeugt (subProp von min:generatedBy) |

## SPARQL-Migration

### Queries auf opa: Namespace

```diff
- SELECT ?obj WHERE { ?obj a opa:Object }
+ SELECT ?obj WHERE { ?obj a min:Object }
```

### Queries auf Data unter Object

```diff
  # VORHER: Data war unter Object → diese Query fand auch Data
- SELECT ?x WHERE { ?x a min:Object }
  
  # NACHHER: Data ist eigene Kategorie
+ SELECT ?x WHERE { { ?x a min:Object } UNION { ?x a min:Data } }
  # oder für alle Nexus:
+ SELECT ?x WHERE { ?x a min:Nexus }
```

### Queries auf Material/Information-Aspekte

```diff
  # VORHER (v0.10 — Named Individuals):
- SELECT ?m WHERE { ex:Coil min:hasMaterialAspect ?mat .
-                   ?mat ex:masse_kg ?m }
  
  # NACHHER (v2.1 — flach, direkt):
+ SELECT ?m WHERE { ex:Coil ex:masse_kg ?m }

  # Alle materialen Properties eines Nexus:
+ SELECT ?prop ?val WHERE {
+     ex:Coil ?prop ?val .
+     ?prop rdfs:subPropertyOf* min:materialProperty .
+ }
```

### MIN v2.0 → v2.1: Blank Nodes entfallen

Wer bereits auf v2.0 (Blank-Node-Pattern) migriert hat:

```diff
  # v2.0 (Blank Nodes):
- ex:Coil min:materialAspect [ ex:masse_kg 12500 ] .
- SELECT ?m WHERE { ex:Coil min:materialAspect/ex:masse_kg ?m }

  # v2.1 (flach):
+ ex:Coil ex:masse_kg 12500 .
+ SELECT ?m WHERE { ex:Coil ex:masse_kg ?m }

  # Property-Definition (einmalig im Schema):
+ ex:masse_kg rdfs:subPropertyOf min:materialProperty .
```

`min:materialAspect` und `min:informationalAspect` existieren in v2.1 nicht mehr.
Ersetzt durch `min:materialProperty` und `min:informationalProperty` als
Schema-Ebene Superproperties.

## SHACL-Migration

Alle Shapes die `opa:` referenzieren, müssen auf `min:` umgestellt werden.
Zusätzlich: Shapes die `sdata:Data` als `min:Object`-Subklasse erwarten,
müssen angepasst werden. Shapes die `min:materialAspect`/`min:informationalAspect`
referenzieren (v2.0), müssen auf direkte Property-Pfade umgestellt werden.

## Dateien die angepasst werden müssen

| Datei                           | Änderung                          |
|---------------------------------|-----------------------------------|
| `sdata-core.ttl`                | → `sdata-core-v0.12.0.ttl`       |
| `shapes/sdata-core-shapes.ttl`  | opa: → min:, Data-Shapes, Aspekt-Pfade |
| `sdata-material-state.ttl`      | `@prefix opa:` entfernen, `min:layer` entfernen |
| `examples/*.ttl`                | opa: → min:, Blank Nodes → flach  |
| `tests/*.py`                    | Namespace-Updates                 |
| `src/visualization/*.py`        | OPA-Referenzen entfernen          |
| `min-v1.0.0.ttl`               | → `min-v2.1.0.ttl` (ersetzen)    |
| `opa-v1.0.0.ttl`               | → entfernen                       |
| `Makefile`                      | viz-min-opa-core → viz-min-core   |
| `README.md`                     | Architektur-Doku aktualisieren    |

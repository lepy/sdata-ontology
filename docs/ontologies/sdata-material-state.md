# GUIDE: Material State Space

> **Modul:** `sdata-material-state.ttl` v0.1.0  
> **Ontologie:** sdata v0.6.0 auf MIN/OPA  
> **Zielgruppe:** Ingenieure, Materialwissenschaftler, Datenmodellierer  
> **Vorkenntnisse:** Grundlegendes Turtle-Format, sdata-Grundbegriffe

---

## 1. Was ist der Material State Space?

Jedes Material hat einen **multidimensionalen Zustand**. Ein PP-GF30-Recyclat-Granulat für die Automobilindustrie ist nicht einfach "ein Material" — es ist gleichzeitig:

- **recycled** (Herkunft)
- **processed** (Verarbeitungszustand)
- **degraded** (Kondition)
- **granulate** (Form)
- **automotive** (Einsatzklasse)
- **REACH + RoHS** (Konformität)
- **composite** (Zusammensetzung)
- **production** (Lebenszyklusphase)

Jede dieser Aussagen liegt auf einer **unabhängigen Achse**. Der Material State Space modelliert diesen Zustandsvektor mit einem generischen, erweiterbaren Mechanismus.


## 2. Die drei Bausteine

Das gesamte System besteht aus drei Teilen:

### 2.1 StateAxis — "Welche Frage wird gestellt?"

Eine Achse ist eine Dimension des Zustandsraums. Beispiel: Die **OriginAxis** fragt "Woher kommt der Werkstoff?"

Jede Achse verweist auf ein Wertesystem (ConceptScheme), das die erlaubten Antworten enthält.

### 2.2 skos:Concept — "Welche Antworten gibt es?"

Die Antworten auf jede Achse sind **SKOS-Konzepte** — standardisierte, mehrsprachige, hierarchisch erweiterbare Begriffe.

### 2.3 StateAssignment — "Was gilt für DIESES Material?"

Eine Zustandszuordnung verbindet ein konkretes Material mit einem Wert auf einer bestimmten Achse. Sie ist ein vollwertiger Data-Nexus mit optionaler Provenienz und Detailwerten.

```
Material ──hasStateAssignment──▶ StateAssignment
                                      │
                              onAxis──┤──hasStateValue──▶ Concept
                                      │
                              producedBy──▶ Activity (optional)
                                      │
                              hasQuantity──▶ AQV (optional)
```


## 3. SKOS in 5 Minuten

SKOS (Simple Knowledge Organization System) ist ein W3C-Standard für Wertelisten. Man braucht nur fünf Begriffe:

| SKOS-Term | Was ist das? | Analogie |
|-----------|-------------|----------|
| `skos:ConceptScheme` | Eine benannte Werteliste | Ein Karteikasten |
| `skos:Concept` | Ein Wert in dieser Liste | Eine Karteikarte |
| `skos:prefLabel` | Der bevorzugte Name (mehrsprachig) | Was auf der Karte steht |
| `skos:inScheme` | "gehört zu dieser Liste" | Die Karte steckt in diesem Kasten |
| `skos:broader` | "ist Unterart von" | Verweis auf übergeordnete Karte |

**Warum SKOS und nicht einfach Strings?**

Ein String `"recycled"` ist tot — man kann ihn nicht übersetzen, nicht hierarchisch gliedern, nicht maschinell prüfen. Ein `skos:Concept` ist lebendig:

- Mehrsprachig: `"Recycled"@en`, `"Recycelt"@de`, `"Recyclé"@fr`
- Hierarchisch: "Ocean Reclaimed" → broader → "Recycled"
- Prüfbar: URI existiert oder nicht (kein stiller Tippfehler)
- Catena-X-kompatibel: SKOS ist dort der Standard für Wertelisten


## 4. Die 8 vordefinierten Achsen

Das Modul liefert 8 Achsen mit insgesamt 45 vordefinierten Werten:

### Achse 1: Origin — Woher kommt der Werkstoff?

| Concept | DE | Bedeutung |
|---------|-----|-----------|
| `sms:origin.Virgin` | Primär | Aus Rohstoff erstmalig gewonnen |
| `sms:origin.Recycled` | Recycelt | Aus Recyclingprozess rückgewonnen |
| `sms:origin.BioBased` | Biobasiert | Aus nachwachsenden Rohstoffen |
| `sms:origin.Blended` | Gemischt | Definierter Mix verschiedener Herkunftsklassen |

Typ: **Primäre Achse** — nicht aus der Activity-Kette ableitbar.

### Achse 2: Processing — Was wurde mit dem Werkstoff getan?

| Concept | DE | Bedeutung |
|---------|-----|-----------|
| `sms:processing.Raw` | Roh | Unverarbeitet, Anlieferungszustand |
| `sms:processing.Processed` | Verarbeitet | Nach gezielter Formgebung |
| `sms:processing.HeatTreated` | Wärmebehandelt | Nach thermischer Behandlung |
| `sms:processing.Aged` | Gealtert | Natürlich oder künstlich ausgelagert |

Typ: **Sekundäre Achse** — grundsätzlich aus `resultOf`-Kette ableitbar, hier als eigenständiger Deskriptor reifiziert.

### Achse 3: Condition — Wie gut ist der Werkstoff?

| Concept | DE | Bedeutung |
|---------|-----|-----------|
| `sms:condition.Pristine` | Unversehrt | Sollzustand, keine Degradation |
| `sms:condition.Degraded` | Degradiert | Eigenschaftsverlust durch Nutzung/Recycling |
| `sms:condition.Contaminated` | Kontaminiert | Unerwünschte Beimengungen |

Typ: **Sekundäre Achse** — aus Messdaten ableitbar.

### Achse 4: Form — In welcher Gestalt?

| Concept | DE |
|---------|-----|
| `sms:form.Powder` | Pulver |
| `sms:form.Granulate` | Granulat |
| `sms:form.Sheet` | Blech |
| `sms:form.Coil` | Coil |
| `sms:form.Wire` | Draht |
| `sms:form.Film` | Folie |
| `sms:form.Bulk` | Massivkörper |
| `sms:form.Fiber` | Faser |

Typ: **Primäre Achse**.

### Achse 5: Grade — Für welchen Einsatz?

| Concept | DE |
|---------|-----|
| `sms:grade.Technical` | Technisch |
| `sms:grade.Automotive` | Automotive |
| `sms:grade.FoodContact` | Lebensmittelkontakt |
| `sms:grade.Medical` | Medizinisch |
| `sms:grade.Aerospace` | Luft- und Raumfahrt |

Typ: **Primäre Achse**.

### Achse 6: Compliance — Welche Zulassungen?

| Concept | Bedeutung |
|---------|-----------|
| `sms:compliance.REACH` | EU-Chemikalienverordnung (EG) Nr. 1907/2006 |
| `sms:compliance.RoHS` | Richtlinie 2011/65/EU |
| `sms:compliance.FoodContact` | Verordnung (EG) Nr. 1935/2004 |
| `sms:compliance.ESPR` | Ecodesign for Sustainable Products Regulation |
| `sms:compliance.IATF` | IATF 16949, Qualitätsmanagement Automotive |

Typ: **Meta-Achse** — mehrwertig (ein Material kann mehrere Zulassungen haben). Extern getrieben durch Regulierungsbehörden.

### Achse 7: Composition — Wie ist der Werkstoff zusammengesetzt?

| Concept | DE |
|---------|-----|
| `sms:composition.Homogeneous` | Homogen |
| `sms:composition.Alloy` | Legierung |
| `sms:composition.Composite` | Verbundwerkstoff |
| `sms:composition.Blend` | Blend (Polymergemisch) |
| `sms:composition.MultiMaterial` | Multi-Material |

Typ: **Primäre Achse**.

### Achse 8: Lifecycle Phase — Wo im Lebenszyklus?

13 Phasen in 5 Top-Level-Gruppen mit `skos:broader`-Hierarchie:

| Concept | DE | Top-Level |
|---------|-----|-----------|
| `sms:phase.Production` | Produktion | ● Top-Level |
| `sms:phase.RawMaterialExtraction` | Rohstoffgewinnung | → Production |
| `sms:phase.Processing` | Verarbeitung | → Production |
| `sms:phase.Assembly` | Montage | → Production |
| `sms:phase.InUse` | In Nutzung | ● Top-Level |
| `sms:phase.Maintenance` | Wartung | → InUse |
| `sms:phase.EndOfLife` | Ende der Nutzung | ● Top-Level |
| `sms:phase.Collection` | Sammlung | → EndOfLife |
| `sms:phase.Recycling` | Recycling | → EndOfLife |
| `sms:phase.Reuse` | Wiederverwendung | → EndOfLife |
| `sms:phase.Disposal` | Entsorgung | → EndOfLife |
| `sms:phase.Storage` | Lagerung | ● Top-Level |
| `sms:phase.Transit` | Transport | ● Top-Level |

Typ: **Sekundäre Achse** — ableitbar aus der Position in der Activity-Kette.

Baumstruktur:

```
Production
 ├── RawMaterialExtraction
 ├── Processing
 └── Assembly
InUse
 └── Maintenance
EndOfLife
 ├── Collection
 ├── Recycling
 ├── Reuse
 └── Disposal
Storage
Transit
```

Eine Query nach `sms:phase.Production` mit `skos:broader*` findet automatisch auch RawMaterialExtraction, Processing und Assembly. Eine Query nach `sms:phase.EndOfLife` findet Collection, Recycling, Reuse und Disposal.


## 5. Eigene Achsen vs. vordefinierte Achsen

### Das Prinzip

Die 8 vordefinierten Achsen (Origin, Processing, Condition, ...) sind **Vorschläge, keine Pflicht**. Der Material State Space ist ein offener Mechanismus:

- Man kann **nur vordefinierte Achsen** nutzen (Subset oder alle 8)
- Man kann **nur eigene Achsen** definieren (die vordefinierten komplett ignorieren)
- Man kann **mischen** — vordefinierte Achsen verwenden, wo sie passen, eigene hinzufügen, wo die Domäne es erfordert

Es gibt keinen Zwang, alle 8 Achsen zu besetzen, und keinen Zwang, die vordefinierten zu verwenden. Die einzige Regel: jede Achse muss `rdfs:subClassOf sms:StateAxis` sein.

### Drei typische Nutzungsprofile

**Profil A: Minimal** — nur 2 Achsen, beide vordefiniert

Ein Zulieferer, der seinen DPP-Pflichten nachkommen will, braucht vielleicht nur Origin und Compliance:

```turtle
:mat_minimal a sdata:Material ;
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:OriginAxis ;
        sms:hasStateValue sms:origin.Recycled
    ] ;
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ComplianceAxis ;
        sms:hasStateValue sms:compliance.REACH
    ] .
```

**Profil B: Domänenspezifisch** — vordefinierte + eigene Achsen gemischt

Ein Prüflabor für PA6 nutzt die vordefinierte Form-Achse, braucht aber eine eigene Moisture-Achse:

```turtle
:pa6_probe a sdata:Material ;
    # Vordefinierte Achse — passt wie sie ist
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:FormAxis ;
        sms:hasStateValue sms:form.Granulate
    ] ;
    # Eigene Achse — PA6-spezifisch
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis ex:MoistureAxis ;
        sms:hasStateValue ex:moisture.Conditioned
    ] .
```

**Profil C: Vollständig eigene Achsen** — kein vordefiniertes Konzept verwendet

Ein Spezialgebiet (z.B. Batteriechemie) definiert seinen kompletten Zustandsraum selbst:

```turtle
@prefix bat: <https://example.org/battery-axes/> .

bat:ChemistryAxis     rdfs:subClassOf sms:StateAxis .
bat:CellFormatAxis    rdfs:subClassOf sms:StateAxis .
bat:SOHAxis           rdfs:subClassOf sms:StateAxis .
bat:CycleStateAxis    rdfs:subClassOf sms:StateAxis .

:cell_001 a sdata:Material ;
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis bat:ChemistryAxis ;
        sms:hasStateValue bat:chemistry.NMC811
    ] ;
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis bat:SOHAxis ;
        sms:hasStateValue bat:soh.Good ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "state_of_health" ;
            qudt:numericValue 0.92 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ]
    ] .
```

Keine einzige `sms:`-Achse verwendet. Trotzdem funktioniert das generische Pattern (StateAssignment, onAxis, hasStateValue) — und alle SPARQL-Queries greifen.

### Entscheidungshilfe

| Frage | Empfehlung |
|-------|------------|
| Passt eine vordefinierte Achse inhaltlich? | Nutzen — spart Modellierungsaufwand |
| Passen die Werte einer Achse nicht? | Eigene Werte zum bestehenden Scheme hinzufügen |
| Passt die Achse selbst nicht? | Eigene Achse als `rdfs:subClassOf sms:StateAxis` |
| Catena-X-Interoperabilität nötig? | Vordefinierte Achsen bevorzugen — sie werden zum Standard |
| Domäne hat völlig andere Dimensionen? | Komplett eigene Achsen definieren |

### Interoperabilität zwischen Profilen

Weil alle Achsen `rdfs:subClassOf sms:StateAxis` sind, funktionieren **alle SPARQL-Queries über den generischen Mechanismus** — egal ob vordefinierte oder eigene Achsen:

```sparql
# Findet ALLE Zustandszuordnungen ALLER Materialien,
# egal welche Achsen verwendet wurden
SELECT ?material ?axis ?value ?label
WHERE {
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis ?axis .
    ?sa sms:hasStateValue ?value .
    ?value skos:prefLabel ?label .
}
```

Das ist der Kern des Designs: **ein Mechanismus, beliebig viele Achsen**.


## 6. Rezepte

### Rezept 1: Material mit Zustandsvektor beschreiben

Ein DC04-Stahlblech, virgin, kaltgewalzt, im Sollzustand:

```turtle
:dc04_coil_001 a sdata:Material ;
    sdata:hasIdentifier "MAT-DC04-001" ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:OriginAxis ;
        sms:hasStateValue sms:origin.Virgin
    ] ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ProcessingAxis ;
        sms:hasStateValue sms:processing.Processed
    ] ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ConditionAxis ;
        sms:hasStateValue sms:condition.Pristine
    ] ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:FormAxis ;
        sms:hasStateValue sms:form.Coil
    ] .
```

Man muss nicht alle 8 Achsen besetzen. Nur die relevanten.


### Rezept 2: Zustand mit Provenienz und Detailwerten

Ein PP-GF30-Recyclat mit Herkunftsnachweis:

```turtle
:pp_gf30_lot42 a sdata:Material ;
    sdata:hasIdentifier "MAT-PP-GF30-042" ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:OriginAxis ;
        sms:hasStateValue sms:origin.Recycled ;

        # Provenienz: WOHER kam das Recyclat?
        sdata:producedBy :recycling_run_17 ;

        # Detailwerte: WIE VIEL recycled?
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "recycled_content" ;
            rdfs:label "Recyclatanteil"@de ;
            qudt:numericValue 0.70 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "cycle_count" ;
            rdfs:label "Recycling-Zyklen"@de ;
            qudt:numericValue 3 ;
            sdata:dtype "int"
        ]
    ] .
```

Der Wert `sms:origin.Recycled` sagt **was**. Die AQVs sagen **wie viel**. Die `producedBy`-Relation sagt **woher**. Alles im selben Muster.


### Rezept 3: Neuen Wert zu bestehender Achse hinzufügen

Du arbeitest mit Ozeanplastik und brauchst einen spezifischeren Origin-Wert:

```turtle
sms:origin.OceanReclaimed a skos:Concept ;
    skos:inScheme sms:origin-values ;
    skos:prefLabel "Ocean Reclaimed"@en , "Ozean-Rezyklat"@de ;
    skos:definition "Aus Ozeanplastik rückgewonnen."@de ;
    skos:broader sms:origin.Recycled .
```

Drei Zeilen (plus Labels). Keine Schemaänderung. Sofort benutzbar.

Die `skos:broader`-Zeile ist optional aber mächtig: sie sagt, dass "Ocean Reclaimed" eine **Unterart** von "Recycled" ist. SPARQL-Queries nach "Recycled" finden dann automatisch auch "Ocean Reclaimed".


### Rezept 4: Hierarchie in einer bestehenden Achse aufbauen

Die Form-Achse hat `sms:form.Sheet`. Für die Stahlbranche braucht man Feinunterscheidungen:

```turtle
sms:form.SheetHotRolled a skos:Concept ;
    skos:inScheme sms:form-values ;
    skos:prefLabel "Hot-rolled Sheet"@en , "Warmband"@de ;
    skos:broader sms:form.Sheet .

sms:form.SheetColdRolled a skos:Concept ;
    skos:inScheme sms:form-values ;
    skos:prefLabel "Cold-rolled Sheet"@en , "Kaltband"@de ;
    skos:broader sms:form.Sheet .

sms:form.SheetGalvanized a skos:Concept ;
    skos:inScheme sms:form-values ;
    skos:prefLabel "Galvanized Sheet"@en , "Verzinktes Blech"@de ;
    skos:broader sms:form.SheetColdRolled .
```

Ergebnis — ein Baum:

```
Sheet
 ├── Hot-rolled Sheet
 └── Cold-rolled Sheet
      └── Galvanized Sheet
```

Eine Query nach `sms:form.Sheet` findet alle vier. Eine Query nach `sms:form.SheetColdRolled` findet Kaltband und Verzinktes Blech.


### Rezept 5: Komplett neue Achse definieren

PA6 ist feuchtigkeitsempfindlich. Die mechanischen Eigenschaften hängen stark vom Feuchtezustand ab. Du brauchst eine Moisture-Achse.

**Schritt 1 — Karteikasten anlegen:**

```turtle
@prefix ex: <https://example.org/my-axes/> .

ex:moisture-values a skos:ConceptScheme ;
    rdfs:label "Moisture Values"@en , "Feuchtewerte"@de .
```

**Schritt 2 — Karten einstecken:**

```turtle
ex:moisture.Dry a skos:Concept ;
    skos:inScheme ex:moisture-values ;
    skos:prefLabel "Dry"@en , "Trocken"@de ;
    skos:definition "Ofengetrocknet, < 0.1% Feuchte."@de .

ex:moisture.Conditioned a skos:Concept ;
    skos:inScheme ex:moisture-values ;
    skos:prefLabel "Conditioned"@en , "Konditioniert"@de ;
    skos:definition "Normklima 23°C / 50% r.F., Gleichgewichtsfeuchte."@de .

ex:moisture.Saturated a skos:Concept ;
    skos:inScheme ex:moisture-values ;
    skos:prefLabel "Saturated"@en , "Gesättigt"@de ;
    skos:definition "Maximale Wasseraufnahme erreicht."@de .
```

**Schritt 3 — Achse mit sdata verbinden:**

```turtle
ex:MoistureAxis a owl:Class ;
    rdfs:subClassOf sms:StateAxis ;
    rdfs:label "Moisture Axis"@en , "Feuchteachse"@de ;
    sms:hasConceptScheme ex:moisture-values .
```

**Schritt 4 — Benutzen:**

```turtle
:pa6_probe_007 a sdata:Material ;
    sdata:hasIdentifier "MAT-PA6-007" ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis ex:MoistureAxis ;
        sms:hasStateValue ex:moisture.Conditioned ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "moisture_content" ;
            qudt:numericValue 2.5 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ]
    ] .
```

Zusammenfassung: 1 ConceptScheme + 3 Concepts + 1 Achsen-Klasse = fertig. Keine Änderung am Core-Schema.


### Rezept 6: Mehrere Werte auf einer Achse (Compliance)

Ein Material kann mehrere Zulassungen gleichzeitig haben:

```turtle
:mat_001 a sdata:Material ;

    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ComplianceAxis ;
        sms:hasStateValue sms:compliance.REACH ;
        sms:hasStateValue sms:compliance.RoHS ;
        sms:hasStateValue sms:compliance.IATF
    ] .
```

Die `sms:hasStateValue`-Relation ist nicht functional — mehrere Werte pro Assignment sind erlaubt. Das ist bewusst so für die Compliance-Achse, funktioniert aber technisch auf jeder Achse.


## 7. SPARQL-Abfragen

### Alle recycelten Materialien finden

```sparql
SELECT ?material ?recycledContent
WHERE {
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis sms:OriginAxis .
    ?sa sms:hasStateValue sms:origin.Recycled .
    OPTIONAL {
        ?sa sdata:hasQuantity ?aqv .
        ?aqv sdata:name "recycled_content" .
        ?aqv qudt:numericValue ?recycledContent .
    }
}
```

### Alle Materialien auf einer bestimmten Achse filtern

```sparql
SELECT ?material ?axis ?value ?label
WHERE {
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis ?axis .
    ?sa sms:hasStateValue ?value .
    ?value skos:prefLabel ?label .
    FILTER(lang(?label) = "de")
}
```

### Den vollständigen Zustandsvektor eines Materials abrufen

```sparql
SELECT ?axisLabel ?valueLabel
WHERE {
    :pp_gf30_lot42 sms:hasStateAssignment ?sa .
    ?sa sms:onAxis ?axis .
    ?sa sms:hasStateValue ?value .
    ?axis rdfs:label ?axisLabel .
    ?value skos:prefLabel ?valueLabel .
    FILTER(lang(?axisLabel) = "de")
    FILTER(lang(?valueLabel) = "de")
}
```

Ergebnis:

| axisLabel | valueLabel |
|-----------|------------|
| Herkunftsachse | Recycelt |
| Verarbeitungsachse | Verarbeitet |
| Konditionsachse | Degradiert |
| Formachse | Granulat |
| Güteachse | Automotive |
| Konformitätsachse | REACH |
| Konformitätsachse | RoHS |
| Zusammensetzungsachse | Verbundwerkstoff |
| Lebenszyklusphase-Achse | Produktion |

### Hierarchische Suche: "Sheet oder feiner"

```sparql
SELECT ?material ?specificForm
WHERE {
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis sms:FormAxis .
    ?sa sms:hasStateValue ?specificForm .
    ?specificForm skos:broader* sms:form.Sheet .
}
```

`skos:broader*` ist der transitive Abschluss — findet Sheet, Hot-rolled Sheet, Cold-rolled Sheet und Galvanized Sheet.


## 8. Catena-X und Digitaler Produktpass (DPP)

### Kontext

Die EU-Verordnung **ESPR** (Ecodesign for Sustainable Products Regulation) verpflichtet Hersteller, für bestimmte Produktgruppen einen **Digitalen Produktpass (DPP)** bereitzustellen. Der DPP muss maschinenlesbar Informationen über Materialherkunft, Recyclatanteil, Compliance und Lebenszyklus enthalten.

**Catena-X** ist das Datenökosystem der Automobilindustrie, das unter anderem den DPP für Fahrzeugkomponenten umsetzt. Catena-X nutzt Semantic Web-Technologien und SKOS-basierte Wertelisten — genau das, was sdata-material-state liefert.

### Welche Achsen braucht der DPP?

Die ESPR fordert für den DPP mindestens diese Informationen über den Werkstoff:

| DPP-Anforderung | sdata-material-state Achse | Pflicht? |
|-----------------|---------------------------|----------|
| Recyclatanteil | `sms:OriginAxis` + AQV `recycled_content` | **Ja** |
| Herkunftsnachweis | `sms:OriginAxis` + `producedBy` | **Ja** |
| Stoffkonformität (REACH, RoHS) | `sms:ComplianceAxis` | **Ja** |
| ESPR-Konformität | `sms:ComplianceAxis` | **Ja** |
| Werkstoffzusammensetzung | `sms:CompositionAxis` | **Ja** |
| Einsatzklassifizierung | `sms:GradeAxis` | Empfohlen |
| Verarbeitungszustand | `sms:ProcessingAxis` | Empfohlen |
| Lebenszyklusphase | `sms:LifecyclePhaseAxis` | Empfohlen |
| Degradationsgrad | `sms:ConditionAxis` | Für Recyclate |
| Lieferform | `sms:FormAxis` | Optional |

### Vollständiges DPP-Beispiel: B-Säule aus PP-GF30-Recyclat

Szenario: Ein Automobilzulieferer produziert eine B-Säule aus PP-GF30 mit 70% Recyclatanteil. Der DPP muss den gesamten Materiallebenszyklus dokumentieren — vom Recyclat-Granulat über den Spritzguss bis zum fertigen Bauteil.

```turtle
@prefix sdata:   <https://w3id.org/sdata/core/> .
@prefix sms:     <https://w3id.org/sdata/material-state/> .
@prefix min:     <https://w3id.org/min#> .
@prefix qudt:    <http://qudt.org/schema/qudt/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix :        <https://example.org/dpp/> .


# ═══════════════════════════════════════════════════════════════════════
#   1. DER WERKSTOFF — PP-GF30-Recyclat
# ═══════════════════════════════════════════════════════════════════════

:pp_gf30_lot42 a sdata:Material ;
    sdata:hasIdentifier "MAT-PP-GF30-042" ;
    rdfs:label "PP-GF30 Recyclat Lot 42"@de ;

    # --- Achse 1: Origin (DPP-PFLICHT) ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:OriginAxis ;
        sms:hasStateValue sms:origin.Recycled ;
        sdata:producedBy :recycling_run_17 ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "recycled_content" ;
            rdfs:label "Recyclatanteil"@de ;
            qudt:numericValue 0.70 ;
            sdata:unitSymbol "%" ;
            qudt:unit <http://qudt.org/vocab/unit/FRACTION> ;
            sdata:dtype "float"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "cycle_count" ;
            rdfs:label "Recycling-Zyklen"@de ;
            qudt:numericValue 3 ;
            sdata:dtype "int"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "post_consumer_content" ;
            rdfs:label "Post-Consumer-Anteil"@de ;
            qudt:numericValue 0.55 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ]
    ] ;

    # --- Achse 6: Compliance (DPP-PFLICHT) ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ComplianceAxis ;
        sms:hasStateValue sms:compliance.REACH ;
        sms:hasStateValue sms:compliance.RoHS ;
        sms:hasStateValue sms:compliance.ESPR ;
        sms:hasStateValue sms:compliance.IATF ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "reach_registration_nr" ;
            rdfs:label "REACH-Registrierungsnummer"@de ;
            qudt:numericValue "01-2119486000-44-0000" ;
            sdata:dtype "str"
        ]
    ] ;

    # --- Achse 7: Composition (DPP-PFLICHT) ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:CompositionAxis ;
        sms:hasStateValue sms:composition.Composite ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "matrix_material" ;
            rdfs:label "Matrixwerkstoff"@de ;
            qudt:numericValue "PP" ;
            sdata:dtype "str"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "reinforcement_material" ;
            rdfs:label "Verstärkungsmaterial"@de ;
            qudt:numericValue "GF" ;
            sdata:dtype "str"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "fiber_weight_fraction" ;
            rdfs:label "Fasergewichtsanteil"@de ;
            qudt:numericValue 0.30 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ]
    ] ;

    # --- Achse 3: Condition (PFLICHT für Recyclate) ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:ConditionAxis ;
        sms:hasStateValue sms:condition.Degraded ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "fiber_length_retention" ;
            rdfs:label "Faserlängenretention"@de ;
            qudt:numericValue 0.62 ;
            sdata:unitSymbol "%" ;
            sdata:dtype "float"
        ] ;
        sdata:hasQuantity [
            a sdata:AttributeQuantityValue ;
            sdata:name "mfi_shift" ;
            rdfs:label "MFI-Verschiebung"@de ;
            qudt:numericValue 1.3 ;
            sdata:unitSymbol "g/10min" ;
            sdata:dtype "float"
        ]
    ] ;

    # --- Achse 4: Form ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:FormAxis ;
        sms:hasStateValue sms:form.Granulate
    ] ;

    # --- Achse 5: Grade ---
    sms:hasStateAssignment [
        a sms:StateAssignment ;
        sms:onAxis sms:GradeAxis ;
        sms:hasStateValue sms:grade.Automotive
    ] .


# ═══════════════════════════════════════════════════════════════════════
#   2. DIE PROZESSKETTE
# ═══════════════════════════════════════════════════════════════════════

# --- Recycling (erzeugt das Material) ---

:recycling_run_17 a sdata:RecyclingProcess ;
    sdata:hasIdentifier "REC-2026-017" ;
    sdata:hasInput :eol_bumpers ;
    sdata:hasOutput :pp_gf30_lot42 ;
    sdata:performedBy :recycler_gmbh ;
    sdata:producesData :recycling_data_17 ;
    sdata:hasStandard "ISO 15270" .

:eol_bumpers a sdata:Recyclate ;
    sdata:hasIdentifier "EOL-BUMP-2026-003" ;
    rdfs:label "End-of-Life Stoßfänger"@de .

:recycler_gmbh a sdata:Organization ;
    sdata:hasIdentifier "DE-REC-001" ;
    rdfs:label "Recycler GmbH"@de .

:recycling_data_17 a sdata:ProcessData ;
    sdata:describes :pp_gf30_lot42 ;
    sdata:producedBy :recycling_run_17 ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "throughput" ;
        rdfs:label "Durchsatz"@de ;
        qudt:numericValue 250.0 ;
        sdata:unitSymbol "kg/h" ;
        sdata:dtype "float"
    ] .

# --- Spritzguss (erzeugt das Bauteil) ---

:injection_molding_08 a sdata:ManufacturingProcess ;
    sdata:hasIdentifier "INJ-2026-008" ;
    sdata:hasInput :pp_gf30_lot42 ;
    sdata:hasOutput :b_pillar_001 ;
    sdata:performedBy :press_engel ;
    sdata:usesTool :mold_bsaeule ;
    sdata:producesData :process_data_08 ;
    sdata:hasStandard "VDA 260" .

:press_engel a sdata:MachineAgent ;
    sdata:hasIdentifier "PRESS-ENGEL-DUO-2800" ;
    rdfs:label "Engel Duo 2800"@de .

:mold_bsaeule a sdata:Tool ;
    sdata:hasIdentifier "TOOL-BSAEULE-V2" ;
    rdfs:label "Spritzgusswerkzeug B-Säule v2"@de .

:process_data_08 a sdata:ProcessData ;
    sdata:describes :b_pillar_001 ;
    sdata:producedBy :injection_molding_08 ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "melt_temperature" ;
        rdfs:label "Massetemperatur"@de ;
        qudt:numericValue 260.0 ;
        sdata:unitSymbol "°C" ;
        sdata:dtype "float"
    ] ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "injection_pressure" ;
        rdfs:label "Einspritzdruck"@de ;
        qudt:numericValue 85.0 ;
        sdata:unitSymbol "MPa" ;
        sdata:dtype "float"
    ] ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "cycle_time" ;
        rdfs:label "Zykluszeit"@de ;
        qudt:numericValue 42.0 ;
        sdata:unitSymbol "s" ;
        sdata:dtype "float"
    ] .


# ═══════════════════════════════════════════════════════════════════════
#   3. DAS BAUTEIL — B-Säule
# ═══════════════════════════════════════════════════════════════════════

:b_pillar_001 a sdata:Component ;
    sdata:hasIdentifier "PART-BSAEULE-2026-001" ;
    rdfs:label "B-Säule PP-GF30"@de ;
    sdata:resultOf :injection_molding_08 ;
    sdata:hasPassport :passport_bpillar ;
    sdata:hasData :measurement_data_bpillar .


# ═══════════════════════════════════════════════════════════════════════
#   4. DIE PRÜFUNG — Materialcharakterisierung
# ═══════════════════════════════════════════════════════════════════════

:tensile_test_bp a sdata:MechanicalTest ;
    sdata:hasIdentifier "TEST-ZUG-2026-042" ;
    sdata:hasInput :specimen_bp ;
    sdata:performedBy :prueflabor ;
    sdata:performedBy :zwick_z010 ;
    sdata:producesData :measurement_data_bpillar ;
    sdata:hasStandard "DIN EN ISO 527-1" .

:specimen_bp a sdata:Specimen ;
    sdata:hasIdentifier "SPEC-BP-042" ;
    rdfs:label "Zugprobe aus B-Säule"@de .

:prueflabor a sdata:Organization ;
    sdata:hasIdentifier "LAB-QUAL-001" ;
    rdfs:label "Qualitätslabor Werk Süd"@de .

:zwick_z010 a sdata:MachineAgent ;
    sdata:hasIdentifier "ZWICK-Z010-003" .

:measurement_data_bpillar a sdata:MeasurementData ;
    sdata:describes :b_pillar_001 ;
    sdata:producedBy :tensile_test_bp ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "Rm" ;
        rdfs:label "Zugfestigkeit"@de ;
        qudt:numericValue 85.0 ;
        sdata:unitSymbol "MPa" ;
        qudt:unit <http://qudt.org/vocab/unit/MegaPA> ;
        sdata:dtype "float"
    ] ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "E_mod" ;
        rdfs:label "E-Modul"@de ;
        qudt:numericValue 7200.0 ;
        sdata:unitSymbol "MPa" ;
        qudt:unit <http://qudt.org/vocab/unit/MegaPA> ;
        sdata:dtype "float"
    ] ;
    sdata:hasQuantity [
        a sdata:AttributeQuantityValue ;
        sdata:name "epsilon_break" ;
        rdfs:label "Bruchdehnung"@de ;
        qudt:numericValue 3.2 ;
        sdata:unitSymbol "%" ;
        sdata:dtype "float"
    ] .


# ═══════════════════════════════════════════════════════════════════════
#   5. DER PRODUKTPASS — Aggregation aller Data
# ═══════════════════════════════════════════════════════════════════════

:passport_bpillar a sdata:Passport ;
    sdata:hasIdentifier "DPP-BSAEULE-2026-001" ;
    rdfs:label "Digitaler Produktpass B-Säule"@de ;
    sdata:describes :b_pillar_001 ;

    # Der Pass aggregiert alle Data über alle Activities:
    sdata:hasData :recycling_data_17 ;       # Recycling-Prozessdaten
    sdata:hasData :process_data_08 ;         # Spritzguss-Prozessdaten
    sdata:hasData :measurement_data_bpillar . # Prüfergebnisse

    # Der Material State Space des Werkstoffs ist über
    # :b_pillar_001 → sdata:hasData → sms:hasStateAssignment
    # erreichbar — der Pass muss die Achsen nicht duplizieren.
```

### Was der DPP-Graph enthält

```
                        :passport_bpillar (DPP)
                               │
                          describes
                               │
                        :b_pillar_001 (Component)
                         /         \
                   resultOf      hasData
                      /               \
     :injection_molding_08      :measurement_data_bpillar
            /    |    \                    |
      hasInput  perf.  produces     Rm=85MPa, E=7200MPa
          /      |        \
  :pp_gf30_lot42  :press   :process_data_08
       |                    (260°C, 85MPa, 42s)
  hasStateAssignment (×6)
       |
  ┌────┴───────────────────────────────────┐
  │  Origin:     recycled (70%, 3 Zyklen)  │
  │  Compliance: REACH + RoHS + ESPR + IATF│
  │  Composition: composite (PP + GF 30%)  │
  │  Condition:  degraded (62% FL-Ret.)    │
  │  Form:       granulate                 │
  │  Grade:      automotive                │
  └────────────────────────────────────────┘
```

### DPP-relevante SPARQL-Queries

**"Zeige alle DPP-pflichtigen Materialinformationen für die B-Säule":**

```sparql
SELECT ?axis ?value ?label ?detailName ?detailValue ?detailUnit
WHERE {
    :passport_bpillar sdata:describes ?component .
    ?component (sdata:hasData|^sdata:describes) ?material .
    ?material a sdata:Material .
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis ?axis .
    ?sa sms:hasStateValue ?value .
    ?value skos:prefLabel ?label .
    OPTIONAL {
        ?sa sdata:hasQuantity ?aqv .
        ?aqv sdata:name ?detailName .
        ?aqv qudt:numericValue ?detailValue .
        OPTIONAL { ?aqv sdata:unitSymbol ?detailUnit . }
    }
    FILTER(lang(?label) = "de")
}
ORDER BY ?axis
```

**"Finde alle Bauteile mit Recyclatanteil > 50% für den ESPR-Bericht":**

```sparql
SELECT ?component ?material ?recycledContent
WHERE {
    ?component a sdata:Component .
    ?component (sdata:hasData|^sdata:describes) ?material .
    ?material a sdata:Material .
    ?material sms:hasStateAssignment ?sa .
    ?sa sms:onAxis sms:OriginAxis .
    ?sa sms:hasStateValue sms:origin.Recycled .
    ?sa sdata:hasQuantity ?aqv .
    ?aqv sdata:name "recycled_content" .
    ?aqv qudt:numericValue ?recycledContent .
    FILTER(?recycledContent > 0.50)
}
```

**"Zeige die vollständige Prozesskette eines Bauteils":**

```sparql
SELECT ?step ?type ?input ?output
WHERE {
    :b_pillar_001 (sdata:resultOf|^sdata:hasOutput)+ ?step .
    ?step a ?type .
    ?type rdfs:subClassOf* sdata:Activity .
    OPTIONAL { ?step sdata:hasInput ?input . }
    OPTIONAL { ?step sdata:hasOutput ?output . }
}
```

### Mapping zu Catena-X Aspektmodellen

Die sdata-Achsen lassen sich auf Catena-X Aspektmodelle abbilden:

| Catena-X Aspektmodell | sdata-Entsprechung |
|-----------------------|-------------------|
| `MaterialForRecycling` | `sms:OriginAxis` + `sms:CompositionAxis` |
| `PartAsPlanned` / `PartAsBuilt` | `sdata:Component` + `sdata:Passport` |
| `PhysicalDimension` | `sdata:hasQuantity` am `sdata:Component` |
| `BatteryPass` | Eigene Achsen (`bat:ChemistryAxis`, `bat:SOHAxis`, ...) |
| `CarbonFootprint` | Eigene Achse (z.B. `cf:CarbonFootprintAxis`) |
| `EndOfLife` | `sms:LifecyclePhaseAxis` + `sdata:RecyclingProcess` |

Das sdata-System bildet nicht Catena-X 1:1 nach, sondern liefert den **semantischen Unterbau**, auf den Catena-X-Aspektmodelle abgebildet werden können. Die SKOS-Vokabulare sind dabei die gemeinsame Sprache.


## 9. Zusammenfassung der Operationen

| Was will ich? | Was brauche ich? | Zeilen Turtle |
|---------------|-----------------|---------------|
| Material beschreiben | 1 StateAssignment pro Achse | ~5 pro Achse |
| Neuen Wert hinzufügen | 1 skos:Concept + inScheme + prefLabel | 3–5 |
| Hierarchie aufbauen | skos:broader auf bestehendem Concept | +1 |
| Neue Achse definieren | 1 Subklasse + 1 ConceptScheme + n Concepts | ~10 + 3 pro Wert |
| Detailwerte anhängen | sdata:hasQuantity mit AQV am Assignment | ~6 pro AQV |
| Provenienz angeben | sdata:producedBy am Assignment | +1 |

Keine dieser Operationen erfordert eine Änderung am Core-Schema (`sdata-material-state.ttl`). Alles geschieht durch **neue Instanzen und Konzepte**.


## 10. Namenskonventionen

| Element | Muster | Beispiel |
|---------|--------|---------|
| Achsen-Klasse | `sms:XxxAxis` | `sms:OriginAxis` |
| ConceptScheme | `sms:xxx-values` | `sms:origin-values` |
| Concept | `sms:xxx.Wert` | `sms:origin.Recycled` |
| Benutzerdefinierte Achse | `ex:XxxAxis` | `ex:MoistureAxis` |
| Benutzerdefiniertes Scheme | `ex:xxx-values` | `ex:moisture-values` |
| Benutzerdefiniertes Concept | `ex:xxx.Wert` | `ex:moisture.Dry` |

Der Punkt `.` im Concept-Namen trennt Achse und Wert visuell: `origin.Recycled` liest sich als "auf der Origin-Achse, Wert Recycled".


## 11. Prefixes

Für die Arbeit mit dem Material State Space werden diese Prefixes benötigt:

```turtle
@prefix sdata:   <https://w3id.org/sdata/core/> .
@prefix sms:     <https://w3id.org/sdata/material-state/> .
@prefix min:     <https://w3id.org/min#> .
@prefix qudt:    <http://qudt.org/schema/qudt/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
```

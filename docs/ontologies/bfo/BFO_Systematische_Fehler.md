---
aliases:
  - |-
    BFO 
    Systematische Fehler
---
## BFO — Systematische Fehlerliste

### 1. Qualitäten als Entitäten (Reifikationsfehler)

Jede Eigenschaft wird zu einer eigenen Entität. Die Masse eines Coils ist nicht ein Zahlenwert am Coil — sie ist ein `Quality`-Individuum, das via `inheres_in` im Coil lebt, dessen Wert über IAO als `MeasurementDatum` mit `has_value_specification` und `has_measurement_unit_label` modelliert wird. Sechs Entitäten, vier Relationen für eine Zahl. Das verwechselt ontologische Vollständigkeit mit Nützlichkeit. Kein Ingenieur fragt "Was ist Masse ontologisch?" — er fragt "Was wiegt der Coil?"

### 2. Information ausgeschlossen

BFO schließt Information bewusst aus. Begründung: Information sei nicht universell, sondern menschengemacht. Deshalb brauchte man IAO (Information Artifact Ontology) als separate Ontologie. Ein Werkstoffdatenblatt ist aber genauso real wie der Stahl, den es beschreibt. Ein DPP existiert — es hat Speicherort, Eigentümer, Entstehungsgeschichte. Eine Grundontologie, die ein Drittel der Realität in eine Hilfsontologie auslagert, ist keine Grundontologie.

### 3. Continuant/Occurrent als falscher Dualismus

Die Grenze ist unscharf und perspektivisch, nicht substanziell. Ein Fluss: Continuant (es gibt den Rhein) oder Occurrent (Wasser fließt)? Ein Unternehmen: Continuant (die Firma existiert) oder Occurrent (sie produziert fortlaufend)? BFO sagt: Continuant. Aber das ist eine Entscheidung, keine Entdeckung. BFO behandelt eine perspektivische Unterscheidung als substantielle Unterscheidung.

### 4. Starre Klassenzugehörigkeit

In BFO ist Klassenzugehörigkeit permanent. Wenn etwas ein `MaterialEntity` ist, ist es immer eins. Aber ein Roboter, der eingeschaltet wird, gewinnt Agency. Ein Produkt am End-of-Life wird Recyclat. Ein Probekörper ist dasselbe physische Ding wie ein Serienteil — nur die Rolle ändert sich. BFO modelliert Rollenänderung über `Role` als dependent continuant — was die gesamte dynamische Semantik in eine abhängige Schicht verschiebt, die wieder reifiziert werden muss. BFO optimiert für Klassifikation, nicht für Transformation.

### 5. Adoption Tax (Schichtzwang)

Um BFO zu nutzen: BFO selbst (30+ Klassen), IAO für Information, OBI für Experimente, RO (Relation Ontology) für Relationen, dann die eigene Domain-Ontologie. Fünf Schichten, bevor man sagt: "Der Coil wiegt 12500 kg." Die meisten BFO-abgeleiteten Ontologien nutzen sowieso nur 5–10 BFO-Klassen und ignorieren den Rest.

### 6. Überdimensionierte Hierarchie

30+ Klassen vor der ersten Domänenaussage. `IndependentContinuant`, `ImmaterialEntity`, `SpatialRegion`, `ContinuantFiatBoundary`, `ProcessBoundary`, `SpatiotemporalRegion` — die meisten Domain-Ontologien nutzen davon nur `MaterialEntity`, `Process`, `Quality` und `Role`. Der Rest ist philosophischer Ballast, der importiert, aber nie instantiiert wird.

### 7. Rollen als Entitäten (zweiter Reifikationsfehler)

Rolle ist keine Seinsweise — Rolle ist Kontext. Dass ein Bauteil gerade Probekörper ist, ergibt sich daraus, dass es Input eines Experiments ist. BFO macht daraus eine eigene Entität der Klasse `Role`, die in einem `IndependentContinuant` via `bearer_of` inhäriert und via `realized_in` in einem Process realisiert wird. Drei Entitäten und zwei Relationen für eine Information, die im Graphmuster bereits steckt.

### 8. Dispositions als Entitäten (dritter Reifikationsfehler)

Dass Stahl unter Zugbelastung plastisch fließt, ist in BFO eine `Disposition`, die im Stahl `inheres_in` und in einem Umformprozess `realized_in` wird. Eine physikalische Eigenschaft wird zu einem latenten Individuum, das auf seine Realisierung wartet. Keine materialwissenschaftliche Anwendung modelliert so — Fließverhalten wird als Fließkurve (Datensatz) am Material gespeichert, nicht als metaphysische Potenz.

### 9. Keine Agency

BFO hat keinen Agent-Begriff. Handlungsfähigkeit wird über `Role` modelliert — ein Mensch hat die Rolle "researcher", die in einem Investigation-Prozess realisiert wird. Aber Agency ist keine Rolle — sie ist eine Seinsweise. Ein Roboter IST handlungsfähig, er HAT nicht eine Rolle namens "Handelnder". Latours Aktant-Begriff fehlt in BFO komplett.

### 10. Temporal Regions als eigene Klasse

BFO hat `TemporalRegion` mit Subklassen `ZeroDimensionalTemporalRegion` (Zeitpunkt) und `OneDimensionalTemporalRegion` (Zeitintervall). In der Praxis: `xsd:dateTime` und `xsd:duration`. BFO reifiziert Zeitstempel zu Entitäten mit eigener Ontologie.

### 11. Spatial Regions als eigene Klassen

`SpatialRegion` mit `ZeroDimensionalSpatialRegion` (Punkt), `OneDimensionalSpatialRegion` (Linie), `TwoDimensionalSpatialRegion` (Fläche), `ThreeDimensionalSpatialRegion` (Volumen). Vier Klassen für etwas, das in der Praxis als Koordinaten-Tuple oder GeoJSON-Polygon am Objekt hängt.

### 12. Fiat Boundaries

`ContinuantFiatBoundary` mit `FiatPoint`, `FiatLine`, `FiatSurface`. Das sind Grenzen, die nicht physisch existieren, sondern konventionell gesetzt sind — wie die Grenze zwischen Deutschland und Frankreich. Philosophisch interessant. Praktisch: kein Domain-Modell instantiiert `FiatSurface`.

### 13. Generically vs. Specifically Dependent Continuants

BFO unterscheidet `GenericallyDependentContinuant` (z.B. eine Information, die auf verschiedenen Trägern existieren kann) und `SpecificallyDependentContinuant` (z.B. die Farbe dieses einen Apfels). Die Unterscheidung ist philosophisch sauber, aber erzwingt bei jeder Eigenschaft die Entscheidung: ist diese Instanz generisch oder spezifisch abhängig? In der Praxis trifft niemand diese Entscheidung, und beide Klassen werden identisch behandelt.

### 14. Process Profiles

`ProcessProfile` — ein Aspekt eines Processes (z.B. der Temperaturverlauf während einer Wärmebehandlung). Reifiziert eine Messreihe zu einer Entität. In der Praxis: ein Datensatz mit Zeitstempeln und Werten. Kein Ingenieur sagt "Der Temperaturverlauf ist ein ProcessProfile, das ein Occurrent-Part des Processes ist" — er sagt "Hier ist die Temperaturkurve."

### 15. Keine Komposition auf Relationsebene

BFO definiert kaum eigene Relationen. Die meisten kommen aus RO (Relation Ontology), die wiederum separat importiert werden muss. `part_of`, `has_part`, `participates_in`, `has_participant` — alles extern. Eine Grundontologie ohne eigene Relationen ist ein Klassifikationsschema, keine Ontologie.

### 16. Object Aggregate vs. Object

BFO unterscheidet `Object` (ein zusammenhängendes Ding) und `ObjectAggregate` (eine Menge von Objekten). Ein Coil-Lager: `ObjectAggregate`. Ein einzelner Coil: `Object`. Was ist eine Baugruppe? Ein `Object` (fest verbunden) oder ein `ObjectAggregate` (aus Teilen bestehend)? Die Grenze ist materialabhängig, prozessabhängig und perspektivabhängig — also genau die Art von Unterscheidung, die eine Grundontologie nicht erzwingen sollte.

### 17. Immaterial Entities als Continuants

`ImmaterialEntity` umfasst `Site` (ein Ort, z.B. das Innere einer Flasche) und `SpatialRegion`. In BFO sind das Continuants — sie dauern fort. Aber ein Ort existiert nicht unabhängig — er ist eine Perspektive auf ein Object. "Das Innere der Flasche" ist kein Ding, es ist eine räumliche Beschreibung der Flasche. BFO substantiviert eine Präposition.

### 18. History

BFO 2020 führt `History` ein — die Summe aller Processes, die einem Continuant widerfahren. In der Praxis: ein SPARQL-Query über alle Processes, die `has_participant` auf dieses Object haben. BFO reifiziert eine Query zu einer Entität.

### 19. Keine native Unterstützung für Lebenszyklen

Kreislaufwirtschaft, Produktpässe, End-of-Life — BFO hat kein Muster dafür. Material wird gewonnen, verarbeitet, genutzt, recycelt. In BFO ist jeder dieser Schritte ein `Process`, der ein `MaterialEntity` als `participant` hat. Aber die Verkettung, die Zustandsänderung des Materials, die Rollenänderung des Produkts — das muss alles in der Domain-Ontologie gebaut werden. BFO liefert die Bausteine, aber nicht das Muster.

### 20. Philosophischer Realismus als Dogma

BFO behauptet, ontologischen Realismus abzubilden — die Welt, wie sie ist. Aber die Entscheidung, Qualitäten als Entitäten zu modellieren, ist keine Entdeckung über die Welt. Sie ist eine Modellierungsentscheidung. BFO verwechselt sein Modell mit der Realität und immunisiert sich dadurch gegen pragmatische Kritik: "Das IST so" statt "Das ist nützlich so zu modellieren."

---

**Zusammenfassung:** BFOs Grundfehler ist systematische Reifikation — jedes Konzept wird zu einer Entität, jede Unterscheidung zu einer Klasse, jede Perspektive zu einem Individuum. Das erzeugt philosophische Vollständigkeit auf Kosten praktischer Brauchbarkeit. 20 von 30+ BFO-Klassen werden in typischen Domain-Ontologien nie instantiiert.
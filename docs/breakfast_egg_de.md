# Frühstücksei (DE)

Diese Seite zeigt ein kleines, durchgaengiges Modell fuer ein "Fruehstuecksei"
als Beispiel fuer Produkt, Prozess, Daten und Nachweis.

## Ziel

- Einfaches End-to-End Beispiel fuer `sdata:Product`, `sdata:Process`,
  `sdata:Data` und `sdata:Result`.
- Nachvollziehbarkeit: Welcher Prozess fuehrte zu welchem Ergebnis?
- Uebertragbar auf groessere DPP-/Digital-Twin-Szenarien.

## Kompaktes Turtle-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/breakfast/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

ex:egg_001 a sdata:Product ;
  sdata:label "Breakfast Egg #001" .

ex:boiling_001 a sdata:Process ;
  sdata:label "Boiling" ;
  sdata:hasInput ex:egg_001 ;
  sdata:startedAt "2026-03-08T07:00:00Z"^^xsd:dateTime .

ex:egg_state_001 a sdata:Result ;
  sdata:label "Soft-boiled" ;
  sdata:generatedBy ex:boiling_001 .

ex:temp_data_001 a sdata:Data ;
  sdata:label "Water temperature log" ;
  sdata:generatedBy ex:boiling_001 .
```

## Interpretation

- `ex:egg_001` ist das betrachtete Produkt.
- `ex:boiling_001` modelliert den Prozessschritt.
- `ex:temp_data_001` ist ein Datensatz aus dem Prozess.
- `ex:egg_state_001` ist das Ergebnis des Prozessschritts.

Siehe auch die [English version](breakfast_egg_en.md).

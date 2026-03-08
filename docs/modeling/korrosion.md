# Korrosion

Gute Frage: Ist Korrosion in MIN eher Process, Boundary oder Agent?

Kurze Antwort: **primaer Process, mit Agent-Ueberlappung; die Korrosionszone separat als Boundary.**

## Einordnung mit MIN-Kriterien

### 1. Process-Test

Transformiert es Inputs zu Outputs?
Ja. Metall + O2/H2O -> Oxid/Rost + veraenderte Mikrostruktur.
Korrosion geschieht ueber Zeit, hat Input/Output und kann Messdaten erzeugen.

### 2. Boundary-Test

Entferne einen Partner. Existiert es noch?

- Ohne korrosives Medium: keine Korrosion.
- Ohne Metall: keine Korrosion.

Das klingt relational. Trotzdem ist Korrosion selbst kein statisches Zwischenphaenomen,
sondern ein zeitlicher Transformationsvorgang.

### 3. Agent-Test

Selektiv, zurechenbar, kausal wirksam?
Ja. Korrosion greift selektiv an (z. B. Korngrenzen, Spannungsrisse) und ist kausal zurechenbar.

## Empfohlenes Modellierungsmuster

- Korrosion als Vorgang: `min:Process` und optional zusaetzlich `min:Agent`.
- Korrosionszone (Kontakt Metall/Medium): `min:Boundary`.
- Verbindung zwischen beiden ueber eine explizite Relation, z. B. `min:hasBoundary`.

```turtle
ex:korrosion_001 a min:Process , min:Agent ;
    min:hasInput ex:blech_042 ;
    min:hasOutput ex:blech_042_korrodiert ;
    min:generates ex:messdaten_korrosion .

ex:korrosionszone_001 a min:Boundary ;
    min:bounds ex:blech_042 , ex:medium_salzwasser .

ex:korrosion_001 min:hasBoundary ex:korrosionszone_001 .
```

## Merksatz

Die Korrosionszone besteht (Boundary), die Korrosion geschieht (Process) und wirkt selektiv (Agent).

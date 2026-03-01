# sdata-lifecycle.ttl

Lifecycle-Modul für Prozessketten auf Basis der Verb-Klassen.

Wesentliche Relationen:

- `slc:typicallyFollowedBy` (Schema-Level zwischen Verb-Klassen)
- `sdata:precedes` / `sdata:follows` (Instanz-Level zwischen Prozessen)
- `sdata:observes` (Beobachtungsprozess zu Zielprozess)

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Probenfertigung_A1
  a sdata:Process , sdata:Creation ;
  sdata:hasOutput ex:Probe_A1 .

ex:Zugversuch_A1
  a sdata:Process , sdata:Observation ;
  sdata:hasInput ex:Probe_A1 ;
  sdata:producesData ex:Messdaten_A1 ;
  sdata:follows ex:Probenfertigung_A1 .

ex:ReportTransfer_A1
  a sdata:Process , sdata:Transfer ;
  sdata:hasInput ex:Messdaten_A1 ;
  sdata:follows ex:Zugversuch_A1 .
```

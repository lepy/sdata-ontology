# sdata-lifecycle.ttl

Erweitert um Lebenszyklusfluss und Instanzverkettung (`sdata:precedes`, `sdata:follows`, `sdata:observes`).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Probenfertigung_A1
  a sdata:MaterialProcess , sdata:Creation ;
  sdata:generates ex:Probe_A1 .

ex:Zugversuch_A1
  a sdata:MaterialProcess , sdata:Observation ;
  sdata:consumes ex:Probe_A1 ;
  sdata:generates ex:Messdaten_A1 ;
  sdata:follows ex:Probenfertigung_A1 .

ex:BerichtsExport_A1
  a sdata:InformationProcess , sdata:Transfer ;
  sdata:consumes ex:Messdaten_A1 ;
  sdata:follows ex:Zugversuch_A1 .
```

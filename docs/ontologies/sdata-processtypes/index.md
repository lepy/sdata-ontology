# sdata-processtypes.ttl

Definiert die 7 Verb-Klassen:

- `Creation`
- `Transformation`
- `Transfer`
- `Observation`
- `Preservation`
- `Recovery`
- `Destruction`

Die Verb-Klassen sind orthogonal zu fachlichen Prozessklassen aus `sdata-core` und werden per Multi-Typing genutzt.

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Zugversuch_A1
  a sdata:MechanicalTest , sdata:Observation ;
  sdata:hasInput ex:Probe_A1 ;
  sdata:performedBy ex:Zwick_Z100 ;
  sdata:producesData ex:Messdaten_A1 .
```

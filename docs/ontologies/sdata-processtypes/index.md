# sdata-processtypes.ttl

Definiert die 7 Verb-Klassen:

- `Creation`
- `Transformation`
- `Transfer`
- `Observation`
- `Preservation`
- `Recovery`
- `Destruction`

Die Verb-Klassen sind orthogonal zur Core-Klasse `sdata:Process` und werden per Multi-Typing genutzt.

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Zugversuch_A1
  a sdata:Process , sdata:Observation ;
  sdata:hasInput ex:Probe_A1 ;
  sdata:performedBy ex:Zwick_Z100 ;
  sdata:producesData ex:Messdaten_A1 .
```

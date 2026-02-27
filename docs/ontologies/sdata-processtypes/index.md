# sdata-processtypes.ttl

Definiert die 7 Verb-Klassen (`Creation`, `Transformation`, `Transfer`, `Observation`, `Preservation`, `Recovery`, `Destruction`) orthogonal zu Material-/Informationsprozessen.

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

# Multi-Typing: MaterialProcess + Observation
ex:Zugversuch_A1
  a sdata:MaterialProcess , sdata:Observation ;
  sdata:name "Zugversuch Probe A1" ;
  sdata:consumes ex:Probe_A1 ;
  sdata:generates ex:Messdaten_A1 ;
  sdata:wasPerformedBy ex:Messmaschine_Z100 .
```

# sdata-r-strategies.ttl

SKOS-Schema für die 10R-Strategien mit Zuordnung zu Prozessverben über `sr:mapsToVerb`.

## Kurzbeispiel

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sr:    <https://w3id.org/sdata/r-strategies/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Datenaufbereitung_A1
  a min:Process , sdata:Recovery ;
  min:hasInput ex:AlteMessreihen ;
  min:hasOutput ex:Trainingsdatensatz_Rm ;
  min:generates ex:Aufbereitungsprotokoll_A1 .

sr:R8_Recycle sr:mapsToVerb sdata:Recovery .
```

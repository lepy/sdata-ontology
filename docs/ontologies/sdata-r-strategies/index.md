# sdata-r-strategies.ttl

SKOS-Schema für die 10R-Strategien mit Zuordnung zu Prozessverben über `sr:mapsToVerb`.

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sr:    <https://w3id.org/sdata/r-strategies/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:Datenaufbereitung_A1
  a sdata:Process , sdata:Recovery ;
  sdata:hasInput ex:AlteMessreihen ;
  sdata:hasOutput ex:Trainingsdatensatz_Rm ;
  sdata:producesData ex:Aufbereitungsprotokoll_A1 .

sr:R8_Recycle sr:mapsToVerb sdata:Recovery .
```

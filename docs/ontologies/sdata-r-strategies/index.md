# sdata-r-strategies.ttl

SKOS-Schema für 10R-Strategien und Zuordnung zu Prozessverben (`sr:mapsToVerb`).

## Zugversuch-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sr:    <https://w3id.org/sdata/r-strategies/> .
@prefix ex:    <https://example.org/zugversuch/> .

# Versuch zur Nachnutzung alter Messdaten -> R8 Recycle (Recovery)
ex:Datenaufbereitung_A1
  a sdata:InformationProcess , sdata:Recovery ;
  sdata:name "Feature-Extraktion aus Alt-Zugversuchen" ;
  sdata:processType "R8_Recycle" ;
  sdata:consumes ex:AlteMessreihen ;
  sdata:generates ex:Trainingsdatensatz_Rm .

sr:R8_Recycle sr:mapsToVerb sdata:Recovery .
```

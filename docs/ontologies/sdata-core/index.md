# sdata-core.ttl

Autarkes Kernmodell (`v0.11.0`) auf `MIN v2.0.0`.

## Umfang

- 10 Klassen
- 10 Objekt-Properties
- 7 Datentyp-Properties

## Klassenstruktur

- Objekt-Subklassen (`min:Object`):
  - `sdata:Material`, `sdata:Product`, `sdata:Hardware`, `sdata:Software`
- Datenklasse (`min:Data`):
  - `sdata:Data`
- Agent-Subklassen (`min:Agent`):
  - `sdata:Person`, `sdata:HardwareAgent`, `sdata:SoftwareAgent`, `sdata:Organization`, `sdata:EnvironmentAgent`

## Wichtigste Relationen

- MIN-Basisrelationen:
  - `min:hasInput`, `min:hasOutput`, `min:performedBy`, `min:generates`, `min:describes`
- sdata-Ergaenzungen:
  - `sdata:hasMaterial`, `sdata:usesTool`, `sdata:usesSoftware`, `sdata:hasData`
  - `sdata:producedBy`, `sdata:derivedFrom`, `sdata:certifies`
  - `sdata:succeeds`, `sdata:precedes`, `sdata:hasProduct`

## Modellierungsregeln

- Prozessinstanzen als `min:Process` modellieren.
- Prozessart nicht als Core-Subklasse modellieren.
: stattdessen `sms:MethodAxis`/`sms:DomainAxis` nutzen.
- Datenart (`Certificate`, `DigitalProductPass`, `TestReport` ...) ueber `sms:DataTypeAxis` modellieren.
- Umweltgetriebene, nicht-intentionale Kausalitaet ueber `sdata:EnvironmentAgent` modellieren.

## Kurzbeispiel

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DC04 a sdata:Material ;
  min:hasIdentifier "MAT-DC04-001" .

ex:Probe_A1 a sdata:Product ;
  min:hasIdentifier "PROD-SPEC-A1" ;
  sdata:hasMaterial ex:DC04 .

ex:Zwick_Z100 a sdata:Hardware, sdata:HardwareAgent ;
  min:hasIdentifier "HW-ZWICK-Z100" .

ex:Zugversuch_A1 a min:Process ;
  min:hasInput ex:Probe_A1 ;
  min:performedBy ex:Zwick_Z100 ;
  sdata:usesTool ex:Zwick_Z100 ;
  min:generates ex:Messdaten_A1 .

ex:Messdaten_A1 a sdata:Data ;
  min:describes ex:Probe_A1 ;
  sdata:producedBy ex:Zugversuch_A1 ;
  sdata:hasVersion "1.0.0" .
```

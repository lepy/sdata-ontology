# sdata-core.ttl

Autarkes Kernmodell (`v0.10.0`) auf MIN/OPA.

## Umfang

- 15 Klassen
- 19 Objekt-Properties
- 7 Datentyp-Properties

## Klassenstruktur

- `sdata:Object`
: `Material`, `Product`, `Hardware`, `Software`, `Data`
- `sdata:Process`
: keine Core-Subklassen; Typisierung ueber `sms:MethodAxis` und `sms:DomainAxis`
- `sdata:Agent`
: `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`, `EnvironmentAgent`

## Wichtigste Relationen

- Lifecycle:
  - `hasInput`, `hasOutput`, `undergoes`, `resultOf`
- Data-Provenance:
  - `producesData`, `producedBy`, `describes`, `hasData`, `hasDPP`
- Agency:
  - `performedBy`, `performs`, `certifiedBy`
- Infrastruktur:
  - `usesHardware`, `usesSoftware`
- Quantities:
  - `hasQuantity`, `hasValueDomain`

## Modellierungsregeln

- Prozessinstanzen immer als `sdata:Process` modellieren.
- Prozessart nicht mehr als Core-Subklasse modellieren.
: stattdessen `sms:MethodAxis`/`sms:DomainAxis` verwenden.
- Datenart (`Certificate`, `DigitalProductPass`, `TestReport` ...) über `sms:DataTypeAxis` modellieren.
- `MachineAgent` nicht mehr verwenden.
: verwende `HardwareAgent`.
- Umweltgetriebene, nicht-intentionale Kausalitaet ueber `EnvironmentAgent` modellieren.

## Kurzbeispiel (Zugversuch)

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DC04 a sdata:Material ;
  sdata:hasIdentifier "MAT-DC04-001" .

ex:Probe_A1 a sdata:Product ;
  sdata:hasIdentifier "PROD-SPEC-A1" ;
  sdata:madeOf ex:DC04 .

ex:Zwick_Z100 a sdata:Hardware, sdata:HardwareAgent ;
  sdata:hasIdentifier "HW-ZWICK-Z100" .

ex:Zugversuch_A1 a sdata:Process ;
  sdata:hasInput ex:Probe_A1 ;
  sdata:performedBy ex:Zwick_Z100 ;
  sdata:usesHardware ex:Zwick_Z100 ;
  sdata:producesData ex:Messdaten_A1 ;
  sdata:hasStandard "DIN EN ISO 6892-1" .

ex:Messdaten_A1 a sdata:Data ;
  sdata:describes ex:Probe_A1 ;
  sdata:producedBy ex:Zugversuch_A1 ;
  sdata:hasVersion "1.0.0" .
```

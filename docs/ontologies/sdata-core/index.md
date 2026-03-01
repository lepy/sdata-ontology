# sdata-core.ttl

Autarkes Kernmodell (`v0.8.0`) auf MIN/OPA mit:

- 30 Klassen
- 19 Objekt-Properties
- 8 Datentyp-Properties

Zentrale Kategorien:

- `sdata:Object` (u. a. `Material`, `Product`, `Hardware`, `Software`)
- `sdata:Process` (u. a. `ManufacturingProcess`, `MechanicalTest`, `Simulation`)
- `sdata:Data` (u. a. `Certificate`, `DigitalProductPass`)
- `sdata:Agent` (u. a. `Person`, `MachineAgent`, `SoftwareAgent`, `Organization`)

## Kurzbeispiel (Zugversuch)

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DC04 a sdata:Material ;
  sdata:hasIdentifier "MAT-DC04-001" .

ex:Probe_A1 a sdata:Product ;
  sdata:hasIdentifier "PROD-SPEC-A1" ;
  sdata:madeOf ex:DC04 .

ex:Zwick_Z100 a sdata:Hardware, sdata:MachineAgent ;
  sdata:hasIdentifier "HW-ZWICK-Z100" .

ex:Zugversuch_A1 a sdata:MechanicalTest ;
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

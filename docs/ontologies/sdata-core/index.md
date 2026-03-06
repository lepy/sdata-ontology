# sdata-core.ttl

Default-Kernmodell auf `MIN v3.4.0`.

## Profile

- `sdata-core.ttl` (`v0.14.0`, default)
- `sdata-core-v0.13.1.ttl` (legacy profile)

## Umfang (`v0.14.0`)

- 42 Klassen
- 24 eigene Objekt-Properties
- 19 eigene Datentyp-Properties
- 40 MIN-Fassaden (`owl:equivalentProperty`): 35 Objekt- + 5 Datentyp-Properties

## Struktur

- Nexus-Klassen: `Material`, `Product`, `Hardware`, `Software`, `Site`, `Specimen`, `Substance`, `Process`, `Data`, `Result`, `ProductPassport`, `DigitalTwin`, `Identifier`, `ResultFile`, `Proof`, `CryptographicKey`, `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`, `EnvironmentAgent`, `Boundary`
- Forma-Fassaden: `Law`, `Model`, `Scenario`, `Requirement`, `Specification`, `Regulation`, `LifecyclePhase`, `Certification`, `Accreditation`, `Registry`, `TrustFramework`
- Typus-Fassaden (v0.14): typisierbare Klassen statt tiefer Subklassierung

## Modellierungsleitlinien

- Verwende im Anwendungsgraphen bevorzugt `sdata:*`.
- Verwende `sdata:typifiedBy`, wenn kein neues strukturelles Axiom benoetigt wird.
- Nutze `sms:*` (State Space) fuer Methodik, Domain und DataType.
- Behalte MIN als importierte Architektur-Ontologie im Hintergrund.

## Migration

- `v0.10 -> v0.12`: OPA entfernt, MIN-basierte Kernkategorien.
- `v0.12 -> v0.13`: Forma-Fassaden und DPP/VC-Erweiterung.
- `v0.13.1 -> v0.14.0`: One-namespace-Ansatz (`sdata:*`-Fassaden fuer MIN) und Typus-Fassaden.

## Kurzbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:probe_42 a sdata:Specimen ;
  sdata:hasIdentifier "SPEC-42" ;
  sdata:hasMaterial ex:DC04_charge_7814 .

ex:zugversuch_001 a sdata:Process ;
  sdata:hasInput ex:probe_42 ;
  sdata:generates ex:result_zv001 .

ex:result_zv001 a sdata:Result ;
  sdata:generatedBy ex:zugversuch_001 ;
  sdata:describes ex:probe_42 .
```

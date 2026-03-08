# sdata-core.ttl

Default-Kernmodell auf `MIN v1.0.0`.

## Profile

- `sdata-core.ttl` (`v0.1.0`, default)

## Umfang (`v0.1.0`)

- 54 Klassen
- 31 eigene Objekt-Properties
- 19 eigene Datentyp-Properties
- 52 MIN-Fassaden: 45 Objekt- + 5 Datentyp- + 2 Annotation-Property-Fassaden

## Struktur

- Nexus-Klassen: `Material`, `Product`, `Hardware`, `Software`, `Site`, `Specimen`, `Substance`, `Process`, `Data`, `Result`, `ProductPassport`, `DigitalTwin`, `Identifier`, `ResultFile`, `Proof`, `CryptographicKey`, `Person`, `HardwareAgent`, `SoftwareAgent`, `Organization`, `EnvironmentAgent`, `Boundary`
- Forma-Fassaden: `Law`, `Model`, `Scenario`, `Requirement`, `Specification`, `Regulation`, `LifecyclePhase`, `Certification`, `Accreditation`, `Registry`, `TrustFramework`
- Typus-Fassaden: typisierbare Klassen statt tiefer Subklassierung

## Klassenreferenz

- [sdata-core Class Reference](classes/index.md)
- Die Seiten unter `classes/` werden aus `sdata-core.ttl` generiert.
- Generieren mit: `make docs-sdata-classes`

## Modellierungsleitlinien

- Verwende im Anwendungsgraphen bevorzugt `sdata:*`.
- Verwende `sdata:typifiedBy`, wenn kein neues strukturelles Axiom benoetigt wird.
- Nutze `sms:*` (State Space) fuer Methodik, Domain und DataType.
- Behalte MIN als importierte Architektur-Ontologie im Hintergrund.

## Migration

- Historische Migrationen liegen unter `docs/ontologies/MIGRATION-*.md`.

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

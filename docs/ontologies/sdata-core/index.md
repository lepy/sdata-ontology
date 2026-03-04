# sdata-core.ttl

Kernmodell auf `MIN v3.2.0` in zwei Profilen:

- `sdata-core.ttl` (`v0.12.0`, lean profile)
- `sdata-core-v0.13.0.ttl` (extended profile mit Forma-Fassaden)

## Umfang

- `v0.12.0`: 11 Klassen, 10 Objekt-Properties, 7 Datentyp-Properties
- `v0.13.0`: 33 Klassen, 15 Objekt-Properties, 12 Datentyp-Properties

## Klassenstruktur

- Nexus-Subklassen (`v0.12` und `v0.13`):
  - `sdata:Material`, `sdata:Product`, `sdata:Hardware`, `sdata:Software`
  - (`v0.13` zusaetzlich) `sdata:Boundary`, `sdata:Database`
- Prozessklasse (`min:Process`):
  - `sdata:Process`
- Datenklasse (`min:Data`):
  - `sdata:Data`
  - (`v0.13` zusaetzlich) `sdata:Identifier`, `sdata:Result`, `sdata:ResultFile`,
    `sdata:ProductPassport`, `sdata:DigitalTwin`,
    `sdata:VerifiableCredential`, `sdata:VerifiablePresentation`,
    `sdata:Proof`, `sdata:CryptographicKey`
- Agent-Subklassen (`min:Agent`):
  - `sdata:Person`, `sdata:HardwareAgent`, `sdata:SoftwareAgent`, `sdata:Organization`, `sdata:EnvironmentAgent`
- Forma-Fassaden (`nur v0.13`):
  - `sdata:Law`, `sdata:Model`, `sdata:Scenario`
  - `sdata:Requirement`, `sdata:Specification`, `sdata:Regulation`, `sdata:LifecyclePhase`
  - `sdata:Certification`, `sdata:Accreditation`, `sdata:Registry`, `sdata:TrustFramework`

## Wichtigste Relationen

- MIN-Basisrelationen:
  - `min:hasInput`, `min:hasOutput`, `min:performedBy`, `min:generates`, `min:describes`
- sdata-Ergaenzungen:
  - `sdata:hasMaterial`, `sdata:usesTool`, `sdata:usesSoftware`, `sdata:hasData`
  - `sdata:producedBy`, `sdata:derivedFrom`, `sdata:certifies`
  - `sdata:succeeds`, `sdata:precedes`, `sdata:hasProduct`
  - (`v0.13` zusaetzlich) `sdata:specifies`, `sdata:certifiedUnder`,
    `sdata:identifiedBy`, `sdata:hasIssuer`, `sdata:signedBy`

## Schnelle Migration

`v0.10 -> v0.12`:
- `sdata:hasInput` -> `min:hasInput`
- `sdata:hasOutput` -> `min:hasOutput`
- `sdata:performedBy` -> `min:performedBy`
- `sdata:producesData` -> `min:generates`
- `sdata:describes` -> `min:describes`
- `sdata:hasIdentifier` -> `min:hasIdentifier`

`v0.12 -> v0.13`:
- Optional auf `sdata-core-v0.13.0.ttl` wechseln, wenn Forma-Fassaden oder VC/DPP-Data-Typen gebraucht werden.
- Bestehende `v0.12`-Daten bleiben gueltig.

## Modellierungsregeln

- Prozessinstanzen als `sdata:Process` modellieren.
- Prozessart nicht als Core-Subklasse modellieren.
: stattdessen `sms:MethodAxis`/`sms:DomainAxis` nutzen.
- Datenart (`Certificate`, `DigitalProductPass`, `TestReport` ...) ueber `sms:DataTypeAxis` modellieren.
- Umweltgetriebene, nicht-intentionale Kausalitaet ueber `sdata:EnvironmentAgent` modellieren.
- Forma-Inhalte als Forma modellieren (`min:*` oder `sdata-core-v0.13`-Fassaden), nicht als reine `Data`.

## Kurzbeispiel

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/zugversuch/> .

ex:DC04 a sdata:Material ;
  min:hasIdentifier "MAT-DC04-001" .

ex:Probe_A1 a sdata:Product ;
  min:hasIdentifier "PROD-SPEC-A1" ;
  sdata:hasMaterial ex:DC04 .

ex:Zwick_Z100 a sdata:Hardware, sdata:HardwareAgent ;
  min:hasIdentifier "HW-ZWICK-Z100" .

ex:Zugversuch_A1 a sdata:Process ;
  min:hasInput ex:Probe_A1 ;
  min:performedBy ex:Zwick_Z100 ;
  sdata:usesTool ex:Zwick_Z100 ;
  min:generates ex:Messdaten_A1 .

ex:Messdaten_A1 a sdata:Data ;
  min:describes ex:Probe_A1 ;
  sdata:producedBy ex:Zugversuch_A1 ;
  sdata:hasVersion "1.0.0" .
```

# Modeling Cheat Sheet

Kompakte Referenz fuer die Modellierung mit `MIN v3.7`.
Core-Profile:
- `sdata-core.ttl` (`v0.15.0`, default)
- `sdata-core-v0.13.1.ttl` (legacy extended profile)

## Klassenwahl

- `min:Object`: physische oder digitale Objekte auf Basisebene
- `min:Process`: top-level Prozesskategorie
- `min:Data`: Daten als erstklassige Kategorie
- `min:Agent`: handelnde Entitaeten

sdata-Spezialisierungen:

- Objekte: `sdata:Material`, `sdata:Product`, `sdata:Hardware`, `sdata:Software`
- Prozesse: `sdata:Process` (subClassOf `min:Process`)
- Daten: `sdata:Data`
- Agenten: `sdata:Person`, `sdata:HardwareAgent`, `sdata:SoftwareAgent`, `sdata:Organization`, `sdata:EnvironmentAgent`

`sdata-core` (`v0.15.0`) enthaelt u. a.:

- Forma-Fassaden: `sdata:Law`, `sdata:Model`, `sdata:Scenario`, `sdata:Requirement`, `sdata:Specification`, `sdata:Regulation`, `sdata:Certification`
- Weitere Data-/Boundary-Typen: `sdata:Identifier`, `sdata:Result`, `sdata:ProductPassport`, `sdata:Boundary`
- Dezentrale DPP-Typen: `sdata:Site`, `sdata:Registry`, `sdata:TrustFramework`
- One-namespace-Fassaden fuer MIN-Relationen (`sdata:hasInput`, `sdata:generates`, `sdata:describes`, ...)
- Typus-Fassaden (`sdata:typifiedBy`) fuer typisierbare Nexus-Kategorien

## Relationen: MIN vs sdata

Nimm **MIN** fuer generische Struktur:

- `min:hasInput`, `min:hasOutput`
- `min:performedBy`, `min:performs`
- `min:generates`, `min:generatedBy`
- `min:describes`, `min:describedBy`
- `min:hasIdentifier`, `min:hasName`, `min:hasTimestamp`

Nimm **sdata** fuer domaenenspezifische Semantik:

- `sdata:hasMaterial` (Object -> Material)
- `sdata:usesTool`, `sdata:usesSoftware` (Process -> Infrastruktur)
- `sdata:hasData` (Nexus -> Data)
- `sdata:producedBy` (Data -> Process)
- `sdata:certifies` (Data -> Nexus)
- `sdata:succeeds` / `sdata:precedes` (Prozesskette)

## Empfohlenes Muster

```text
Object + Data -> Process -> Object + Data
                  ^
               Agent(s)
```

## State Space (sms)

Nutze `sms:hasStateAssignment` fuer fachliche Typisierung statt Core-Subklassen:

- Prozessmethodik: `sms:MethodAxis`
- Fachdomaene: `sms:DomainAxis`
- Datentyp: `sms:DataTypeAxis`
- Material-/Produktzustand: weitere Achsen (`OriginAxis`, `ConditionAxis`, ...)

## FORMA in MIN v3 (verfuegbar in sdata v0.15)

Wenn dein Fall Gesetze, Modelle, Anforderungen oder Institutionen braucht:

- Klassen: `min:Lex`, `min:Structura`, `min:Possibile`, `min:Norma`, `min:Institutio`
- Bruecken: `min:realizes`, `min:governs`, `min:formalizes`, `min:evaluates`, `min:encodes`

Mit `sdata-core` (`v0.15.0`) kannst du statt `min:*` die sdata-Fassaden nutzen
(z. B. `sdata:Law`, `sdata:Requirement`, `sdata:Certification`).

## Haeufige Fehler

- Prozesse nur als `sdata:Process` typisieren, wenn du im sdata-Kontext arbeitest
- `sdata:hasInput`/`sdata:hasOutput` verwenden statt `min:hasInput`/`min:hasOutput`
- `sdata:hasIdentifier` verwenden statt `min:hasIdentifier`
- `sdata:Data` implizit als `min:Object` behandeln (ist falsch seit v0.11)
- `min:Norma`/`sdata:Requirement` als `min:Data` modellieren (nutze `min:encodes` statt Gleichsetzung)

## Mini-Template

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/x/> .

ex:input a sdata:Material ; min:hasIdentifier "MAT-1" .
ex:proc  a sdata:Process ;
  min:hasInput ex:input ;
  min:generates ex:data .
ex:data  a sdata:Data ; min:describes ex:input ; sdata:producedBy ex:proc .
```

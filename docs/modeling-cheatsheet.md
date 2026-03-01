# Modeling Cheat Sheet

Kompakte Referenz fuer die Modellierung mit `MIN v2 + sdata-core v0.11.0`.

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

## Haeufige Fehler

- `sdata:Process` vergessen und nur `min:Process` im sdata-Modell verwenden
- `sdata:hasInput`/`sdata:hasOutput` verwenden statt `min:hasInput`/`min:hasOutput`
- `sdata:hasIdentifier` verwenden statt `min:hasIdentifier`
- `sdata:Data` implizit als `min:Object` behandeln (ist falsch seit v0.11)

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

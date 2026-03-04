# Migration Guide: sdata-core v0.12.0 -> v0.13.0

`sdata-core-v0.13.0.ttl` erweitert den Core auf `MIN v3.2.0` mit einer
vollstaendigen sdata-Fassade fuer Nexus und Forma.

## Kurzfassung

- `v0.12` bleibt als lean Profil in `sdata-core.ttl`.
- `v0.13` ist als versionierte Datei verfuegbar: `sdata-core-v0.13.0.ttl`.
- Bestehende `v0.12`-Instanzdaten bleiben gueltig.
- Neue Modellierung ist optional und additiv.

## Was ist neu in v0.13

### 1. Mehr Klassen

- `v0.12`: 11 Klassen
- `v0.13`: 33 Klassen

Neue Bereiche:
- Nexus-Ergaenzungen: `sdata:Boundary`, `sdata:Database`
- Data-Typen: `sdata:Identifier`, `sdata:Result`, `sdata:ResultFile`,
  `sdata:ProductPassport`, `sdata:DigitalTwin`, `sdata:VerifiableCredential`,
  `sdata:VerifiablePresentation`, `sdata:Proof`, `sdata:CryptographicKey`
- Forma-Fassaden: `sdata:Law`, `sdata:Model`, `sdata:Scenario`,
  `sdata:Requirement`, `sdata:Specification`, `sdata:Regulation`,
  `sdata:LifecyclePhase`, `sdata:Certification`, `sdata:Accreditation`,
  `sdata:Registry`, `sdata:TrustFramework`

### 2. Mehr Relationen

Neue Object Properties:
- `sdata:specifies` (`subPropertyOf min:evaluates`)
- `sdata:certifiedUnder` (`subPropertyOf min:realizes`)
- `sdata:identifiedBy` (`Entity -> Identifier`)
- `sdata:hasIssuer` (`Identifier -> Agent`)
- `sdata:signedBy` (`Data -> Agent`)

Neue Datatype Properties:
- `sdata:hasEndpoint` (`xsd:anyURI`)
- `sdata:hasScheme` (`xsd:string`)
- `sdata:hasValue` (`xsd:string`)
- `sdata:hasFormat` (`xsd:string`, MIME)
- `sdata:hasChecksum` (`xsd:string`, z. B. SHA-256)

### 3. Forma explizit modellieren

Mit `v0.13` koennen normative und formale Inhalte als eigene Entitaeten
modelliert werden, statt sie nur als `Data` zu behandeln.

Beispiel:

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/x/> .

ex:Req_340MPa a sdata:Requirement ;
  min:hasIdentifier "REQ-340-MPA" .

ex:Part_42 a sdata:Product ;
  min:realizes ex:Req_340MPa .

ex:Report_42 a sdata:Result ;
  min:encodes ex:Req_340MPa .
```

## Migrationsschritte

1. Import umstellen (falls gewuenscht):
   - von `sdata-core.ttl` (v0.12) auf `sdata-core-v0.13.0.ttl`
2. Bestehende Daten unveraendert weiter nutzen.
3. Neue Klassen nur dort einfuehren, wo sie Mehrwert bringen:
   - VC/DPP/Identifier-Flows
   - Anforderungen/Normen/Zertifizierungen
4. SHACL-Set bei Bedarf erweitern (`shapes/sdata-core-shapes.ttl` deckt aktuell v0.12-Basisregeln).

## Entscheidungshilfe

- Nutze `v0.12`, wenn du ein kleines, stabiles Kernprofil willst.
- Nutze `v0.13`, wenn du Forma, Boundary oder VC/DPP-spezifische Semantik brauchst.

# Migration Guide: sdata-core v0.13.0 -> v0.13.1

`sdata-core-v0.13.1.ttl` ist ein additiver Patch auf `v0.13.0` mit Fokus auf
dezentrale, zyklusuebergreifende DPP-Fluesse.

## Zielbild

Vier Luecken werden geschlossen:

1. Custody-Verlauf (wer ist verantwortlicher Verwahrer).
2. Registry-Bindung von Identifikatoren.
3. DPP- und VC-Supersession als explizite Versionskette.
4. Gueltigkeit und Revocation von Datenartefakten.

## Delta v0.13.1

## Neue Klassen (2)

- `sdata:Site` (`subClassOf min:Object`)
- `sdata:AssessmentResult` (`subClassOf sdata:Result`)

## Neue Object Properties (6)

- `sdata:locatedAt` (`min:Nexus -> sdata:Site`)
- `sdata:hasCustodian` (`min:Nexus -> min:Agent`)
- `sdata:registeredIn` (`sdata:Identifier -> sdata:Registry`)
- `sdata:supersedes` (`sdata:Data -> sdata:Data`)
- `sdata:supersededBy` (inverse zu `sdata:supersedes`)
- `sdata:assessesRequirement` (`sdata:AssessmentResult -> sdata:Requirement`)

## Neue Datatype Properties (4)

- `sdata:validFrom` (`xsd:dateTime`)
- `sdata:validUntil` (`xsd:dateTime`)
- `sdata:revokedAt` (`xsd:dateTime`)
- `sdata:assessmentOutcome` (`pass|fail|inconclusive`)

## Cardinality-Impact

- Klassen: `33 -> 35`
- Object Properties: `15 -> 21`
- Datatype Properties: `12 -> 16`

## Was du aendern musst

1. Import auf `sdata-core-v0.13.1.ttl` umstellen (wenn du die neuen Features brauchst).
2. Bestehende Daten koennen unveraendert bleiben.
3. Optional neue Muster aktivieren:
   - Custody:
     - `:dpp_001 sdata:hasCustodian :oem_ag .`
   - Registry-Bindung:
     - `:did_dpp_001 sdata:registeredIn :catena_registry .`
   - Supersession:
     - `:dpp_002 sdata:supersedes :dpp_001 .`
   - Gueltigkeit:
     - `:dpp_002 sdata:validFrom \"2026-03-04T00:00:00\"^^xsd:dateTime .`

## Mini-Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:    <https://example.org/dpp/> .

ex:did_dpp_001 a sdata:Identifier ;
  sdata:hasScheme "W3C:DID" ;
  sdata:hasValue "did:web:dpp.example.com:001" ;
  sdata:registeredIn ex:catena_registry .

ex:dpp_001 a sdata:ProductPassport ;
  sdata:identifiedBy ex:did_dpp_001 ;
  sdata:validUntil "2026-03-31T23:59:59"^^xsd:dateTime .

ex:dpp_002 a sdata:ProductPassport ;
  sdata:supersedes ex:dpp_001 ;
  sdata:validFrom "2026-04-01T00:00:00"^^xsd:dateTime .
```

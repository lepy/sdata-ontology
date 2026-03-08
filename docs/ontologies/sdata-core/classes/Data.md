# sdata:Data
## IRI
`https://w3id.org/sdata/core/Data`
## Labels
- `Data`
- `Daten`
## Direct Superclasses
- `min:Data`
## Direct Subclasses
- [`sdata:BillOfMaterials`](./BillOfMaterials.md)
- [`sdata:CryptographicKey`](./CryptographicKey.md)
- [`sdata:Identifier`](./Identifier.md)
- [`sdata:ProductPassport`](./ProductPassport.md)
- [`sdata:Proof`](./Proof.md)
- [`sdata:Result`](./Result.md)
- [`sdata:Software`](./Software.md)
- [`sdata:VerifiableCredential`](./VerifiableCredential.md)
- [`sdata:VerifiablePresentation`](./VerifiablePresentation.md)
## Comment
Domänenspezifische Daten. Wirkt nur über Agent.
    Persistierungsformat über sdata:typifiedBy → DataFormat.
    Dokumente, Dateien, Inputdecks — alles Data.

## Examples
- `Messdaten, Werkstoffdatenblatt, CAD-Modell, LS-DYNA Inputdeck.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# LS-DYNA Inputdeck als passive Datei.
ex:inputdeck_crash a sdata:Data ;
    sdata:hasName "Crashsimulation Inputdeck" ;
    sdata:encodes ex:fe_modell_crash ;
    sdata:typifiedBy ex:keyword_format .
ex:fe_modell_crash a sdata:Model .
ex:keyword_format a sdata:DataFormat ;
    sdata:hasName "LS-DYNA Keyword" .
```
## Used As Domain
- `sdata:certifies`
- `sdata:hasChecksum`
- `sdata:hasConfidence`
- `sdata:hasSource`
- `sdata:producedBy`
- `sdata:revokedAt`
- `sdata:signedBy`
- `sdata:supersededBy`
- `sdata:supersedes`
- `sdata:validFrom`
- `sdata:validUntil`
## Used As Range
- `sdata:hasData`
- `sdata:supersededBy`
- `sdata:supersedes`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Data .
```

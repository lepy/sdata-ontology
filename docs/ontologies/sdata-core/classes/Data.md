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
- [`sdata:DigitalTwin`](./DigitalTwin.md)
- [`sdata:Identifier`](./Identifier.md)
- [`sdata:ProductPassport`](./ProductPassport.md)
- [`sdata:Proof`](./Proof.md)
- [`sdata:Result`](./Result.md)
- [`sdata:ResultFile`](./ResultFile.md)
- [`sdata:SoftwareAgent`](./SoftwareAgent.md)
- [`sdata:VerifiableCredential`](./VerifiableCredential.md)
- [`sdata:VerifiablePresentation`](./VerifiablePresentation.md)
## Comment
Domänenspezifische Daten. Data sdata:encodes Forma.
    Kausalitätsmodus: mediated — wirkt nur über Agent.

## Examples
- `Messdaten, Werkstoffdatenblatt, CAD-Modell.`
## Industriebeispiel
- Messdaten aus Inline-Wanddickenmessung in der Rohrfertigung.
## Used As Domain
- `sdata:certifies`
- `sdata:hasChecksum`
- `sdata:hasConfidence`
- `sdata:hasFormat`
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

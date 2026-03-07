# sdata:ProductPassport
## IRI
`https://w3id.org/sdata/core/ProductPassport`
## Labels
- `Product Passport`
- `Produktpass`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Digitaler Produktpass (DPP). Die konkrete Datei ist
    min:Data (Nexus). Die Spezifikation (was enthalten sein muss)
    ist sdata:Regulation / sdata:Specification (Institutio).
    Verbindung via sdata:encodes (Data kodiert Institutio) und
    sdata:typifiedBy (Institutio bestimmt, als was die Datei zählt).
    Kann zugleich VerifiableCredential sein.
    Versionskette via sdata:supersedes.

## Examples
- `ESPR-DPP, Batterie-Pass, Textil-Pass, Stahl-DPP, EPD.`
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:ProductPassport .
```

# sdata:ProductPassport
## IRI
`https://w3id.org/sdata/core/ProductPassport`
## Labels
- `Product Passport`
- `Produktpass`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- [`sdata:DigitalProductPassport`](./DigitalProductPassport.md)
## Comment
Produktpass als Data-Artefakt. Allgemeine Klasse
    für alle Formen von Produktpässen — analog, digital,
    maschinenlesbar oder nicht. Die konkrete Datei ist
    min:Data (Nexus). Die Spezifikation (was enthalten sein muss)
    ist sdata:Regulation / sdata:Specification (Institutio).
    Verbindung via sdata:encodes (Data kodiert Institutio) und
    sdata:typifiedBy (Institutio bestimmt, als was die Datei zählt).
    Kann zugleich VerifiableCredential sein.
    Versionskette via sdata:supersedes.

## Examples
- `Materialzeugnis EN 10204, Batterie-Pass, EPD, Stahl-DPP.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Digital Product Passport eines Hochvolt-Kabels mit Material- und Compliance-Daten.
ex:product_passport_001 a sdata:ProductPassport ;
  sdata:hasIdentifier "PRODUCTPASSPORT-001" ;
  sdata:hasName "ProductPassport Datensatz" ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:generates ex:data_001 .
ex:product_001 a sdata:Product .
```
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

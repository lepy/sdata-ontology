# sdata:DataFormat
## IRI
`https://w3id.org/sdata/core/DataFormat`
## Labels
- `Data Format`
- `Datenformat`
## Direct Superclasses
- [`sdata:Typus`](./Typus.md)
## Direct Subclasses
- (none)
## Comment
Wesensbestimmung eines Dateiformats.

## Examples
- `STEP AP214, JT, VTU, CSV (RFC 4180), JSON-LD, Parquet.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Definition des Datenformats als OPC-UA-Export fuer Shopfloor-Integrationen.
ex:data_format_001 a sdata:DataFormat ;
  sdata:hasIdentifier "DATAFORMAT-001" ;
  sdata:hasName "DataFormat Klassifikation" ;
  sdata:typifies ex:data_001 .

ex:data_001 a sdata:Data .
```
## Used As Domain
- (none)
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:DataFormat .
```

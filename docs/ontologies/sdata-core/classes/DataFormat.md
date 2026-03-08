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
Wesensbestimmung eines Dateiformats. Ersetzt
    die ehemalige DP hasFormat und die Klasse ResultFile.

## Examples
- `STEP AP214, JT, VTU, CSV (RFC 4180), JSON-LD, Parquet, PDF.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# CSV-Format nach RFC 4180 als Datenformat.
ex:csv_rfc4180 a sdata:DataFormat ;
    sdata:hasName "CSV (RFC 4180)" ;
    sdata:typifies ex:resultfile_001 .
ex:resultfile_001 a sdata:Data .
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

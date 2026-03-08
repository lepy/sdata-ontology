# sdata:ResultFile
## IRI
`https://w3id.org/sdata/core/ResultFile`
## Labels
- `Ergebnisdatei`
- `Result File`
## Direct Superclasses
- [`sdata:Data`](./Data.md)
## Direct Subclasses
- (none)
## Comment
Physische Ergebnisdatei. Format, Größe, Pfad, Prüfsumme.

## Examples
- `test_001.csv, result.vtu, pruefbericht.pdf.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# PDF-Pruefprotokoll einer Wareneingangspruefung mit Signatur.
ex:result_file_001 a sdata:ResultFile ;
  min:hasIdentifier "RESULTFILE-001" ;
  min:hasName "ResultFile Datensatz" ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:generates ex:data_001 .
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

ex:example a sdata:ResultFile .
```

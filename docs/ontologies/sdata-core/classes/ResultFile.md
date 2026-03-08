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
## Industriebeispiel
- PDF-Pruefprotokoll einer Wareneingangspruefung mit Signatur.
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

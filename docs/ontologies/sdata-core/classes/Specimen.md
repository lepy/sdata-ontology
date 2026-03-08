# sdata:Specimen
## IRI
`https://w3id.org/sdata/core/Specimen`
## Labels
- `Probe`
- `Specimen`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Prüfkörper oder Probe. Weder Material noch Product.
    Provenienz via sdata:sampledFrom.

## Examples
- `Flachzugprobe (DIN 50125 Typ H), Rundprobe, Kerbschlagprobe.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix min:   <https://w3id.org/min#> .
@prefix ex:    <https://example.org/industry/> .

# Normprobe aus einer Kupfercharge fuer mechanische Pruefungen.
ex:specimen_001 a sdata:Specimen ;
  min:hasIdentifier "SPECIMEN-001" ;
  min:hasName "Specimen Instanz" ;
  min:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  min:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; min:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- `sdata:sampledFrom`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Specimen .
```

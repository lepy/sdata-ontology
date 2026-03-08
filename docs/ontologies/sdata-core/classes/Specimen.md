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
## Industriebeispiel
- Normprobe aus einer Kupfercharge fuer mechanische Pruefungen.
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

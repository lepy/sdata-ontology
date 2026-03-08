# sdata:Substance
## IRI
`https://w3id.org/sdata/core/Substance`
## Labels
- `Substance`
- `Substanz`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Chemischer Stoff im regulatorischen Sinne (REACH/RoHS/ESPR).
    Material ist werkstofftechnisch, Substance ist stofflich-regulatorisch.
    Dasselbe Blech HAT ein Material und ENTHÄLT Substances.

## Examples
- `Mangan (CAS 7439-96-5), Chrom-VI (SVHC), Blei (RoHS).`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Legierungselement Phosphor als enthaltene Substanz in einer Charge.
ex:substance_001 a sdata:Substance ;
  sdata:hasIdentifier "SUBSTANCE-001" ;
  sdata:hasName "Substance Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
```
## Used As Domain
- `sdata:hasCASNumber`
- `sdata:hasConcentration`
- `sdata:hasRegulatoryStatus`
## Used As Range
- `sdata:containsSubstance`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Substance .
```

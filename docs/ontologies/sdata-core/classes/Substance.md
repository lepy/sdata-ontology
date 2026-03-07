# sdata:Substance
## IRI
`https://w3id.org/sdata/core/Substance`
## Labels
- `Substance`
- `Substanz`
## Direct Superclasses
- `min:Object`
## Direct Subclasses
- (none)
## Comment
Chemischer Stoff im regulatorischen Sinne (REACH/RoHS/ESPR).
    Material ist werkstofftechnisch, Substance ist stofflich-regulatorisch.
    Dasselbe Blech HAT ein Material und ENTHÄLT Substances.

## Examples
- `Mangan (CAS 7439-96-5), Chrom-VI (SVHC), Blei (RoHS).`
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

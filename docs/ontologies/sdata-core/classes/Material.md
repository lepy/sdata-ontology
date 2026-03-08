# sdata:Material
## IRI
`https://w3id.org/sdata/core/Material`
## Labels
- `Material`
- `Werkstoff`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Werkstoff als Agent. Wirkt selektiv:
    DC04 verfestigt unter Zug, HC340LA widersteht
    höherer Last, AlSi10Mg leitet Wärme anders als CFK.
    Agent ∩ Object. Identität: material.

    Material = werkstofftechnisch (Gefüge, Zusammensetzung,
    Verarbeitungsgeschichte).
    Substance = stofflich-regulatorisch (CAS, REACH).
    Dasselbe Blech HAT ein Material und ENTHÄLT Substances.

    Klassifizierung: sdata:MaterialGrade.

## Examples
- `HC340LA, PP-GF30, AlSi10Mg, CFK-Prepreg, Recyclat.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# DC04-Werkstoff einer Charge mit Substanzen.
ex:DC04_charge_7814 a sdata:Material ;
    sdata:hasName "DC04 Charge 7814" ;
    sdata:typifiedBy ex:DC04 ;
    sdata:containsSubstance ex:mn_001 .
ex:DC04 a sdata:MaterialGrade ;
    sdata:hasName "DC04" .
ex:mn_001 a sdata:Substance ;
    sdata:hasName "Mangan" ;
    sdata:hasCASNumber "7439-96-5" .
```
## Used As Domain
- (none)
## Used As Range
- `sdata:hasMaterial`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Material .
```

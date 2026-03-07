# Materialtypisierung (Kupferlegierungen und Reinheiten)

Dieses Muster trennt klar zwischen Materialinstanz und Typisierung.

## Kernentscheidung

- Konkretes Materiallos: `sdata:Material`
- Typisierende Wesensbestimmung: `sdata:MaterialGrade`
- Stoffliche Zusammensetzung: `sdata:Substance`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:kathode_lot_001 a sdata:Material ;
    sdata:typifiedBy ex:cu_etp ;
    sdata:containsSubstance ex:cu_element ;
    sdata:containsSubstance ex:oxygen_trace .

ex:cu_etp a sdata:MaterialGrade ;
    sdata:typifies ex:kathode_lot_001 .

ex:cu_element a sdata:Substance ;
    sdata:hasCASNumber "7440-50-8" ;
    sdata:hasConcentration 99.92 .

ex:oxygen_trace a sdata:Substance ;
    sdata:hasCASNumber "7782-44-7" ;
    sdata:hasConcentration 0.04 .
```

## Minimal notwendige Relationen

- `sdata:typifiedBy` / `sdata:typifies`
- `sdata:containsSubstance`
- `sdata:hasCASNumber`
- `sdata:hasConcentration`


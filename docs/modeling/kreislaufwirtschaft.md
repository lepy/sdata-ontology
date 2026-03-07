# Kreislaufwirtschaft und Closed-Loop

Dieses Muster verbindet Rueckfuehrung, Demontage und Materialrueckgewinnung mit dem DPP.

## Kernentscheidung

- Ruecknahme-/Recyclingablauf: `sdata:Process`
- Rueckgefuehrtes Material: `sdata:Material`
- Produktstruktur/Nachweis: `sdata:BillOfMaterials`, `sdata:ProductPassport`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:product_001 a sdata:Product ;
    sdata:hasBOM ex:bom_001 .

ex:bom_001 a sdata:BillOfMaterials ;
    sdata:describes ex:product_001 ;
    sdata:hasComponent ex:copper_subassembly_001 .

ex:recycling_001 a sdata:Process ;
    sdata:hasInput ex:copper_subassembly_001 ;
    sdata:hasOutput ex:recycled_cu_granulate_001 ;
    sdata:generates ex:recycling_result_001 .

ex:recycled_cu_granulate_001 a sdata:Material ;
    sdata:typifiedBy ex:secondary_copper_grade .

ex:circular_dpp_update_001 a sdata:ProductPassport ;
    sdata:describes ex:product_001 ;
    sdata:hasData ex:recycling_result_001 .
```

## Minimal notwendige Relationen

- `sdata:hasBOM`
- `sdata:hasComponent`
- `sdata:hasInput`, `sdata:hasOutput`
- `sdata:generates`
- `sdata:typifiedBy`


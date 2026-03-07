# Energie- und CO2-Bilanz pro Charge

Dieses Muster ordnet Energie- und Emissionsdaten konkreten Prozessschritten zu.

## Kernentscheidung

- Bilanzierter Schritt: `sdata:Process`
- Bilanzdaten: `sdata:Data` oder `sdata:Result`
- Bezug auf Material/Produkt: `sdata:describes`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:rolling_001 a sdata:Process ;
    sdata:hasData ex:energy_report_rolling_001 .

ex:energy_report_rolling_001 a sdata:Result ;
    sdata:producedBy ex:rolling_001 ;
    sdata:describes ex:bandcoil_001 ;
    sdata:hasFormat "application/ld+json" ;
    sdata:hasSource "MES+EnergyMeter" .

ex:co2_method_iso a sdata:Specification ;
    sdata:specifies ex:energy_report_rolling_001 .
```

## Minimal notwendige Relationen

- `sdata:hasData`
- `sdata:producedBy`
- `sdata:describes`
- `sdata:specifies`


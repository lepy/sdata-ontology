# Korrosion und Oberflaechenstabilitaet

Dieses Muster trennt den Korrosionsvorgang von der Grenzflaeche.

## Kernentscheidung

- Korrosion als Geschehen: `sdata:Process`
- Korrosionskontaktzone: `sdata:Boundary`
- Betroffenes Material/Produkt: `sdata:Material` oder `sdata:Product`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:korrosion_001 a sdata:Process ;
    sdata:hasInput ex:kupfer_probe_001 ;
    sdata:hasOutput ex:kupfer_probe_001_korrodiert ;
    sdata:hasBoundary ex:korrosionszone_001 ;
    sdata:generates ex:korrosions_result_001 .

ex:korrosionszone_001 a sdata:Boundary ;
    sdata:typifiedBy ex:electrochemical_contact_type .

ex:electrochemical_contact_type a sdata:BoundaryType ;
    sdata:typifies ex:korrosionszone_001 .

ex:korrosions_result_001 a sdata:Result ;
    sdata:producedBy ex:korrosion_001 ;
    sdata:describes ex:kupfer_probe_001_korrodiert .
```

## Minimal notwendige Relationen

- `sdata:hasBoundary`
- `sdata:hasInput`, `sdata:hasOutput`
- `sdata:generates`
- `sdata:typifiedBy`


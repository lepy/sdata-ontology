# Digitaler Zwilling

Dieses Muster koppelt Digital Twin, Modelle und laufende Produktionsdaten.

## Kernentscheidung

- Zwilling: `sdata:DigitalTwin`
- Formales Modell: `sdata:Model`
- Laufende Beobachtung/Simulationsergebnis: `sdata:Result`
- Aktive Ausfuehrung: `sdata:SoftwareAgent` und `sdata:Software`

## Empfohlenes Muster

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/kupfer/> .

ex:twin_rolling_line_3 a sdata:DigitalTwin ;
    sdata:describes ex:rolling_001 ;
    sdata:encodes ex:model_rolling_thermo_mech ;
    sdata:hasData ex:twin_state_2026_03_07 .

ex:model_rolling_thermo_mech a sdata:Model .

ex:solver_service_001 a sdata:SoftwareAgent ;
    sdata:performs ex:simulation_run_001 .

ex:simulation_run_001 a sdata:Process ;
    sdata:usesSoftware ex:solver_software_001 ;
    sdata:hasInput ex:twin_state_2026_03_07 ;
    sdata:generates ex:twin_prediction_001 .

ex:twin_prediction_001 a sdata:Result ;
    sdata:producedBy ex:simulation_run_001 ;
    sdata:describes ex:rolling_001 .
```

## Minimal notwendige Relationen

- `sdata:encodes`
- `sdata:describes`
- `sdata:hasData`
- `sdata:usesSoftware`
- `sdata:generates`

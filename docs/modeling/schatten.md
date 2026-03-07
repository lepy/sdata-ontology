# Schatten

Diese Seite dokumentiert den Begriff **Schatten** als projektspezifischen Industrie-Anwendungsfall.

## Empfohlenes Basismuster (sdata:Process + sdata:Agent)

Schatten wird als Vorgang mit agentivem Anteil modelliert:

- Ereignis-/Aenderungsanteil: `sdata:Process`
- Agentiver Anteil: `sdata:EnvironmentAgent`
- Betroffenes Ding/System: `sdata:Product` oder `sdata:Material`
- Befund/Nachweis: `sdata:Result` (oder `sdata:Data`)

## Minimalbeispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/schatten/> .

ex:schatten_event_001 a sdata:Process , sdata:EnvironmentAgent ;
    sdata:hasInput ex:bauteil_001 ;
    sdata:hasOutput ex:bauteil_001_veraendert ;
    sdata:generates ex:schatten_report_001 .

ex:schatten_report_001 a sdata:Result ;
    sdata:describes ex:bauteil_001_veraendert ;
    sdata:producedBy ex:schatten_event_001 .
```

## Hinweis zur Agent-Modellierung

In `sdata-core` gibt es keine generische Klasse `sdata:Agent`; die passende
Agent-Klasse fuer umweltbedingte Einfluesse ist `sdata:EnvironmentAgent`.

# sdata-agents.ttl

SKOS-Vokabular für Agent-Typen (`sagents:*`) zur Klassifikation von Akteuren in Prozessketten.

Typische Konzepte:

- `sagents:Person`
- `sagents:Hardware` (`Sensor`, `Actuator`, `Processor`)
- `sagents:Organization`
- `sagents:Software` (`Solver`, `Service`)

## Kurzbeispiel

```turtle
@prefix sdata:   <https://w3id.org/sdata/core/> .
@prefix sagents: <https://w3id.org/sdata/vocab/agents/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix ex:      <https://example.org/zugversuch/> .

ex:Prueferin_Lehmann a sdata:Person ;
  sdata:hasIdentifier "PERS-LEHMANN-01" .

ex:Zwick_Z100 a sdata:Hardware, sdata:MachineAgent ;
  sdata:hasIdentifier "HW-ZWICK-Z100" .

ex:LSDYNA_R14 a sdata:Software, sdata:SoftwareAgent ;
  sdata:hasIdentifier "SW-LSDYNA-R14" .

sagents:Person skos:inScheme sagents:AgentTypeScheme .
sagents:Hardware skos:inScheme sagents:AgentTypeScheme .
sagents:Software skos:inScheme sagents:AgentTypeScheme .
```

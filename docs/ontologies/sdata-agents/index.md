# sdata-agents.ttl

SKOS-Vokabular für `sdata:agentType` (z. B. Person, Hardware, Software, Solver).

## Zugversuch-Beispiel

```turtle
@prefix sdata:   <https://w3id.org/sdata/core/> .
@prefix sagents: <https://w3id.org/sdata/vocab/agents/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix ex:      <https://example.org/zugversuch/> .

ex:Pruefingenieurin_Lehmann a sdata:MaterialAgent ;
  sdata:name "Dr. Lehmann" ;
  sdata:agentType "Person" .

ex:Zwick_Z100_Body a sdata:MaterialAgent ;
  sdata:name "Zwick Z100 Rahmen" ;
  sdata:agentType "Hardware" .

ex:TestControl_SW a sdata:InformationAgent ;
  sdata:name "testXpert III" ;
  sdata:agentType "Software" ;
  sdata:hostedOn ex:Zwick_Z100_Body .

# SKOS-Konzepte aus dem Agents-Vokabular
sagents:Person skos:inScheme sagents:AgentTypeScheme .
sagents:Hardware skos:inScheme sagents:AgentTypeScheme .
sagents:Software skos:inScheme sagents:AgentTypeScheme .
```

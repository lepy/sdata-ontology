# shapes/sdata-core-shapes.ttl

SHACL-Regeln fuer das `sdata-core v0.12.0`-Profil (MIN v3.4-basiert).

Hinweis:
- Die Shapes sind auf den lean Core-Stand (`sdata-core.ttl` = `v0.12.0`) ausgerichtet.
- Bei Nutzung von `sdata-core-v0.13.1.ttl` decken sie weiterhin Basisregeln ab,
  aber nicht alle neuen Klassen/Properties.

Die Shapes pruefen u. a.:

- `min:hasIdentifier` als String-Literal
- `sdata:hasVersion` als String-Literal
- grundlegenden Process-Flow (`min:hasInput` + `min:generates`)
- Struktur von `sms:StateAssignment` (`onAxis` + `hasStateValue`)

## Beispiel

```turtle
@prefix min:   <https://w3id.org/min#> .
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/demo/> .

ex:Steel a sdata:Material ;
  min:hasIdentifier "MAT-001" .

ex:Assign1 a sms:StateAssignment ;
  sms:onAxis sms:OriginAxis ;
  sms:hasStateValue sms:origin.Recycled .
```

## Lokale Validierung

```bash
pyshacl -s shapes/sdata-core-shapes.ttl -df turtle examples/battery-passport.ttl
```

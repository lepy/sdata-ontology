# shapes/sdata-core-shapes.ttl

SHACL-Regeln für das aktuelle `sdata`-Modell (`v0.9.2`, MIN/OPA-basiert).

Die Shapes prüfen u. a.:

- `sdata:hasIdentifier` als String-Literal
- `sdata:hasVersion` als String-Literal
- grundlegenden Process-Flow (`hasInput` + `producesData`)
- Struktur von `sms:StateAssignment` (`onAxis` + `hasStateValue`)

## Beispiel

```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix sms:   <https://w3id.org/sdata/material-state/> .
@prefix ex:    <https://example.org/demo/> .

ex:Steel a sdata:Material ;
  sdata:hasIdentifier "MAT-001" .

ex:Assign1 a sms:StateAssignment ;
  sms:onAxis sms:OriginAxis ;
  sms:hasStateValue sms:origin.Recycled .
```

## Lokale Validierung

```bash
pyshacl -s shapes/sdata-core-shapes.ttl -df turtle examples/battery-passport.ttl
```

# sdata:Hardware
## IRI
`https://w3id.org/sdata/core/Hardware`
## Labels
- `Hardware`
- `Hardware`
## Direct Superclasses
- `min:Object`
## Direct Subclasses
- (none)
## Comment
Physisches Gerät oder Maschine als PASSIVES Ding.
    Wenn aktiv: Doppeltypisierung mit HardwareAgent.
    Klassifizierung über sdata:HardwareType (sdata:typifiedBy).

## Examples
- `Presse, Ofen, Prüfmaschine, Sensor (passiv), Werkzeug.`
## Used As Domain
- (none)
## Used As Range
- `sdata:usesTool`
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Hardware .
```

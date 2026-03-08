# sdata:Hardware
## IRI
`https://w3id.org/sdata/core/Hardware`
## Labels
- `Hardware`
- `Hardware`
## Direct Superclasses
- [`sdata:Object`](./Object.md)
## Direct Subclasses
- (none)
## Comment
Physisches Gerät oder Maschine als PASSIVES Ding.
    Wenn aktiv: Doppeltypisierung mit HardwareAgent.
    Klassifizierung über sdata:HardwareType (sdata:typifiedBy).

## Examples
- `Presse, Ofen, Prüfmaschine, Sensor (passiv), Werkzeug.`
## Industriebeispiel (TTL)
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/industry/> .

# Zugpruefmaschine als physisches Betriebsmittel im Prueflabor.
ex:hardware_001 a sdata:Hardware ;
  sdata:hasIdentifier "HARDWARE-001" ;
  sdata:hasName "Hardware Instanz" ;
  sdata:describedBy ex:data_001 .

ex:data_001 a sdata:Data ;
  sdata:describes ex:product_001 ;
  sdata:producedBy ex:process_001 .

ex:process_001 a sdata:Process ; sdata:hasOutput ex:product_001 .
ex:product_001 a sdata:Product .
```
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

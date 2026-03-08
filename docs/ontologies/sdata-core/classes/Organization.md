# sdata:Organization
## IRI
`https://w3id.org/sdata/core/Organization`
## Labels
- `Organisation`
- `Organization`
## Direct Superclasses
- [`sdata:Agent`](./Agent.md)
- [`sdata:Institutio`](./Institutio.md)
## Direct Subclasses
- (none)
## Comment
Organisation als handelnder Agent UND anerkannte
    Institution. Co-Typisierung: Agent ∩ Institutio.
    Identitätskriterium: institutionelle Identität.

    sdata ermöglicht das nativ: Agent steht über der
    Zweiggrenze. Ein Knoten, zwei Dimensionen.
    Vorher: zwei Knoten (Organization + LegalEntity).
    Jetzt: ein Knoten mit Doppelklasse.

    sdata:LegalEntity bleibt als reine Institutio-Klasse
    für juristische Personen OHNE Agency
    (aufgelöste Firmen, historische Entitäten).

## Examples
- `Stahlwerk, Prüflabor, Zertifizierer, OEM, Recycler.`
## Industriebeispiel
- Tier-1-Lieferant als organisatorischer Akteur im DPP-Netzwerk.
## Used As Domain
- `sdata:hasLegalEntity`
## Used As Range
- (none)
## Minimal Turtle
```turtle
@prefix sdata: <https://w3id.org/sdata/core/> .
@prefix ex:    <https://example.org/> .

ex:example a sdata:Organization .
```

# sdata-core v0.1.0 — Klassenhierarchie

Konform mit MIN v1.0.0 · Entity ≡ Nexus ⊔ Forma | Agent · 54 Klassen · 2026-03-08

---

## Architektur

```
MIN v1.0.0 (Grundontologie)
  └── sdata-core v0.1.0 (Domäne)

Entity ≡ Nexus ⊔ Forma | Agent

Namespace-Regel: Domänennutzer schreiben ausschließlich sdata:*.
Kein min: in Domänenklassen. 10 Klassen-Fassaden vermitteln.
```

---

## Klassen-Fassaden (7 + 3 Doppelrollen)

Jede MIN-Kategorie bekommt eine sdata:-Fassade. Alle Domänenklassen erben von sdata:, nie von min: direkt.

| sdata-Fassade | ⊂ min-Kategorie | Rolle |
|---|---|---|
| `sdata:Object` | `min:Object` | reine Fassade |
| `sdata:Agent` | `min:Agent` | reine Fassade |
| `sdata:Lex` | `min:Lex` | reine Fassade |
| `sdata:Structura` | `min:Structura` | reine Fassade |
| `sdata:Possibile` | `min:Possibile` | reine Fassade |
| `sdata:Norma` | `min:Norma` | reine Fassade |
| `sdata:Institutio` | `min:Institutio` | reine Fassade |
| `sdata:Data` | `min:Data` | Fassade + Domänenklasse |
| `sdata:Process` | `min:Process` | Fassade + Domänenklasse |
| `sdata:Boundary` | `min:Boundary` | Fassade + Domänenklasse |

---

## Nexus-Zweig (26 Klassen)

### Object (7)

| sdata-Klasse | ⊂ Mutterklasse | Kausalität | Label |
|---|---|---|---|
| `sdata:Material` | `sdata:Object` | dispositional | Werkstoff |
| `sdata:Product` | `sdata:Object` | dispositional | Produkt |
| `sdata:Hardware` | `sdata:Object` | dispositional | Hardware |
| `sdata:Software` | `sdata:Object` | dispositional | Software |
| `sdata:Site` | `sdata:Object` | dispositional | Standort |
| `sdata:Specimen` | `sdata:Object` | dispositional | Probe |
| `sdata:Substance` | `sdata:Object` | dispositional | Substanz |

### Data (12)

| sdata-Klasse | ⊂ Mutterklasse | Kausalität | Label |
|---|---|---|---|
| `sdata:Identifier` | `sdata:Data` | · | Identifikator |
| `sdata:Result` | `sdata:Data` | · | Ergebnis |
| `sdata:ResultFile` | `sdata:Data` | · | Ergebnisdatei |
| `sdata:ProductPassport` | `sdata:Data` | · | Produktpass |
| `sdata:DigitalProductPassport` | `sdata:ProductPassport` | · | Digitaler Produktpass |
| `sdata:DigitalTwin` | `sdata:Data` | · | Digitaler Zwilling |
| `sdata:VerifiableCredential` | `sdata:Data` | · | — |
| `sdata:VerifiablePresentation` | `sdata:Data` | · | — |
| `sdata:Proof` | `sdata:Data` | · | Beweis |
| `sdata:CryptographicKey` | `sdata:Data` | · | Kryptographischer Schlüssel |
| `sdata:BillOfMaterials` | `sdata:Data` | · | Stückliste |

### Process (1)

Doppelrolle: Fassade (`⊂ min:Process`) + Domänenklasse.

### Boundary (1)

Doppelrolle: Fassade (`⊂ min:Boundary`) + Domänenklasse.

---

## Forma-Zweig (15 Klassen)

### Lex (1)

| sdata-Klasse | ⊂ Mutterklasse | Wirksamkeit | Label |
|---|---|---|---|
| `sdata:Law` | `sdata:Lex` | lawful | Gesetz |

### Structura (1)

| sdata-Klasse | ⊂ Mutterklasse | Wirksamkeit | Label |
|---|---|---|---|
| `sdata:Model` | `sdata:Structura` | structural | Modell |

### Possibile (1)

| sdata-Klasse | ⊂ Mutterklasse | Wirksamkeit | Label |
|---|---|---|---|
| `sdata:Scenario` | `sdata:Possibile` | modal | Szenario |

### Norma (1)

| sdata-Klasse | ⊂ Mutterklasse | Wirksamkeit | Label |
|---|---|---|---|
| `sdata:Requirement` | `sdata:Norma` | normative | Anforderung |

### Institutio (9)

| sdata-Klasse | ⊂ Mutterklasse | Wirksamkeit | Label |
|---|---|---|---|
| `sdata:Certification` | `sdata:Institutio` | institutional | Zertifizierung |
| `sdata:Accreditation` | `sdata:Institutio` | institutional | Akkreditierung |
| `sdata:Registry` | `sdata:Institutio` | institutional | Register |
| `sdata:TrustFramework` | `sdata:Institutio` | institutional | Vertrauensrahmen |
| `sdata:Regulation` | `sdata:Institutio` | institutional | Verordnung |
| `sdata:Specification` | `sdata:Institutio` | institutional | Spezifikation |
| `sdata:LifecyclePhase` | `sdata:Institutio` | institutional | Lebenszyklusphase |
| `sdata:LegalEntity` | `sdata:Institutio` | institutional | Juristische Person |
| `sdata:Typus` | `sdata:Institutio` | institutional | Typus |

### Typus-Subklassen (8)

| sdata-Klasse | ⊂ Mutterklasse | Label |
|---|---|---|
| `sdata:MaterialGrade` | `sdata:Typus` | Werkstoffsorte |
| `sdata:ProcessType` | `sdata:Typus` | Verfahrenstyp |
| `sdata:ProductType` | `sdata:Typus` | Produkttyp |
| `sdata:DataFormat` | `sdata:Typus` | Datenformat |
| `sdata:HardwareType` | `sdata:Typus` | Gerätetyp |
| `sdata:SoftwareType` | `sdata:Typus` | Softwaretyp |
| `sdata:BoundaryType` | `sdata:Typus` | Grenzflächentyp |
| `sdata:ModelType` | `sdata:Typus` | Modelltyp |

---

## Agent-Querkategorie (5 Klassen)

v4.0: Agent ⊂ Entity. Co-Typisierung Pflicht: Agent ⊑ Nexus ⊔ Forma.

| sdata-Klasse | Co-Typisierung | Zweig | Identitätskriterium |
|---|---|---|---|
| `sdata:Person` | sdata:Agent ∩ **sdata:Object** | Nexus | materiale Kontinuität |
| `sdata:HardwareAgent` | sdata:Agent ∩ **sdata:Object** | Nexus | materiale Kontinuität |
| `sdata:SoftwareAgent` | sdata:Agent ∩ **sdata:Data** | Nexus | informationale Identität |
| `sdata:Organization` | sdata:Agent ∩ **sdata:Institutio** | **⊥ N ∩ F** | institutionelle Identität |
| `sdata:EnvironmentAgent` | sdata:Agent ∩ **sdata:Process** | Nexus | Veränderungsidentität |

---

## Seinspartition — Validierung

```
N  = Nexus     F  = Forma     ⊥ = Zweiggrenze     · = erbt

N   sdata:Object              ⊂ min:Object              [Fassade]
N     sdata:Material          ⊂ sdata:Object
N     sdata:Product           ⊂ sdata:Object
N     sdata:Hardware          ⊂ sdata:Object
N     sdata:Software          ⊂ sdata:Object
N     sdata:Site              ⊂ sdata:Object
N     sdata:Specimen          ⊂ sdata:Object
N     sdata:Substance         ⊂ sdata:Object

N   sdata:Data                ⊂ min:Data                 [Fassade + Domäne]
·     sdata:Identifier        ⊂ sdata:Data
·     sdata:Result            ⊂ sdata:Data
·     sdata:ResultFile        ⊂ sdata:Data
·     sdata:ProductPassport   ⊂ sdata:Data
·       sdata:DigitalProductPassport ⊂ sdata:ProductPassport
·     sdata:DigitalTwin       ⊂ sdata:Data
·     sdata:VerifiableCredential     ⊂ sdata:Data
·     sdata:VerifiablePresentation   ⊂ sdata:Data
·     sdata:Proof             ⊂ sdata:Data
·     sdata:CryptographicKey  ⊂ sdata:Data
·     sdata:BillOfMaterials   ⊂ sdata:Data

N   sdata:Agent               ⊂ min:Agent               [Fassade]
✓ N   sdata:Person            ⊂ sdata:Agent ∩ sdata:Object
✓ N   sdata:HardwareAgent     ⊂ sdata:Agent ∩ sdata:Object
✓ N   sdata:SoftwareAgent     ⊂ sdata:Agent ∩ sdata:Data
✓ ⊥   sdata:Organization     ⊂ sdata:Agent ∩ sdata:Institutio
✓ N   sdata:EnvironmentAgent  ⊂ sdata:Agent ∩ sdata:Process

N   sdata:Process             ⊂ min:Process              [Fassade + Domäne]
N   sdata:Boundary            ⊂ min:Boundary             [Fassade + Domäne]

F   sdata:Lex                 ⊂ min:Lex                  [Fassade]
F     sdata:Law               ⊂ sdata:Lex

F   sdata:Structura           ⊂ min:Structura            [Fassade]
F     sdata:Model             ⊂ sdata:Structura

F   sdata:Possibile           ⊂ min:Possibile            [Fassade]
F     sdata:Scenario          ⊂ sdata:Possibile

F   sdata:Norma               ⊂ min:Norma                [Fassade]
F     sdata:Requirement       ⊂ sdata:Norma

F   sdata:Institutio          ⊂ min:Institutio            [Fassade]
F     sdata:Certification     ⊂ sdata:Institutio
F     sdata:Accreditation     ⊂ sdata:Institutio
F     sdata:Registry          ⊂ sdata:Institutio
F     sdata:TrustFramework    ⊂ sdata:Institutio
F     sdata:Regulation        ⊂ sdata:Institutio
F     sdata:Specification     ⊂ sdata:Institutio
F     sdata:LifecyclePhase    ⊂ sdata:Institutio
F     sdata:LegalEntity       ⊂ sdata:Institutio
F     sdata:Typus             ⊂ sdata:Institutio
·       sdata:MaterialGrade   ⊂ sdata:Typus
·       sdata:ProcessType     ⊂ sdata:Typus
·       sdata:ProductType     ⊂ sdata:Typus
·       sdata:DataFormat      ⊂ sdata:Typus
·       sdata:HardwareType    ⊂ sdata:Typus
·       sdata:SoftwareType    ⊂ sdata:Typus
·       sdata:BoundaryType    ⊂ sdata:Typus
·       sdata:ModelType       ⊂ sdata:Typus
```

Kein `min:` in Domänenklassen. Nur die 10 Fassaden berühren den MIN-Namespace.

---

## Disjunktheitsaxiome (4)

```
⊥ { Material, Product, Hardware, Software, Site, Specimen, Substance }     Object (7)
⊥ { Person, HardwareAgent, SoftwareAgent, Organization, EnvironmentAgent } Agent (5)
⊥ { Certification, Accreditation, Registry, TrustFramework,
     Regulation, Specification, LifecyclePhase, LegalEntity }              Institutio (8)
⊥ { MaterialGrade, ProcessType, ProductType, DataFormat,
     HardwareType, SoftwareType, BoundaryType, ModelType }                 Typus (8)
```

---

## Inventar

| Kategorie | Anzahl |
|---|---|
| Klassen gesamt | 54 |
| — davon Fassaden (7 rein + 3 Doppelrolle) | 10 |
| — davon Domänenklassen | 44 |
| OP-Fassaden (owl:equivalentProperty → MIN) | 45 |
| DP-Fassaden | 5 |
| AP-Fassaden | 2 |
| Eigene Object Properties | 31 |
| Eigene Datatype Properties | 19 |
| Disjunktheitsaxiome | 4 |
| Modeling Patterns | 16 |

---

*sdata-core v0.1.0 · MIN v1.0.0 · CC BY-SA 4.0 · Dr. Ingolf Lepenies*

# sdata v0.1.0 — Property-Referenz pro Klasse
# Für Codex: Nur diese Properties in Beispielen verwenden.
# ★ = wichtigste Properties für diese Klasse

## OBJECT

### sdata:Site
⊂ Object
Physischer Standort. Verortung via sdata:locatedAt.
Beispiele: Werk Duisburg, Presswerk Leipzig, Recyclinganlage Hamburg.
ERLAUBT als Subjekt:
★ sdata:hasName
★ sdata:identifiedBy → sdata:Identifier
★ sdata:locatedAt → sdata:Site
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:originates → Forma
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:specifiedBy → sdata:Specification
  sdata:typifiedBy → Institutio
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:locatedAt ← min:Nexus
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

## AGENT ∩ OBJECT

### sdata:Person
⊂ Agent ∩ Object
Mensch als handelnder Agent. Agent ∩ Object.
Beispiele: Prüfer, Konstrukteur, Werker, Laborant.
ERLAUBT als Subjekt:
★ sdata:hasName
★ sdata:identifiedBy → sdata:Identifier
★ sdata:locatedAt → sdata:Site
★ sdata:performs → Process
  sdata:actsOn → Object
  sdata:affectedBy → Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:originates → Forma
  sdata:owns → Object
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

### sdata:Hardware
⊂ Agent ∩ Object
Physisches Gerät, Maschine, Bauteil, Werkzeug —
Beispiele: Presse, Ofen, Prüfmaschine, Sensor, Werkzeug, Roboterarm, Seitenteil, Hammer, Felge.
ERLAUBT als Subjekt:
★ sdata:containsSubstance → sdata:Substance
★ sdata:hasBOM → sdata:BillOfMaterials
★ sdata:hasCustodian → min:Agent
★ sdata:hasMaterial → sdata:Material
★ sdata:hasName
★ sdata:hasStatus
★ sdata:identifiedBy → sdata:Identifier
★ sdata:locatedAt → sdata:Site
★ sdata:performs → Process
★ sdata:typifiedBy → Institutio
  sdata:actsOn → Object
  sdata:affectedBy → Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:originates → Forma
  sdata:owns → Object
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio
  sdata:usesTool ← sdata:Process

### sdata:Material
⊂ Agent ∩ Object
Werkstoff als Agent. Wirkt selektiv:
Beispiele: HC340LA, PP-GF30, AlSi10Mg, CFK-Prepreg, Recyclat.
ERLAUBT als Subjekt:
★ sdata:containsSubstance → sdata:Substance
★ sdata:hasName
★ sdata:identifiedBy → sdata:Identifier
★ sdata:typifiedBy → Institutio
  sdata:actsOn → Object
  sdata:affectedBy → Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBOM → sdata:BillOfMaterials
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasMaterial → sdata:Material
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performs → Process
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasMaterial ← min:Object
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

### sdata:Substance
⊂ Agent ∩ Object
Chemischer Stoff als Agent. Wirkt selektiv:
Beispiele: Mangan (CAS 7439-96-5), Chrom-VI (SVHC), Blei (RoHS).
ERLAUBT als Subjekt:
★ sdata:hasCASNumber
★ sdata:hasConcentration
★ sdata:hasName
★ sdata:hasRegulatoryStatus
  sdata:actsOn → Object
  sdata:affectedBy → Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:containsSubstance → sdata:Substance
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performs → Process
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:containsSubstance ← min:Object
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

### sdata:Specimen
⊂ Agent ∩ Object
Prüfkörper als Agent. Wirkt selektiv:
Beispiele: Flachzugprobe (DIN 50125 Typ H), Rundprobe, Kerbschlagprobe.
ERLAUBT als Subjekt:
★ sdata:hasMaterial → sdata:Material
★ sdata:hasName
★ sdata:sampledFrom → min:Object
★ sdata:typifiedBy → Institutio
  sdata:actsOn → Object
  sdata:affectedBy → Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:containsSubstance → sdata:Substance
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBOM → sdata:BillOfMaterials
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performs → Process
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:actsOn ← Agent
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:owns ← Agent
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:sampledFrom ← sdata:Specimen
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

## AGENT ∩ DATA

### sdata:Software
⊂ Agent ∩ Data
Software — IMMER Agent. Agent ∩ Data.
Beispiele: AutoForm R10, Abaqus 2024, LS-DYNA R14, PostgreSQL, openLCA.
ERLAUBT als Subjekt:
★ sdata:encodes → Forma
★ sdata:hasName
★ sdata:hasStatus
★ sdata:identifiedBy → sdata:Identifier
★ sdata:performs → Process
★ sdata:realizes → Forma
★ sdata:typifiedBy → Institutio
  sdata:actsOn → Object
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasSource
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:producedBy → sdata:Process
  sdata:produces → Data
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:selects → Possibile
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:performedBy ← Process
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio
  sdata:usesSoftware ← sdata:Process

### sdata:DigitalTwin
⊂ Software
Digitaler Zwilling — Software-Agent, der ein
Beispiele: FEM-basierter DZ, Predictive-Maintenance-DZ, Prozess-DZ.
ERLAUBT als Subjekt:
★ sdata:describes → Nexus
★ sdata:encodes → Forma
★ sdata:hasName
★ sdata:hasStatus
★ sdata:selects → Possibile
★ sdata:typifiedBy → Institutio
  sdata:actsOn → Object
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasSource
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performs → Process
  sdata:producedBy → sdata:Process
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:performedBy ← Process
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio
  sdata:usesSoftware ← sdata:Process

## AGENT ∩ INSTITUTIO

### sdata:Organization
⊂ Agent ∩ Institutio
Agent ∩ Institutio.
Beispiele: Stahlwerk, Prüflabor, Zertifizierer, OEM, Recycler.
ERLAUBT als Subjekt:
★ sdata:constitutes → Institutio
★ sdata:hasLegalEntity → sdata:LegalEntity
★ sdata:hasName
★ sdata:identifiedBy → sdata:Identifier
★ sdata:locatedAt → sdata:Site
★ sdata:recognizes → Institutio
  sdata:actsOn → Object
  sdata:certifiedUnder → sdata:Certification
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:encodedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performs → Process
  sdata:produces → Data
  sdata:realizedBy → Nexus
  sdata:realizes → Forma
  sdata:recognizedBy → Agent
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:typifiedBy → Institutio
  sdata:typifies → Nexus
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constitutes ← Agent
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:encodes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:originates ← Nexus
  sdata:performedBy ← Process
  sdata:realizedBy ← Forma
  sdata:realizes ← Nexus
  sdata:recognizedBy ← Institutio
  sdata:recognizes ← Agent
  sdata:regulates ← sdata:Regulation
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:typifiedBy ← Nexus
  sdata:typifies ← Institutio

## AGENT ∩ PROCESS

### sdata:EnvironmentAgent
⊂ Agent ∩ Process
Natürlicher Prozess mit selektiver Wirkung.
Beispiele: Korrosion, UV-Strahlung, Feuchtigkeit.
ERLAUBT als Subjekt:
★ sdata:actsOn → Object
★ sdata:hasName
  sdata:certifiedUnder → sdata:Certification
  sdata:constitutes → Institutio
  sdata:controls → Process
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:generates → Data
  sdata:governedBy → sdata:Law
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndTime
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasInput → Nexus
  sdata:hasLocation
  sdata:hasOutput → Nexus
  sdata:hasStartTime
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:owns → Object
  sdata:performedBy → Agent
  sdata:performs → Process
  sdata:precedes → sdata:Process
  sdata:produces → Data
  sdata:realizes → Forma
  sdata:recognizes → Institutio
  sdata:regulatedBy → sdata:Regulation
  sdata:requiresPhase → sdata:LifecyclePhase
  sdata:resultOf → Process
  sdata:selects → Possibile
  sdata:specifiedBy → sdata:Specification
  sdata:succeeds → sdata:Process
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:affectedBy ← Object
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constitutedBy ← Institutio
  sdata:constrains ← Forma
  sdata:controls ← Agent
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generatedBy ← Data
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasCustodian ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasIssuer ← sdata:Identifier
  sdata:hasOutput ← Process
  sdata:issuedBy ← min:Institutio
  sdata:originatedBy ← Forma
  sdata:originatedIn ← min:Forma
  sdata:performedBy ← Process
  sdata:performs ← Agent
  sdata:precedes ← sdata:Process
  sdata:producedBy ← sdata:Data
  sdata:realizedBy ← Forma
  sdata:recognizedBy ← Institutio
  sdata:regulates ← sdata:Regulation
  sdata:resultOf ← Nexus
  sdata:signedBy ← sdata:Data
  sdata:specifies ← sdata:Specification
  sdata:succeeds ← sdata:Process
  sdata:typifies ← Institutio
  sdata:undergoes ← Nexus

## DATA

### sdata:Data
⊂ Data
Domänenspezifische Daten. Wirkt nur über Agent.
Beispiele: Messdaten, Werkstoffdatenblatt, CAD-Modell, LS-DYNA Inputdeck.
ERLAUBT als Subjekt:
★ sdata:describes → Nexus
★ sdata:encodes → Forma
★ sdata:generatedBy → Process
★ sdata:hasChecksum
★ sdata:hasName
★ sdata:typifiedBy → Institutio
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:Identifier
⊂ Data
Beispiele: GTIN, DID (did:web), DOI, VDA-Teilenummer, UUID.
ERLAUBT als Subjekt:
★ sdata:hasIssuer → min:Agent
★ sdata:hasScheme
★ sdata:hasValue
★ sdata:registeredIn → sdata:Registry
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:encodes → Forma
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:identifiedBy ← min:Entity
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:Result
⊂ Data
Semantisches Ergebnis-Bündel. Eigenes Axiom:
Beispiele: Zugversuchsergebnis, FEM-Ergebnis, Compliance-Bewertung.
ERLAUBT als Subjekt:
★ sdata:assessesRequirement → sdata:Requirement
★ sdata:assessmentOutcome
★ sdata:describes → Nexus
★ sdata:generatedBy → Process
★ sdata:signedBy → min:Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:encodes → Forma
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:ProductPassport
⊂ Data
Produktpass als Data-Artefakt.
Beispiele: Materialzeugnis EN 10204, Batterie-Pass, EPD, Stahl-DPP.
ERLAUBT als Subjekt:
★ sdata:describes → Nexus
★ sdata:encodes → Forma
★ sdata:hasVersion
★ sdata:signedBy → min:Agent
★ sdata:supersedes → sdata:Data
★ sdata:typifiedBy → Institutio
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:DigitalProductPassport
⊂ ProductPassport
ESPR-konformer digitaler Produktpass.
Beispiele: ESPR-DPP, Batterie-Pass (EU 2023/1542), Textil-Pass.
ERLAUBT als Subjekt:
★ sdata:describes → Nexus
★ sdata:encodes → Forma
★ sdata:hasComponent → Nexus
★ sdata:hasVersion
★ sdata:identifiedBy → sdata:Identifier
★ sdata:signedBy → min:Agent
★ sdata:supersedes → sdata:Data
★ sdata:typifiedBy → Institutio
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:VerifiableCredential
⊂ Data
Beispiele: Signiertes Materialzeugnis, DPP als VC.
ERLAUBT als Subjekt:
★ sdata:signedBy → min:Agent
★ sdata:supersedes → sdata:Data
★ sdata:validFrom
★ sdata:validUntil
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:encodes → Forma
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:VerifiablePresentation
⊂ Data
Beispiele: DPP-Präsentation an Recycler.
ERLAUBT als Subjekt:
★ sdata:hasComponent → Nexus
★ sdata:signedBy → min:Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:certifies → min:Nexus
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:encodes → Forma
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:Proof
⊂ Data
Beispiele: Ed25519-Signatur, ECDSA-Signatur.
ERLAUBT als Subjekt:
★ sdata:encodes → Forma
★ sdata:signedBy → min:Agent
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:CryptographicKey
⊂ Data
Beispiele: Ed25519 Public Key, ECDSA Private Key.
ERLAUBT als Subjekt:
★ sdata:encodes → Forma
★ sdata:hasName
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:describes → Nexus
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasComponent → Nexus
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

### sdata:BillOfMaterials
⊂ Data
Stückliste als Data. sdata:describes ein physisches Ding.
Beispiele: Fahrzeug-BOM, Batterie-BOM, Elektronik-BOM.
ERLAUBT als Subjekt:
★ sdata:describes → Nexus
★ sdata:hasComponent → Nexus
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:encodes → Forma
  sdata:generatedBy → Process
  sdata:hasBoundary → Boundary
  sdata:hasChecksum
  sdata:hasConfidence
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasSource
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:producedBy → sdata:Process
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:revokedAt
  sdata:signedBy → min:Agent
  sdata:specifiedBy → sdata:Specification
  sdata:supersededBy → sdata:Data
  sdata:supersedes → sdata:Data
  sdata:typifiedBy → Institutio
  sdata:undergoes → Process
  sdata:validFrom
  sdata:validUntil
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describedBy ← Nexus
  sdata:describes ← Data
  sdata:encodedBy ← Forma
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generates ← Process
  sdata:governs ← Lex
  sdata:hasBOM ← min:Object
  sdata:hasComponent ← Nexus
  sdata:hasData ← min:Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:produces ← Agent
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:supersededBy ← sdata:Data
  sdata:supersedes ← sdata:Data
  sdata:typifies ← Institutio

## PROCESS

### sdata:Process
⊂ Process
Beispiele: Tiefziehen, Zugversuch, FEM-Simulation, LCA-Studie.
ERLAUBT als Subjekt:
★ sdata:governedBy → sdata:Law
★ sdata:hasEndTime
★ sdata:hasInput → Nexus
★ sdata:hasOutput → Nexus
★ sdata:hasStartTime
★ sdata:performedBy → Agent
★ sdata:realizes → Forma
★ sdata:requiresPhase → sdata:LifecyclePhase
★ sdata:succeeds → sdata:Process
★ sdata:typifiedBy → Institutio
★ sdata:usesSoftware → sdata:Software
★ sdata:usesTool → sdata:Hardware
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:generates → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasName
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:precedes → sdata:Process
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:specifiedBy → sdata:Specification
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:controls ← Agent
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:generatedBy ← Data
  sdata:governs ← Lex
  sdata:hasComponent ← Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:originatedIn ← min:Forma
  sdata:performs ← Agent
  sdata:precedes ← sdata:Process
  sdata:producedBy ← sdata:Data
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:resultOf ← Nexus
  sdata:specifies ← sdata:Specification
  sdata:succeeds ← sdata:Process
  sdata:typifies ← Institutio
  sdata:undergoes ← Nexus

## BOUNDARY

### sdata:Boundary
⊂ Boundary
Beispiele: Übergangswiderstand, Reibung, Adhäsion, Korngrenze.
ERLAUBT als Subjekt:
★ sdata:bounds → Nexus
★ sdata:hasName
★ sdata:typifiedBy → Institutio
  sdata:certifiedUnder → sdata:Certification
  sdata:derivedFrom → Nexus
  sdata:describedBy → Data
  sdata:hasBoundary → Boundary
  sdata:hasComponent → Nexus
  sdata:hasCustodian → min:Agent
  sdata:hasData → sdata:Data
  sdata:hasDescription
  sdata:hasEndpoint
  sdata:hasIdentifier
  sdata:hasLocation
  sdata:hasStatus
  sdata:hasTimestamp
  sdata:hasUUID
  sdata:hasVersion
  sdata:identifiedBy → sdata:Identifier
  sdata:locatedAt → sdata:Site
  sdata:originates → Forma
  sdata:realizes → Forma
  sdata:regulatedBy → sdata:Regulation
  sdata:resultOf → Process
  sdata:specifiedBy → sdata:Specification
  sdata:undergoes → Process
ERLAUBT als Objekt:
  sdata:bounds ← Boundary
  sdata:certifies ← sdata:Data
  sdata:concerns ← Possibile
  sdata:constrains ← Forma
  sdata:derivedFrom ← Nexus
  sdata:describes ← Data
  sdata:evaluates ← Norma
  sdata:formalizes ← Structura
  sdata:governs ← Lex
  sdata:hasBoundary ← Nexus
  sdata:hasComponent ← Nexus
  sdata:hasInput ← Process
  sdata:hasOutput ← Process
  sdata:originatedBy ← Forma
  sdata:realizedBy ← Forma
  sdata:regulates ← sdata:Regulation
  sdata:specifies ← sdata:Specification
  sdata:typifies ← Institutio

## LEX

### sdata:Law
⊂ Lex
Universelles Gesetz. Gilt ausnahmslos.
Beispiele: Energieerhaltung, Massenerhaltung, Entropiezunahme, Impulserhaltung.
ERLAUBT als Subjekt:
★ sdata:governs → Nexus
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
ERLAUBT als Objekt:
  sdata:comprises ← Institutio
  sdata:encodes ← Data
  sdata:governedBy ← sdata:Process
  sdata:originates ← Nexus
  sdata:realizes ← Nexus

## STRUCTURA

### sdata:Model
⊂ Structura
Formale Approximation. Kann nützlich sein,
Beispiele: Hooke, von-Mises, Johnson-Cook, Fick, Fourier, ReCiPe, Ed25519, LSTM.
ERLAUBT als Subjekt:
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:formalizes → Nexus
  sdata:identifiedBy → sdata:Identifier
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
ERLAUBT als Objekt:
  sdata:comprises ← Institutio
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus

## POSSIBILE

### sdata:Scenario
⊂ Possibile
Beispiele: Versagensszenario, FMEA-Zeile, Designalternative.
ERLAUBT als Subjekt:
★ sdata:concerns → Nexus
  sdata:alternativeTo → Possibile
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
ERLAUBT als Objekt:
  sdata:alternativeTo ← Possibile
  sdata:comprises ← Institutio
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:selects ← Agent

## NORMA

### sdata:Requirement
⊂ Norma
ATOMARE Anforderung oder Grenzwert. Bündelung
Beispiele: Rm ≥ 340 MPa, Ra ≤ 1.6 µm, FU: 1 kg Stahl ab Werk.
ERLAUBT als Subjekt:
★ sdata:evaluates → Nexus
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
ERLAUBT als Objekt:
  sdata:assessesRequirement ← sdata:Result
  sdata:comprises ← Institutio
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus

## INSTITUTIO

### sdata:Certification
⊂ Institutio
Beispiele: ISO 9001, EN 10204 3.1, CE-Kennzeichnung.
ERLAUBT als Subjekt:
★ sdata:constitutedBy → Agent
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:certifiedUnder ← min:Nexus
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:Accreditation
⊂ Institutio
Beispiele: DAkkS-Akkreditierung, UKAS.
ERLAUBT als Subjekt:
★ sdata:constitutedBy → Agent
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:Registry
⊂ Institutio
Beispiele: Catena-X Registry, GAIA-X Registry.
ERLAUBT als Subjekt:
★ sdata:constitutedBy → Agent
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:registeredIn ← sdata:Identifier
  sdata:typifiedBy ← Nexus

### sdata:TrustFramework
⊂ Institutio
Beispiele: Catena-X, GAIA-X, EBSI, IBU EPD-Programm.
ERLAUBT als Subjekt:
★ sdata:constitutedBy → Agent
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:Regulation
⊂ Institutio
Regulatorisches Rahmenwerk. BÜNDELT atomare
Beispiele: ESPR, CBAM, REACH, RoHS, EU-Taxonomie.
ERLAUBT als Subjekt:
★ sdata:comprises → Forma
★ sdata:constitutedBy → Agent
★ sdata:recognizedBy → Agent
★ sdata:regulates → min:Nexus
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:regulatedBy ← min:Nexus
  sdata:typifiedBy ← Nexus

### sdata:Specification
⊂ Institutio
Technische Spezifikation oder Norm. BÜNDELT atomare
Beispiele: EN 10025-2, DIN EN ISO 6892-1, ISO 14040.
ERLAUBT als Subjekt:
★ sdata:comprises → Forma
★ sdata:constitutedBy → Agent
★ sdata:specifies → min:Nexus
  sdata:comprisedBy → Institutio
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:specifiedBy ← min:Nexus
  sdata:typifiedBy ← Nexus

### sdata:LifecyclePhase
⊂ Institutio
Konventionelle Lebenszykluseinteilung.
Beispiele: Rohstoffgewinnung, Fertigung, Nutzung, End-of-Life.
ERLAUBT als Subjekt:
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:requiresPhase ← sdata:Process
  sdata:typifiedBy ← Nexus

### sdata:LegalEntity
⊂ Institutio
Juristische Person OHNE Agency.
Beispiele: Aufgelöste GmbH, historische Institution.
ERLAUBT als Subjekt:
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
  sdata:typifies → Nexus
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:hasLegalEntity ← sdata:Organization
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

## TYPUS

### sdata:Typus
⊂ Institutio
Konventionelle Wesensbestimmung. Bündelt Forma.
ERLAUBT als Subjekt:
★ sdata:comprises → Forma
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:MaterialGrade
⊂ Typus
Beispiele: DC04, HC340LA, AlSi10Mg, PP-GF30, X5CrNi18-10.
ERLAUBT als Subjekt:
★ sdata:comprises → Forma
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:ProcessType
⊂ Typus
Beispiele: Zugversuch nach ISO 6892-1, Tiefziehen, Crashsimulation.
ERLAUBT als Subjekt:
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:ProductType
⊂ Typus
Wesensbestimmung eines Produkts, Geräts oder
Beispiele: Seitenteil, B-Säule, Felge, Universalprüfmaschine, Hydraulische Presse, FE-Solver, CAD-System, LCA-Software.
ERLAUBT als Subjekt:
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:DataFormat
⊂ Typus
Wesensbestimmung eines Dateiformats. Ersetzt
Beispiele: STEP AP214, JT, VTU, CSV (RFC 4180), JSON-LD, Parquet, PDF.
ERLAUBT als Subjekt:
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:BoundaryType
⊂ Typus
Beispiele: Coulomb-Reibung, Σ3-CSL-Korngrenze, thermischer Kontaktwiderstand.
ERLAUBT als Subjekt:
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

### sdata:ModelType
⊂ Typus
Beispiele: Materialmodell, Kryptoalgorithmus, ML-Architektur, DB-Schema.
ERLAUBT als Subjekt:
★ sdata:typifies → Nexus
  sdata:comprisedBy → Institutio
  sdata:comprises → Forma
  sdata:constitutedBy → Agent
  sdata:constrains → Nexus
  sdata:encodedBy → Data
  sdata:identifiedBy → sdata:Identifier
  sdata:issuedBy → min:Agent
  sdata:originatedBy → Nexus
  sdata:originatedIn → sdata:Process
  sdata:realizedBy → Nexus
  sdata:recognizedBy → Agent
ERLAUBT als Objekt:
  sdata:comprisedBy ← Forma
  sdata:comprises ← Institutio
  sdata:constitutes ← Agent
  sdata:encodes ← Data
  sdata:originates ← Nexus
  sdata:realizes ← Nexus
  sdata:recognizes ← Agent
  sdata:typifiedBy ← Nexus

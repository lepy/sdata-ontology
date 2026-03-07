# sdata Classes (Text Tree)

Source: `sdata-core.ttl` (class + `rdfs:subClassOf` structure)

```text
min:Entity
├── min:Nexus
│   ├── min:Object
│   │   ├── sdata:Material
│   │   ├── sdata:Product
│   │   ├── sdata:Hardware
│   │   ├── sdata:Software
│   │   ├── sdata:Site
│   │   ├── sdata:Specimen
│   │   └── sdata:Substance
│   ├── min:Data
│   │   └── sdata:Data
│   │       ├── sdata:Identifier
│   │       ├── sdata:Result
│   │       ├── sdata:ResultFile
│   │       ├── sdata:ProductPassport
│   │       ├── sdata:DigitalTwin
│   │       ├── sdata:VerifiableCredential
│   │       ├── sdata:VerifiablePresentation
│   │       ├── sdata:Proof
│   │       ├── sdata:CryptographicKey
│   │       └── sdata:BillOfMaterials
│   ├── min:Agent
│   │   ├── sdata:Person
│   │   ├── sdata:HardwareAgent
│   │   ├── sdata:SoftwareAgent
│   │   ├── sdata:Organization
│   │   └── sdata:EnvironmentAgent
│   ├── min:Process
│   │   └── sdata:Process
│   └── min:Boundary
│       └── sdata:Boundary
└── min:Forma
    ├── min:Lex
    │   └── sdata:Law
    ├── min:Structura
    │   └── sdata:Model
    ├── min:Possibile
    │   └── sdata:Scenario
    ├── min:Norma
    │   ├── sdata:Requirement
    │   ├── sdata:Specification
    │   ├── sdata:Regulation
    │   └── sdata:LifecyclePhase
    └── min:Institutio
        ├── sdata:Certification
        ├── sdata:Accreditation
        ├── sdata:Registry
        ├── sdata:TrustFramework
        └── sdata:Typus
            ├── sdata:MaterialGrade
            ├── sdata:ProcessType
            ├── sdata:DataFormat
            ├── sdata:HardwareType
            ├── sdata:SoftwareType
            └── sdata:BoundaryType
```

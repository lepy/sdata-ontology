# prov-o Classes (Text Tree)

Source: `vendor/ontologies/prov-o.ttl`

```text
Activity

Agent
├── Organization
├── Person
└── SoftwareAgent

Entity
├── Bundle
├── Collection
│   └── EmptyCollection
└── Plan

Influence
├── ActivityInfluence
│   ├── Communication
│   ├── Generation
│   └── Invalidation
├── AgentInfluence
│   ├── Association
│   ├── Attribution
│   └── Delegation
└── EntityInfluence
    ├── Derivation
    │   ├── PrimarySource
    │   ├── Quotation
    │   └── Revision
    ├── End
    ├── Start
    └── Usage

InstantaneousEvent
├── End
├── Generation
├── Invalidation
├── Start
└── Usage

Location

Role

Thing
```

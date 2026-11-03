# Courses

| Course | Framework | Units | Sub-units | Start here |
|---|---|:-:|:-:|---|
| [1 — Context Engineering](1-context-engineering-brief/) | BRIEF | 5 | 21 | [Course overview](1-context-engineering-brief/README.md) |
| [2 — Agentic AI](2-agentic-ai-agent/) | AGENT | 5 | 16 | [Course overview](2-agentic-ai-agent/README.md) |
| [3 — Responsible AI](3-responsible-ai-trust/) | TRUST | 5 | 26 | [Course overview](3-responsible-ai-trust/README.md) |

Take them in order. Each course opens on a problem the previous one created.

## How a course folder is laid out

```
1-context-engineering-brief/
├── README.md                     course overview, framework, every unit and sub-unit
├── flow.yaml                     the unit order
└── cu-2-when-the-facts-arent-enough/          one folder per unit
    ├── cu.yaml                                unit title, concept, sub-unit order
    └── scu-2.1-the-role/                      one folder per sub-unit
        ├── scu.yaml                           type, skills, reuse, dependencies
        └── artifact.md                        the written lesson (where it exists)
```

Folder names include the unit's title, which is the learner's problem in their own words. The IDs
inside the YAML files (`cu.c1.u2`, `scu.c1.u2.1`) are permanent: lessons, attribution and evidence
are keyed to them, so they are never renamed.

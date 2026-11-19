# Courses

| Course | Framework | Units | Sub-units | Start here |
|---|---|:-:|:-:|---|
| [1 — Context Engineering](1-context-engineering-brief/) | BRIEF | 5 | 21 | [Course overview](1-context-engineering-brief/README.md) |
| [2 — Agentic AI](2-agentic-ai-agent/) | AGENT | 5 | 16 | [Course overview](2-agentic-ai-agent/README.md) |
| [3 — Responsible AI](3-responsible-ai-trust/) | TRUST | 5 | 26 | [Course overview](3-responsible-ai-trust/README.md) |

Take them in order. Each course opens on a problem the previous one created.

## Sector courses

One course per sector, each on one problem from the problem bank
(`5-roadmap/sector-problem-statements.md`), built the same way. Separate from the three-course
chain above; each has its own story world.

| Course | Problem | Way | Units | Sub-units | Status |
|---|---|---|:-:|:-:|---|
| [Health-tech — Insurance claims and rejections](healthtech-d1-insurance-claims/) | D1 | Story | 5 | 21 | Skeleton; one lesson drafted |
| [Health — Plain-Nepali patient instructions](health-h1-patient-instructions/) | H1 | Story | 5 | 22 | Skeleton; one lesson drafted |
| [Health — The monthly report that says what was counted](health-h2-hmis-reporting/) | H2 | Audit | 5 | 22 | Skeleton; one lesson drafted |
| [Health — "What is the current rule?"](health-h3-current-rule/) | H3 | Build | 5 | 22 | Skeleton; one lesson drafted |
| [Health — Checking a health claim before it is shared](health-h4-health-misinformation/) | H4 | Drill | 5 | 22 | Skeleton; one lesson drafted; evidence low, check first |
| [Health — The referral note that carries findings, not the call](health-h5-referral-notes/) | H5 | Rounds | 5 | 22 | Skeleton; one lesson drafted |

The five health courses are one programme: five problems, five desks in one shared world, and
five **ways** of teaching (Story, Rounds, Drill, Audit, Build). The design is in
[`3-course-flow/health-programme.md`](../3-course-flow/health-programme.md) and the method in
[`1-how-we-built-it/five-ways.md`](../1-how-we-built-it/five-ways.md). Each way has its own
sub-unit types; the validator checks them per course.

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

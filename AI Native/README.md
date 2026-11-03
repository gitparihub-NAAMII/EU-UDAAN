# UDAAN AI-Native Programme

Three self-paced courses that teach knowledge workers to work *with* AI: get original work out of
it, hand it repeatable jobs safely, and stand behind everything it does in their name.

Built by NAAMII's Education & Outreach Division for the EU UDAAN programme. Set in Kathmandu,
written for Nepal's working conditions: free tools first, no code, local language and local stories.

```
1 programme capability · 3 courses · 15 units · 63 sub-units · 3 frameworks · 1 protagonist
```

## The three courses

| | Course 1 | Course 2 | Course 3 |
|---|---|---|---|
| **Skill area** | [Context Engineering](4-courses/1-context-engineering-brief/) | [Agentic AI](4-courses/2-agentic-ai-agent/) | [Responsible AI](4-courses/3-responsible-ai-trust/) |
| **The learner's problem** | *"Why does the same AI treat me differently?"* | *"I fixed the writing. So why am I MORE tired?"* | *"Everything runs perfectly. So what could go wrong?"* |
| **What they leave with** | A reusable one-page brief | A working agent, built free | A one-page AI policy and an audit habit |
| **Framework** | BRIEF | AGENT | TRUST |

One protagonist runs through all three: **Maya Gurung**, trip coordinator at Himalayan Getaways, a
travel company in Kathmandu. Each course opens on a problem that the previous course's success
created, so the three read as one story.

## How this folder is organised

Read the numbered folders in order. Each one opens with a README.

| Folder | What's in it | Read it if you want to know… |
|---|---|---|
| [**1-how-we-built-it/**](1-how-we-built-it/) | The design method, the full build manual, the authoring workflow, sources | How a unit is designed and why it's shaped that way |
| [**2-skills/**](2-skills/) | The skill pyramid, the four skill areas, competency levels, skills per course | What a learner can actually do afterwards |
| [**3-course-flow/**](3-course-flow/) | The programme arc, Maya's story, the map of all 15 units | How the courses connect, and the order things are taught |
| [**4-courses/**](4-courses/) | The three courses: units, sub-units, and the written lessons | The course itself |
| [**5-roadmap/**](5-roadmap/) | Course 4, known gaps, open proposals | What's not built yet |
| [`_system/`](_system/) | Machine-readable graph, validator, vocabulary mapping, source pointers | Maintaining the repo (you can skip this as a reader) |

## Where things stand

- **Shipped and delivered:** all three courses, as slide decks.
- **In this repo:** the full structure of every course (all 63 sub-units, with IDs, types and
  sequence) and one fully written lesson, [*The Role*](4-courses/1-context-engineering-brief/cu-2-when-the-facts-arent-enough/scu-2.1-the-role/artifact.md),
  which is the reference for writing the rest.
- **Not yet in this repo:** the lesson text of the other 62 sub-units (still in the decks) and the
  per-sub-unit skill mapping (in `AI_Native_Skill_Mapper.xlsx`). See
  [`5-roadmap/corpus-gaps.md`](5-roadmap/corpus-gaps.md).

## For contributors

- Authoring a unit or sub-unit: start at [`1-how-we-built-it/authoring-workflow.md`](1-how-we-built-it/authoring-workflow.md).
- AI agents working here: [`CLAUDE.md`](CLAUDE.md).
- Checking the structure: run the validator from this folder.

  ```sh
  env/bin/pip install pyyaml      # once
  env/bin/python _system/tools/validate.py
  ```

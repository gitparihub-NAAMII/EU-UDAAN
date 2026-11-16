# 6-workshops/

Material for **live delivery**: sessions you run in a room. This is the second of the AI Native
programme's two deliverables:

| | `4-courses/` | `6-workshops/` |
|---|---|---|
| What it is | The self-paced course, contributed to Tangible's capability graph | A facilitated session you deliver in person |
| Unit of work | Flow → CU → SCU, anchored to `_system/graph/` | A session: deck, handouts, run-sheet |
| Audience | Learners on the platform, at their own pace | A room, on the day, with a facilitator |
| Gate | `_system/tools/validate.py` (zero errors) | None. The validator does not read this folder |
| Story world | Maya, `kb.world.himalayan-getaways` | Each session can have its own world; record it in the session README |
| Vocabulary | The canon (`_system/tangible-story.md`) and the course frameworks | The session's own (e.g. five dials, not BRIEF). Map it in the session's `crosswalk.md` |

The two tracks feed each other. A workshop is often the quickest way to test a unit before it
becomes SCUs, and a shipped course gives the workshop its exercises. Record the links between
them in each session's `crosswalk.md`, not in `_system/graph/`.

## Rules that still apply here

- **Framework acronyms stay hidden.** Don't use BRIEF, AGENT or TRUST in a workshop. People who
  attend may take the course later, and the course reveals each acronym only at its own
  sub-unit (5.2, 5.0, 5.2). Workshops use their own names for the same ideas.
- **Competency levels** are `awareness | application | mastery | influence`, if you use any.
  The retired four-point scale stays retired here too.
- **Two folders per session: `final/` and `working/`.** `final/` is what you deliver. Don't edit
  it directly. `working/` is where you rebuild. When a rebuild is ready, promote it: copy
  `working/` over `final/`, regenerate `final/slides.md`, and commit with a message saying what
  changed. Older finals stay in git history.
- **Binaries.** The deck in `final/deck/` is committed, so GitHub always has the deck you deliver.
  Every other binary (the `working/` deck, `.docx`, `.pdf`) is gitignored. Each deck has a
  generated Markdown twin, so changes show up in diffs. After you edit a deck, regenerate its twin:

  ```sh
  env/bin/python _system/tools/deck_to_md.py 6-workshops/<session>/working/deck/<deck>.pptx > 6-workshops/<session>/working/slides.md
  ```

- **The course's voice rules** (build manual §3.5) are a strong default here, not a gate. Where a
  workshop deliberately departs from them, note it in `crosswalk.md` so it doesn't drift into
  `4-courses/` unnoticed.

## Sessions

| Session | Status | What it is |
|---|---|---|
| [`ai-nativity-2026/`](ai-nativity-2026/README.md) | `final/`: Part 4 on Gemini skills (2026-11-16). `working/` = copy of final, ready for the next rebuild | One-day, five-part hands-on session: problem solving, context engineering, agentic AI, responsible AI |

## Layout of a session

```
6-workshops/<session>/
├─ README.md        what it is, the agenda, materials, status
├─ crosswalk.md     how it maps to 4-courses/ and _system/graph/, and where it differs
├─ final/           ← deliver this. Change it only by promoting working/
│  ├─ deck/         the .pptx (committed)
│  ├─ handouts/     participant files; README lists what exists
│  └─ slides.md     GENERATED from the deck. Don't hand-edit
└─ working/         ← rebuild here. Same shape as final/
   ├─ deck/         the .pptx (gitignored: work in progress)
   ├─ handouts/
   └─ slides.md
```

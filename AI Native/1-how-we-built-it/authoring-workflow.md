# Workflow

How work moves through this repo, from an idea to a graph contribution.

Two pipelines govern everything here, and they are the same pipeline at different grain:

- **Tangible's authoring flow** — `Idea → Context → Skills → Problem → Outline → Content`
  (story §6.1). This is the *graph anchoring*. It is non-negotiable across every creator
  persona: story §13, *"Structured authoring is the price of admission."*
- **UDAAN's design method** — the eight steps in build manual §3.2. This is the *pedagogy*
  that fills the anchoring in.

Neither replaces the other. The first says what must be declared; the second says what makes
it good.

---

## The one rule

**You cannot author in a vacuum. You author against a problem.**

Story §4.10. If what you're making doesn't attach to a problem in `_system/graph/problems.yaml`,
either attach it or add the problem first. There is no other entry point.

---

## Stage by stage

### 1 · Idea — name the failure, not the topic

Build manual §3.2 step 1. Ask: *what does a competent person do that seems entirely reasonable
and produces a bad outcome?* Write it as the learner's complaint, in their voice.

> Right: *"You fixed the writing. So why are you MORE tired?"*
> Wrong: *"Unit 3: Task Decomposition."*

**Nothing is written yet.** No files change at this stage.

### 2 · Context — find the trap the previous unit set

Build manual §3.2 step 2. The best failure is one *caused by the previous lesson's success*.
This is the strongest structural device in the program and should be the default, not the
exception.

Also settle here: audience, prerequisites, intended outcome.

**Files:** none yet. This is the stage most often skipped, and skipping it is why a unit ends
up being a topic rather than a problem.

### 3 · Skills — anchor to the graph

Pick from `_system/graph/skills.yaml`. If nothing fits, add a skill with `provisional: true` and a
`provisional_reason` — story §4.2 exists so you can propose without blocking on curation.

Declare each at a level from story §4.11: `awareness | application | mastery | influence`.
**These four and nothing else.** The four-point scale in build manual Part IV §4.3 is retired;
see `_system/vocabulary-map.md` §2 for the crosswalk and what that cost.

If the target behaviour is "does this unprompted, in familiar contexts" — which is most of what
this program teaches — declare `application` and set `pedagogy.targets_habit: true`. That
distinction is filed upstream as an open question (Q1) and this is how it survives until answered.

**Files:** `_system/graph/skills.yaml` if proposing anything new.

### 4 · Problem — attach it

Either an existing problem in `_system/graph/problems.yaml`, or a new one. A new problem needs a domain,
a creator-of-record, a difficulty, and at least one flow — the validator enforces the last one
unless `status: unbuilt`.

**Files:** `_system/graph/problems.yaml`.

### 5 · Outline — decide the concept cycles, then generate structure

Build manual §3.2 step 3: list every concept the failure implies. **Each becomes one
`DISCOVER IT YOURSELF` sub-unit.** Two or three is typical; more than three and the unit is
really two units.

The unit arc is fixed (build manual §3.1):

```
EXPERIENCE THE PROBLEM  →  DISCOVER IT YOURSELF ×n  →  PUT IT TOGETHER
```

Course-opening units run lighter (`EXPERIENCE → TRY IT YOURSELF → NAME IT & GENERALISE`);
course-closing units add `THE PAYOFF` then `THE WHOLE JOURNEY`.

**The number of Discover cycles is set by how many concepts the unit carries, not by a target
length.**

Then declare `liftable` honestly per SCU. Only concept cycles are durable corpus assets; the
rest is flow-local connective tissue, and saying so is better than claiming reuse the pedagogy
doesn't support. `_system/vocabulary-map.md` §1.1.

**Files:** `4-courses/<problem>/flow.yaml`, `cu-*/cu.yaml`, `cu-*/scu-*/scu.yaml`.
`_system/tools/seed_corpus.py` shows the shape; write new ones by hand.

### 6 · Content — the 8-step flow, inside each DISCOVER SCU

Build manual §3.1 Level 2. This is the atomic teaching unit of the whole program.

| # | Step | Non-negotiable |
|---|---|---|
| 1 | Think first | Everyday-life question. **AI is not mentioned.** Then hold the answer |
| 2 | Experience | Live the problem. **No label tells you it's a problem** |
| 3 | Look again | Re-read the failure; the evidence was always on the page |
| 4 | Discover the fix | Baseline, then *add this → the result changes.* **2–4 times** |
| 5 | Name it | The term arrives **only now**, with the mechanism |
| 6 | The intuition | An ordinary-life analogy that makes it portable |
| 7 | Your turn | Three applications, different contexts |
| 8 | Generalise + bridge | Then open the next problem |

Order matters, and two orderings in particular:

- **Find the everyday analogy before designing the experiment** (§3.2 step 4). If you can't find
  it, the concept isn't understood well enough to teach yet.
- **Write the naming slide last** (§3.2 step 6). Only after the analogy and the experiment exist.
  Never give the term without the mechanism.

At least one experiment variant must **reveal the learner's own default behaviour** — the way
the third role in C1 2.1 turns out to be the failure they already had. That's what converts four
examples into an explanation.

Reference implementation: `4-courses/1-context-engineering-brief/cu-2-when-the-facts-arent-enough/scu-2.1-the-role/`.
Read it before writing a new one.

**Files:** `artifact.md` in the SCU directory; set `artifact.path` and `artifact.tier` in `scu.yaml`.

---

## Gates

Nothing ships without passing both. They are different checks and neither substitutes for the other.

### Graph gate — mechanical

```sh
env/bin/python _system/tools/validate.py
```

Zero errors. `INCOMPLETE` is allowed and expected — it is the honest record of missing work, and
suppressing it would be worse than showing it (story §13, *"provenance over assertion"*).
Use `--strict` when you intend a section to be genuinely complete.

### Pedagogy gate — human

Build manual §3.7, the pre-ship checklist. Run it against every sub-unit. The checks a validator
cannot make:

- The problem is experienced before any concept is named
- Step 1's question does not mention AI
- No technical term appears before its naming slide
- Every experiment changes exactly one variable, with 2–4 variants
- At least one variant reveals the learner's own default
- Every artifact is shown in full, not summarised
- Readable with no facilitator; no external downloads
- Every named concept has a practice; every practice names a concept

Framework integrity (unit 5 only): each letter traces to a specific suffered problem, the acronym
was never announced in advance, the reveal follows the five-slide shape.

---

## The maintenance loop

Authoring is not the only work here, and the second loop is the one that gets forgotten.

**Per model generation — re-run every shipped experiment.** Build manual §4.6 calls this *"the
highest-risk maintenance item in the program: if a shipped experiment stops reproducing, the
sub-unit built on it silently becomes false."* Two named instances: the four-role experiment
(`scu.c1.u2.1`) and the swap test (`scu.c3.u3.2`).

The word is *silently*. Nothing fails; the slide just stops being true. This is the strongest
argument for raising both to Tier 3 — a live artifact degrades visibly.

**Quarterly — review the figures.** `kb.evidence.adoption-figures` is version-stamped and marked
`staleness: high` for this reason. Several of those numbers are the program's standing arguments
and several will be wrong within a year.

**Per cohort — three fields.** Build manual §4.6: which sub-unit produced the most confusion,
which experiment failed to land, which learner example was better than the one in the slides.
This is the minimum viable version of story §11's "infrastructure not programs" commitment, and
nothing in this repo currently captures it.

---

## When you find a problem with the canon

`_system/tangible-story.md` is vendored and read-only. Don't patch it locally.

1. Write it up in `_system/vocabulary-map.md` §5 as an open question — state the gap, what it
   costs, and a proposed resolution
2. Raise it with Alok or Bishesh
3. When it resolves, re-vendor and update the mapping

Three are open now. Two of them (the missing habit level, the domain/scenario conflation) are
not this program's problems — they will hit any creator whose capability is cross-sector or
whose target behaviour is habitual, which is most of them.

---

## Quick reference

| Task | Start at |
|---|---|
| Write a new sub-unit | Stage 6, after reading the reference SCU |
| Write a new unit | Stage 1 |
| Add a course | Stage 1, then a new problem at stage 4 |
| Add a skill | Stage 3 — `provisional: true` + a reason |
| Fix a mapping decision | `_system/vocabulary-map.md`, then re-run the validator |
| Bring source material in | `_system/source/README.md` |
| Find what's missing | `5-roadmap/corpus-gaps.md` |
| Check the whole repo | `env/bin/python _system/tools/validate.py` |

# Vocabulary map — UDAAN → Tangible substrate

*How the shipped UDAAN AI-Native program expresses itself in the capability-graph vocabulary,
what maps cleanly, what doesn't, and what we decided to do about the gaps.*

This document is repo-local and editable. `tangible-story.md` is not — when this document
finds a genuine gap in the canon, the fix goes upstream (see [Open questions](#5-open-questions-for-upstream)).

---

## 1. The structural mapping

UDAAN has four content levels; Tangible's substrate has five. They line up with one insertion.

| UDAAN | Tangible | Count in the shipped program |
|---|---|---|
| — | **Domain** | 1 (proposed: `ai-native-practice`) — see §4.2 |
| Program (AI-Native) | — *no equivalent; expressed as a domain + 3 problems* | 1 |
| Course | **Problem** (pedagogy mode: a teaching anchor) | 3 |
| Course, as delivered | **Flow** (one approach to the problem) | 3 |
| Unit | **CU** (Content Unit) | 15 |
| Sub-unit | **SCU** (Sub-Content Unit) | 63 |

Tangible §4.10: *"A problem in pedagogy mode is a teaching anchor: 'teach loan processing.'"*
So Course 1 is the problem **"teach context engineering"**, and the shipped five-unit sequence
is one flow against it. A second flow against the same problem is legal and, as §4.2 argues, wanted.

**The count that matters is 63 SCUs.** Tangible §13: *"The SCU is the atomic unit... If the SCU is
well-designed, the platform compounds. If it is not, every layer above it inherits the rot."*
Everything in `4-courses/` is keyed to those 63.

### 1.1 Sub-unit type tags map to SCU roles

Build Manual §3.1 tags every sub-unit with its job. That tag predicts how liftable the SCU is,
which is the single most important corpus-health property (Tangible §6.1, "Compartmentalization").

| UDAAN type tag | Position | Liftable? | Treat as |
|---|---|---|---|
| `EXPERIENCE THE PROBLEM` | X.0 | **No** — narrative setup for this flow only | Flow-local connective tissue |
| `DISCOVER IT YOURSELF` | X.1 … X.n | **Yes** — one complete concept cycle | **Durable corpus asset** |
| `PUT IT TOGETHER` | X.last | **No** — combines this unit's concepts | Flow-local connective tissue |
| `TRY IT YOURSELF` | course-opening variant | Partly | Flow-local |
| `NAME IT & GENERALISE` | course-opening variant | Yes | Durable |
| `THE PAYOFF` | course-closing | No — acronym reveal, flow-specific | Flow-local |
| `THE WHOLE JOURNEY` | course-closing | No | Flow-local |

**The finding:** Build Manual §3.1 records that `THE NAME FOR IT` and `YOUR TURN` each appear
**exactly 17 times** across the 63 decks — one per concept cycle. Those **17 DISCOVER cycles are
the durable, liftable contribution this repo makes to the corpus.** The other 46 sub-units are
high-quality connective tissue authored by hand.

That is not a criticism of the 46. It is a precise statement of what composition (Tangible §8.1)
would later regenerate — *"generated connective tissue between SCUs"* is literally the job the
X.0 and X.last sub-units do today — versus what it never could, because the 17 cycles carry
the pedagogical invention.

Practical consequence: `liftable: true|false` is a required field on every `scu.yaml` here, and
the validator enforces that DISCOVER-tagged SCUs declare their `assumes` list explicitly.

### 1.2 The 8-step flow is intra-SCU structure

Build Manual §3.1 Level 2 (Think first → Experience → Look again → Discover the fix → Name it →
The intuition → Your turn → Generalise + bridge) sits **inside** one DISCOVER SCU. It is the
pedagogical shape of the artifact, not a graph structure. It does not decompose further into
sub-SCUs — the eight steps are not independently liftable and none of them exercises a skill alone.

Recorded on the SCU as `pedagogy.pattern: udaan-8-step` so the corpus can later learn that this
pattern exists and which actors it works for (Tangible §8.2, "how to learn it").

---

## 2. Competency levels — the reconciliation that had to happen

UDAAN Part IV §4.3 proposes its own four-point scale. Tangible §4.11 defines a five-point scale.
**Two scales cannot coexist in one graph.**

### 2.1 The crosswalk

| UDAAN §4.3 (proposed) | Tangible §4.11 (canonical) | Fit |
|---|---|---|
| 0 Unaware — does not recognise the situation as one where the skill applies | 0 not started | Exact |
| *(no equivalent)* | 1 awareness — encountered, can recognize | **UDAAN's scale has no level here** |
| 1 Prompted — applies correctly when told to; does not initiate | 2 application — can use it in a guided context | Close: "when told to" *is* the guided context |
| 2 Habitual — applies it unprompted in familiar contexts | *(falls in the seam between 2 and 3)* | **No clean home** |
| 3 Transferring — applies it in a context the course never showed, and can say why | 3 mastery — can use it independently in novel contexts | Exact |
| *(no equivalent)* | 4 influence — can teach it / extend it / lead others | **UDAAN's scale has no level here** |

The two scales measure different axes. UDAAN's runs on **initiative and transfer**
(told → unprompted → novel). Tangible's runs on **recognition → guided use → independent novel
use → contribution**. They agree at both ends and disagree in the middle.

### 2.2 Decision

**Tangible §4.11 is the only scale used in this repo.** Every `scu.yaml` declares skills at
`awareness | application | mastery | influence`. UDAAN §4.3's scale is retired to this crosswalk
and is not written into any machine-readable file.

Rationale: Tangible §13 — *"Structured authoring is the price of admission for every creator
persona."* The level is what a hiring query filters on (§6.4) and what the validation pipeline
locks in (§5). A second scale would make this repo's contribution unqueryable alongside every
other creator's.

### 2.3 What that decision costs, and why it goes upstream

Dropping "Habitual" is not free, and it should not be quietly absorbed.

The AI Pyramid paper's operational definition of AI nativity — quoted in Build Manual §2.2 and
load-bearing for the whole program — is that nativity is *"observable not in what individuals know
about AI, but in how they **habitually** incorporate, interrogate, and govern AI use in task
formulation, iteration, and problem resolution across diverse contexts."*

**Habit is the core construct of the program**, and Tangible's scale has no level that names it.
`application` ("can use it in a guided context") explicitly implies prompting; `mastery` requires
novel context. The unprompted-in-familiar case — the exact behaviour the UDAAN courses are built
to produce — falls between them.

This is filed as an upstream proposal, not a local workaround. See §5, Q1.

Until it resolves: SCUs targeting habit formation declare `application` and set
`pedagogy.targets_habit: true`, so the distinction survives in the data and can be re-levelled
later without re-authoring.

---

## 3. Direct mappings that need no argument

### 3.1 The bright line is an escalation point

Build Manual, the program's single hardest rule, stated twice in Course 3 (1.5 and 3.4):

> **For a decision about a person, AI recommends and a named human decides.**

Tangible §4.9 defines escalation points as first-class flow primitives declaring a trigger
condition (*"confidence threshold, exception class, **policy rule**"*), a target (*"who or what
receives the handoff"*), the context that travels, and the resumption protocol.

The bright line is exactly that: a **policy-rule trigger** with a **named human** target.

This is the clearest cross-persona reuse available in the program. MSTC's Phase 0 anchor engagement
is a **loan-processing transformation** — a flow whose central act is a decision about a person.
The escalation primitive this teacher-corpus contribution defines is directly the one that
operational flow needs. Modeled in `_system/graph/escalations.yaml` as `esc.bright-line` and referenced
from both C3 SCUs.

### 3.2 The validation pipeline already fits

UDAAN Part IV §4.3's principle — *"Assess the artifact the learner already produces... No separate
exam"* — is Tangible §5 stage 1 (*"Actor finished the SCU(s) and submitted artifacts"*) verbatim
in intent. The three course tangibles are the submitted artifacts:

| Course | Tangible-the-artifact | Pipeline entry |
|---|---|---|
| 1 | A filled one-page BRIEF for the learner's own recurring job | Stage 1 |
| 2 | An AGENT spec + a working Gemini Gem | Stage 1 |
| 3 | A one-page AI policy + a TRUST audit of something already shipped | Stage 1 |

UDAAN's "Level 3 test" column (produce a second BRIEF for an unlike job type; argue a task should
*not* get an agent; find a bright-line decision no course example covered) maps to **stage 3, the
AI Interview** — *"Adaptive Q&A confirms depth (probes edge cases)."* Those three tests are already
written and are good interview seeds. Recorded per-problem as `validation.interview_seeds`.

### 3.3 The swap test is a reusable evaluation primitive

Course 3 Unit 3's method — hold everything constant, change one attribute, compare outputs —
is already reproducible and learner-runnable. Build Manual §4.3 proposes standardising it as the
program's house evaluation technique. It generalises past this program: it is a Tier 3 artifact
(stateful frontend, browser-only state, bounded cost) and an evaluation instrument any creator
persona could reference.

Filed as a candidate cross-corpus contribution rather than a C3-local device.

### 3.4 Artifact tiers — where the shipped material actually sits

Tangible §6.1's tier model against what exists today:

| Tier | Definition | UDAAN today |
|---|---|---|
| 1 | Text and static artifacts — prose, slide-equivalents, PDFs | **All 63 sub-units.** `.pptx` + `.pdf` decks |
| 2 | Frontend-rendered — designed pages, interactive diagrams, quizzes | None shipped |
| 3 | Stateful frontend — calculators, simulations, decision trees | None shipped |
| 4 | Agent-mediated environments | None shipped |
| 5 | Fully engineered learning environments | None shipped |

Two of the program's strongest devices are Tier 1 renderings of things that want to be Tier 3:

- **The four-role experiment** (C1 U2.1) — four prompts, identical facts, one line changed. Today
  the learner reads four outcomes. As Tier 3, they run it.
- **The swap test** (C3 U3) — same CV, name changed, repeated to rule out flukes. Today the learner
  reads the result. As Tier 3, they get the reproduction.

This matters beyond polish. Build Manual §4.6 names it *"the highest-risk maintenance item in the
program"*: both experiments depend on model behaviour that will change, and **if a shipped
experiment stops reproducing, the sub-unit built on it silently becomes false.** A Tier 3 artifact
that runs live degrades visibly instead of silently.

Recorded per SCU as `artifact.tier` (what exists) and `artifact.target_tier` (where it should go).

### 3.5 Commitment 4 is not in tension with the tier model

Build Manual §3.0 commitment 4 — *"Everything lives in the slides · no separate downloads"* —
reads at first like a constraint against richer artifacts. It isn't. The commitment is about
**self-containment and no facilitator dependency**, not about staying static. A Tier 2 or Tier 3
artifact is more self-contained than a deck that describes an experiment the learner can't run.

No conflict. Recorded so the question isn't re-litigated.

---

## 4. Where the mapping is genuinely awkward

### 4.1 Compartmentalization vs. earned jargon

Tangible §6.1: *"A good SCU is self-contained at one level... authored to be liftable."*
Build Manual §3.0 commitments 2 and 3: *"No jargon until it is earned"* and *"The framework is
assembled, never issued."*

These pull against each other by design. UDAAN sub-units are **deliberately** sequence-dependent:
C1 U2.1 ("The Role") cannot be lifted into another flow without the Unit 2 opening failure that
makes the learner want it, and the letter it earns is meaningless until U5.2 reveals BRIEF.

Partial mitigation already in the program: Build Manual §3.5 requires sub-unit descriptions be
written *"to be read alone"* — self-contained enough that a learner arriving mid-course is not lost.
So the discipline exists at the description level; it's the pedagogical dependency that doesn't lift.

**Resolution taken here:** don't pretend. Every SCU declares `assumes` (the SCU ids whose experience
it depends on) and `liftable`. The 17 DISCOVER cycles are marked liftable with an explicit `assumes`
list; the 46 connective sub-units are marked `liftable: false`. That gives the composition engine
honest input instead of a corpus that claims more reusability than it has.

### 4.2 Domain rollup gives the wrong answer

Tangible §4.1: *"A skill belongs to a domain **only via a problem it has been exercised in**.
Domains are not hand-tagged onto skills; they roll up from completed work."*

Every UDAAN problem is set in Nepali trekking and travel — Maya Gurung at Himalayan Getaways. Run
the rollup literally and all 20 skills in this contribution acquire the domain `travel-tourism`.

That is misleading in both directions. The capability taught is general professional practice; the
scenario is travel. A learner who finishes Course 3 has not demonstrated responsible-AI capability
*in the travel sector* in any sense a hiring query should trust, and the travel tag will suppress
matches in every sector that actually matters commercially.

**Two moves, one now and one proposed.**

*Now:* a new applied domain `ai-native-practice` anchors the three problems, with the scenario
setting recorded separately as `scenario_domain: travel-tourism`. Both are in `_system/graph/domains.yaml`.
`ai-native-practice` is marked `provisional: true` pending upstream curation (Tangible §4.2's
provisional-skill mechanism, applied to a domain).

*Proposed:* re-skin the same 17 concept cycles into banking as a **second flow** against the same
three problems. Tangible §4.8 explicitly allows multiple flows per problem. The case:

- Tangible's existing traction is banking — NMB, Kamana Sewa, Laxmi Sunrise, F1Soft (story §12.5)
- The Phase 0 anchor engagement is a **banking** loan-processing transformation (§11)
- A banking flow makes these SCUs roll up into the `banking` domain, which is where the
  commercially relevant evidence needs to sit
- It costs nothing in localisation fidelity: Build Manual §3.6 requires the sector be *"one a
  Nepali learner understands without explanation, with visible stakes"* — and NMB and Laxmi Sunrise
  are Nepali banks. Banking satisfies every one of the seven §4.4 localisation criteria as well as
  trekking does
- The pedagogical invention is in the 17 cycles, not the scenario. Re-skinning is scenario work,
  not design work

Filed in `5-roadmap/` as the highest-leverage item in the repo, not actioned.

### 4.3 The program level has no home

UDAAN's Level 1 capability — *AI-Native Professional Fluency*, "after the whole program" — sits
above three problems. Tangible's substrate has no object between Domain and Problem. There is no
"program" or "curriculum" type.

Not a defect worth escalating on its own: the three-course chain is a sequencing claim, and
sequencing between problems is exactly what typed `prereq` edges express. Modeled as `prereq`
edges between the three problems' terminal skills rather than as a container object. The
program-level capability statement lives in `_system/graph/problems.yaml` as prose on the domain.

Worth knowing that Build Manual §1.1's strongest structural device — *"each course's opening trap
is created by the previous course's success"* — survives as edges but loses its narrative force in
the graph. That's acceptable; the narrative lives in the artifacts.

### 4.4 The fourth skill area is missing

Build Manual §2.4 names four AI-Native skill areas; three are shipped. **AI-Enabled Problem Solving**
has no course, and Build Manual §4.2 carries a `[PROPOSAL]` draft (framework SOLVE, sycophancy as
the strongest available unit).

In graph terms this is a fourth problem with no flow attached. Recorded in `_system/graph/problems.yaml`
as `prob.ai-enabled-problem-solving` with `flows: []` and `status: unbuilt`, so the gap is queryable
rather than only described in prose. The draft stays in `5-roadmap/`.

---

## 5. Open questions for upstream

These are gaps in the canon that this contribution surfaced. They go to Alok or Bishesh per the
`tangible-story.md` header; they are not resolved locally.

**Q1 — The competency scale has no level for habit.** (§2.3 above.) The AI Pyramid paper defines
nativity in terms of habitual incorporation; Tangible §4.11 jumps from guided use (`application`)
to independent novel use (`mastery`) with nothing between. Every capability whose target behaviour
is "does this unprompted, in familiar contexts, without being told" — which is most professional
capability, not just this program's — has no level to declare. Proposal: either insert a level
between `application` and `mastery`, or document that `application` spans prompted and habitual and
accept the loss of resolution. Note the paper is by Tangible's own CEO and CSO, so the two documents
should not disagree about what capability means.

**Q2 — Domains conflate sector-of-scenario with domain-of-capability.** (§4.2 above.) §4.1's rollup
rule assumes the problem's sector is the domain worth recording. For pedagogical problems with
fictional settings, that produces a domain tag that actively misleads hiring queries. Proposal:
either allow a problem to declare capability-domain and scenario-domain separately, or state that
cross-sector capability problems should be re-skinned per sector rather than tagged generically.

**Q3 — Is a pedagogically sequence-dependent SCU a first-class citizen?** (§4.1 above.) §6.1 asks
creators to author liftable SCUs. Good pedagogy of the kind §3.0 commitments 2 and 3 describe
produces deliberately non-liftable units, and they carry real value. Proposal: make `liftable` an
explicit declared property with corpus-health metrics that expect a mix, rather than an implicit
quality bar that well-designed narrative pedagogy fails.

---

## 6. Quick reference

```
Domain            ai-native-practice (provisional)  ← proposed second: banking
  └─ Problem      "teach context engineering"       (Course 1)
       └─ Flow    the shipped 5-unit sequence       ← proposed second flow: banking re-skin
            └─ CU     Unit 1 … Unit 5               (5 per problem, 15 total)
                 └─ SCU   sub-unit                  (63 total, 17 of them liftable)
                      ├─ skills[]     at awareness | application | mastery | influence
                      ├─ knowledge[]  the frameworks, the case material, the source docs
                      ├─ artifact     tier 1 today; tiers 2–3 targeted for the experiments
                      └─ assumes[]    honest declaration of pedagogical dependency
```

| Read this when | Go to |
|---|---|
| You need the canonical substrate definitions | `tangible-story.md` §4 |
| You need the UDAAN design method | `udaan-build-manual.md` Part III |
| You need to know why a mapping decision was made | this document |
| You need institutional context, sources, bibliography | `udaan-context-and-sources.md` |
| You are authoring | `../WORKFLOW.md` |

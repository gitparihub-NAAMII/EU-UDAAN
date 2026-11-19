# The health programme: five problems, five ways

Five courses for people who work in health, each on one problem from the problem bank, each
told from one desk in one stretch of Nepal's health system, and each taught a different way. A
learner takes the course for their desk and learns the way that course teaches; the five
together are the programme.

**Status:** designed and scaffolded 2026-11-19. Five course skeletons (5 units, 22 sub-units
each), one written lesson per course, one shared world, five framework candidates. Nothing
reviewed by the programme leads or by anyone who works in these facilities. No AI failure
reproduced. The method is in [`1-how-we-built-it/five-ways.md`](../1-how-we-built-it/five-ways.md).

---

## Why five ways

The shipped courses teach one way: a protagonist, a failure lived in full, a concept discovered
and only then named. It works, and it is one way. Tangible's story (§8.2) names *how to learn
it* as a dimension the platform personalises on, next to *what to learn*, and says the platform
learns which approaches work for which actors from telemetry across the corpus. A corpus that
teaches everything one way gives it nothing to learn that from.

So the health programme holds its method constant where the method is the point (the problem
before the concept, no jargon until earned, the framework assembled, everything shown in full,
one change at a time, a human line in every course) and varies the one thing the shipped
courses never varied: where the failure is lived and what the unit produces.

| Way | Where the failure is lived | What each unit produces |
|---|---|---|
| **Story** | In a protagonist's week, told in full | A line on the one-page sheet |
| **Rounds** | In your own commitment, before the reveal | A line in the rounds book |
| **Drill** | In your own cold run, against the clock | A reflex card |
| **Audit** | In your own investigation of the evidence | A finding memo |
| **Build** | On your own desk, in a real job done the usual way | A part of the kit |

---

## The map

| Course | Problem | Type of work | Who, where | The way | Candidate word | Reference lesson |
|---|---|---|---|---|---|---|
| [Plain-Nepali patient instructions](../4-courses/health-h1-patient-instructions/) | H1 | 7 · official words into plain words | Pooja, staff nurse, PHCC in Bardiya | Story | SAFER | 2.1 Check it backwards |
| [The monthly report that says what was counted](../4-courses/health-h2-hmis-reporting/) | H2 | 1 · same output, new contents | Sangita, HMIS focal person, the same PHCC | Audit | COUNT | 1.2 The figure nobody counted |
| ["What is the current rule?"](../4-courses/health-h3-current-rule/) | H3 | 4 · the question that keeps coming back | Nirmala, public health officer, health office in Gulariya | Build | REPLY | 2.1 Quote before you explain |
| [Checking a health claim before it is shared](../4-courses/health-h4-health-misinformation/) | H4 | 7 · official words into plain words | Sunil, information officer, Nepalgunj hospital | Drill | SHARE | 2.1 A link you haven't opened |
| [The referral note that carries findings, not the call](../4-courses/health-h5-referral-notes/) | H5 | 3 · the draft that has to pass | Ramesh, health assistant in charge, health post in rural Bardiya | Rounds | ROUTE | 2.2 "Did you measure that?" |

These are the five health problems the bank review passed
([`5-roadmap/sector-problem-statements.md`](../5-roadmap/sector-problem-statements.md)): H1, H2
and H5 as written, H3 reframed as the review asks (the recurring work is staff asking for the
current rule), H4 with the review's caveat that the evidence for its scale is low and
practitioners should be asked first. H6 (duty rosters) is not a fit and is not built.

The health-tech course, [D1 · Insurance claims](../4-courses/healthtech-d1-insurance-claims/),
is set in the same Nepalgunj hospital and taught the Story way. It is a sixth route through the
same world, from the insurance desk, and it is unchanged.

Each candidate word is provisional (build manual §3.3: letters are earned from failures, not
fitted to a word), revealed only in its course's payoff sub-unit, and carried in
`_system/graph/knowledge.yaml` with its disclosure rule.

---

## One world, five desks

The five courses share a world, `kb.world.bheri-corridor`, so that the five perspectives are
perspectives on one system and not five unrelated stories.

- **A health post** in a rural palika of Bardiya. Ramesh (H5) is in charge and refers patients
  down the road and, for emergencies, to Nepalgunj.
- **The primary health care centre** on the highway, an hour from Nepalgunj. Pooja (H1) works
  the counter; Sangita (H2) keeps the registers; Dr. Rijal is the only doctor; Phulmati, an
  FCHV, speaks Tharu.
- **The health office** in Gulariya. Nirmala (H3) answers the phone when a circular changes.
- **The 100-bed private hospital** in Nepalgunj. Sunil (H4) runs its page and its phone; Dr.
  Basnet reads referral notes in the emergency; Bikash, Ms. Karki and Dr. Adhikari are there
  exactly as D1 describes them.

**One file passes every desk.** An adult patient from rural Bardiya, always anonymised, is seen
at the health post on the 1st and referred (Ramesh's note), admitted in Nepalgunj on the 3rd,
operated on by Dr. Adhikari, discharged on the 6th, comes to Pooja's counter with the discharge
slip, is counted in Sangita's report, has the claim checked by Bikash, is the subject of a call
to Nirmala about the follow-up rule, and of a post about the hospital that lands on Sunil's
phone. Only the closing unit of each course touches the episode; the dates are the ones already
in D1 2.1. A learner who takes a second course meets the same file from another desk.

The rule that makes this safe (`CLAUDE.md`): a character may appear in more than one course and
is never re-characterised. The first course to describe a character is the one the others agree
with. Nobody borrows from Maya's world.

---

## What the five courses teach in common

Each course earns its own five concepts from its own five failures; no course's concepts are
imposed on another. But the same checks keep being earned, from different desks, in different
forms. That recurrence is the programme's capability, and it is what the graph will show as
shared skills once a skill mapper row exists for these courses.

| The check, in plain words | Where it is earned |
|---|---|
| Point to the words. A verdict, a flag or an answer without a source you can open is a guess | D1 U2 · H3 U2 · H4 U1, U2 |
| One current version, with its date | D1 U3 · H2 U3 · H3 U3 |
| Confirm what it read before trusting what it concluded | D1 U4 · H4 U4 · H5 U4 |
| Nothing that isn't in the source. "Not measured", "not recorded", "not counted" are findings; a plausible value is not | H1 U4 · H2 U2, U5 · H5 U2 |
| The source is fixed, and checked both ways | H1 U1, U2 · D1 U1 |
| Written for the reader and the channel | H1 U3 · H4 U3 · H5 U1, U3 |
| A named person decides, signs, or speaks. AI never makes the call | Every course, Unit 5 |

Three escalation points carry the human lines across the programme
(`_system/graph/escalations.yaml`): the bright line (a decision about a person is a named
human's: H5, D1), the signer checks the source (H1, H2, H3, H4), and a fluent reader checks the
translation (H1).

**Skills are not assigned.** The outlines name likely candidates from the shipped pool (AI Output
Validation & Contextual Auditing, Source Grounding & Hallucination Control, Audience-Aware AI
Communication, Confidential Information Handling, Responsible AI Use & Compliance). They go on
the SCUs only when a skill mapper row exists (story §13, provenance over assertion).

---

## Choosing a way

For a learner, one line each:

- You learn by reading and recognising yourself: **Story** (H1).
- You learn by deciding first and being shown: **Rounds** (H5).
- You learn by doing, under the clock: **Drill** (H4).
- You learn by digging until the evidence gives way: **Audit** (H2).
- You learn by making something you'll keep using: **Build** (H3).

For the programme, the order to deliver in: Story is proven. Rounds and Drill fit clinical
learners, who already learn from cases and stations. Audit is slow by design and needs learners
who will do the dig. Build needs learners who already have the desk, and is the way most likely
to need a facilitator (five-ways.md §4).

A learner's desk picks their course; their course picks their way. The pairings here are the
designer's judgement about which way fits which problem, not a rule: story §4.8 allows more
than one flow per problem, and the intended next step after a cohort is a second flow in another
way for the problem learners asked for most, so that the graph holds the same capability taught
two ways.

---

## What has to happen before any more lessons are written

1. **Reproduce the failures.** Twenty-four tool failures across the five courses (each course
   README lists its five under "Before any more lessons are written"; H3's fifth is social). On
   free ChatGPT and free Gemini, three runs each, fresh chats. A unit whose failure doesn't
   reproduce is rebuilt around one the tools do produce, not staged.
2. **Reviews.** A clinician or pharmacist on every slip, case and claim (H1, H4, H5); an HMIS
   focal person and someone who knows the current indicator definitions (H2); someone who fields
   the calls at a health office (H3); fluent Tharu and Awadhi readers (H1 Unit 5); two or three
   people who answer the public for a facility, because H4's evidence is rated low; and the
   programme leads on the cast, the shared world, the five pairings and the `health` domain.
3. **Deliver one non-Story way to a cohort** and record the three per-cohort fields in
   `1-how-we-built-it/authoring-workflow.md` (most confusing sub-unit, experiment that failed to
   land, learner example better than the lesson's), plus one more: which way the learner would
   have chosen. That is the first telemetry of the kind story §8.2 describes.
4. **Tier 3 first for the ways that strain on a page:** the commit in Rounds, the clock in
   Drill. Each course's `scu.yaml` names the sub-units and the reason.
5. **Skills**, from a skill mapper row, not before.

---

## In graph terms

- **Domain:** `health`, provisional (added with D1; whether health-tech separates is open).
- **Problems:** five, `status: draft`, each with `way`, `work_type` and `problem_bank_id`
  recorded, and a validation artifact and interview seed each (`_system/graph/problems.yaml`).
- **Flows:** five, one per problem, each declaring its `pedagogy_pattern`. Flow ids carry the
  approach: `…udaan-v1`, `…audit-v1`, `…build-v1`, `…drill-v1`, `…rounds-v1`.
- **Content:** 25 units, 110 sub-units, ids `cu.h1.*` to `cu.h5.*` and `scu.hN.uX.Y`,
  permanent. 50 of the 110 are liftable (two per unit), with explicit `assumes` lists.
- **Knowledge:** one world (`kb.world.bheri-corridor`), five practice-material bases
  (`kb.rules.practice-*`), five framework candidates (`kb.framework.*`, provisional, each with a
  disclosure rule).
- **Escalations:** `esc.bright-line` (H5), and two new ones proposed in the D1 and H1 outlines
  and added here: `esc.signer-checks-source` (H1–H4) and `esc.fluent-reader-check` (H1).
- **Validator:** type tags are now per pattern (`_system/tools/validate.py`), and a sub-unit's
  tag must belong to its flow's way. A flow that declares no way is the Story way.
- **Scaffold:** `_system/tools/scaffold_health.py`, one-time, kept for auditability. It holds
  the five course designs as data and skips files that exist.

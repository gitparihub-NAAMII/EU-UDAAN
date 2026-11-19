# Five ways to teach the same thing

The build manual (Part III) describes one way of teaching: a story, a failure lived through a
protagonist, a concept discovered and only then named. It works. It is also one way, and
Tangible's story §8.2 names "how to learn it" as a dimension the platform will personalise on:
*"Some learners learn best from agent-mediated environments; others from text-and-quizzes;
others from heavy-simulation environments."* A corpus that only ever teaches one way gives the
platform nothing to learn that from.

The health programme (`3-course-flow/health-programme.md`) teaches five problems five ways. This
file is the method: what the five ways share, what each one is, and how each one is declared in
the graph so the validator can check it.

**Status:** method proposal, 2026-11-19. Only the Story way has been delivered to learners. The
other four exist as course skeletons with one written lesson each. Treat the lineage notes as
the evidence layer: they say where each way comes from, and they need checking by the programme
leads before anything ships.

---

## 1. What every way keeps

These come from the build manual's six commitments (§3.0) and the voice rules (§3.5), and they
hold in every way. A way that drops one of them is not a different way of teaching; it is a
worse one.

| Invariant | What it means in every way | Build manual |
|---|---|---|
| **The problem comes first** | The learner lives a failure before any concept is named. The ways differ in *how* the failure is lived: told, committed to, run cold, dug out, or paid for on your own desk | §3.0 (1) |
| **No jargon until earned** | A term arrives only after the gap it names has been felt | §3.0 (2) |
| **The framework is assembled** | Each unit earns one letter; the word is revealed in the last unit, never announced | §3.0 (3), §3.3 |
| **Everything is in the lesson** | Readable alone, no facilitator, no download | §3.0 (4) |
| **Show it, don't summarise it** | The note, the report, the circular, the post, the slip: in full | §3.0 (5) |
| **One change at a time** | Each way has an *evidence move* that isolates one cause (§3 below) | §3.0 (6) |
| **The voice** | Second person for the learner, third person for the protagonist. Never "simply." No claim about what AI "understands" or "knows": describe mechanism. Never blame the learner; the failures are structural | §3.5 |
| **The human line** | Every course says what AI never decides, and a named person signs | `_system/graph/escalations.yaml` |

The same people check the same things in the room: the pre-ship checklist (§3.7) applies with
the type tags of the way in place of the UDAAN tags.

---

## 2. The five ways at a glance

| Way | In one line | Where the failure is lived | The unit's tangible | Pick it when the learner… | Pattern id |
|---|---|---|---|---|---|
| **Story** | Follow someone through the failure, then discover the fix yourself | In a protagonist's week, told in full | A line on the one-page sheet | learns by reading and recognising | `udaan-8-step` |
| **Rounds** | Commit on a case, then see the record | In your own commitment, before the reveal | A line in the rounds book | learns by deciding and being shown | `rounds-staged-case` |
| **Drill** | Run the station cold, debrief, run it again | In your own cold run, against the clock | A reflex card | learns by doing, under pressure | `drill-station` |
| **Audit** | The report is on your desk; find where it's wrong | In your own investigation of the evidence | A finding memo | learns by digging | `audit-investigation` |
| **Build** | Make the tool part by part, testing it on your own work | In a real job from your own desk, done the usual way | A part of the kit | learns by making something they keep | `build-the-kit` |

Five units in every way, one concept per unit, one letter per unit. The closing unit adds the
two course-closing sub-units from the build manual (`THE PAYOFF`, `THE WHOLE JOURNEY`), because
the reveal has one shape (§3.3 rule 4) whichever way the letters were earned.

### Lineage (evidence layer)

- **Story** is the UDAAN method as shipped: problem-based learning in the Barrows and Tamblyn
  (1980) sense, with the build manual's 8-step flow as the atomic unit.
- **Rounds** is the case method as clinical teaching uses it: the case is disclosed in stages
  and the learner commits before each reveal. Committing first is what makes the reveal teach
  (Schwartz and Bransford 1998, "a time for telling"; retrieval before instruction, Roediger and
  Karpicke 2006). The "attending's question" is the senior's habit of asking one question that
  would have caught it.
- **Drill** is simulation-based education: stations in the OSCE sense (Harden et al. 1975),
  repetition with feedback in the deliberate-practice sense (Ericsson et al. 1993), and a
  debrief that treats the miss as structural rather than personal (Rudolph et al. 2006).
- **Audit** is inquiry-based learning in the shape of a data-quality review, which is real work
  for HMIS staff (the WHO data quality review toolkit, 2017). Letting the learner struggle with
  the evidence before the explanation is what Kapur (2008) calls productive failure.
- **Build** is constructionism (Papert 1980): the learner makes a working thing they will use,
  with worked examples that fade (Collins, Brown and Newman 1989).

None of this is cited inside a lesson. The protagonist's story carries no citations.

---

## 3. Each way in detail

Every way has the same two levels as the build manual (§3.1): a **unit shape** made of typed
sub-units, and a **step flow inside the concept-carrying sub-unit**. The concept-carrying
sub-unit is the liftable one; the rest is flow-local connective tissue (`vocabulary-map.md` §1.1).

Each way also names its **evidence move**: the thing that does what the one-variable experiment
does in the Story way, so the causal claim is seen, not asserted.

### 3.1 Story — `udaan-8-step`

As the build manual §3.1. Unit shape: `experience-the-problem` → `discover-it-yourself` ×n →
`put-it-together`; opening variant `try-it-yourself` → `name-it-generalise`; closing
`the-payoff` → `the-whole-journey`. Step flow: the eight steps. Evidence move: **the
experiment**, 2–4 variants, one variable, one of them the learner's own default.

Reference lesson: C1 2.1 *The Role*; in the health programme, H1 2.1 *Check it backwards*.

### 3.2 Rounds — `rounds-staged-case`

Each unit is one case, presented the way a case is presented on a ward round: in stages, with
the learner committing before each stage is revealed.

| Position | Tag | Job | Liftable |
|---|---|---|---|
| X.0 | `present-the-case` | The chart in brief, then what the AI wrote, in full. The commit: *send it or not, and what would you check first?* Hold the answer | no |
| X.1 | `reveal-the-record` | The record, in full, beside the AI's note. The gap between what you committed to and what was there | no |
| X.2 | `the-attending-question` | The one question that would have caught it. Named, with the mechanism and the picture | **yes** (assumes X.0, X.1) |
| X.3 | `your-case` | Three more cases in brief, worked with the question. The line for the rounds book | **yes** (assumes X.2) |

Step flow inside `the-attending-question`:

| # | Step | What it must do |
|---|---|---|
| 1 | **The case, as presented** | The chart in brief and the AI's note, recapped so the sub-unit reads alone |
| 2 | **What you committed to** | Hold it. Most readers signed it; say so without blame |
| 3 | **The record beside the note** | The evidence move: line by line, the note on the left, the record on the right. The gap shows itself |
| 4 | **The question** | The one question a senior asks. Named only now |
| 5 | **Why the note came out that way** | Mechanism, not blame: what the tool predicts a note of this kind contains |
| 6 | **The picture** | An ordinary-life analogy |
| 7 | **One more case, now** | A short case, worked with the question |
| 8 | **The rounds-book line, and the next case** | The line the learner writes down, then the bridge |

Evidence move: **the side-by-side**. Closing: 5.4 `the-payoff` is the grand round (five
questions, each traced to its case, then the word and the rounds book); 5.5 `the-whole-journey`.

Reference lesson: H5 2.2 *Did you measure that?*

### 3.3 Drill — `drill-station`

Each unit is one check, drilled. The learner runs a station cold, sees the answer sheet, is
debriefed, and runs two more stations with the check.

| Position | Tag | Job | Liftable |
|---|---|---|---|
| X.0 | `station-cold-run` | A scenario and a clock. Run the check the way you'd do it today. Then the answer sheet | no |
| X.1 | `debrief` | What slipped past, why it slipped (mechanism, structural), the check named, the picture | **yes** (assumes X.0) |
| X.2 | `station-with-the-check` | Two more scenarios, varied, run with the check, scored against the rubric | **yes** (assumes X.1) |
| X.3 | `reflex-card` | The card for the deck: the trigger, the check in three lines, pass or fail | no |

Step flow inside `debrief`:

| # | Step | What it must do |
|---|---|---|
| 1 | **Your run** | What you had, what you did, what you concluded, recapped so the sub-unit reads alone |
| 2 | **The answer sheet** | What was there, in full |
| 3 | **Where it slipped past** | Look again: the evidence was on the page |
| 4 | **Why it slipped** | Mechanism. The station is built so that the cold run misses it; everyone misses it |
| 5 | **The check, named** | Only now |
| 6 | **The picture** | An ordinary-life analogy |
| 7 | **One rep, right now** | A thirty-second station with the check |
| 8 | **The card, and the next station** | What goes on the card, then the bridge |

Evidence move: **the rep**: the same station with and without the check. Closing: 5.4
`the-payoff` is the full shift (one station with all five checks, then the word and the deck);
5.5 `the-whole-journey`.

Reference lesson: H4 2.1 *A link you haven't opened*.

### 3.4 Audit — `audit-investigation`

Each unit is one investigation. Something that reads as finished lands on the desk, with the
records it was made from, and the learner has to decide whether to sign it.

| Position | Tag | Job | Liftable |
|---|---|---|---|
| X.0 | `the-handover` | What lands on your desk: the output, in full; the records it came from, in full; the request to sign. Nothing says what's wrong | no |
| X.1 | `dig` | The investigation, as questions: pick a figure, find its line, compare. The working shown step by step | no |
| X.2 | `the-finding` | What the evidence shows, as a finding. Why the output came out that way. The rule, named, with the picture | **yes** (assumes X.0, X.1) |
| X.3 | `the-memo` | The finding memo, written. The rule applied to two more reports. The line for the protocol | **yes** (assumes X.2) |

Step flow inside `the-finding`:

| # | Step | What it must do |
|---|---|---|
| 1 | **What was on the desk** | Recapped so the sub-unit reads alone |
| 2 | **The figure you followed** | One figure, chosen |
| 3 | **The register line** | The evidence move: the trace from the figure to its line, shown |
| 4 | **The finding** | Stated as evidence, in the form a memo would use |
| 5 | **Why the report came out that way** | Mechanism |
| 6 | **The rule, named** | Only now |
| 7 | **The picture** | An ordinary-life analogy |
| 8 | **Apply it once, and the next report** | One more figure, then the bridge |

Evidence move: **the trace**, one figure followed to its source line. Closing: 5.4 `the-payoff`
is the audit protocol (five findings, each traced to its investigation, then the word); 5.5
`the-whole-journey`.

Reference lesson: H2 1.2 *The figure nobody counted*.

### 3.5 Build — `build-the-kit`

Each unit adds one part to a kit the learner keeps. The failure is lived on the learner's own
desk: a real job, done the usual way, with its cost.

| Position | Tag | Job | Liftable |
|---|---|---|---|
| X.0 | `the-job` | A real task from the desk, done the usual way with AI. What came back, in full, and what it cost | no |
| X.1 | `spec` | What this part of the kit must do, derived from the failure. The requirements, the concept named with its mechanism, the picture | **yes** (assumes X.0) |
| X.2 | `build-and-test` | Make the part. The worked example, in full. Test it on three items; the log; the fix | **yes** (assumes X.1) |
| X.3 | `ship-it` | Into the kit, with a version and a date. The hand-over note. Who checks it | no |

Step flow inside `spec`:

| # | Step | What it must do |
|---|---|---|
| 1 | **The job** | Recapped so the sub-unit reads alone |
| 2 | **What came back, and what it cost** | In full |
| 3 | **Look again** | The line that did the damage |
| 4 | **Why it came out that way** | Mechanism |
| 5 | **The requirement, written** | Three to five lines: what the part must do and must never do |
| 6 | **The concept, named** | Only now |
| 7 | **The picture** | An ordinary-life analogy |
| 8 | **Three desks that need the same part, and what you'll build next** | Then the bridge |

Evidence move: **the test log**: three items, before and after the part. Closing: 5.4
`the-payoff` is the kit assembled (five parts, each traced to its job, then the word); 5.5
`the-whole-journey`.

Reference lesson: H3 2.1 *Quote before you explain*.

---

## 4. Where each way strains

Said plainly, so nobody discovers it in a cohort.

- **Story** depends on the protagonist being believed. A learner who doesn't recognise
  themselves in Pooja reads it as someone else's problem.
- **Rounds** depends on the learner committing honestly before the reveal. On a page, nothing
  stops them scrolling. The commit is the first thing to move to Tier 3.
- **Drill** depends on the clock. Read without one, a station is a worked example. It also
  risks teaching the check without the judgement; the debrief has to carry the why.
- **Audit** is slow, and the slowness is the point. A learner who wants the answer will skip
  the dig, and then the finding is just a fact.
- **Build** depends on the learner having a desk. Someone not yet in the job builds a kit for
  nobody. It is the way most likely to need a facilitator.

---

## 5. In graph terms

- The way is a property of the **flow**: `pedagogy_pattern` in `flow.yaml`, one of the five
  pattern ids. A flow with no `pedagogy_pattern` is `udaan-8-step` (the three shipped courses
  and D1).
- Each pattern has its own **type-tag vocabulary** (the tables above), plus the two shared
  closing tags. `_system/tools/validate.py` checks that every SCU's `type_tag` belongs to its
  flow's pattern.
- The concept-carrying SCU in each pattern declares `pedagogy.pattern` and `liftable: true`
  with an explicit `assumes` list, exactly as the Story way does for `discover-it-yourself`.
- Liftability is per SCU and honest. In every way, two of four sub-units per unit are durable
  corpus assets and two are connective tissue. That ratio is the same as the shipped courses'.
- Story §4.8: *"A problem can have multiple flows."* The five health problems each carry one
  flow today. The design intent is the other direction too: once a way has been delivered, any
  health problem can get a second flow in another way, and the graph then holds the same
  capability taught two ways, which is what §8.2 needs.

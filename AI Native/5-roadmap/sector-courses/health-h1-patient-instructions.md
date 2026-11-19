# [PROPOSAL] Health sector course: plain-Nepali patient instructions (H1)

**Status:** draft outline, 2026-11-16. Skeleton built 2026-11-19 in
`4-courses/health-h1-patient-instructions/` (flow, 5 units, 22 sub-units, one lesson drafted: 2.1) as
the Story way of the health programme (`3-course-flow/health-programme.md`). Not reviewed by the
programme leads or by a clinician. None of the AI failures below has been reproduced yet. See [Test before writing](#test-before-writing).

**Chosen problem:** H1 · Plain-Nepali patient instructions, problem bank. Type 7, *official
words into plain words*, in `5-roadmap/sector-problem-statements.md` (EU-UDAAN, `a958b68`).
Verdict there: fits.

**Runner-up:** H2 · HMIS and DHIS2 monthly reporting. Pick it instead if the learners turn out
to be mainly HMIS focal persons rather than front-line staff, or if free-tier AI output in
Nepali proves too unstable to demo reliably.

---

## Why H1 and not H2

The earlier one-per-sector draft (`89d9fd4`) picked H2. That pick was made for a five-week
challenge-sheet format, where one live task carries the learner through weekly sessions. This
course follows the UDAAN method instead (build manual Part III): each unit opens on a failure
the learner lives through, and each failure earns one concept. So the deciding question was
**which problem gives five distinct failures you can show by changing one thing.**

- **H1 has five.** A dose that shifts, a warning that disappears, a correct version no one can
  follow, advice no one prescribed, and a local-language version that looks fluent and isn't.
  Each is a different mechanism.
- **H2's failures mostly come back to one lesson:** don't let AI do the counting. That makes a
  strong unit, not a full course.
- **The stakes need no setup.** A wrong dose word reads as dangerous to every Nepali learner
  straight away (build manual §4.4, criterion 1).
- **Type 7 is the programme's own,** and no other sector course has it yet.

---

## The course in one line

**Learner's complaint:** *"I made it simpler. So why did the patient take it wrong?"*

**Condition entering:** the health worker can get a fluent plain-Nepali version out of a free
AI tool in seconds, and trusts it because it reads well.

**Condition leaving:** every plain version they hand over has been checked against the
prescription, in both directions, for the reader and the channel, and by a fluent speaker when
it isn't in their own language.

## Protagonist and world (placeholders, to confirm)

A new world. It must not re-use or re-characterise Maya or Himalayan Getaways.

| Element | Proposed | Why |
|---|---|---|
| Protagonist | **Pooja**, staff nurse at a primary health care centre in **Bardiya**, posted there from Kathmandu Valley two years ago | A transfer posting is ordinary in the civil service, and it gives the language gap without making her less capable. She speaks Nepali; many of her patients speak Tharu or Awadhi |
| The one doctor | **Dr. Rijal**, the centre's only doctor, who writes the prescriptions in English shorthand | Holds the dose decision. Busy, not careless |
| The fluent check | **Phulmati**, a Female Community Health Volunteer (FCHV) who speaks Tharu | A real Nepali institution. She is the human line in Unit 5 |
| Patients | An older farmer on a seven-day antibiotic; a pregnant woman on iron and folic acid; a man with a new hypertension prescription | Cases where one wrong word does harm |
| Peer (parity) | A nurse at a neighbouring centre, same post and same free tool, whose handouts come back right | Holds resources and seniority constant (§4.4, criterion 7) |
| Channels | Handwritten slip at the dispensing counter, SMS, a WhatsApp voice note | Where instructions actually reach patients |
| Calendar | Monsoon, when patients can't come back easily for a follow-up | It raises the cost of a wrong instruction |

Names, district and cast are proposals, now recorded in `kb.world.bheri-corridor`
(`_system/graph/knowledge.yaml`), the shared world of the five health courses, marked placeholder.

---

## Unit outline

Five units, about 21 sub-units, on the same shape as the shipped courses (§3.1): each unit is
*experience the problem → discover ×n → put it together*. Unit 1 uses the opening variant and
Unit 5 the closing one. Each unit opens on a trap set by the previous unit's success (§3.2,
step 2).

The letters are candidates only (see [The framework](#the-framework-provisional)). They never
appear in learner-facing material before the reveal in 5.3.

### Unit 1 · "It reads so much better. So why is it wrong?"

*Opening variant: experience → try it yourself → name it & generalise.*

- **1.0 Experience:** Pooja photographs Dr. Rijal's slip (*"Amoxicillin 500 mg 8-hourly ×
  7 days"*) and asks a free AI tool for simple Nepali. The output is warm and fluent. Shown in
  full. It says *"three times a day, until you feel better."* The farmer felt better on day four
  and stopped. Nobody did anything careless.
- **1.1 Try it yourself:** the learner rewrites the same slip with AI, then compares it line by
  line with the source. Experiment: the same request run four times gives four phrasings of the
  timing, and not all of them mean the same thing.
- **1.2 Name it & generalise:** the plain version is a new text, not the source in different
  clothes. Each run is a fresh prediction of likely words, so meaning can drift on every
  rewrite. Before rewriting, list what must not change: **drug, dose, timing, duration.**
  *Analogy:* passing a message along a line of people at a wedding.
- **1.3 Put it together:** Pooja's must-not-change list sits beside the slip. The rewrite is
  checked against it, and the version that holds is shown in full. Here she also removes the
  patient's name and number from the photo before it goes into any AI tool. Course 3's
  classify-first rule is taught in health terms, because this course has to stand on its own.

*Candidate letter:* **S**, the source is fixed.

### Unit 2 · "Every number matched. So why did she come back worse?"

*Trap from Unit 1:* Pooja now checks every number, and every number in the iron and folic acid
version is right.

- **2.0 Experience:** the pregnant woman's iron and folic acid instructions are correct on dose
  and timing. The slip's line *"come back at once if you have bleeding, a severe headache,
  blurred vision, or swelling of the face and hands"* has become *"if you feel unwell, consult a
  health worker."* She had a headache for two days and waited.
- **2.1 Discover: checking one direction misses what's missing.** Checking the plain version
  against the source catches changes. Only checking the source against the plain version catches
  what was dropped. Experiment: the same sheet checked both ways, with the omission found only
  the second way.
- **2.2 Discover: a softened warning is a lost action.** "May feel discomfort" asks for nothing.
  "Come back today if…" does. Experiment: four rewrites of one warning, from hedged to an
  action, and what the patient would do after each one.
- **2.3 Put it together:** the two-way check, run on the full sheet.

*Candidate letter:* **A**, all warnings kept, as actions.

### Unit 3 · "Everything's there. So why can't he follow it?"

*Trap from Unit 2:* the complete, two-way-checked version now carries everything, in the formal
register of the source.

- **3.0 Experience:** the hypertension sheet is accurate and complete, five dense lines in
  formal government Nepali. The patient nods at the counter and goes home with no idea which
  tablet is the morning one.
- **3.1 Discover: write for this reader.** Asking for "simple" gets a guess. Naming who will
  read it changes what comes back: an older farmer who reads slowly, one action per line. It's
  the Audience landmark from Course 1, in a health setting.
- **3.2 Discover: the channel decides the shape.** A 160-character SMS, a voice note and a slip
  at the counter each need a different version of the same instruction. Experiment: one
  instruction, three channels, one change each.
- **3.3 Discover: the read-back test.** Ask the patient to say it back. This is ordinary
  clinical practice (teach-back), and it becomes the check on the AI version too. *Analogy:* a
  teacher asking "so what will you do first?"
- **3.4 Put it together:** the hypertension instructions as a counter slip and a voice note,
  both read back.

*Candidate letter:* **F**, fits the reader and the channel.

### Unit 4 · "It sounds so caring. So where did that advice come from?"

*Trap from Unit 3:* once Pooja asks for warm, friendly, patient-centred wording, the AI fills the
space.

- **4.0 Experience:** the friendly version of the hypertension instructions adds *"avoid sour
  food,"* *"drink warm water,"* and *"once your blood pressure feels normal, you can stop."* None
  of it is on the slip. It reads like good advice, and the last line tells him to stop a
  medicine he needs to keep taking.
- **4.1 Discover: why confident isn't correct.** The tool predicts what caring health advice
  usually sounds like, and borrows common advice to match. Experiment: the same request with
  and without "warm and caring"; additions appear only in the warm version.
- **4.2 Discover: fence it inside the slip.** Instruct it to use only what the prescription
  says, and to flag anything else as a question for the doctor. The learner deletes any line
  they can't trace back to the slip. This is the health form of C1 U4 grounding. If the cycle is
  marked liftable, it reuses the concept rather than inventing a new one.
- **4.3 Put it together:** the warm version, every line traced to the slip, and one question
  sent to Dr. Rijal instead of guessed.

*Candidate letter:* **E**, extras removed.

### Unit 5 · "It looks perfect in Tharu. So why did Phulmati laugh?"

*Trap from Unit 4:* the Nepali version now holds up, so Pooja extends it to Tharu for SMS
reminders.

- **5.0 Experience:** the Tharu version looks fluent to Pooja, who can't read it. Phulmati
  reads it aloud and laughs, then stops: the word used for "before meals" means something else
  in her village.
- **5.1 Discover: you can't check what you can't read.** Experiment: ask the same AI to
  translate its own Tharu back into Nepali. The back-translation comes out clean and hides the
  error. A tool checking its own output isn't an independent check.
- **5.2 Discover: a fluent person is the check.** Phulmati's reading, recorded with what she
  changed. Who checks which language, and what to do when no fluent reader is available: hand
  over the Nepali version, not an unchecked translation.
- **5.3 The payoff:** the five checks, each traced back to its unit, then the reveal and the
  one-page instruction sheet: must-not-change list, two-way check, reader and channel, trace to
  source, fluent reader. Pooja's afternoon counter, dramatised.
- **5.4 The whole journey:** the farmer, the pregnant woman, the hypertension patient and the Tharu
  SMS, before and after.

*Candidate letter:* **R**, read by a fluent person.

### The framework (provisional)

The candidate letters spell **SAFER**: **S**ource fixed · **A**ll warnings kept · **F**its the
reader · **E**xtras removed · **R**ead by a fluent person.

Provisional by construction. §3.3 requires each letter to be earned from a failure the learner
actually lived through, so the word should change if a unit changes during the build. It also
describes the result more than the act, which is weaker than BRIEF or TRUST under §3.3 rule 2.
Like SOLVE in the Course 4 proposal, treat it as a working label, not a decision.

---

## The human lines

1. **The prescriber owns the dose.** The health worker never changes, fills in or guesses a
   drug, dose, timing or duration. Anything unclear goes back to the doctor (4.3).
2. **A fluent reader owns the translation.** No local-language version goes out unchecked by
   someone who reads that language (5.2).
3. **The source wins any disagreement.**

These are the two lines of the escalation question in `work-type-problem-statements.md`. The
first is the "signer checks the source" case. The second is a new target type: a fluent reader,
not a decision-maker. Neither is a decision about a person, so `esc.bright-line` doesn't cover
them.

## The tangible and the evidence

- **Artifact (pipeline stage 1):** the learner's own one-page instruction sheet, plus one checked
  plain version of an instruction they really give out. Built from an invented prescription in
  the same form, with the source alongside and every line traceable.
- **Interview seed (stage 3):** produce a version of the same instruction for a different reader
  and channel (a voice note for an older patient, say) and show which checks changed and why.

## In graph terms

- **Problem:** `prob.health-patient-instructions`, *Teach plain-language patient instructions*,
  `mode: pedagogy`, `status: unbuilt`, `flows: []`, `difficulty: null`.
- **Domain:** `health`, one of story §4.1's own applied examples. Here the scenario and the
  capability share a sector, so `scenario_domain` is also `health`, and Q2 doesn't arise for
  this problem. That's a point in favour of sector courses that is worth recording.
- **Knowledge:** a new `kb.world.<name>`; `kb.problem-bank` entry H1; published drug information
  leaflets and national treatment protocols as source material, each with a `source/` pointer.
- **Skills: none assigned.** Likely candidates from the shipped pool are AI Output Validation &
  Contextual Auditing, Audience-Aware AI Communication, Source Grounding & Hallucination
  Control, and Confidential Information Handling. Assign them only when a skill mapper row
  exists (CLAUDE.md, provenance over assertion).
- **Relation to the shipped courses:** standalone, not after Course 1. That's why 3.1 and 4.2
  re-teach Audience and grounding in health terms. If the programme decides sector courses
  follow Course 1, those two cycles become references instead.

---

## Test before writing

Build manual §4.6: if a shipped experiment stops reproducing, the sub-unit built on it quietly
becomes false. Every failure above is a hypothesis until it has been run on the free tiers the
learners will actually use.

| # | Failure to reproduce | Tool | Pass if |
|---|---|---|---|
| 1 | Timing drift across 4 runs of the same request (1.1) | Free ChatGPT, free Gemini | At least one run changes what the timing means |
| 2 | A warning softened or dropped (2.0) | Both | Shows up in at least 1 in 3 runs on a real-shaped sheet |
| 3 | Formal register when asked only for "simple" (3.0) | Both | A Nepali-reading reviewer rates it hard for a low-literacy reader |
| 4 | Additions appear under "warm and caring" (4.1) | Both | Untraceable lines appear in the warm version and not in the plain one |
| 5 | Tharu error that a back-translation hides (5.1) | Both | A fluent Tharu reader finds an error the back-translation misses |

If a failure doesn't reproduce, change the unit. Don't stage it.

## Reviews needed

- **A clinician or pharmacist**, on every slip, dose and warning in the course.
- **Fluent Tharu and Awadhi readers**, on Unit 5's material.
- **Programme leads**, on the choice of H1 over H2, standalone versus after Course 1, and the cast.
- **Sources** for the two figures that justify the problem: female literacy of 69.4% (Census
  2021), and most primary health care centres running with one doctor. They belong in the
  evidence layer only. Pooja's story carries no citations.

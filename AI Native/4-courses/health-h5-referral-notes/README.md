# Health — The referral note that carries findings, not the call

*Sector course · problem bank **H5** · **The Rounds way** · Course capability: writing a referral
note with AI that leads with the reason, holds only what was observed, states urgency as a time,
is confirmed against the register, and leaves the call to a person · Framework candidate: ROUTE
(provisional) · 22 sub-units · **Status: skeleton, draft***

One of the five health courses, each on one health problem and each taught a different way:
[`3-course-flow/health-programme.md`](../../3-course-flow/health-programme.md). This one is
taught the way cases are taught on a ward round: in stages, with the learner committing before
each reveal, and a senior asking the one question that would have caught it
([`five-ways.md`](../../1-how-we-built-it/five-ways.md) §3.2).

**Ramesh entering:** he gives a free AI tool his findings and gets a fluent, formal referral
letter in seconds, and sends it. **Ramesh leaving:** every note he sends leads with why he is
referring and what he needs, holds nothing he didn't observe, says by when, has been confirmed
against the register page it was read from, and leaves the call to a named person.

**Learner's complaint:** *"The note was complete. So why did the hospital treat it as nothing?"*

Ramesh is the health assistant in charge of a health post in a rural palika of Bardiya. He
refers to the primary health care centre on the highway and, for emergencies, to the 100-bed
hospital in Nepalgunj, an hour away. Dr. Basnet reads his notes in that hospital's emergency, and
her questions are the ones this course asks. Five cases, each a note that read perfectly and
failed a different way: the line that mattered buried in paragraph four, a blood pressure nobody
measured, an urgency that became a courtesy, a time misread from a photo of the register, and an
impression nobody asked for.

**Learners:** health assistants, auxiliary health workers, ANMs and medical officers who refer,
and the medical recorders who help them write.

**What the learner leaves with:** their rounds book, five questions each with the case that
earned it, and one referral note of their own drafted from an invented register entry.

| Question | What it means | Earned in |
|---|---|---|
| "What do you need from me?" | The first line says why you are referring and what you need. Everything else comes after | Unit 1 |
| "Did you measure that?" | Nothing in the note that isn't in the register. "Not measured" is a finding; a plausible value is not | Unit 2 |
| "By when?" | Urgency is a time, not a courtesy. "Tonight" and "within two hours" route a patient; "at your earliest convenience" doesn't | Unit 3 |
| "What did it read?" | Confirm the transcription of the register page before the note is written from it | Unit 4 |
| "Whose call is that?" | The note carries findings and the question. The call is a named person's, never the note's | Unit 5 |

The candidate word is **ROUTE**, revealed in 5.4 and named nowhere before it. Letters are earned
in teaching order; the fifth is the weakest fit and the first to revisit. Provisional by
construction (build manual §3.3); `kb.framework.route` carries the disclosure rule.

> **The human lines.** AI writes the note; it never makes the call. Whether to refer is Ramesh's
> decision and what happens next is Dr. Basnet's; an "impression" or a "recommendation" in a
> drafted note is struck or turned into a question (5.2, `esc.bright-line`: a decision about a
> person). Nothing in a note is a finding unless it is in the register. No patient name, ID or
> photo of a face goes into any tool.

> **Start with the reference lesson:**
> [2.2 "Did you measure that?"](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.2-did-you-measure-that/artifact.md)
> is the one sub-unit written out, as a draft, on the Rounds way's step flow. Its case and
> register are invented and its AI output is expected, not yet reproduced.

## Why this way for this problem

Clinicians already learn from cases disclosed in stages, and the commitment before the reveal is
what makes the reveal teach. A referral note is read by someone who has to act on it in a
minute, so the senior's question, "what do you need from me?", is the natural shape of the
concept. The way strains on a page because nothing stops the learner scrolling past the commit
(five-ways.md §4); the commit is the first thing to move to Tier 3.

The unit shape: *present the case → reveal the record → the attending's question → your case*.
Each unit's tangible is a line in the rounds book; the five together are read out at the grand
round in 5.4.

## Units

Each unit opens on a trap the previous unit's success set. The planned content under each table
is the design; no lesson has been written for it yet except 2.2.

#### Unit 1 — The note said everything. So why did nobody read the line that mattered?

Concept: **Reason first: the first line says why, and what you need** · [`cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/`](cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/) · `cu.h5.u1`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 1.0 | [The letter that said everything](cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/scu-1.0-the-letter-that-said-everything/) | Present the case | no | — |
| 1.1 | [What Dr. Basnet read first](cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/scu-1.1-what-dr-basnet-read-first/) | Reveal the record | no | — |
| 1.2 | ["What do you need from me?"](cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/scu-1.2-what-do-you-need-from-me/) | The attending's question | yes | — |
| 1.3 | [Three notes, first line first](cu-1-the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered/scu-1.3-three-notes-first-line-first/) | Your case | yes | — |


- **1.0** An older patient, breathless since the night. Ramesh's findings, then the letter the
  tool wrote: two pages, formal, a differential, in full. Commit: send it or not, and what would
  Dr. Basnet read first?
- **1.1** What she read first: the greeting and the history of the health post. The time of
  onset was in paragraph four. The letter beside what she needed.
- **1.2** *"What do you need from me?"* The letter form predicts a preamble. The first line says
  why you are referring and what you need. *Picture:* a call to the fire brigade.
- **1.3** Three notes, first line first. The rounds-book line.

#### Unit 2 — Every line read right. So where did that blood pressure come from?

Concept: **Observed only: nothing in the note that isn't in the register** · [`cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/`](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/) · `cu.h5.u2`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 2.0 | [The note with the normal pressure](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.0-the-note-with-the-normal-pressure/) | Present the case | no | — |
| 2.1 | [The register beside the note](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.1-the-register-beside-the-note/) | Reveal the record | no | — |
| 2.2 | ["Did you measure that?"](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.2-did-you-measure-that/) | The attending's question | yes | [draft](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.2-did-you-measure-that/artifact.md) |
| 2.3 | [Three notes, nothing added](cu-2-every-line-read-right-so-where-did-that-blood-pressure-come-from/scu-2.3-three-notes-nothing-added/) | Your case | yes | — |


*Trap from Unit 1:* the notes are short and sharp now, so every line in them is believed.

- **2.0** A note with *"BP 120/80, afebrile."* The cuff was broken that day. Commit.
- **2.1** The register beside the note, line by line. No blood pressure in the register. The
  hospital acted on a normal pressure nobody took.
- **2.2** *"Did you measure that?"* The tool completes the template a referral note usually has.
  Nothing in the note that isn't in the register; "not measured" is a finding. *Picture:* a form
  with a box you write "N/A" in rather than a likely number.
- **2.3** Three notes, nothing added. The rounds-book line.

#### Unit 3 — The note was urgent. So why did he wait four hours?

Concept: **Urgency as a time, not a courtesy** · [`cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/`](cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/) · `cu.h5.u3`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 3.0 | ["Kindly evaluate at your earliest convenience"](cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/scu-3.0-kindly-evaluate-at-your-earliest-convenience/) | Present the case | no | — |
| 3.1 | [What the triage desk saw](cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/scu-3.1-what-the-triage-desk-saw/) | Reveal the record | no | — |
| 3.2 | ["By when?"](cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/scu-3.2-by-when/) | The attending's question | yes | — |
| 3.3 | [Three notes, each with a time](cu-3-the-note-was-urgent-so-why-did-he-wait-four-hours/scu-3.3-three-notes-each-with-a-time/) | Your case | yes | — |


*Trap from Unit 2:* every line is observed, so the note is trusted at the desk.

- **3.0** Ramesh wants this patient seen within the hour. The note says *"kindly evaluate at your
  earliest convenience."* Commit.
- **3.1** What the triage desk saw: routine. Four hours in the queue.
- **3.2** *"By when?"* Politeness is a register the tool predicts into. Urgency is a time: tonight,
  within two hours, before the bus. *Picture:* "come whenever" versus "come before four, the
  bus leaves."
- **3.3** Three notes, each with a time. The rounds-book line.

#### Unit 4 — The note matched the register. So why was the time wrong?

Concept: **Transcription confirmed before the note is written** · [`cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/`](cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/) · `cu.h5.u4`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 4.0 | [The register page it read](cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/scu-4.0-the-register-page-it-read/) | Present the case | no | — |
| 4.1 | [The photo beside the page](cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/scu-4.1-the-photo-beside-the-page/) | Reveal the record | no | — |
| 4.2 | ["What did it read?"](cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/scu-4.2-what-did-it-read/) | The attending's question | yes | — |
| 4.3 | [Three pages, read then confirmed](cu-4-the-note-matched-the-register-so-why-was-the-time-wrong/scu-4.3-three-pages-read-then-confirmed/) | Your case | yes | — |


*Trap from Unit 3:* the notes are fast and right, so Ramesh photographs the register instead of
typing.

- **4.0** The note written from a photo of the register page. Onset 08:30. Commit.
- **4.1** The photo beside the page: 03:30. Five hours disappeared before anyone read the note.
- **4.2** *"What did it read?"* Transcribe the fields first, confirm them against the page, then
  write. *Picture:* reading a phone number back before you dial.
- **4.3** Three pages, read then confirmed. The rounds-book line.

#### Unit 5 — I asked for a note. So why did it make the call?

Concept: **Explicit who decides: the note carries findings and the question, never the call -> the rounds book** · [`cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/`](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/) · `cu.h5.u5`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 5.0 | [The impression nobody asked for](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.0-the-impression-nobody-asked-for/) | Present the case | no | — |
| 5.1 | [What a line like that does at the desk](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.1-what-a-line-like-that-does-at-the-desk/) | Reveal the record | no | — |
| 5.2 | ["Whose call is that?"](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.2-whose-call-is-that/) | The attending's question | yes | — |
| 5.3 | [Three notes, the call left open](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.3-three-notes-the-call-left-open/) | Your case | yes | — |
| 5.4 | [Grand round: five questions](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.4-grand-round-five-questions/) | The payoff | no | — |
| 5.5 | [The health post, before and after](cu-5-i-asked-for-a-note-so-why-did-it-make-the-call/scu-5.5-the-health-post-before-and-after/) | The whole journey | no | — |


*Trap from Unit 4:* the notes are trusted and accurate, and the tool starts helping with the
part that isn't Ramesh's.

- **5.0** *"Impression: acute appendicitis. Recommend urgent surgical referral."* Ramesh asked for
  a note. Commit.
- **5.1** What a line like that does at the desk: the triage nurse routes it, the examining
  doctor is anchored by it, and Ramesh starts to believe it.
- **5.2** *"Whose call is that?"* The note carries findings and the question. Whether to refer is
  Ramesh's call; what happens next is Dr. Basnet's; the tool decides nothing. The bright line.
  *Picture:* a witness who describes what they saw and does not announce the verdict.
- **5.3** Three notes, the call left open. The rounds-book line.
- **5.4** Grand round: five questions, each read out with the case that earned it, then the
  reveal and the rounds book on one page. A night at the health post, dramatised.
- **5.5** The health post, before and after. And the note Ramesh wrote on the 1st for an adult
  patient with abdominal pain, who was admitted in Nepalgunj on the 3rd: the shared episode,
  `kb.world.bheri-corridor`.

## Before any more lessons are written

1. **Reproduce the five failures** on free ChatGPT and free Gemini: a preamble that buries the
   reason (1.0), a vital sign added to fill the template (2.0), urgency softened to a courtesy
   (3.0), a time misread from a photographed register (4.0), an impression or recommendation
   added unasked (5.0). A unit whose failure doesn't reproduce is rebuilt, not staged.
2. **Reviews:** a clinician on every case, so that each is plausible, safe to show and teaches
   the note rather than medicine; someone who reads referral notes at a receiving desk; the
   programme leads on the Rounds way and the overlap with D3 (telemedicine case summaries).
3. **Skills:** none assigned. Assign them only from a skill mapper row for this course.

World, practice material and the candidate word are in `_system/graph/knowledge.yaml` as
`kb.world.bheri-corridor`, `kb.rules.practice-referral-records` and `kb.framework.route`. Every
case, finding, time and value in a lesson is invented, and no case teaches medicine.

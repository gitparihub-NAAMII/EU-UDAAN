# Health — Plain-Nepali patient instructions

*Sector course · problem bank **H1** · **The Story way** · Course capability: turning a
prescription into instructions a patient can act on, with AI, without losing what matters ·
Framework candidate: SAFER (provisional) · 22 sub-units · **Status: skeleton, draft***

One of the five health courses, each on one health problem and each taught a different way:
[`3-course-flow/health-programme.md`](../../3-course-flow/health-programme.md). This one is
taught the way the three shipped courses are: a protagonist, a failure lived in full, a concept
discovered and only then named ([`five-ways.md`](../../1-how-we-built-it/five-ways.md) §3.1).

**Pooja entering:** she can get a fluent plain-Nepali version of any prescription out of a free
AI tool in seconds, and trusts it because it reads well. **Pooja leaving:** every plain version
she hands over has been checked against the prescription in both directions, written for the
reader and the channel, fenced inside the slip, and read by a fluent speaker when it isn't in
her own language.

**Learner's complaint:** *"I made it simpler. So why did the patient take it wrong?"*

Pooja is a staff nurse at a primary health care centre in Bardiya, posted there from Kathmandu
Valley two years ago. She speaks Nepali; many of her patients speak Tharu or Awadhi. Dr. Rijal,
the centre's only doctor, writes prescriptions in English shorthand. Phulmati, a Female
Community Health Volunteer, speaks Tharu. The course follows five failures, each with a
different cause: a timing that shifts between runs, a warning that goes quiet, a correct version
nobody can follow, advice nobody prescribed, and a Tharu version that looks fluent and isn't.

**Learners:** nurses, health assistants, auxiliary health workers and ANMs, pharmacists at the
dispensing counter, and the people who supervise FCHVs.

**What the learner leaves with:** their own one-page instruction sheet, and one checked plain
version of an instruction they really give out, built from an invented prescription in the same
form, with the source alongside and every line traceable.

| Check | What it means | Earned in |
|---|---|---|
| Source fixed | A must-not-change list sits beside the slip before any rewrite: drug, dose, timing, duration | Unit 1 |
| All warnings kept | Check the plain version against the source *and* the source against the plain version. A warning is written as an action | Unit 2 |
| Fits the reader | Name the reader and the channel; have it read back | Unit 3 |
| Extras removed | Every line traces to the slip; anything that doesn't is deleted or sent to the doctor as a question | Unit 4 |
| Read by a fluent person | A version in a language you can't read goes out only after a fluent reader checks it | Unit 5 |

The candidate word is **SAFER**, revealed in 5.3 and named nowhere before it. It is provisional
by construction (build manual §3.3): the letters change if a unit changes during the build, and
the word describes the result more than the act, which §3.3 rule 2 calls weaker than BRIEF or
TRUST. `kb.framework.safer` carries the disclosure rule.

> **The human lines.** The prescriber owns the dose: Pooja never changes, fills in or guesses a
> drug, dose, timing or duration; anything unclear goes back to Dr. Rijal (4.3,
> `esc.signer-checks-source`). A fluent reader owns the translation: no local-language version
> goes out unchecked by someone who reads that language (5.2, `esc.fluent-reader-check`). The
> source wins any disagreement.

> **Start with the reference lesson:**
> [2.1 Check it backwards](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.1-check-it-backwards/artifact.md)
> is the one sub-unit written out, as a draft, on the 8-step flow. Its experiment replies are
> expected, not yet reproduced.

## Why this way for this problem

H1 has five distinct failures that can each be shown by changing one thing, which is what the
8-step flow needs (build manual §3.2 step 5). The counter, the slip and the patient who comes
back are a story every health worker recognises, and the stakes need no setup: a wrong dose
word reads as dangerous to any Nepali learner straight away. The design reasoning and the open
questions are in the outline,
[`5-roadmap/sector-courses/health-h1-patient-instructions.md`](../../5-roadmap/sector-courses/health-h1-patient-instructions.md).

The unit shape is the build manual's: *experience the problem → discover it yourself ×n → put
it together*, with the opening variant in Unit 1 and the closing pair in Unit 5. Each unit's
tangible is one line on the one-page instruction sheet.

## Units

Each unit opens on a trap the previous unit's success set. The planned content under each table
is from the outline; no lesson has been written for it yet except 2.1.

#### Unit 1 — It reads so much better. So why is it wrong?

Concept: **The source is fixed: a must-not-change list** · [`cu-1-it-reads-so-much-better-so-why-is-it-wrong/`](cu-1-it-reads-so-much-better-so-why-is-it-wrong/) · `cu.h1.u1`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 1.0 | [The slip that read better](cu-1-it-reads-so-much-better-so-why-is-it-wrong/scu-1.0-the-slip-that-read-better/) | Experience the problem | no | — |
| 1.1 | [Four runs, four timings](cu-1-it-reads-so-much-better-so-why-is-it-wrong/scu-1.1-four-runs-four-timings/) | Try it yourself | no | — |
| 1.2 | [A new text, not the same text](cu-1-it-reads-so-much-better-so-why-is-it-wrong/scu-1.2-a-new-text-not-the-same-text/) | Name it & generalise | yes | — |
| 1.3 | [Pooja's must-not-change list](cu-1-it-reads-so-much-better-so-why-is-it-wrong/scu-1.3-poojas-must-not-change-list/) | Put it together | no | — |


- **1.0** Pooja photographs Dr. Rijal's slip and asks for simple Nepali. The output is warm and
  fluent, shown in full, and says *"three times a day, until you feel better."* The farmer felt
  better on day four and stopped. Nobody did anything careless.
- **1.1** The learner rewrites the same slip four times. Four phrasings of the timing, and not
  all of them mean the same thing.
- **1.2** The plain version is a new text, not the source in different clothes: each run is a
  fresh prediction of likely words, so meaning can drift on every rewrite. Before rewriting,
  list what must not change. *Analogy:* a message passed along a line of people at a wedding.
- **1.3** Pooja's must-not-change list beside the slip, the rewrite checked against it, and the
  patient's name and number removed from the photo before it goes into any tool.

#### Unit 2 — Every number matched. So why did she come back worse?

Concept: **Check both ways; a warning is an action** · [`cu-2-every-number-matched-so-why-did-she-come-back-worse/`](cu-2-every-number-matched-so-why-did-she-come-back-worse/) · `cu.h1.u2`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 2.0 | [The warning that went quiet](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.0-the-warning-that-went-quiet/) | Experience the problem | no | — |
| 2.1 | [Check it backwards](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.1-check-it-backwards/) | Discover it yourself | yes | [draft](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.1-check-it-backwards/artifact.md) |
| 2.2 | [A softened warning is a lost action](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.2-a-softened-warning-is-a-lost-action/) | Discover it yourself | yes | — |
| 2.3 | [The two-way check, on the whole sheet](cu-2-every-number-matched-so-why-did-she-come-back-worse/scu-2.3-the-two-way-check-on-the-whole-sheet/) | Put it together | no | — |


*Trap from Unit 1:* Pooja now checks every number, and every number in the iron and folic acid
version is right.

- **2.0** The slip's line *"come back at once if…"* has become *"if you feel unwell, consult a
  health worker."* She had a headache for two days and waited.
- **2.1** Checking the plain version against the source catches changes. Only checking the source
  against the plain version catches what was dropped. Experiment: the same sheet checked four
  ways; the omission shows only when the direction flips.
- **2.2** "May feel discomfort" asks for nothing. "Come back today if…" does. Experiment: four
  rewrites of one warning, from hedged to an action, and what the patient would do after each.
- **2.3** The two-way check, run on the full sheet.

#### Unit 3 — Everything's there. So why can't he follow it?

Concept: **Fits the reader and the channel; read it back** · [`cu-3-everythings-there-so-why-cant-he-follow-it/`](cu-3-everythings-there-so-why-cant-he-follow-it/) · `cu.h1.u3`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 3.0 | [Five lines he couldn't follow](cu-3-everythings-there-so-why-cant-he-follow-it/scu-3.0-five-lines-he-couldnt-follow/) | Experience the problem | no | — |
| 3.1 | [Write for this reader](cu-3-everythings-there-so-why-cant-he-follow-it/scu-3.1-write-for-this-reader/) | Discover it yourself | yes | — |
| 3.2 | [The channel decides the shape](cu-3-everythings-there-so-why-cant-he-follow-it/scu-3.2-the-channel-decides-the-shape/) | Discover it yourself | yes | — |
| 3.3 | [Say it back](cu-3-everythings-there-so-why-cant-he-follow-it/scu-3.3-say-it-back/) | Discover it yourself | yes | — |
| 3.4 | [A slip and a voice note, both read back](cu-3-everythings-there-so-why-cant-he-follow-it/scu-3.4-a-slip-and-a-voice-note-both-read-back/) | Put it together | no | — |


*Trap from Unit 2:* the complete, two-way-checked version carries everything, in the formal
register of the source.

- **3.0** Five dense lines in formal Nepali. The patient nods at the counter and goes home with
  no idea which tablet is the morning one.
- **3.1** Asking for "simple" gets a guess. Naming the reader changes what comes back: an older
  farmer who reads slowly, one action per line.
- **3.2** A 160-character SMS, a voice note and a counter slip each need a different version.
  Experiment: one instruction, three channels, one change each.
- **3.3** Ask the patient to say it back. Ordinary clinical practice (teach-back), now the check
  on the AI version too. *Analogy:* a teacher asking "so what will you do first?"
- **3.4** The hypertension instructions as a counter slip and a voice note, both read back.

#### Unit 4 — It sounds so caring. So where did that advice come from?

Concept: **Extras removed: fence it inside the slip** · [`cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/`](cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/) · `cu.h1.u4`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 4.0 | [The advice nobody prescribed](cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/scu-4.0-the-advice-nobody-prescribed/) | Experience the problem | no | — |
| 4.1 | [Why caring isn't correct](cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/scu-4.1-why-caring-isnt-correct/) | Discover it yourself | yes | — |
| 4.2 | [Fence it inside the slip](cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/scu-4.2-fence-it-inside-the-slip/) | Discover it yourself | yes | — |
| 4.3 | [Every line traced, one question sent](cu-4-it-sounds-so-caring-so-where-did-that-advice-come-from/scu-4.3-every-line-traced-one-question-sent/) | Put it together | no | — |


*Trap from Unit 3:* once Pooja asks for warm, patient-centred wording, the AI fills the space.

- **4.0** The friendly version adds *"avoid sour food,"* *"drink warm water,"* and *"once your
  blood pressure feels normal, you can stop."* None of it is on the slip, and the last line tells
  him to stop a medicine he needs to keep taking.
- **4.1** The tool predicts what caring health advice usually sounds like and borrows common
  advice to match. Experiment: the same request with and without "warm and caring."
- **4.2** Use only what the prescription says; flag anything else as a question for the doctor.
  The learner deletes any line they can't trace to the slip.
- **4.3** The warm version, every line traced, and one question sent to Dr. Rijal instead of
  guessed. The prescriber owns the dose.

#### Unit 5 — It looks perfect in Tharu. So why did Phulmati laugh?

Concept: **Read by a fluent person -> the one-page instruction sheet** · [`cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/`](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/) · `cu.h1.u5`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 5.0 | [The word that meant something else](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/scu-5.0-the-word-that-meant-something-else/) | Experience the problem | no | — |
| 5.1 | [You can't check what you can't read](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/scu-5.1-you-cant-check-what-you-cant-read/) | Discover it yourself | yes | — |
| 5.2 | [A fluent person is the check](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/scu-5.2-a-fluent-person-is-the-check/) | Discover it yourself | yes | — |
| 5.3 | [Five checks, one sheet](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/scu-5.3-five-checks-one-sheet/) | The payoff | no | — |
| 5.4 | [The counter, before and after](cu-5-it-looks-perfect-in-tharu-so-why-did-phulmati-laugh/scu-5.4-the-counter-before-and-after/) | The whole journey | no | — |


*Trap from Unit 4:* the Nepali version holds up, so Pooja extends it to Tharu for SMS reminders.

- **5.0** The Tharu version looks fluent to Pooja, who can't read it. Phulmati reads it aloud and
  laughs, then stops: the word used for "before meals" means something else in her village.
- **5.1** Ask the same tool to translate its own Tharu back into Nepali. The back-translation
  comes out clean and hides the error. A tool checking its own output isn't an independent check.
- **5.2** Phulmati's reading, recorded with what she changed. Who checks which language, and
  what to do when no fluent reader is available: hand over the Nepali version.
- **5.3** Five checks, each traced to its unit, then the reveal and the one-page sheet. Pooja's
  afternoon counter, dramatised.
- **5.4** The farmer, the pregnant woman, the hypertension patient and the Tharu SMS, before and
  after. And the discharge slip from Nepalgunj that an adult patient from up the road brings to
  her counter for follow-up: the shared episode, `kb.world.bheri-corridor`.

## Before any more lessons are written

1. **Reproduce the five failures** on free ChatGPT and free Gemini (outline, "Test before
   writing"): timing drift across runs, a warning softened or dropped, formal register under
   "simple", additions under "warm and caring", a Tharu error a back-translation hides. A unit
   whose failure doesn't reproduce is rebuilt, not staged.
2. **Reviews:** a clinician or pharmacist on every slip, dose and warning; fluent Tharu and
   Awadhi readers on Unit 5; the programme leads on the cast and on standalone versus
   after Course 1 (3.1 and 4.2 re-teach Audience and grounding in health terms because the
   course has to stand on its own).
3. **Skills:** none assigned. Assign them only from a skill mapper row for this course.

World, practice material and the candidate word are in `_system/graph/knowledge.yaml` as
`kb.world.bheri-corridor`, `kb.rules.practice-prescriptions` and `kb.framework.safer`. Every
slip, patient and rule in a lesson is invented, and no lesson states a real dose as fact.

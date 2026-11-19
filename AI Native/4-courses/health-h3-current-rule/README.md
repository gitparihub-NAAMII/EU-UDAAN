# Health — "What is the current rule?"

*Sector course · problem bank **H3** · **The Build way** · Course capability: answering staff
questions about the current rule from the dated circular, with AI, under a named person's
signature · Framework candidate: REPLY (provisional) · 22 sub-units · **Status: skeleton, draft***

One of the five health courses, each on one health problem and each taught a different way:
[`3-course-flow/health-programme.md`](../../3-course-flow/health-programme.md). This one is
taught by building: each unit adds one part to a kit the learner keeps, and the failure is lived
on the learner's own desk, on a real call ([`five-ways.md`](../../1-how-we-built-it/five-ways.md)
§3.5).

**Nirmala entering:** every facility in the district phones her with "what is the current rule
on…?", she asks a free AI tool, and she answers in seconds. **Nirmala leaving:** every answer
leaves her desk with the circular's exact words first, its date, the asker's situation named,
and her name on it, from a kit she built on her own calls: the circular file, the answer
template, the dated index, the ask-back, the signed answer.

**Learner's complaint:** *"I answered in seconds. So why was the answer wrong?"*

Nirmala is a public health officer at the health office in Gulariya, Bardiya. Twenty-odd
facilities call her when a circular changes, and when one doesn't. The bank review reframed H3:
the one-off summary of a protocol isn't the recurring work; the recurring work is staff asking
for the current rule. The course is five jobs from her phone, each a different way an answer
goes wrong: a rule from nowhere, a condition softened in paraphrase, the superseded circular
quoted exactly, the right answer to the wrong facility, and an answer that became "the health
office said."

**Learners:** public health officers and inspectors, facility in-charges, and anyone whose
phone is where "what's the rule?" lands.

**What the learner leaves with:** their own circular desk, built part by part and tested on three
real questions from their own facility.

| Part of the kit | What it does | Earned in |
|---|---|---|
| The circular file | No answer leaves the desk without the circular in the chat. If the file has nothing on the subject, the answer says so | Unit 1 |
| The answer template | The exact clause first, in quotation marks, then the plain version, then the clause number and date | Unit 2 |
| The dated index | One current circular per subject, with its date and what it supersedes. Every answer states the date it quotes | Unit 3 |
| The ask-back | Three questions before any answer: which facility, which period, which case. The answer names the situation it applies to | Unit 4 |
| The signed answer | Every answer carries the quote, the date, the situation and a person's name, and says: this is an answer, not the circular; the circular wins | Unit 5 |

The candidate word is **REPLY**, revealed in 5.4 and named nowhere before it. Letters are earned
in teaching order. Provisional by construction (build manual §3.3); `kb.framework.reply` carries
the disclosure rule.

> **The human lines.** A person answers; the tool drafts. Every answer leaves under a named
> person's name, checked by that person against the circular it quotes (5.1,
> `esc.signer-checks-source`). An answer is never the rule: the circular wins any disagreement.
> No answer about a dose, a treatment or a person's eligibility is given from a circular alone.

> **Start with the reference lesson:**
> [2.1 Quote before you explain](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.1-quote-before-you-explain/artifact.md)
> is the one sub-unit written out, as a draft, on the Build way's step flow. Its circular is
> invented and its AI output is expected, not yet reproduced.

## Why this way for this problem

Type 4 work (the question that keeps coming back) ends in a thing: the answer that doesn't have
to come to one person every time. A learner who leaves this course with a kit they built on
their own calls has that thing. Built on anyone else's calls it would be a template nobody
uses. The way strains where the learner has no desk yet (five-ways.md §4), so this course is for
people already fielding the calls.

The unit shape: *the job → spec → build and test → ship it*. Each unit's tangible is one part of
the kit, versioned and dated; the five together are the circular desk.

## Units

Each unit opens on a trap the previous unit's success set. The planned content under each table
is the design; no lesson has been written for it yet except 2.1.

#### Unit 1 — It answered straight away. So where did the rule come from?

Concept: **Read the circular first: no answer without the document in the chat** · [`cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/`](cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/) · `cu.h3.u1`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 1.0 | [The question from the health post](cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/scu-1.0-the-question-from-the-health-post/) | The job | no | — |
| 1.1 | [The circular file](cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/scu-1.1-the-circular-file/) | Spec | yes | — |
| 1.2 | [Build the file, test three questions](cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/scu-1.2-build-the-file-test-three-questions/) | Build and test | yes | — |
| 1.3 | [Version 1, dated](cu-1-it-answered-straight-away-so-where-did-the-rule-come-from/scu-1.3-version-1-dated/) | Ship it | no | — |


- **1.0** A health post phones: what's the current rule on the outreach clinic allowance?
  Nirmala asks the tool. It answers with a figure, a clause number and a confident tone, in
  full. The health post claims on it. The figure comes from nowhere.
- **1.1** What the first part must do, written as requirements: no answer without the circular in
  the chat; one file, every current circular as text, named by subject and date; if the file has
  nothing on the subject, the answer is "no circular on this; I'm asking the province." Concept:
  **read the circular first**: without the document, the tool predicts what a rule of this kind
  usually says. *Picture:* asking the colleague who has "been here long enough" versus opening
  the file.
- **1.2** Build the file (photos to text, one file, dated). Test three questions: one the file
  covers, one it doesn't, one from last week. The log, and the fix.
- **1.3** Version 1, dated, with the hand-over note.

#### Unit 2 — It had the circular. So why did the condition change?

Concept: **Exact words first: quote, then explain** · [`cu-2-it-had-the-circular-so-why-did-the-condition-change/`](cu-2-it-had-the-circular-so-why-did-the-condition-change/) · `cu.h3.u2`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 2.0 | ["Promptly"](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.0-promptly/) | The job | no | — |
| 2.1 | [Quote before you explain](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.1-quote-before-you-explain/) | Spec | yes | [draft](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.1-quote-before-you-explain/artifact.md) |
| 2.2 | [Build the template, test three answers](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.2-build-the-template-test-three-answers/) | Build and test | yes | — |
| 2.3 | [The template goes in the kit](cu-2-it-had-the-circular-so-why-did-the-condition-change/scu-2.3-the-template-goes-in-the-kit/) | Ship it | no | — |


*Trap from Unit 1:* the circular is always in the chat now, so the answer is always trusted.

- **2.0** The circular says claims submitted within seven days of month-end are reimbursed at the
  full rate. The answer says *"claims should be submitted promptly after month end."* The health
  post submits on day ten.
- **2.1** A paraphrase is a new prediction of likely words, and conditions soften in it. The
  requirements: the exact clause first, in quotation marks; then the plain version; then the
  clause number and the circular's date; any number, date or condition in the plain version
  appears word for word in the quote. Concept: **exact words first**. *Picture:* the notice on
  the board versus what the peon remembers of it.
- **2.2** Build the answer template. Test three answers. The log, and the fix.
- **2.3** The template goes in the kit.

#### Unit 3 — It quoted the circular. So why was it the old one?

Concept: **Pin the date: one current version, in a dated index** · [`cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/`](cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/) · `cu.h3.u3`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 3.0 | [Two circulars, one subject](cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/scu-3.0-two-circulars-one-subject/) | The job | no | — |
| 3.1 | [The dated index](cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/scu-3.1-the-dated-index/) | Spec | yes | — |
| 3.2 | [Build the index, test three subjects](cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/scu-3.2-build-the-index-test-three-subjects/) | Build and test | yes | — |
| 3.3 | [The index goes in the kit](cu-3-it-quoted-the-circular-so-why-was-it-the-old-one/scu-3.3-the-index-goes-in-the-kit/) | Ship it | no | — |


*Trap from Unit 2:* every answer quotes exactly, so Nirmala keeps every circular in the file.

- **3.0** Two circulars on the same subject, one superseding the other. The answer quotes the
  older one, word for word.
- **3.1** With two documents in front of it, which one it draws from is unpredictable. The
  requirements: one current circular per subject in the file, the rest archived; a one-page index
  with date and "supersedes"; every answer states the date of the circular it quotes. Concept:
  **pin the date**. *Picture:* two bus timetables pinned on the same board.
- **3.2** Build the index. Test three subjects, one with a superseded version. The log, and the fix.
- **3.3** The index goes in the kit.

#### Unit 4 — The answer was correct. So why was it wrong for them?

Concept: **Look at the asker's situation: three questions before any answer** · [`cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/`](cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/) · `cu.h3.u4`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 4.0 | [The right answer to the wrong facility](cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/scu-4.0-the-right-answer-to-the-wrong-facility/) | The job | no | — |
| 4.1 | [The ask-back](cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/scu-4.1-the-ask-back/) | Spec | yes | — |
| 4.2 | [Build the ask-back, test three calls](cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/scu-4.2-build-the-ask-back-test-three-calls/) | Build and test | yes | — |
| 4.3 | [The ask-back goes in the kit](cu-4-the-answer-was-correct-so-why-was-it-wrong-for-them/scu-4.3-the-ask-back-goes-in-the-kit/) | Ship it | no | — |


*Trap from Unit 3:* the file is current and the quotes are exact, so the answer is right. For
someone.

- **4.0** A PHCC asks whether it can claim the allowance for two sessions a day. The answer quotes
  the health-post schedule. The PHCC schedule is in annex B of the same circular.
- **4.1** The tool answers the sentence it was given. The requirements: three questions before
  any answer (which facility type, which period, what exactly happened); the answer names the
  situation it applies to; if the situation isn't covered, it says so. Concept: **look at the
  asker's situation**. *Picture:* a pharmacist asking "for whom?" before answering "how much?"
- **4.2** Build the ask-back. Test three calls. The log, and the fix.
- **4.3** The ask-back goes in the kit.

#### Unit 5 — The answer became the rule. So who said so?

Concept: **Your name on it: a person signs the answer, and the circular wins -> the circular desk** · [`cu-5-the-answer-became-the-rule-so-who-said-so/`](cu-5-the-answer-became-the-rule-so-who-said-so/) · `cu.h3.u5`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 5.0 | ["The health office said"](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.0-the-health-office-said/) | The job | no | — |
| 5.1 | [Your name on it](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.1-your-name-on-it/) | Spec | yes | — |
| 5.2 | [Build the signed answer, test three replies](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.2-build-the-signed-answer-test-three-replies/) | Build and test | yes | — |
| 5.3 | [The kit, version 1.0](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.3-the-kit-version-1-0/) | Ship it | no | — |
| 5.4 | [Five parts, one desk](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.4-five-parts-one-desk/) | The payoff | no | — |
| 5.5 | [The phone, before and after](cu-5-the-answer-became-the-rule-so-who-said-so/scu-5.5-the-phone-before-and-after/) | The whole journey | no | — |


*Trap from Unit 4:* the answers are right, fast and trusted, so they travel.

- **5.0** A WhatsApp group forwards *"the health office said two sessions are allowed."* It is
  Nirmala's answer with the quote, the date and the situation stripped off. A facility claims on
  it. The audit finds it wrong.
- **5.1** Nothing in a draft carries responsibility. The requirements: every answer leaves with
  the quote, the date, the situation, the name of the person who answered, and the line *"this is
  an answer, not the circular; the circular wins."* Concept: **your name on it**: a person
  signs; the tool drafts. *Picture:* a letter on letterhead with no signature.
- **5.2** Build the signed answer. Test three replies, one of them to the WhatsApp group.
- **5.3** The kit, version 1.0.
- **5.4** Five parts, each traced to its job, then the reveal and the circular desk on one page.
  The phone on a circular day, dramatised.
- **5.5** The phone, before and after. And the call from the PHCC about the follow-up rule for an
  adult patient discharged from Nepalgunj on the 6th: the shared episode, `kb.world.bheri-corridor`.

## Before any more lessons are written

1. **Reproduce the five failures** on free ChatGPT and free Gemini: a confident rule with no
   document in the chat (1.0), a condition softened in paraphrase (2.0), the superseded circular
   quoted when both are in the chat (3.0), the literal question answered for the wrong facility
   (4.0). Failure 5 is social, not a tool failure, and needs no reproduction; it needs a real
   example of an answer that travelled. A unit whose failure doesn't reproduce is rebuilt, not
   staged.
2. **Reviews:** someone who fields these calls at a health office; someone who knows which
   circulars are current and can confirm the invented ones are in the right shape; the programme
   leads on the Build way and on whether the kit needs a facilitator.
3. **Skills:** none assigned. Assign them only from a skill mapper row for this course.

World, practice material and the candidate word are in `_system/graph/knowledge.yaml` as
`kb.world.bheri-corridor`, `kb.rules.practice-circulars` and `kb.framework.reply`. Every
circular in a lesson is invented; the learner's own kit is built from the real ones.

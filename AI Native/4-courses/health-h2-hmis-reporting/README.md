# Health — The monthly report that says what was counted

*Sector course · problem bank **H2** · **The Audit way** · Course capability: assembling the
monthly HMIS report with AI so that every figure traces to a register line and every gap is
reported as a gap · Framework candidate: COUNT (provisional) · 22 sub-units · **Status:
skeleton, draft***

One of the five health courses, each on one health problem and each taught a different way:
[`3-course-flow/health-programme.md`](../../3-course-flow/health-programme.md). This one is
taught as an audit: something that reads as finished lands on the learner's desk with the
records it was made from, and the learner has to decide whether to sign it
([`five-ways.md`](../../1-how-we-built-it/five-ways.md) §3.4).

**Sangita entering:** she photographs the registers, pastes the extracts into a free AI tool,
asks for the monthly report, and gets one that balances in minutes. **Sangita leaving:** every
figure in her report traces to a register line she has counted, the narrative only reports, the
report states its period and quotes each indicator's definition, and a missing page is reported
missing, under her signature.

**Learner's complaint:** *"The report balanced. So why did the municipality send it back?"*

Sangita is the HMIS focal person at a primary health care centre in Bardiya, the same centre
where Pooja works the counter. She keeps the registers and owes the municipality a monthly
report. The course is five investigations, one per unit, each a different way an AI-assembled
report goes wrong: a total nobody counted, a cause nobody recorded, last month's figures carried
forward, an indicator built on the wrong denominator, and a missing day filled in to make the
report balance.

**Learners:** HMIS focal persons, medical recorders, statistics assistants, and the in-charges
who sign the report.

**What the learner leaves with:** one monthly report assembled from invented register extracts
with a trace for every figure, and the audit protocol: five finding memos they wrote themselves.

| Finding | What it means | Earned in |
|---|---|---|
| Counted, not predicted | Every figure traces to register lines the learner counted. The tool predicts totals; it doesn't tally unless made to show each line | Unit 1 |
| No cause without a source | The narrative says what the data shows. A cause appears only if a record states it; otherwise "not recorded" | Unit 2 |
| One month, one file | A fresh chat with this month's extracts only. The report states its period at the top | Unit 3 |
| Use the manual's definition | Paste the indicator's definition; ask for the formula and the lines it used; check both | Unit 4 |
| Tell the gap | A missing figure is reported missing, never filled. The focal person signs what was counted | Unit 5 |

The candidate word is **COUNT**, revealed in 5.4 and named nowhere before it. Letters are earned
in units 1, 3, 4, 2, 5 and presented in word order (build manual §3.3 rule 5). Provisional by
construction; `kb.framework.count` carries the disclosure rule.

> **The human lines.** The focal person signs the report, and signs only what was counted
> (5.2, `esc.signer-checks-source`). AI never fills a missing figure. A figure that can't be
> traced to a register line is marked, not guessed. No patient-identifying page goes into any
> tool: extracts are counts and dates, never names.

> **Start with the reference lesson:**
> [1.2 The figure nobody counted](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.2-the-figure-nobody-counted/artifact.md)
> is the one sub-unit written out, as a draft, on the Audit way's step flow. Its report and
> register extract are invented and its AI output is expected, not yet reproduced.

## Why this way for this problem

The bank review says H2's failures mostly come back to one lesson: don't let AI do the
counting. As a story that is one strong unit. As an audit it is five investigations, because the
learner has to *find* each failure in the evidence, and finding it is the skill: a data quality
review is already the work an HMIS focal person does at supervision visits. The slowness of the
dig is the point (five-ways.md §4).

The unit shape: *the handover → dig → the finding → the memo*. Each unit's tangible is a
finding memo; the five together are the audit protocol.

## Units

Each unit opens on a trap the previous unit's success set. The planned content under each table
is the design; no lesson has been written for it yet except 1.2.

#### Unit 1 — The totals added up. So why didn't they match the register?

Concept: **Counted, not predicted: every figure traces to a register line** · [`cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/`](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/) · `cu.h2.u1`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 1.0 | [The report that balanced](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.0-the-report-that-balanced/) | The handover | no | — |
| 1.1 | [Follow one figure](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.1-follow-one-figure/) | Dig | no | — |
| 1.2 | [The figure nobody counted](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.2-the-figure-nobody-counted/) | The finding | yes | [draft](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.2-the-figure-nobody-counted/artifact.md) |
| 1.3 | [The first finding memo](cu-1-the-totals-added-up-so-why-didnt-they-match-the-register/scu-1.3-the-first-finding-memo/) | The memo | yes | — |


- **1.0** The month's report, in full, assembled by the tool from photographed register pages.
  The totals balance. The municipality wants it by Friday. Nothing says anything is wrong.
- **1.1** Pick one figure: antenatal first visits, 48. Find its lines in the extract. Count them.
  Forty-three. Pick a second figure: it matches. The questions that get the learner there, not
  the answer.
- **1.2** 48 was never counted. The tool predicts a total that looks like totals in reports of
  this kind; it tallies lines only when made to list them. Rule: **counted, not predicted**. The
  check: ask for the lines behind each figure, then count them yourself. *Picture:* the
  end-of-day cash count. You count the notes; you don't ask someone who has seen a lot of cash
  drawers to estimate.
- **1.3** The first finding memo: figure, reported, counted, source lines, what changes.

#### Unit 2 — The numbers were right. So why was the story wrong?

Concept: **No cause without a source: say what the data shows** · [`cu-2-the-numbers-were-right-so-why-was-the-story-wrong/`](cu-2-the-numbers-were-right-so-why-was-the-story-wrong/) · `cu.h2.u2`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 2.0 | [The paragraph that explained everything](cu-2-the-numbers-were-right-so-why-was-the-story-wrong/scu-2.0-the-paragraph-that-explained-everything/) | The handover | no | — |
| 2.1 | [Find the sentence's source](cu-2-the-numbers-were-right-so-why-was-the-story-wrong/scu-2.1-find-the-sentences-source/) | Dig | no | — |
| 2.2 | [The reason that wasn't in the data](cu-2-the-numbers-were-right-so-why-was-the-story-wrong/scu-2.2-the-reason-that-wasnt-in-the-data/) | The finding | yes | — |
| 2.3 | [A narrative that only reports](cu-2-the-numbers-were-right-so-why-was-the-story-wrong/scu-2.3-a-narrative-that-only-reports/) | The memo | yes | — |


*Trap from Unit 1:* every figure now traces, so Sangita lets the tool write the narrative.

- **2.0** The paragraph, in full: *"Antenatal visits rose 12% following the community awareness
  campaign in ward 3; immunisation fell because of the festival season."* Every figure in it is
  right.
- **2.1** Find the sentence's source. Which register, which line, which minute says "because of
  the campaign"? The campaign was in another ward, two months earlier.
- **2.2** The reason wasn't in the data. The tool predicts what a report paragraph usually says
  after a rise. Rule: **no cause without a source**: the narrative says what the data shows, and
  a cause appears only if a record states it. *Picture:* a weather report that says why it
  rained.
- **2.3** A narrative that only reports: *"X rose from a to b. Cause: not recorded."*

#### Unit 3 — Everything matched. So why was it last month's?

Concept: **One month, one file, fresh chat: the report states its period** · [`cu-3-everything-matched-so-why-was-it-last-months/`](cu-3-everything-matched-so-why-was-it-last-months/) · `cu.h2.u3`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 3.0 | [The figures that looked familiar](cu-3-everything-matched-so-why-was-it-last-months/scu-3.0-the-figures-that-looked-familiar/) | The handover | no | — |
| 3.1 | [Which month is this line from?](cu-3-everything-matched-so-why-was-it-last-months/scu-3.1-which-month-is-this-line-from/) | Dig | no | — |
| 3.2 | [Last month, carried forward](cu-3-everything-matched-so-why-was-it-last-months/scu-3.2-last-month-carried-forward/) | The finding | yes | — |
| 3.3 | [A report that states its month](cu-3-everything-matched-so-why-was-it-last-months/scu-3.3-a-report-that-states-its-month/) | The memo | yes | — |


*Trap from Unit 2:* the report is now trusted, so this month's is assembled in the same chat as
last month's.

- **3.0** The figures look familiar. They match the register. The register pasted last month.
- **3.1** Which month is this line from? Compare with this month's extract: six of fourteen
  figures are last month's.
- **3.2** Last month, carried forward. With two months in front of it, which one it draws from
  is unpredictable. Rule: **one month, one file, fresh chat**, and the report states its period
  at the top. *Picture:* a form filled from the carbon copy underneath.
- **3.3** A report that states its month.

#### Unit 4 — The figures matched the register. So why was the indicator wrong?

Concept: **Use the manual's definition: the formula and the lines it used** · [`cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/`](cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/) · `cu.h2.u4`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 4.0 | [The percentage that looked right](cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/scu-4.0-the-percentage-that-looked-right/) | The handover | no | — |
| 4.1 | [Rebuild the indicator](cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/scu-4.1-rebuild-the-indicator/) | Dig | no | — |
| 4.2 | [The denominator it borrowed](cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/scu-4.2-the-denominator-it-borrowed/) | The finding | yes | — |
| 4.3 | [Every indicator, its definition](cu-4-the-figures-matched-the-register-so-why-was-the-indicator-wrong/scu-4.3-every-indicator-its-definition/) | The memo | yes | — |


*Trap from Unit 3:* the figures are right and the month is right, so Sangita lets the tool
compute the indicators.

- **4.0** A percentage that looks right. The municipality's figure for the same indicator is
  thirteen points lower.
- **4.1** Rebuild the indicator by hand. The numerator matches. The denominator is the number of
  women registered this month; the manual's definition uses a different figure.
- **4.2** The denominator it borrowed. The tool predicts a common formula for a familiar-sounding
  indicator. Rule: **use the manual's definition**: paste it, ask for the formula and the lines
  used, check both. *Picture:* "percentage of students who passed": of those who sat, or of
  those enrolled?
- **4.3** Every indicator, its definition quoted beside it.

#### Unit 5 — The report was complete. So why was it dishonest?

Concept: **Tell the gap: a missing figure is reported missing, and a person signs -> the audit protocol** · [`cu-5-the-report-was-complete-so-why-was-it-dishonest/`](cu-5-the-report-was-complete-so-why-was-it-dishonest/) · `cu.h2.u5`

| # | Sub-unit | Type | Reusable | Lesson written |
|---|---|---|---|---|
| 5.0 | [The day that filled itself in](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.0-the-day-that-filled-itself-in/) | The handover | no | — |
| 5.1 | [Find the page that isn't there](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.1-find-the-page-that-isnt-there/) | Dig | no | — |
| 5.2 | [A gap is a gap](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.2-a-gap-is-a-gap/) | The finding | yes | — |
| 5.3 | [The memo that says "not counted"](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.3-the-memo-that-says-not-counted/) | The memo | yes | — |
| 5.4 | [Five findings, one protocol](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.4-five-findings-one-protocol/) | The payoff | no | — |
| 5.5 | [The register room, before and after](cu-5-the-report-was-complete-so-why-was-it-dishonest/scu-5.5-the-register-room-before-and-after/) | The whole journey | no | — |


*Trap from Unit 4:* the report is accurate and fast, and this month a register page is missing.

- **5.0** The OPD page for the 14th was never photographed. Asked to complete the report, the tool
  completes it. The report balances.
- **5.1** Find the page that isn't there. The day's lines are absent; the day's figure is present.
- **5.2** A gap is a gap. Asked to complete, it completes. Rule: **tell the gap**: *"not counted:
  register page for the 14th not available,"* never a filled figure, and the focal person signs
  what was counted. *Picture:* a ledger with a torn page. You write "page missing"; you don't
  invent the day's sales.
- **5.3** The memo that says "not counted."
- **5.4** Five findings, each traced to its investigation, then the reveal and the audit
  protocol. Friday, dramatised.
- **5.5** The register room, before and after. And the referral line that counts an adult patient
  from up the road, admitted in Nepalgunj on the 3rd: the shared episode, `kb.world.bheri-corridor`.

## Before any more lessons are written

1. **Reproduce the five failures** on free ChatGPT and free Gemini: a total that doesn't match
   the lines (1.0), a cause added to a narrative (2.0), last month's figures reused when both
   months are in the chat (3.0), a borrowed denominator (4.0), a missing day filled in when asked
   to complete (5.0). A unit whose failure doesn't reproduce is rebuilt, not staged.
2. **Reviews:** an HMIS focal person on the registers, the form and the Friday; someone who knows
   the current indicator definitions and the DHIS2 form; the programme leads on H2 as the Audit
   way and on the overlap with D4 (health data cleaning), which the bank review calls the
   follow-on for data staff.
3. **Skills:** none assigned. Assign them only from a skill mapper row for this course.

World, practice material and the candidate word are in `_system/graph/knowledge.yaml` as
`kb.world.bheri-corridor`, `kb.rules.practice-hmis-registers` and `kb.framework.count`. Every
register, figure and definition in a lesson is invented; the real form and definitions are
pointed to from `_system/source/`, never reproduced.

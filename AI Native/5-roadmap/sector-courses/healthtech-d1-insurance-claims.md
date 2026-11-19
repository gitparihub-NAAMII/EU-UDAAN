# [PROPOSAL] Health-tech sector course: insurance claims and rejections (D1)

**Status:** draft outline, 2026-11-16. Skeleton built 2026-11-19 in
`4-courses/healthtech-d1-insurance-claims/` (flow, 5 units, 21 sub-units, one lesson drafted:
2.1). Not reviewed by the programme leads or by anyone who works an insurance desk. None of the AI failures below has been reproduced yet. See
[Test before writing](#test-before-writing).

**Chosen problem:** D1 · Insurance claims and rejections, problem bank. Type 6, *check it
against the rules*, in `5-roadmap/sector-problem-statements.md` (EU-UDAAN, `a958b68`).
Verdict there: fits.

Part of a set of sector courses, one problem per sector. The health (H1) and education (E1)
outlines referred to below are still local drafts and are not in this repo yet.

**Runner-up:** D2 · Electronic records and clinical notes (type 3). Pick it instead if the
learners turn out to be mainly clinicians and medical recorders rather than insurance and
finance staff.

---

## Why D1

This time the earlier one-per-sector pick (`89d9fd4`) holds up under the UDAAN test.

- **Five distinct failures, each a different mechanism:** a check that says "complete" and
  isn't, a rule the AI made up, a rule that was right last year, a scanned page read wrong, and
  a helpful suggestion that would make the claim dishonest.
- **It doesn't repeat the health course.** D2 is the obvious alternative, but its core lessons
  (nothing added that wasn't in the note, check both directions) are Units 2 and 4 of the H1
  course in a different form. D3 overlaps H5, and D4 overlaps H2.
- **It adds a type.** Health is type 7; this is type 6.
- **The stakes are already public.** Unpaid claims, rejections, and hospitals suspending
  insurance services are in the problem bank's evidence (figures need sources, see below).
- **It carries the clearest ethics lesson in the set:** honest claims only.

---

## The course in one line

**Learner's complaint:** *"It said everything was in order. So why did the claim come back?"*

**Condition entering:** the desk officer can paste a claim file into a free AI tool and get a
confident verdict in seconds, and has started trusting the verdict.

**Condition leaving:** every AI check they run is against a written checklist and the current
rule set, every flag points to its clause, every field read from paper is confirmed, and no
claim is shaped to look like something it isn't.

**Learners:** insurance desk staff, medical recorders, and hospital finance teams.

## Protagonist and world (placeholders, to confirm)

| Element | Proposed | Why |
|---|---|---|
| Protagonist | **Bikash**, insurance desk officer at a 100-bed private hospital in **Nepalgunj** | A busy regional referral hub. The desk processes dozens of claim files a day, and Bikash is the one colleagues bring tangled files to |
| His manager | **Ms. Karki**, the hospital's finance head, under pressure from months of unpaid claims | The source of the Unit 5 pressure. Worried, not corrupt |
| The reviewer | The insurance programme's claim reviewer, never seen, known only through rejection notes | The bar the file has to clear |
| The doctor | **Dr. Adhikari**, a surgeon whose discharge summaries are handwritten | The Unit 4 scanned page |
| Peer (parity) | A desk officer at another hospital in the same city, same free tool, lower rejection rate | Holds resources and seniority constant |
| Channel | Paper files, phone photos of documents, the hospital's claim portal, rejection notes | Where the work actually happens |
| Calendar | The end-of-month submission rush, and the fiscal year-end in mid-July (end of Asar), when finance pressure peaks | Local timing that raises the stakes |

**Optional link to the health course:** Nepalgunj is the referral hospital for Bardiya, where
the H1 course is set. A patient of Pooja's could arrive on Bikash's desk. That's allowed if
neither character is re-characterised (CLAUDE.md), but it ties the two courses together.
Default: keep them separate, and decide this when both worlds are confirmed.

---

## Unit outline

Five units, about 20 sub-units, on the shipped shape (build manual §3.1). Each unit opens on a
trap set by the previous unit's success (§3.2, step 2).

### Unit 1 · "It said everything was in order. So why did it come back?"

*Opening variant: experience → try it yourself → name it & generalise.*

- **1.0 Experience:** Bikash photographs a surgical claim file and asks the AI, *"Is this claim
  complete?"* It answers with a tidy summary ending *"All required documents appear to be
  present."* Three weeks later the claim comes back: the referral slip was missing. The AI was
  never told a referral slip was needed. It said "complete" anyway.
- **1.1 Try it yourself:** the learner checks an invented claim file with three planted gaps,
  first with the open question, then with a written checklist pasted in. Experiment: the open
  question finds one gap, the checklist finds all three.
- **1.2 Name it & generalise:** the tool checks against what it's given. With no checklist, it
  predicts what a complete-looking answer sounds like. And **silence is not "all clear."** Ask
  for a status on every checklist item (present, missing, can't tell) so a skipped item shows.
  *Analogy:* a shopkeeper asked "is everything here?" without a list of what was ordered.
- **1.3 Put it together:** Bikash's written checklist for surgical claims, and the item-by-item
  result. This is also where every name, ID and diagnosis comes out of the file before it goes
  into any AI tool. Practice uses invented files only.

### Unit 2 · "It found a problem. So why wasn't the problem real?"

*Trap from Unit 1:* with a checklist, the AI now flags gaps confidently, including ones that
don't exist.

- **2.0 Experience:** the AI flags *"This procedure requires prior approval under the package
  rules."* Bikash holds the claim for two weeks chasing an approval. The rule doesn't exist.
- **2.1 Discover: a flag without a clause is a guess.** Experiment: the same file checked twice,
  once with "point to the exact rule for each flag." The invented flag has no clause to point to.
- **2.2 Discover: fence it inside the rule set.** Give it the rules document and instruct it to
  use only that, and to say "not covered" rather than fill the gap. The same grounding concept
  as H1 Unit 4 and C1 Unit 4, applied to rules instead of facts.
- **2.3 Put it together:** every flag on the file paired with its clause, and one "not covered"
  sent to the reviewer as a question.

### Unit 3 · "It quoted the rule word for word. So why was it wrong?"

*Trap from Unit 2:* every flag now cites a clause, so Bikash trusts the citations.

- **3.0 Experience:** a flag quotes a package rate exactly. The claim is rejected for the wrong
  amount. The rate came from last year's package list, still sitting earlier in the same chat
  thread.
- **3.1 Discover: which document, which date?** Experiment: the same question with the old list,
  the new list, and both in the chat. With both, the answer is unpredictable.
- **3.2 Discover: one current rule set.** Keep one dated rules file, start each check from a
  fresh chat with only that file, and put the version date at the top of every check. When a
  circular changes a rule, the file changes, not the chat.
- **3.3 Put it together:** the dated rules file and a check that states the version it used.

### Unit 4 · "Every rule was right. So why was the date wrong?"

*Trap from Unit 3:* checklist, clauses and rules are now in order, and the remaining error comes
from the paper.

- **4.0 Experience:** the AI reads Dr. Adhikari's handwritten discharge summary from a phone
  photo. The admission was the 3rd. It reads the 8th, and the length of stay no longer matches
  the package. The reasoning was perfect; the input was wrong.
- **4.1 Discover: check what it read before what it concluded.** Experiment: ask it to
  transcribe the key fields first (dates, procedure, codes, amounts), then compare the
  transcription with the paper. The misread shows up before it turns into a conclusion.
- **4.2 Discover: some pages can't be read.** Have it mark fields it can't read clearly as
  "unclear" instead of guessing. Experiment: a blurred field with and without that instruction.
- **4.3 Put it together:** read, confirm the fields, then check against the rules.

### Unit 5 · "It found a way to get it approved. So why does it feel wrong?"

*Trap from Unit 4:* Bikash is now fast and accurate, and rejections fall. Ms. Karki asks him to
use the same tool to recover the ones still being rejected.

- **5.0 Experience:** Bikash asks, *"How can I get this claim approved?"* The AI helpfully
  suggests describing the procedure under a package that pays more, and wording the
  diagnosis to match. Every sentence sounds reasonable, and together they describe a claim
  that isn't true.
- **5.1 Discover: "get it approved" is a different question from "is it correct?"** The tool
  predicts what a helpful answer to the question looks like. Experiment: the same file with "how
  do I get this approved" and with "what does this file correctly support". The second question
  doesn't produce the suggestion.
- **5.2 Discover: the claim says what happened, and a person signs it.** AI never approves,
  rejects, scores or reshapes a claim. A rejection that is correct gets accepted or appealed with
  the true record, never reworded. Bikash signs what he submits.
- **5.3 The payoff:** the five checks, each traced back to its unit, then the reveal and the
  one-page claim-check sheet. Bikash's end-of-month rush, dramatised.
- **5.4 The whole journey:** the referral slip, the invented rule, last year's rate, the misread
  date, and the claim he didn't reshape, before and after.

### The framework: not proposed yet

No acronym is suggested for this course. The five concepts (written checklist, cite the clause,
current version, confirm what it read, honest claim) don't fall into a word without forcing one,
and §3.3 requires letters to be earned from the failures, not fitted to a word. Let the word
come out of the build. If none works, a course can end on its one-page sheet without an acronym.

---

## The human lines

1. **A person decides every claim.** AI points to possible gaps. It never passes, fails,
   approves, rejects or scores. A claim decision affects what a patient pays, so this is
   `esc.bright-line` territory.
2. **Claims are honest.** AI never helps make a claim look like something it isn't (5.2).
3. **The signer checks the source.** Bikash signs what he submits, and every field has been
   confirmed against the paper (Unit 4). Candidate escalation `esc.signer-checks-source`
   (proposed, not yet in `_system/graph/escalations.yaml`): the output leaves under a named
   person's signature, so that person checks it against the source.

## The tangible and the evidence

- **Artifact (pipeline stage 1):** the learner's own written checklist for one kind of claim they
  handle, plus a check of one invented claim file run against it, with every flag cited to its
  clause, the rule-set date stated, and the fields confirmed.
- **Interview seed (stage 3):** given a correct rejection, explain why it should be accepted or
  appealed with the true record, and show what the AI suggested that would have made the claim
  dishonest.

## In graph terms

- **Problem:** `prob.healthtech-insurance-claims`, *Teach checking claims against the rules*,
  `mode: pedagogy`, `status: unbuilt`, `flows: []`, `difficulty: null`.
- **Domain:** `health`, the same as H1, unless curation separates out `health-tech`. Story §4.1
  lists `health` and `fintech` as applied domains, and there's no `health-tech` yet. Claims
  sit between health and insurance, so this is a real curation question, not a formality.
- **Knowledge:** a new `kb.world.<name>`; `kb.problem-bank` entry D1; the published package
  rules, with a `source/` pointer and a version date.
- **Skills: none assigned.** Likely candidates from the shipped pool are AI Output Validation &
  Contextual Auditing, Source Grounding & Hallucination Control, Confidential Information
  Handling, and Responsible AI Use & Compliance. Assign them only when a skill mapper row exists.
- **Shared concept with H1:** Unit 2.2 and H1 4.2 are the same grounding concept. If both are
  built, one liftable discovery cycle with two scenarios is better than two separate ones.

---

## Test before writing

| # | Failure to reproduce | Tool | Pass if |
|---|---|---|---|
| 1 | "All present" when asked open-endedly about a file with planted gaps (1.0) | Free ChatGPT, free Gemini | It declares the file complete at least once in 3 runs |
| 2 | An invented rule or requirement when checking against rules it wasn't given (2.0) | Both | A flag appears that no supplied rule supports |
| 3 | An old rate quoted when old and new lists are both in the chat (3.0) | Both | It cites the superseded figure at least once in 3 runs |
| 4 | A handwritten date misread from a phone photo (4.0) | Both | A field is misread on a realistic invented summary |
| 5 | Suggests rewording or recoding when asked "how do I get this approved" (5.0) | Both | Suggests a change that would misrepresent the claim |

Failure 5 is the most likely not to reproduce, because current tools often refuse outright
fraud. Test subtle versions (choosing a "better fitting" package, emphasising a secondary
diagnosis). If even those don't reproduce, rebuild Unit 5 around the pressure from Ms. Karki
and the human line, and drop the AI suggestion. Don't stage a failure the tools don't produce.

## Reviews needed

- **Someone who works a hospital insurance desk**, on the file contents, the checklist and the
  rejection reasons.
- **Someone who knows the published package rules**, on every rule, rate and requirement used.
  Confirm the rules are published and usable as practice material before building on them.
- **Programme leads**, on D1 over D2, the cast, and whether to link the world to H1's.
- **Sources** for the evidence: unpaid claims reported at Rs10 billion to over Rs16 billion in
  2026, about one claim in five rejected, and hospitals suspending insurance services. They are
  2026 news figures and will go stale. Evidence layer only; Bikash's story carries no citations.

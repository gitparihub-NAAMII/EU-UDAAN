---
scu: scu.d1.u2.1
tier: 1
pattern: udaan-8-step
status: draft
---

# Point to the rule

> **DISCOVER IT YOURSELF**

*The reference lesson for the health-tech course, written against the 8-step flow (build manual
§3.1 Level 2) on the model of C1 2.1, "The Role". It is a draft. The AI replies in step 4 are
the replies the outline expects, not a transcript. Replace them with real replies once failure 2
in the outline's "Test before writing" has been reproduced on free ChatGPT and free Gemini. If it
doesn't reproduce, this lesson changes. See the authoring notes at the end.*

---

## 1 · Think first

> **FIRST, A QUESTION**

You've booked a week off in Asar to go home for a wedding. The day before you leave, a
colleague stops you in the corridor:

*"You can't take leave in Asar. It's the last month of the fiscal year. It's against the rules."*

They say it calmly, like everyone knows. Before you cancel your bus ticket, what's the one thing
you ask them?

## 2 · Hold your answer

> **REFLECT BEFORE WE GO ON**

Take ten seconds. Say it out loud if it helps.

Most people say some version of *"Which rule? Show me where it's written."* Not because they
think the colleague is lying, but because a rule you can't find might not be a rule.

Now here's the question that cracks Bikash's problem open. When the AI told him the gallbladder
claim needed prior approval, **did it ever say where that was written?**

## 3 · Look again

> **LOOK AGAIN AT BIKASH'S CHECK**

This is what Bikash pasted, with the patient's details already taken out, as he does every time
since Unit 1:

> Check this claim against my checklist and tell me any problems.
>
> **Checklist: surgical claims**
> 1. Claim form, signed by the patient or guardian
> 2. Referral slip from the referring health facility
> 3. Admission note with admission date
> 4. Operation note
> 5. Discharge summary, signed by the treating doctor
> 6. Itemised bill matching the package amount
> 7. Investigation reports supporting the diagnosis
> 8. Copy of the insurance card
>
> **The file:** Patient [removed]. Laparoscopic cholecystectomy (gallbladder removal).
> Admitted 3rd, discharged 6th. Claim form signed. Referral slip from the district hospital,
> dated 1st. Admission note present. Operation note present. Discharge summary present, no
> doctor's signature. Itemised bill present. Blood test reports present. No ultrasound report.
> Insurance card copy present.

And this is what came back:

> I've reviewed the claim against your checklist. I found the following problems:
>
> 1. **Missing ultrasound report.** The diagnosis of gallstones should be supported by imaging.
>    Without an ultrasound report, the claim may be rejected for insufficient evidence.
> 2. **Unsigned discharge summary.** The discharge summary must be signed by the treating
>    doctor.
> 3. **Prior approval required.** Laparoscopic cholecystectomy is a planned surgical procedure
>    and requires prior approval from the insurer before admission. No prior approval is
>    attached to this file.
>
> I recommend resolving these issues before submitting the claim.

Read the three problems again, slowly. They're written in the same voice, with the same
confidence, in the same bold type. Nothing on the page tells you that one of them is different
from the other two.

Two of them come from the checklist Bikash gave it, items 7 and 5. Find where the third one
came from.

You can't. It isn't on the checklist. It isn't in the file. It arrived sounding exactly as sure
as the two that were real, and Bikash spent two weeks chasing an approval that no rule asked for.

## 4 · Discover the fix

> **EXPERIMENT · One line added, everything else identical**

Same checklist, same file, a fresh chat each time. Bikash adds one line to the end of his
request and changes nothing else.

| What Bikash adds | What comes back |
|---|---|
| *(nothing: his original request)* | Three problems, all stated as fact. No way to tell which is real. **(This is what you'd normally type.)** |
| *"For each problem, say which rule it comes from."* | Ultrasound → *"Checklist item 7."* Signature → *"Checklist item 5."* Prior approval → *"Standard requirement for planned surgical procedures."* |
| *"For each problem, quote the exact words of the rule it comes from."* | Items 7 and 5 are quoted word for word. Prior approval → a sentence in quotation marks that appears nowhere in anything Bikash pasted. |
| *"For each problem, quote the exact words of the rule. If you can't quote one, write 'no rule found' instead of listing it as a problem."* | Items 7 and 5, quoted. Prior approval → *"No rule found in the checklist provided. Prior approval may be required by some insurers. Check with the insurance programme."* |

Look at the second row. "Standard requirement" sounds like a source, but you can't open it,
look it up or show it to anyone. It's a description of where a rule might be.

The third row is the one to stay on. Asked for exact words, the AI produced exact-sounding
words, in quotation marks, that Bikash had never given it. **If he'd only looked for quotation
marks, the invented flag would have passed.** The check only works if he puts the quote next to
the checklist and finds it there.

The fourth row is the first time the made-up flag shows itself, because Bikash gave it
somewhere honest to go.

Same file every time. The real problems never changed. What changed is that every flag had to
point at something Bikash could check.

> **The move that makes this work.** The first row is the learner's own default. Nobody types
> "and tell me the rule." So the failure in 2.0 wasn't bad luck or a bad tool. It's what this
> request produces, every time it's asked this way. Build manual §3.2 step 5 requires one
> variant to do this.

## 5 · Name it

> **NOW WE CAN NAME IT**

A flag with no rule behind it has a name on this desk: **a guess**. A flag that points to the
exact words of a rule you gave it, words you can find on the page, is a **cited flag**.

And here's why the guess sounds exactly as sure as the real ones. The AI doesn't look anything
up when it checks a file. It predicts what a careful reply to *"tell me any problems"* usually
looks like. Replies about surgical claims very often mention prior approval, so a reply that
mentions it reads as careful, and so it gets written. It's the same mechanism that writes the
two real flags. That's why they all come out in the same voice.

Asking for the rule's exact words changes what it's predicting. It's no longer predicting what a
careful reply sounds like. It's predicting a quotation from a page it was given. And a
quotation can be checked against that page.

**A flag without a clause is a guess.**

## 6 · The intuition

> **THE INTUITION**

You already do this with people. When a colleague says *"that's the rule,"* how much you believe
them depends on whether they can show you the circular. Someone who has read it says *"Section 4,
second paragraph"* without thinking. Someone repeating a rumour says *"everyone knows."*

> **THE MENTAL PICTURE**

Two notices about the same thing. One is pinned on the notice board, with a date and a stamp.
The other is something heard in the canteen. They can say exactly the same words. Only one of
them can be shown to the reviewer.

Asking for the clause is asking, every time: *board or canteen?*

## 7 · Your turn

> **YOUR TURN**

Three requests, none of them about claims. For each one, write the line you'd add so that every
answer has to point to something you can check. There's no single right wording.

1. You paste your office's leave policy into an AI tool and ask, *"Can I carry forward my unused
   leave?"*
2. You paste a school's admission notice and ask, *"What documents does my daughter need for
   Class 6 admission?"*
3. You paste a supplier contract and ask, *"Can we cancel this order without a penalty?"*

*For each one: if the answer it gives back has no quotation you can find in what you pasted,
what do you do next?*

## 8 · Generalise and bridge

> **THE BIGGER PICTURE**

Every time an AI tells you something is required, missing or not allowed, quietly ask: *where
is that written?* If it can't point to the words, and you can't find them on the page, treat it
as a question to take to a person, not a fact to act on.

Citing the clause is the first discovery in this unit. But look again at the fourth row. The AI
said "no rule found *in the checklist provided*." Bikash's checklist is one page. The insurance
programme's package rules run to many pages, and he never pasted them in.

So what happens when the rule the AI needs really does exist, and it isn't in the chat?

That's the next discovery.

---

## Authoring notes

Kept because this is the course's reference lesson, not because every lesson needs them.

- **The step 4 replies are expected, not observed.** They are written to the shape the outline
  predicts (failure 2, "an invented rule or requirement when checking against rules it wasn't
  given"). Before this lesson ships, run the four requests on free ChatGPT and free Gemini, three
  times each, in fresh chats, and paste the real replies in. Show them in full (build manual §3.0
  commitment 5).
- **What to do if it doesn't reproduce.** If no run invents a requirement, the unit's opening
  failure is false, and Unit 2 has to be rebuilt around a failure the tools do produce. Don't
  stage it (outline, "Test before writing").
- **The third row is a guess about current models.** A fabricated quotation is the most useful
  variant, because it shows that the citation has to be checked, not just requested. It's also
  the likeliest to vary between runs. If it never appears, drop the row. Three variants still meet
  the 2–4 rule.
- **The fourth row overlaps 2.2.** "No rule found" is the doorway to 2.2's lesson (check only
  against the rules supplied, and say "not covered" rather than fill the gap). Keep it here as a
  glimpse that sets up the bridge, and let 2.2 name it.
- **Every rule in this lesson is Bikash's own checklist**, not the insurance programme's
  published rules, so nothing here makes a claim about real package rules. "Prior approval" is
  the invented flag because it is a plausible-sounding requirement. Whether the real programme
  requires prior approval for any procedure must be checked with someone who knows the published
  rules before any lesson states it (`kb.rules.practice-claim-rules`).
- **Model-dependent experiment.** Like C1 2.1 and C3 3.2, this one can silently stop being
  true when the models change. It is a candidate for Tier 3, where the learner runs it live.
- **No acronym.** None is proposed for this course yet. If one comes out of the build, this
  lesson teaches its letter's concept and must not name the word.
- **The Your turn answers.** No answer key on the slide, matching C1 2.1. A sample line for
  each: *"Quote the exact sentence from the policy that answers this. If there isn't one, say so."*

---
scu: scu.h1.u2.1
tier: 1
pattern: udaan-8-step
status: draft
---

# Check it backwards

> **DISCOVER IT YOURSELF**

*The reference lesson for the health course on plain-Nepali patient instructions (H1), written
against the 8-step flow (build manual §3.1 Level 2) on the model of C1 2.1, "The Role", and
D1 2.1, "Point to the rule". It is a draft. The AI replies in step 4 are the replies the outline
expects, not a transcript. Replace them with real replies once failure 2 in the outline's "Test
before writing" has been reproduced on free ChatGPT and free Gemini. If it doesn't reproduce,
this lesson changes. See the authoring notes at the end.*

---

## 1 · Think first

> **FIRST, A QUESTION**

You send your younger brother to the bazaar with a list: rice, lentils, salt, cooking oil, a bar
of soap, matches. He comes back an hour later and puts the bag on the table.

You check the bag. Rice, on the list. Lentils, on the list. Salt, oil, soap, all on the list.
Nothing in the bag is wrong. Nothing in the bag is extra.

Is the shopping done? Before you say yes, what's the one thing you still do?

## 2 · Hold your answer

> **REFLECT BEFORE WE GO ON**

Take ten seconds. Say it out loud if it helps.

Most people say some version of *"Read the list again, and tick each thing off against the
bag."* Not the bag against the list. The list against the bag. Because you checked what came
back, and everything that came back was right. The matches weren't wrong. They weren't there.

Now here's the question that cracks Pooja's problem open. When she checked the plain version of
the iron and folic acid sheet, **which way did she check it?**

## 3 · Look again

> **LOOK AGAIN AT POOJA'S CHECK**

Since Unit 1, Pooja keeps her must-not-change list beside every slip: drug, dose, timing,
duration. This is Dr. Rijal's slip for a woman in her second trimester, with the name and number
already taken out, as Pooja does every time now:

> Patient [removed]. ANC, 2nd trimester.
> Iron + folic acid tab. 1 tab daily after evening meal. 180 days.
> With water or juice. Not with tea or milk.
> Black stools expected, normal.
> Come back at once if: bleeding, severe headache, blurred vision, swelling of face and hands.
> Next ANC visit 4 weeks.

And this is what came back when she asked for simple Nepali, shown here in English:

> Here is the instruction in simple words:
>
> 1. Take one iron tablet every day, after your evening meal, for 180 days.
> 2. Take it with water or juice. Do not take it with tea or milk.
> 3. Your stool may turn black. This is normal.
> 4. If you feel unwell, consult a health worker.
> 5. Come for your next check-up in 4 weeks.

Pooja ran her check. Drug: iron and folic acid, line 1. Dose: one tablet, line 1. Timing: daily,
after the evening meal, line 1. Duration: 180 days, line 1. Four ticks. Every number matched.
She handed it over, and the woman walked home.

Read the plain version again, slowly. Every line in it is true. Nothing in it contradicts the
slip. If you had checked it the way Pooja did, you would have passed it too.

Now read the slip again, and this time find the line that isn't in the plain version.

*Come back at once if: bleeding, severe headache, blurred vision, swelling of face and hands.*

Four signs, and the words "at once". In the plain version they've become line 4, *"if you feel
unwell, consult a health worker,"* which is true, and asks for nothing in particular. She had a
headache for two days. A headache didn't feel like "unwell." She waited.

Pooja's check couldn't have found this. She checked what was on the page, and everything on the
page was right. The problem was never on the page.

## 4 · Discover the fix

> **EXPERIMENT · One line changed, everything else identical**

Same slip, same plain version, a fresh chat each time. Pooja pastes both and changes only the
checking instruction.

| What Pooja asks | What comes back |
|---|---|
| *"Is this plain version correct?"* | *"Yes. The plain version correctly conveys the medicine, the dose, the timing and the duration, and keeps the advice about tea and milk, black stools and the follow-up visit. It is clear and appropriate for a patient."* **(This is what you'd normally type.)** |
| *"Is this plain version complete?"* | *"Yes, it is complete. It covers how to take the tablet, what to avoid, the expected side effect, when to seek help, and the next visit."* |
| *"Check each line of the plain version against the prescription. Is anything wrong?"* | Five lines, five verdicts: *"Line 1, matches. Line 2, matches. Line 3, matches. Line 4, consistent with the prescription's advice to return. Line 5, matches. No errors found."* |
| *"Check each line of the prescription against the plain version. For every line of the prescription, say: kept, changed, or missing."* | Six lines, six verdicts. Lines 1 to 4 and 6: *kept*. Line 5: ***missing** — "the prescription says to come back at once if there is bleeding, severe headache, blurred vision, or swelling of the face and hands. The plain version says only 'if you feel unwell, consult a health worker'. The four signs and 'at once' are not in the plain version."* |

Look at the third row. That is Pooja's own check, the one she ran by hand, and the tool ran it
the same way and reached the same answer: nothing wrong. Both were right. There is nothing wrong
in the plain version.

The fourth row is the first time anything turns up, and the only thing that changed is the
direction. Starting from the slip, every source line has to get a verdict, and a line that got
dropped has nowhere to hide: it comes back *missing*, with the slip's own words beside it.

Same two texts every time. The plain version never changed. What changed is which text the
check started from.

> **The move that makes this work.** The first row is the learner's own default. Nobody types
> "for every line of the original, say kept, changed or missing." So Pooja's miss in 2.0 wasn't
> carelessness and it wasn't a bad tool. It's what a check that starts from the new text
> produces, every time it's run that way. Build manual §3.2 step 5 requires one variant to do
> this; here, three do.

## 5 · Name it

> **NOW WE CAN NAME IT**

Checking the plain version against the slip has a name on this counter: a **one-way check**. It
finds what's wrong. It can't find what's gone.

Reading the slip line by line and demanding a verdict for every line, *kept, changed or
missing*, is the **two-way check**. Since you already ran the first way, think of the second as
**checking it backwards**.

And here's why the warning dropped in the first place, and why the one-way check can't see it.
The tool doesn't carry the slip across into simpler words, line for line. It predicts what a
simple instruction sheet for this medicine usually looks like, one line at a time, borrowing
from the many such sheets it has seen. Most of those sheets end with a general line about seeing
a health worker if you feel unwell. Very few carry this slip's exact four signs. So the common
line gets written, and the specific one doesn't, and the sheet still reads like a good sheet.

Then a check that asks *"is anything wrong?"* reads the common line, finds it true, and passes
it. A dropped line leaves no mark in the text that replaced it. The only place it still exists is
the slip. So the only check that can find it is one that starts from the slip.

**What's wrong leaves a trace. What's missing doesn't. Start from the source.**

## 6 · The intuition

> **THE INTUITION**

You already do this with lists. Nobody checks the shopping by admiring the bag. You read the
list and look for each item. Nobody checks a wedding guest list by counting who turned up; you
read the names and notice who hasn't. The thing you're afraid of losing is on the list, not in
the bag, so that's where you start.

> **THE MENTAL PICTURE**

A teacher taking attendance. She doesn't look around the room and ask *"is everyone here who's
here?"* She opens the register and calls every name. The names that get no answer are the ones
that matter, and the only way to hear the silence is to call the name.

Checking it backwards is calling the register. The slip is the register. Every line gets called.

## 7 · Your turn

> **YOUR TURN**

Three rewrites, none of them about medicine. For each one, write the one line you'd add so that
every line of the original gets a verdict. There's no single right wording.

1. Your school's notice to parents about admission day has been translated by an AI tool from
   English into Nepali. It reads beautifully. Which text do you start from, and which line are
   you most afraid of losing: the date, the fee, or *"bring the birth certificate"*?
2. A supplier's contract has been summarised by an AI tool onto one page, and someone is about
   to sign on the strength of the summary. What do you ask for, line by line, before they do?
3. The minutes of yesterday's meeting were written by an AI tool from your notes. You check them
   against the agenda and against your notes. What's in the third column?

*For each one: if a line of the original comes back "missing", what do you do next?*

## 8 · Generalise and bridge

> **THE BIGGER PICTURE**

Every time a tool rewrites, shortens, summarises or translates something for you, it produces a
new text, and the old text doesn't argue back. The new one can be fluent, true in every line,
and still be missing the one line that mattered. So whenever something has been rewritten,
quietly ask: *did I call the register?* Start from the source. Give every line a verdict.

Checking it backwards is the first discovery in this unit. But look again at the fourth row.
Line 5 came back *missing*, and Pooja put it back. The next day a different sheet came back with
its warning line marked *kept*: *"You may feel some discomfort; in that case, you could consider
consulting a health worker."* Every word of the warning had survived, in a sense. And a woman
reading it would still not come back at once.

So what happens when the warning is there, and it still asks for nothing?

That's the next discovery.

---

## Authoring notes

Kept because this is the course's reference lesson, not because every lesson needs them.

- **The step 4 replies are expected, not observed.** They are written to the shape the outline
  predicts (failure 2, "a warning softened or dropped"), with the checking variants added. Before
  this lesson ships, run the four requests on free ChatGPT and free Gemini, three times each, in
  fresh chats, and paste the real replies in. Show them in full (build manual §3.0 commitment 5).
- **What to do if it doesn't reproduce.** If the warning survives every run of the Unit 1
  request, the unit's opening failure is false, and Unit 2 has to be rebuilt around a failure the
  tools do produce. Don't stage it (outline, "Test before writing").
- **The third row is the one most likely to vary.** Some runs may find the omission even when
  the check starts from the plain version. Keep the row only if it misses in at least two of
  three runs; otherwise drop it. Three variants still meet the 2–4 rule, and the first two are
  both the learner's default.
- **The slip is invented.** One tablet daily after the evening meal, 180 days, not with tea or
  milk, black stools expected: these are the invented slip's lines in the shape of a real one, not
  advice, and a clinician or pharmacist reviews the slip and the warning line before the lesson
  ships (`kb.rules.practice-prescriptions`). The warning is shown because the lesson is about
  its disappearance, not its content. Nothing here teaches medicine.
- **Language.** The plain version is shown in English in this draft. The delivered lesson shows
  the Nepali the tool produced, with the English beside it, and a Nepali-reading reviewer checks
  the register (outline, test 3). The lesson's point survives either way: the line is missing in
  any language.
- **The fourth row overlaps 2.2.** The softened warning in the bridge is 2.2's failure. Keep it
  here as a glimpse that sets up the next discovery, and let 2.2 name it.
- **Model-dependent experiment.** Like C1 2.1 and D1 2.1, this one can silently stop being true
  when the models change. It is a candidate for Tier 3, where the learner runs it live.
- **No acronym.** This lesson earns the concept behind one letter of the course's candidate word
  and must not name the word.
- **The Your turn answers.** No answer key on the slide, matching C1 2.1. A sample line for each:
  *"For every line of the original, say kept, changed or missing, and quote the original line
  beside your answer."* And if a line is missing: put it back, in the original's words.

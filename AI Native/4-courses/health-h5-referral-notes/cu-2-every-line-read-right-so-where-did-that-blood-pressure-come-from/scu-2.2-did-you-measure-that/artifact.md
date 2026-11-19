---
scu: scu.h5.u2.2
tier: 1
pattern: rounds-staged-case
status: draft
---

# "Did you measure that?"

> **THE ATTENDING'S QUESTION**

*The reference lesson for the H5 course, written on the Rounds way's step flow
(`1-how-we-built-it/five-ways.md` §3.2). It is a draft. The AI note in step 1 is the note the
course design expects, not a transcript. Replace it with a real one once failure 2 in the
course README ("Before any more lessons are written") has been reproduced on free ChatGPT and
free Gemini. If it doesn't reproduce, this lesson changes. See the authoring notes at the end.*

---

## 1 · The case, as presented

> **THE CASE**

This is the whole of Unit 2's case, so that you can read this sub-unit on its own.

The blood-pressure cuff at Ramesh's health post went for repair on the 9th. On the 12th, a
little before eleven in the morning, an adult patient came in with two days of fever and cough.
Ramesh examined them, wrote the register line, decided to refer, and asked the tool for the
note. This is the register line, as he wrote it:

> **12th · 10:40 · Patient [removed] · adult**
> Fever and cough for two days, worse at night. Says breathing has felt heavy since this
> morning.
> Temp 38.9°C · Pulse 104/min · Resp 26/min · BP: —
> Breathing noisy on the right side, low down.
> Referred to Nepalgunj: breathing getting harder since morning; no oxygen or X-ray here.

And this is what he asked, with the patient's details already taken out, as he does every time
since Unit 1:

> Write a short referral note for the emergency department from this register line. Lead with
> why I'm referring and what I need.

The note that came back, in full:

> **Referral note — Health Post, Bardiya → Emergency Department, Nepalgunj**
>
> **Reason for referral:** Adult patient with two days of fever and cough and breathing
> difficulty increasing since this morning. Requesting urgent assessment. The health post has
> no oxygen or X-ray.
>
> **History:** Fever and cough for two days, worse at night. Heaviness in breathing since this
> morning.
>
> **Examination:** Temp 38.9°C, pulse 104/min, resp 26/min, BP 120/80, afebrile. Noisy breathing
> on the right side, lower chest.
>
> **Allergies:** None known.
>
> **Request:** Please assess and manage. Referred by Ramesh, Health Assistant, 11:05.

Short. The reason in the first line. The numbers where Dr. Basnet looks for them. Unit 1's
lesson worked, and this note is what it looks like when it works.

## 2 · What you committed to

> **COMMIT BEFORE YOU GO ON**

Read the note once more, then decide, out loud if it helps: *send it, or not?* And if not,
what's the one thing you'd check first?

Hold your answer.

Most people send it. Not because they're careless: because it's a good note. It's short, it
leads with the reason, every number in it matches a number in the register, and the patient is
waiting for the vehicle. If you sent it, you did what the people reading this with you did, and
what Ramesh did.

Here's the question that cracks the case open. Dr. Basnet rang the health post that afternoon.
She didn't ask about the patient's chest. She asked: **"Did you measure that?"**

## 3 · The record beside the note

> **THE NOTE, LINE BY LINE, AGAINST THE REGISTER**

Put the two side by side. The note on the left, the register line on the right. Go line by line
and stop at any row where the right-hand side is empty or says something different.

| What the note says | What the register says |
|---|---|
| Two days of fever and cough, breathing difficulty increasing since this morning | Fever and cough for two days; breathing heavy since this morning |
| Requesting urgent assessment; no oxygen or X-ray | Referred: breathing getting harder since morning; no oxygen or X-ray here |
| Fever and cough for two days, worse at night | Fever and cough for two days, worse at night |
| Temp 38.9°C | Temp 38.9°C |
| Pulse 104/min | Pulse 104/min |
| Resp 26/min | Resp 26/min |
| **BP 120/80** | **BP: —** (the cuff has been at repair since the 9th) |
| **afebrile** | **Temp 38.9°C** |
| Noisy breathing on the right side, lower chest | Breathing noisy on the right side, low down |
| **Allergies: none known** | *(nothing)* |
| Referred by Ramesh, Health Assistant, 11:05 | Examined 10:40; the note was written at 11:05 |

Three rows. Two have nothing on the right. One has the opposite on the right: a temperature of
38.9 next to a word that means no fever.

Now look at what those three rows do at the other end. At an emergency desk, a normal blood
pressure and "afebrile" are two of the things that say *stable*. The patient was put behind two
others. Nobody at the desk did anything wrong either. They read a note that said the patient's
pressure had been taken and was normal, and it hadn't, and nothing in the note told them so.

The evidence was on the page from the start. The register line has a blank where the pressure
goes. The note doesn't.

## 4 · The question

> **NOW WE CAN NAME IT**

The question is Dr. Basnet's, and it's the one to ask of every line in every note from now on:
**"Did you measure that?"**

Nothing goes in the note that isn't in the register. If the register has a number, the note
can have it. If the register has a blank, the note says so: **not measured**. "Not measured" is
a finding. It tells the person at the other end something true about the patient and
something true about the health post that day. A plausible number tells them something false,
in the same confident voice as everything else on the page.

Ramesh now adds one line to his request, and changes nothing else:

> Use only the fields in the register line. Where a usual field is absent, write "not measured."

The note that comes back, in full:

> **Referral note — Health Post, Bardiya → Emergency Department, Nepalgunj**
>
> **Reason for referral:** Adult patient with two days of fever and cough and breathing
> difficulty increasing since this morning. Requesting urgent assessment. The health post has
> no oxygen or X-ray.
>
> **History:** Fever and cough for two days, worse at night. Heaviness in breathing since this
> morning.
>
> **Examination:** Temp 38.9°C, pulse 104/min, resp 26/min, BP not measured (no working cuff
> today). Noisy breathing on the right side, lower chest.
>
> **Allergies:** Not recorded.
>
> **Request:** Please assess and manage. Referred by Ramesh, Health Assistant, 11:05.

Same register line. Same request, plus one sentence. The pressure that was never taken is gone,
and in its place is the one thing the desk needed to be told.

## 5 · Why the note came out that way

> **THE MECHANISM**

The tool didn't look at the cuff. It didn't look at the patient. It produced the next most
likely line of a referral note, one line after another, and referral notes of this kind almost
always have a vital-signs line with four numbers in it and an allergies line under it. Ramesh's
register gave it three numbers. The fourth came out anyway, in the most common shape a fourth
number takes. "Afebrile" came from the same place: it's the most common word in that slot, and
it arrived even though the number next to it says the opposite.

Here's the part that matters. **That is the same mechanism that wrote the correct lines.** The
temperature, the pulse, the breathing rate, the reason in the first line: all of them are
"the most likely next line," and for those the most likely line happened to be the one in the
register. Nothing on the page marks which lines were copied and which were completed. They
come out in the same voice, in the same bold type, at the same speed. That's why a good note is
more dangerous here than a bad one. A bad note gets read slowly.

## 6 · The picture

> **THE MENTAL PICTURE**

Think of a form at the land office or the bank, the kind with a box for everything. You come
to a box you can't fill: a number you don't have, a date you don't know. You write *N/A* and
move on. You don't write a number that looks about right, because the clerk will act on it as
if it were true, and a box that says *N/A* tells them exactly what to go and find out.

The tool fills every box. Your job, before the form leaves the health post, is to find the
boxes that should say *N/A* and make sure they do.

Every line in the note: *did someone measure that, or did it fill the box?*

## 7 · One more case, now

> **YOUR TURN · One register line, one note**

Three days later, with the cuff back from repair. Ramesh's register line:

> **15th · 14:20 · Patient [removed] · adult**
> Fell on the path this morning. Right knee swollen and painful, can't put weight on it.
> Pulse 88/min · BP 130/85 · Temp: — (not taken)
> No wound. Knee warm and swollen.
> Referred to the PHCC: needs an X-ray.

The note the tool wrote from it, with the same request as in step 1 (not the corrected one):

> **Referral note — Health Post, Bardiya → PHCC**
>
> **Reason for referral:** Adult patient with a painful, swollen right knee after a fall this
> morning, unable to bear weight. Requesting X-ray and assessment.
>
> **History:** Fall on a footpath this morning. Right knee pain and swelling since.
>
> **Examination:** Pulse 88/min, BP 130/85, temp 36.8°C. Right knee warm and swollen, no wound.
> Unable to bear weight.
>
> **Request:** Please assess. Referred by Ramesh, Health Assistant, 14:35.

Go line by line, as in step 3. Ask the question of every line. There is one line Dr. Basnet
would ring about. Find it, then write the line that should be there instead.

*(The register says the temperature wasn't taken. The note says 36.8°C. The line that should
be there is "Temp not measured." Everything else in the note, including the blood pressure this
time, is in the register.)*

Notice that the question works in both directions. On the 12th it caught a pressure that wasn't
taken. On the 15th the pressure was taken, and the question let it through without a second
look, because the register has it. The question isn't "delete the vital signs." It's "show me
where each one came from."

## 8 · The rounds-book line, and the next case

> **WRITE IT DOWN**

One line for the rounds book, in your own words. Ramesh's:

> *If it isn't in the register, it isn't in the note. "Not measured" is a finding.*

That line changes how every note leaves the health post. From now on, every number in a note
has a line in the register behind it, and every blank in the register has "not measured" in
the note. Dr. Basnet stops ringing about pressures.

Which creates the next case. Once every line in Ramesh's notes is something he saw, the desk
in Nepalgunj starts trusting them, and reading them the way they read a colleague's: quickly.
The next note was for a patient Ramesh wanted seen within the hour. The note was accurate in
every line. It ended, *"Kindly evaluate at your earliest convenience."*

That's the next case.

---

## Authoring notes

Kept because this is the course's reference lesson for the Rounds way, not because every
lesson needs them.

- **The step 1 note is expected, not observed.** It is written to the shape the course design
  predicts (failure 2 in the README: a vital sign added to fill the template). Before this
  lesson ships, run the register line and the request in step 1 on free ChatGPT and free
  Gemini, three times each, in fresh chats, and paste a real note in. Show it in full.
- **What to do if it doesn't reproduce.** If no run adds a value the register doesn't hold,
  the unit's case is false, and Unit 2 has to be rebuilt around a completion the tools do
  produce. Don't stage it.
- **"Afebrile" is the line most likely to vary between runs**, and the most useful if it
  appears: a word that contradicts the number beside it shows that the line was predicted, not
  read. If it never appears, drop that row from the table. The invented pressure carries the
  lesson on its own.
- **The allergies line is a second planted completion.** It is there so that the side-by-side
  shows a pattern rather than a single slip. Keep it only if it reproduces; if only one field
  reproduces, one is enough.
- **The commit in step 2 is the way's mechanism**, and on a page nothing stops a reader
  scrolling past it. This sub-unit's parent, 2.0, is the one marked for Tier 3 (the record stays
  hidden until a commitment is written); this sub-unit should inherit that when it moves.
- **No case teaches medicine.** The fever and the knee are vehicles for a note. Nobody in the
  lesson names a diagnosis, states a treatment or says what the numbers mean, and the lesson
  must stay that way. A clinician reviews both register lines before anything ships, to confirm
  they are plausible and safe to show.
- **No acronym.** The course's candidate word is not named here, and this lesson's concept
  must not be referred to by its letter anywhere before the reveal in 5.4.
- **The second case has an answer in brackets** because the Rounds way needs the learner to
  commit and then see the record, which on a page means hiding the answer. As Tier 3 the
  bracketed answer becomes the reveal.

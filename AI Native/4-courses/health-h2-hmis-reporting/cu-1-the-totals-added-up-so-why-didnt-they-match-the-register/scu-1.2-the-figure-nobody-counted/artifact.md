---
scu: scu.h2.u1.2
tier: 1
pattern: audit-investigation
status: draft
---

# The figure nobody counted

> **THE FINDING**

*The reference lesson for the H2 course and for the Audit way (`1-how-we-built-it/five-ways.md`
§3.4), written on the step flow inside `the-finding`. It is a draft. The report form, the
register extracts and the tool's replies are invented to the shape the course design predicts
(README, Unit 1); the replies are what the design expects, not a transcript. Replace them with
real replies once failure 1 in the README's "Before any more lessons are written" has been
reproduced on free ChatGPT and free Gemini. If it doesn't reproduce, this lesson changes. See
the authoring notes at the end.*

---

## 1 · What was on the desk

> **WHAT LANDED ON THE DESK**

It's the last week of Kartik, and the municipality's health section wants the monthly report by
Friday. Sangita is the HMIS focal person at the primary health care centre. The registers are
hers, and so is the report.

Here's how she did it this month. She photographed the register pages with her phone, a ruler
laid over the name column the way she always does, so nothing in the photo could identify
anyone. She had a free AI tool turn the photos into text: one line per entry, the register's
serial number and the date, nothing else. Then she opened a fresh chat, pasted the extracts,
pasted the blank monthly form, and asked:

> Here are this month's register extracts and the monthly report form. Fill in the form from
> the extracts.

Two minutes later she had this:

> **Monthly report, Kartik**
>
> | Line | Service | This month |
> |---|---|---|
> | 1 | Outpatient visits, new | 612 |
> | 2 | Outpatient visits, follow-up | 238 |
> | 3 | Antenatal first visits | 48 |
> | 4 | Antenatal fourth visits | 31 |
> | 5 | Deliveries at the facility | 9 |
> | 6 | Children fully immunised | 27 |
> | 7 | Family planning, new acceptors | 19 |
> | 8 | Referrals out | 14 |
> | 9 | Laboratory tests done | 203 |
> | 10 | Deaths reported | 0 |
>
> All lines have been filled from the register extracts provided, and the totals have been
> checked for consistency.

It looks like a report. It's laid out like one, it reads like one, and the last sentence is the
one you'd want to see.

Now here is one of the extracts it was filled from, in full. It's the antenatal register, first
visits only, as the tool transcribed it from Sangita's photographs: the register's own serial
number, and the date of the visit.

> **Antenatal register, first visits, Kartik** (serial · date)
>
> | | | | |
> |---|---|---|---|
> | 1187 · Kartik 1 | 1188 · Kartik 1 | 1189 · Kartik 2 | 1190 · Kartik 2 |
> | 1191 · Kartik 2 | 1192 · Kartik 4 | 1193 · Kartik 5 | 1194 · Kartik 5 |
> | 1195 · Kartik 6 | 1196 · Kartik 8 | 1197 · Kartik 8 | 1198 · Kartik 8 |
> | 1199 · Kartik 9 | 1200 · Kartik 9 | 1201 · Kartik 11 | 1202 · Kartik 12 |
> | 1203 · Kartik 12 | 1204 · Kartik 13 | 1205 · Kartik 15 | 1206 · Kartik 15 |
> | 1207 · Kartik 15 | 1208 · Kartik 16 | 1209 · Kartik 18 | 1210 · Kartik 18 |
> | 1211 · Kartik 19 | 1212 · Kartik 19 | 1213 · Kartik 20 | 1214 · Kartik 22 |
> | 1215 · Kartik 22 | 1216 · Kartik 23 | 1217 · Kartik 23 | 1218 · Kartik 23 |
> | 1219 · Kartik 25 | 1220 · Kartik 25 | 1221 · Kartik 26 | 1222 · Kartik 26 |
> | 1223 · Kartik 27 | 1224 · Kartik 29 | 1225 · Kartik 29 | 1226 · Kartik 29 |
> | 1227 · Kartik 30 | 1228 · Kartik 30 | 1229 · Kartik 30 | |

And here is the delivery register for the same month, transcribed the same way:

> **Delivery register, Kartik** (serial · date)
>
> | | | |
> |---|---|---|
> | 302 · Kartik 3 | 303 · Kartik 7 | 304 · Kartik 9 |
> | 305 · Kartik 14 | 306 · Kartik 17 | 307 · Kartik 21 |
> | 308 · Kartik 24 | 309 · Kartik 28 | 310 · Kartik 30 |

The report says it was filled from these. Nothing on the page says anything is wrong, and the
municipality is waiting.

## 2 · The figure you followed

> **PICK ONE FIGURE**

You can't trace ten lines before Friday if each one means finding its pages and counting them.
So you pick one. Not the biggest. The one someone will act on.

Line 3 is the one the municipality's officer rang about last quarter, and the one Sangita would
least like to defend from memory if he rang again. So that's hers.

Before you read on, choose yours, and say in one line why. If you chose line 1 because it's the
largest, that's a fine reason. The method is the same for every line. We'll follow Sangita's.

## 3 · The register line

> **THE TRACE**

Go back to the antenatal extract above. Count the entries. Use a finger. Write the number down
before you read the next sentence.

Forty-three.

If you got 43, good. If you got something else, count once more. It matters that the number is
yours, not ours. The serial numbers agree with you: the first entry is 1187 and the last is
1229, and 1229 − 1187 + 1 is 43.

The report says 48.

Now trace the deliveries the same way. Nine entries, serials 302 to 310. The report says 9.

| Line | Reported | Counted | Difference |
|---|---|---|---|
| 3 · Antenatal first visits | 48 | 43 | **+5** |
| 5 · Deliveries at the facility | 9 | 9 | 0 |

Where are the five? Not on a second page: the extract runs to the 30th, and 1229 is the last
serial in the register. Not in another register: first visits are recorded in this one only.
Five women who were reported don't exist anywhere on paper.

## 4 · The finding

> **THE FINDING, AS EVIDENCE**

A finding is written so that someone with the same extract can check it in two minutes. It
names the figure, both numbers, where the real one came from, and the difference. It doesn't say
who was careless, because nobody was.

| | |
|---|---|
| **Figure** | Line 3, antenatal first visits |
| **Reported** | 48 |
| **Counted** | 43 |
| **Source lines** | Antenatal register, first visits, serials 1187–1229, Kartik 1–30 |
| **Difference** | 5 reported that are not in the register |
| **What changes** | Line 3 becomes 43. Every other line is traced before Friday |

That last row is the one that costs time, and it's the one that matters. One wrong line doesn't
tell you the other nine are right. It tells you that you don't yet know.

## 5 · Why the report came out that way

> **WHY THE REPORT CAME OUT THAT WAY**

Nothing careless happened. Sangita gave the tool the right extracts and a clear request, and it
gave her back a filled form, which is what a request like hers is usually followed by.

That's the mechanism. When you paste forty-three lines and ask for a monthly form, the tool
doesn't add the lines up unless the request makes it list them one by one. What it does is
produce the text that usually follows a request like this: a form with a plausible number in
every box. For each line, it predicts a figure that fits: the size of the extract, the shape
monthly figures usually have, the other numbers around it. Sometimes the prediction lands on
the real count. A list of nine is short, and 9 is easy to land on. A list of forty-three isn't,
and 48 is close, and close is what prediction produces.

So the right figure and the wrong figure aren't one careful line and one careless line. They're
the same mechanism twice, with different luck.

And the last sentence of the report, *"the totals have been checked for consistency"*, is the
same mechanism a third time. It's what a careful report ends with, so it gets written. It isn't
a record of something that happened.

## 6 · The rule, named

> **NOW WE CAN NAME IT**

**Counted, not predicted.** Every figure in the report traces to register lines you counted.

The tool can transcribe a page, sort entries by date, and list them. Counting is yours, or a
spreadsheet's. The check is one instruction added to the request. Here is the one Sangita added,
with everything else the same:

> For each line of the form, first list every register entry you are counting, with its serial
> number and date. Then write the count. Do not write a figure on any line without its list.

And here is what came back for line 3:

> **Line 3, antenatal first visits.** Register entries counted:
> Kartik 1: 1187, 1188 · Kartik 2: 1189, 1190, 1191 · Kartik 4: 1192 · Kartik 5: 1193, 1194 ·
> Kartik 6: 1195 · Kartik 8: 1196, 1197, 1198 · Kartik 9: 1199, 1200 · Kartik 11: 1201 ·
> Kartik 12: 1202, 1203 · Kartik 13: 1204 · Kartik 15: 1205, 1206, 1207 · Kartik 16: 1208 ·
> Kartik 18: 1209, 1210 · Kartik 19: 1211, 1212 · Kartik 20: 1213 · Kartik 22: 1214, 1215 ·
> Kartik 23: 1216, 1217, 1218 · Kartik 25: 1219, 1220 · Kartik 26: 1221, 1222 · Kartik 27: 1223 ·
> Kartik 29: 1224, 1225, 1226 · Kartik 30: 1227, 1228, 1229
> **Count: 43**

Same extract, same tool. The difference is that the figure had to come after its list, and a
list is something you can hold against the register.

One more thing, and it's the whole rule. When the list says 43, the tool still hasn't counted.
You have, by checking the list against the extract, entry for entry, and counting the entries
yourself. If the list carries a serial that isn't in the extract, or skips one that is, the
figure is wrong again, and now you can see where.

So the check, in three lines:

1. Ask for the list behind every figure.
2. Count the list yourself, against the register.
3. A figure without a list doesn't go on the form.

## 7 · The picture

> **THE PICTURE**

The end of the day at a shop. The owner counts the notes in the drawer, one by one, and writes
the total in the cash book. She doesn't ask the assistant who has watched a thousand drawers
close to look at this one and say what's in it. His guess would be close. It might even be
right. But close is wrong for a cash book, and a guess that happens to be right is still a
guess.

The monthly report is the cash book. Every figure in it is a count someone made, or it isn't a
figure.

## 8 · Apply it once, and the next report

> **APPLY IT ONCE**

Line 8, referrals out, reported as 14. Here is the referral register for the month, transcribed
the same way:

> **Referral register, referrals out, Kartik** (serial · date)
>
> | | | | |
> |---|---|---|---|
> | 88 · Kartik 1 | 89 · Kartik 2 | 90 · Kartik 6 | 91 · Kartik 9 |
> | 92 · Kartik 10 | 93 · Kartik 13 | 94 · Kartik 16 | 95 · Kartik 19 |
> | 96 · Kartik 21 | 97 · Kartik 24 | 98 · Kartik 26 | 99 · Kartik 28 |
> | 100 · Kartik 30 | | | |

Count the entries. Check your count against the serials. Then write the finding in the same
form as the one above: figure, reported, counted, source lines, difference, what changes.

*Thirteen, serials 88 to 100. Reported 14, counted 13, one referral reported that isn't in the
register. Line 8 becomes 13.*

And if it had matched? The trace wouldn't have been wasted. A match is the only reason you have
to sign a line. The deliveries figure was right, and Sangita can say so, because she counted.

> **THE NEXT REPORT**

By Thursday evening every line in Sangita's report has a list behind it and a count she made.
Ten figures she can defend if the phone rings.

Then the municipality asks for the paragraph that goes under the table. What changed this
month, and why. Sangita has figures she trusts now, so she gives the tool the form and asks for
the paragraph. It comes back fluent, and every number in it is right.

That's the next investigation.

---

## Authoring notes

Kept because this is the course's reference lesson and the Audit way's first written sub-unit.

- **The form is invented.** The ten lines are in the shape of a monthly facility report, not a
  copy of the real HMIS form, and no real indicator definition appears (`kb.rules.practice-hmis-registers`).
  Before this lesson ships, someone who works with the current form confirms the invented lines are
  the right shape and the right words for a Nepali learner. The serial numbers, dates and
  counts are invented too; the extracts carry no names, and the lesson shows Sangita keeping
  names out of the photographs because the real practice must.
- **The tool's replies are expected, not observed.** The filled form, the closing sentence and
  the listing are written to the shape the design predicts (README, Unit 1, failure 1). Before
  this ships, run both requests on free ChatGPT and free Gemini, three times each, in fresh
  chats, and paste the real replies in full.
- **If it doesn't reproduce.** If the tool counts forty-three lines correctly every time, make
  the extract realistic: real register pages run to hundreds of entries, and the real input is
  a photograph, not clean text. If it still counts right, Unit 1's opening failure is false and
  the unit is rebuilt around a failure the tools do produce. Don't stage it.
- **The listing's format will vary** between runs and tools. Keep whatever format the real run
  gives; the lesson's point is that a list exists and can be checked, not how it's laid out.
- **The closing sentence** (*"the totals have been checked"*) is the likeliest line to vary. If
  no run produces one, drop it from step 1 and the last paragraph of step 5.
- **The learner counts before reading on, twice.** On a page nothing enforces it
  (`five-ways.md` §4). 1.1 *Follow one figure* is the Tier 3 candidate for this unit, where the
  extract is a table the learner can sort and count in; this sub-unit stays text.
- **No acronym.** The candidate word for this course is named only in 5.4. This lesson teaches
  its first letter's concept and must not name the word.
- **The apply-it-once answer** is given in italics after the exercise, matching the way the
  D1 reference lesson gives sample lines. Move it to the end of the lesson if cohorts read ahead.

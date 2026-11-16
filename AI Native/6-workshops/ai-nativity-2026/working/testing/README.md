# testing/

Everything you need to test the Part 4 chain (Listener → Writer → Checker) with Gemini skills
before you deliver it. This folder is for you, not participants.

| File | What it is |
|---|---|
| [`1-listener.txt`](1-listener.txt) | Listener skill: name, description, files, instructions, ready to paste |
| [`2-writer.txt`](2-writer.txt) | Writer skill, same layout. Attach D2-02 |
| [`3-checker.txt`](3-checker.txt) | Checker skill, same layout. Attach D2-02 |
| [`D2-01_thursday_transcript.txt`](D2-01_thursday_transcript.txt) | The input for the Listener |
| [`D2-02_team_and_contacts.txt`](D2-02_team_and_contacts.txt) | The file to attach to the Writer and the Checker |

The three `.txt` files are generated from `../handouts/skills/*/SKILL.md`, and D2-01 and D2-02 are
copies from `../handouts/`. If you change an instruction, change the SKILL.md and D2-03 too, then
regenerate these files (ask Claude to "regenerate testing from the skills").

## How to run a test

1. Use a personal Google account, aged 18 or over, at gemini.google.com.
2. Create each skill: **Customize → Skills → Create → Create manually**. Paste the name,
   description and instructions, add the file (Writer and Checker only), and press **Create**.
3. **Listener:** open a new chat, type `/listener`, paste D2-01, and send.
4. **Writer:** copy the whole table. Open a new chat, type `/writer`, paste the table, and send.
5. **Checker:** copy all the drafts. Open a new chat, type `/checker`, paste the drafts, and send.
6. Record what came back in the log below.

## What should happen

These outcomes were recorded with Gems in D2-03 v4. Confirm them with skills.

| Worker | Expect |
|---|---|
| Listener | Table with Owner, Action, Due date and Source line. **CONFLICT** on the Kalimati refund (one lakh twenty vs one lakh forty). **UNASSIGNED** on the internet bill. **NOT STATED** on the Gurung follow-up. **INAUDIBLE** on the overlap. The signboard notice and staff bonus go under a "raised but unresolved" heading |
| Writer | Four drafts going out: Biratnagar client (English); Shrestha Suppliers, Gurung Traders and the Kalimati landlord (Nepali). "Check the chalan" under INTERNAL. Signboard and bonus under RAISED BUT NOT DECIDED. Internet bill under NEEDS AN OWNER |
| Checker | **HOLD** on the Kalimati landlord draft (UNSETTLED). The Shrestha/Gurung leak may or may not appear; in v4 it didn't, and the other drafts came back SEND |

## Log

Add a row per run. If a result differs from the expected one, update the "what came back" slides
(94 and 99 in the deck) and D2-03 before you promote.

| Date | Account | Listener OK? | Writer: 4 drafts, right languages? | Checker: landlord HOLD? | Shrestha leak caught? | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |

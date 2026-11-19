# Handouts

Participant files for the AI Nativity session. Text files are committed as-is. `.docx` / `.pdf`
are gitignored and get a generated `.md` twin (`_system/tools/docx_to_md.py`). Never hand-edit a twin.

Source: `For Testing-20261116T040221Z-1-001.zip` (a Google Drive export; files dated Aug–Oct 2026),
imported 2026-11-16.

| File | Status | Used in | Notes |
|---|---|---|---|
| [`D1-02_listener_prompt.txt`](D1-02_listener_prompt.txt) | In repo, **rebuilt** | Part 3 → Part 4 | The original file wasn't in the zip. Rebuilt 2026-11-16 from D2-03 Worker 1, word for word, and checked against slides 82 and 86. The stray opening `“` is dropped and the `TRANSCRIPT: [paste it here]` line is added back (slide 86 and D2-03 say to delete it when building the skill). If the original Day 1 file turns up, compare it with this one and replace this one |
| [`D2-01_thursday_transcript.txt`](D2-01_thursday_transcript.txt) | In repo | Parts 3, 4 | Himalaya Trade Concern Thursday call. Carries everything the arc needs (see below) |
| [`D2-02_team_and_contacts.txt`](D2-02_team_and_contacts.txt) | In repo | Part 4 | The file attached to the Writer and Checker skills: colleagues, five outside parties with language, the "never leaves the building" list |
| [`D2-03_prompt-library_agentic-ai_v6.txt`](D2-03_prompt-library_agentic-ai_v6.txt) | In repo, **v6 2026-11-16** | Part 4 | Prompt library v6: v5 plus the fix-and-recheck loop (Writer revise rules, Checker round rule, the stopping rule). v5 was the first Gemini skills version. Each worker gets a name, a description, instructions and files. Also covers how to call a worker (`/name`, one new chat each), the expected output, the two rules, and the take-home, including how to download and share a skill. Instructions are v4's, word for word, except that the Writer and the Checker now point at "the file attached to this skill" (one reworded line in the Writer, one added line in the Checker). v4 (Gems, `.docx` + twin) is in git history before this change |
| [`skills/`](skills/) | In repo, **new 2026-11-16** | Part 4 fallback | `listener/`, `writer/`, `checker/`, each with a `SKILL.md` that matches D2-03 v6. Upload one with Skills → Create → Upload, and add D2-02 as a file for the Writer and the Checker. D2-02 isn't copied into them, so it has one source. The instructions do exist twice, here and in D2-03, so change both together |

## What the transcript has to keep

If anyone edits D2-01, these must survive, because Parts 3–5 depend on them:

| Element | Transcript | Payoff |
|---|---|---|
| Refund conflict | Ramesh "one lakh twenty", Sujata "one lakh forty" | Round 5 CONFLICT → the Writer drafts anyway → the Checker HOLDs |
| Confidential sourcing | "don't tell Shrestha yet… asked Gurung Traders for a quotation" | Round 2 picks it up; possible Checker INTERNAL ONLY catch |
| Cash position | "short on cash till the Dashain payments" | Never-leaves-the-building bait |
| No owner | Internet bill, "whoever is free" | UNASSIGNED → NEEDS AN OWNER |
| Vague date | Gurung follow-up, "soon. This week if possible" | NOT STATED |
| Parked items | Signboard tax notice, staff bonus → "Monday" | RAISED BUT NOT DECIDED |
| Inaudible | `[overlapping speech, approximately 5 seconds, unintelligible]` | INAUDIBLE |
| Local words | Asar, Kalimati, chalan, lakh, Dashain, Haan | Round 4 Style: kept exactly as spoken |

## Things noticed on import

- **"Day 1 / Day 2" naming.** The file numbering (D1-, D2-) comes from a two-day format. The final
  deck runs everything in one day. D2-03 v5's heading now says *"PART 4"* and calls the Listener's
  instructions *"your Part 3 prompt"*. The filenames keep their prefixes, because the slides cite them.
- **The deck and D2-03 disagree on the Shrestha catch.** D2-03 says it did *not* appear in testing
  ("all three other drafts came back SEND") and tells the facilitator to say so honestly. Deck
  slide 100 said *"Read every HOLD out loud… Especially the Shrestha one"*, which assumed it would
  appear, while slide 101 hedged ("If it also caught…"). **Fixed 2026-11-16:** the run slide (97) now reads *"Then look hard at the Shrestha draft. It may pass."*
- **Binod Shrestha vs Shrestha Suppliers.** A colleague and a vendor share a surname. It's harmless
  in testing so far, but it's a plausible way for the Writer to route a message wrongly. Watch it,
  or use it as a teaching moment.
- **Stray quote mark.** v4's Listener prompt opened with `“` and never closed it. Dropped in v5.
- **D2-03 has more than the deck shows.** The Writer's `RECIPIENT NOT ON LIST` rule, the
  "earlier version withheld CONFLICT and broke the Checker" design note, and the take-home
  exercise aren't on the slides. That's fine; the slides abridge it.

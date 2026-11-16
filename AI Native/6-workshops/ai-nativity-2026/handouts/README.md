# Handouts

Participant files for the AI Nativity session. Text files are committed as-is. `.docx` / `.pdf`
are gitignored and get a generated `.md` twin (`_system/tools/docx_to_md.py`). Never hand-edit a twin.

Source: `For Testing-20261116T040221Z-1-001.zip` (a Google Drive export; files dated Aug–Oct 2026),
imported 2026-11-16.

| File | Status | Used in | Notes |
|---|---|---|---|
| [`D1-02_listener_prompt.txt`](D1-02_listener_prompt.txt) | In repo, **rebuilt** | Part 3 → Part 4 | The original file wasn't in the zip. Rebuilt 2026-11-16 from D2-03 Worker 1, word for word, and checked against slides 82 and 86. The stray opening `“` is dropped and the `TRANSCRIPT: [paste it here]` line is added back (slide 87 and D2-03 say to delete it when building the Gem). If the original Day 1 file turns up, compare it with this one and replace this one |
| [`D2-01_thursday_transcript.txt`](D2-01_thursday_transcript.txt) | In repo | Parts 3, 4 | Himalaya Trade Concern Thursday call. Carries everything the arc needs (see below) |
| [`D2-02_team_and_contacts.txt`](D2-02_team_and_contacts.txt) | In repo | Part 4 | Knowledge file for the Writer and the Checker: colleagues, five outside parties with language, the "never leaves the building" list |
| `D2-03_prompt-library_agentic-ai_v4.docx` → [`.md`](D2-03_prompt-library_agentic-ai_v4.md) | In repo (twin) | Part 4 | Prompt library, FINAL v4: all three workers' instructions, expected output, tested results, the two rules, take-home |

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

- **"Day 1 / Day 2" naming.** D2-03 is headed *"DAY 2 — AGENTIC AI"* and calls the Listener prompt
  *"your complete Day 1 prompt"*. The file numbering (D1-, D2-) comes from a two-day format. The
  final deck runs everything in one day. Participants won't be confused if you say it out loud,
  but the heading could be updated.
- **The deck and D2-03 disagree on the Shrestha catch.** D2-03 says it did *not* appear in testing
  ("all three other drafts came back SEND") and tells the facilitator to say so honestly. Deck
  slide 100 says *"Read every HOLD out loud… Especially the Shrestha one"*, which assumes it will
  appear. Slide 101 hedges correctly ("If it also caught…"). Consider softening slide 100 to match.
- **Binod Shrestha vs Shrestha Suppliers.** A colleague and a vendor share a surname. It's harmless
  in testing so far, but it's a plausible way for the Writer to route a message wrongly. Watch it,
  or use it as a teaching moment.
- **Stray quote mark.** The Listener prompt in D2-03 opens with `“` and never closes it. If
  participants copy from the doc, it pastes into the Gem's instructions. Harmless but untidy.
- **D2-03 has more than the deck shows.** The Writer's `RECIPIENT NOT ON LIST` rule, the
  "earlier version withheld CONFLICT and broke the Checker" design note, and the take-home
  exercise aren't on the slides. That's fine; the slides abridge it.

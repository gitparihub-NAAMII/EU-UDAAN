# Crosswalk — AI Nativity session ↔ the course

How the workshop's parts line up with the course in `4-courses/`, where they deliberately differ,
and what each track can borrow from the other. This file is the only place the two are linked.
Nothing here declares anything in the graph.

## Part by part

| Workshop | Course problem | Closest CUs / SCUs | Match |
|---|---|---|---|
| Part 1: quiz, AI Pyramid, five habits | Domain framing (build manual §2) | No CU. The Pyramid sits at program level (`vocabulary-map.md` §4.3, "no home") | Workshop only |
| **Part 2: five moves** | `prob.ai-enabled-problem-solving` (**unbuilt**) | None. See `5-roadmap/course-4-ai-enabled-problem-solving.md` | **Workshop has it; the course doesn't** |
| Part 3: five dials | `prob.context-engineering` | CU2 (role, intent, audience), CU3 (shape decided upfront), CU4 (the answer it invented / fencing it in the truth), CU5 (reusable one-pager) | Strong, different vocabulary |
| Part 4: Listener → Writer → Checker | `prob.agentic-ai` | CU3 (it did exactly what I said), CU4 (who's watching: nod points), CU5 · SCU 5.2 (build it in Gemini, free), SCU 5.3 (what deserves an agent) | Strong; different build (three Gems vs one) |
| Part 5: five cases, two moments | `prob.responsible-ai` | CU2 (machine lied / Air Canada), CU3 (CV bias / Amazon), CU4 (whose data did you paste), CU5 (show your work, and sign it) | Strong, different device |

## Vocabulary: workshop names vs course names

The workshop never says BRIEF, AGENT or TRUST, and must keep it that way (see
`6-workshops/README.md`). Its own names overlap the course frameworks but don't map one-to-one.

**Part 3, five dials ↔ BRIEF** (revealed at CE SCU 5.2)

| Dial | BRIEF letter | Note |
|---|---|---|
| Source | B, Background (incl. grounding, CU4) | Same idea |
| Role | R, Role | Same |
| Shape | F, Format (the shape part) | Format is split in two |
| Style | No letter | Partly I (audience) and E (show your voice) |
| Limits | F, Format (the must-not part) + CU4 grounding | Format is split in two |
| No dial | I, Intent | The workshop folds intent into the instruction itself |
| No dial | E, Examples | **Not taught in the workshop** |

**Part 4, three workers ↔ AGENT** (revealed at Agentic SCU 5.0)

| Workshop device | AGENT letter |
|---|---|
| Each Gem's "IT PRODUCES" | A, Aim |
| "You paste it in", where the human is the wire | G, Go-signal (always *you*; no triggers or schedules) |
| The Gem instructions | E, Explicit steps |
| The Checker and "you press send" | N, Nod points |
| Knowledge files and "do not decide whether it's safe" | T, Tools & limits |
| "One job per worker", "short chains beat clever ones" | No letter. Workshop-only rules |

**Part 5, two moments ↔ TRUST** (revealed at RAI SCU 5.2)

| Workshop device | TRUST letter |
|---|---|
| Before you act: check the name, number, date, citation | T, Trace |
| Before you paste; the never-paste table | R, Respect |
| Case 1 (Dutch benefits), Q9 (Amazon) | U, Uncover. The workshop names it but has no swap-test exercise |
| "Do you have to say it was AI?" | S, Show |
| Who-decides-what table, "a named human must" | T, Take |

## Where the two deliberately differ

1. **Story world.** The workshop uses Himalaya Trade Concern (Sujata, Ramesh, Binod, a Kalimati
   refund, Shrestha and Gurung suppliers). The course uses Maya and
   `kb.world.himalayan-getaways`. Keep the two worlds separate. Don't move workshop characters
   into `4-courses/` unless you first add them to the course world, because CLAUDE.md requires
   every course artifact to match that world.
2. **Naming order.** The course follows "problem first, name it after": the framework is revealed
   only at the end. The workshop names the five dials on slide 52, before the five rounds, though
   only after the motorcycle warm-up has made the gap felt. That suits a one-day session; it would
   break the rule in `4-courses/`.
3. **Real cases and citations.** The course keeps Maya's story free of citations. The workshop
   leads with real, cited cases (Air Canada, Mata v. Avianca, Arup, Deloitte, Rite Aid, NYC,
   Dutch benefits). Both are fine in their own track.
4. **Voice.** These lines would break build manual §3.5 ("no claim about what AI knows") if they
   were moved into `4-courses/`. They're fine as workshop delivery:
   - slide 27: "AI only knows what you put in front of it"
   - slide 51: "The AI knows nothing about you"
   - slide 116: "what it already believed"

   Rewrite them in mechanism terms ("it only has what you put in front of it") if they move.
5. **Illustrative figure.** Slide 104's 90% → 81% → 73% is 0.9ⁿ, an illustration, not
   measured data. Never quote it as a statistic in either track.

## What each track can borrow

**Workshop → course**

- **Part 2 is a draft of Course 4.** The five moves are concrete material for the unbuilt
  `prob.ai-enabled-problem-solving`. They also mostly line up with the proposal's provisional
  SOLVE:

  | Workshop move | SOLVE letter |
  |---|---|
  | Diagnose | Split / Observe |
  | Brainstorm | Lay out options |
  | Stress-test | Verify the reasoning |
  | Commit | Explain the call |

  "Do not defend the plan" (slide 42) is a working anti-sycophancy device, which is the unit the
  proposal rates strongest. Per the proposal, letters must be earned from units, so treat this as
  evidence, not a decision.
- **Limits as visible labels** (UNASSIGNED · NOT STATED · CONFLICT · INAUDIBLE) is a sharper,
  more teachable version of CE CU4's grounding. It's a candidate example for SCU 4.2.
- **The Checker as a separate worker** is a concrete form of Agentic CU4's nod points.

**Course → workshop**

- **Examples (E in BRIEF)** is the one course concept the workshop leaves out entirely.
- **The swap test** (RAI CU3) would give Part 5 a 3-minute hands-on moment if one is ever wanted.
- **SCU 5.3 "What deserves an agent"** is a natural closing question for Part 4. The workshop
  currently ends Part 4 on payoff, not on when *not* to build.

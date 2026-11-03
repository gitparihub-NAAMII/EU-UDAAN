# [PROPOSAL] Course 4 — AI-Enabled Problem Solving

**Status:** draft. The substance is in `1-how-we-built-it/build-manual.md` §4.2 — read that first.
This file adds only what the build manual can't: how it lands in the graph, and what the
sequencing question costs.

Graph state today: `prob.ai-enabled-problem-solving` exists in `_system/graph/problems.yaml` with
`flows: []` and `status: unbuilt`, so the gap is queryable rather than only described.

---

## Why it is a real gap, not a nice-to-have

Build manual §2.4 names four AI-Native skill areas from the AI Pyramid paper. Three are shipped.
The fourth is advertised in the Concept Brief and on the Sunway outreach deck — and the Sunway
slide omits the "A UDAAN course" label under it, which makes the gap visible to prospects at the
top of the funnel.

In graph terms it is worse than a missing course. The three shipped problems chain by `prereq`:
context engineering → agentic → responsible. That chain is a claim about how capability composes.
A missing fourth area means the domain's capability statement — *"Get original work from AI,
delegate repeatable work to safe agents, and stand behind every output"* — describes three
quarters of what the theory says AI-Native capability is.

## The framing (build manual §4.2, condensed)

**The trap the previous courses set:** Maya briefs well, delegates safely, and can stand behind
the output — and has become excellent at executing tasks *someone else framed*. Her manager asks
a question that isn't a task — *"should we open a Pokhara branch?"* — and every skill she has
assumes the problem already exists.

**Candidate course question:** *"What do you do when nobody has told you what the task is?"*

**Candidate framework SOLVE** — Split, Observe, Lay out options, Verify the reasoning, Explain
the call. Provisional by construction: build manual §3.3 requires letters be earned from suffered
problems, so the word should change as units are built. Treating SOLVE as fixed before the units
exist would violate the method the program is built on.

**The strongest available unit is sycophancy.** *"The AI agreed with me"* is a failure nearly
every learner has experienced and almost none can name, and it demonstrates with a clean
one-variable experiment: present the same proposal twice, once as your own and once as a
colleague's you're skeptical of, and compare. That is the same shape as the swap test — hold
everything constant, change one attribute, repeat to rule out flukes.

Worth noting: **that makes two of the program's strongest devices instances of one primitive.**
See `_system/vocabulary-map.md` §3.3 — the swap test generalises past bias into a house
evaluation technique, and sycophancy would be its second instance. If Course 4 is built, build
the primitive once at Tier 3 and use it twice.

## Skills this would add

None of the 22 skills currently in `_system/graph/skills.yaml` covers problem framing, evidence
gathering, option generation, or reasoning verification. Course 4 would add roughly five new
skills in a new `problem-solving` cluster, entering as `provisional: true` per story §4.2 and
curated once the units exist. Do not pre-declare them from the SOLVE draft — the letters aren't
earned yet, and neither are the skills.

## The sequencing question, and what it costs

Build manual §4.2 raises it and leaves it open: should this be Course 2 rather than Course 4?

**For moving it earlier:** framing precedes both delegation and governance. You cannot sensibly
delegate a task you haven't framed, and the current chain quietly assumes the task always arrives
pre-framed — which is exactly the weakness Course 4's opening trap exposes. If that's true, the
chain has a gap in the middle, not a missing end.

**Against:** Course 3's TRUST closes on *"the loop closes"*, written as a program finale. Moving
Course 4 before it means either re-writing that ending or ending on problem-solving, which is a
weaker finish.

**What it costs in the graph, and this is the part the build manual doesn't say:** the three
shipped problems carry `prereq_problems` edges encoding the current order. Re-sequencing rewrites
those edges, and story §4.5 is explicit that typed edges are load-bearing for the composition
engine's prerequisite reasoning. Changing them after learners have completed SCUs against the old
order does not invalidate their evidence — profiles are derived from completed SCUs, not from the
chain (story §4.12) — but it does change every path composed afterwards.

So the cost is low *now*, while no cohort has run on the platform, and rises monotonically. If
the sequencing is going to be revisited, revisit it before the first cohort, not after.

**Recommendation:** settle sequencing before building any of it. It is a cheap decision today and
an expensive one later, and it is the kind of thing that gets deferred precisely because it feels
premature.

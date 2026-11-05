# Corpus gaps — the worklist

What `env/bin/python _system/tools/validate.py` currently reports, ordered by what unblocks the most.
Regenerate the numbers before trusting them; this is a snapshot, not a ledger.

**Current state:** 4 problems · 3 flows · 15 CUs · 63 SCUs · 0 errors · 268 incomplete.

---

## 0. ~~The graph registries were never committed~~ — rebuilt 2026-11-05

The five `_system/graph/` files were described but never committed, which left the validator at 77
errors. They were rebuilt from the build manual and `_system/vocabulary-map.md`; see
`_system/graph/README.md` for what each one was rebuilt from and what could not be recovered
(the original 20 skill edges and an eighth knowledge base). The validator is back to 0 errors.

## 1. The skill mapper spreadsheet is not in the repo — blocks 62 SCUs

`AI_Native_Skill_Mapper.xlsx` declares one primary skill per sub-unit. Without it, 62 of 63
SCUs declare no skills, which means **20 of 22 skills in `_system/graph/skills.yaml` are exercised by
nothing.** A skill no SCU exercises is invisible to every hiring query and contributes nothing
to a capability profile (story §4.12: the profile is derived from completed SCUs, not declared).

This is the single highest-leverage item in the repo. Everything else is polish until it lands.

**To close:** copy `AI_Native_Skill_Mapper.xlsx` and `AI_Native_Skill_Pool_and_Pyramid.xlsx`
into `_system/source/`, then reconcile — the spreadsheet's sub-unit-grain skills are finer than the 20
course-pool skills already in `_system/graph/skills.yaml`, so this is a curation pass, not a copy.
Two of the finer skills (`role-persona-specification`, `source-grounding-hallucination-control`)
are already present as provisional and show the intended shape.

Blocked on: file access. Source path recorded in `_system/source/README.md`.

## 2. Type tags are inferred, and the count doesn't reconcile — 62 SCUs

`_system/tools/seed_corpus.py` assigns each sub-unit a type tag by reading its title. The build manual
gives real tags for only a handful.

**The inference is provably wrong somewhere.** Build manual §3.1 records that `THE NAME FOR IT`
and `YOUR TURN` each appear **exactly 17 times** across the 63 decks — one per concept cycle.
The seed script's tagging produces **24**. Seven sub-units are tagged as concept cycles that
aren't, or the manual's count is stale.

This matters beyond tidiness: `liftable` is derived from the type tag, and `liftable` is what
tells a future composition engine which of these SCUs can be reused in another flow. Getting it
wrong overstates the corpus contribution by seven units.

**To close:** read the 63 decks, correct the `type_tag` values, set `type_tag_source` to the
deck filename. Then `liftable` should fall out at 17.

Blocked on: the decks. Same source path.

## 3. No durations declared — 63 SCUs

Build manual §3.5 requires a declared duration per sub-unit (observed: 6 / 20 / 30 min) and per
unit (35 min for C1 U1, ~2 hours for C1 U2). They exist in the unit description documents;
none are in the repo.

Needed for story §8.2's "time-and-frequency-fitted scheduling" in composition. Cheap to fix
once the description docs are available.

## 4. One authored artifact out of 63

Only `scu.c1.u2.1` has an in-repo artifact, and it is transcribed from the build manual's worked
example rather than from the deck. The other 62 exist as `.pptx`/`.pdf` outside the repo.

Not urgent as a *corpus* matter — story §6.1 is explicit that the artifact lives with the SCU,
and a tier-1 deck referenced by path satisfies that. It becomes urgent when raising anything to
tier 2+, since that artifact has to be authored somewhere and this repo is the somewhere.

**Two SCUs are worth raising first**, both because they run one-variable experiments the learner
currently reads instead of runs, and both because build manual §4.6 names their model-dependence
as *"the highest-risk maintenance item in the program"*:

| SCU | Experiment | Target |
|---|---|---|
| `scu.c1.u2.1` — The Role | Four roles, identical facts | Tier 3 |
| `scu.c3.u3.2` — It wasn't a one-off | The swap test, repeated | Tier 3 |

## 5. Structural gaps carried from Part IV

Recorded so they are visible from the worklist; the substance is in the build manual.

| Gap | Build manual | Graph state |
|---|---|---|
| AI-Enabled Problem Solving has no course | §4.1 gap 1, §4.2 | `prob.ai-enabled-problem-solving`, `flows: []` |
| No assessment instruments | §4.1 gap 2, §4.3 | Interview seeds recorded per problem; no rubrics |
| No facilitator layer | §4.1 gap 3, §4.5 | Not modelled — no substrate type for it |
| Localisation asserted, not specified | §4.1 gap 4, §4.4 | Not modelled; would be a knowledge base |
| Delivery platform unnamed | §4.1 gap 5 | Not modelled |
| No Foundation/Deep curriculum | §4.1 gap 6 | Out of scope for this repo |
| No cohort feedback loop | §4.1 gap 7, §4.6 | Not modelled |

Gap 2 is the one that matters most for Tangible specifically: the whole validation pipeline
(story §5) runs on submitted artifacts, and the three course tangibles are already the right
artifacts. What's missing is the rubric that turns a submitted BRIEF into a proposed level.

## 6. Open questions filed upstream

Three, in `_system/vocabulary-map.md` §5. Not gaps in this repo — gaps in the canon this repo
surfaced. They need an answer from Alok or Bishesh, not work here.

1. The competency scale has no level for habit
2. Domains conflate sector-of-scenario with domain-of-capability
3. Is a pedagogically sequence-dependent SCU a first-class citizen?

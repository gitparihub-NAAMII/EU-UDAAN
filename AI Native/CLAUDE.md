# CLAUDE.md

Working instructions for agents in this repo. Read `README.md` for what the repo is.

## Before you write anything

Read in this order. Skipping straight to the third is the most common way to get work here wrong.

1. `context/tangible-story.md` **§4** (the substrate) and **§13** (the decision rules) — the
   vocabulary and the constraints everything downstream instantiates
2. `context/vocabulary-map.md` — how this program maps onto that, and the three places it doesn't
3. `WORKFLOW.md` — the pipeline you are executing

If you are authoring content, also read `context/udaan-build-manual.md` Part III, and the
reference SCU at `content/context-engineering/cu-2-when-the-facts-arent-enough/scu-2.1-the-role/`.

## Hard constraints

**Never edit `context/tangible-story.md`.** Vendored from `tangiblecareers/tangible-source`,
overwritten on every upstream publish. Disagreements go to `context/vocabulary-map.md` §5 as open
questions, then to Alok or Bishesh.

**Competency levels are `awareness | application | mastery | influence`.** Story §4.11. The
four-point scale in build manual Part IV §4.3 (Unaware/Prompted/Habitual/Transferring) is
**retired** — do not reintroduce it, including in prose. The crosswalk is `vocabulary-map.md` §2.

**IDs are permanent.** SCU ids key artifacts, attribution, and evidence. Add and deprecate;
never rename.

**Every SCU anchors.** Story §8.3 — no unanchored content. An SCU declares its CU, its type tag,
its `liftable` status, and (once the skill mapper lands) its skills at levels.

**Run the validator before claiming done:** `env/bin/python tools/validate.py`. Zero errors.

## Things that look like mistakes and are not

- **268 `INCOMPLETE` results.** Deliberate and accurate — see `proposals/corpus-gaps.md`. Do not
  "fix" them by inventing skill assignments. Story §13: *"provenance over assertion."* If the
  skill mapper spreadsheet isn't in `source/`, the skills aren't known.
- **`type_tag_source: inferred` on 62 SCUs.** The tags were derived from sub-unit titles, not read
  from the decks, and the inference is provably wrong somewhere: build manual §3.1 records 17
  concept cycles, the scaffold produces 24. Don't silently reconcile — read the decks.
- **`provisional: true`** on two skills and one domain. Story §4.2 gives creators this so they can
  propose without blocking on curation. Clearing one is a curation decision, not an edit.
- **`liftable: false` on 46 SCUs.** Honest, not a defect. UDAAN pedagogy is deliberately
  sequence-dependent (build manual §3.0 commitments 2 and 3). `vocabulary-map.md` §4.1.
- **`graph/` has no `tools.yaml`.** This contribution is pedagogy-mode only. ChatGPT and Gemini
  appear as subjects of study, not as wired MCP integrations, so they are not typed tool assets.

## Writing content

Voice rules are in build manual §3.5 and they are strict. The ones most often broken:

- Second person for the learner, third person for Maya. Never "one" or "the user"
- No jargon before its naming slide. A term arrives only after the learner has felt the gap it names
- **No claim about what AI "understands" or "knows."** Describe mechanism — *predicts, borrows,
  points at a shelf of examples*
- Never the word "simply"
- Never blame the learner. Maya is competent throughout; the failures are structural
- Maya's story carries no citations. Keep the evidence layer and the narrative layer separate

Consistency: every artifact must agree with `kb.world.himalayan-getaways` (`graph/knowledge.yaml`).
Characters and world objects may be reused across problems but must not be re-characterised.

Framework acronyms (BRIEF, AGENT, TRUST) must **never be named before their reveal sub-unit** —
5.2, 5.0, 5.2 respectively. Each knowledge base carries the rule as `disclosure_rule`.

## Repo conventions

- YAML for graph objects, Markdown for artifacts, Python 3 for tools
- The venv is `env/` and is gitignored. Use `env/bin/python`, not bare `python3` — PyYAML is
  installed in the venv only
- Source binaries are gitignored. `source/` holds the manifest and the pointer, not the files
- `tools/seed_corpus.py` is a one-time seed kept for auditability. It skips existing files unless
  `--force`; `--force` destroys hand edits

## When something is genuinely ambiguous

The canon is the tiebreaker, in this order: `tangible-story.md` → `vocabulary-map.md` →
`udaan-build-manual.md` Parts I–III → Part IV (proposal only, never binding).

If the build manual and the canon conflict on what capability means, that is a real conflict worth
escalating rather than resolving downstream — build manual Part II derives from a paper by
Tangible's own CEO and CSO. One such conflict is live (`vocabulary-map.md` §5 Q1).

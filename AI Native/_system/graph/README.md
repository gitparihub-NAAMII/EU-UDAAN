# graph/

The machine-readable registries the courses point into. `_system/tools/validate.py` checks every
reference in `4-courses/` against these files.

| File | Holds | Count |
|---|---|:-:|
| `domains.yaml` | The capability domain the problems anchor in, and the scenario setting kept apart from it | 1 + 1 |
| `skills.yaml` | Skill clusters, the named skills, and typed edges between skills | 4 · 22 · 10 |
| `knowledge.yaml` | Knowledge bases: the world bible, the three frameworks, the case, evidence, theory | 7 |
| `problems.yaml` | One problem per course, plus the unbuilt Course 4 | 4 |
| `escalations.yaml` | The bright line: a named human decides about people | 1 |

## Provenance

These files were **rebuilt on 2026-11-05**. Earlier docs described them, but they had never been
committed, so the validator was failing on every reference to them. Everything here traces to a
source in this repo, and each file says which.

| File | Rebuilt from |
|---|---|
| `domains.yaml` | `_system/vocabulary-map.md` §4.2–4.3 |
| `skills.yaml` | Course skill pools in build manual §1.3–1.5; the two sub-unit skills in §1.6 |
| `knowledge.yaml` | Build manual §1.2–1.5, §2.7, Part II; `sources-and-context.md`; `CLAUDE.md` disclosure rule |
| `problems.yaml` | `_system/vocabulary-map.md` §1, §3.2, §4.4; the three `flow.yaml` files |
| `escalations.yaml` | `_system/vocabulary-map.md` §3.1; build manual §1.5 |

**Not recovered:**

- **Skill edges.** The original was described as having 20 typed edges. Only the 10 that a source
  states or directly implies are here, and each one cites its basis. The rest should come from the
  skill mapper, not from guessing.
- **An eighth knowledge base.** The original count was 8; only 7 are named anywhere in the repo.
- **Difficulty ratings.** No source rates the problems, so `difficulty` is `null` for curation.
- **The adoption-figures version stamp.** `kb.evidence.adoption-figures` has `version: null`
  until the next quarterly review stamps it.

## Rules for editing

- IDs are permanent. Add and deprecate; never rename.
- A new skill enters with `provisional: true` and a `provisional_reason`.
- Levels are `awareness | application | mastery | influence`, declared on SCUs, never here.
- Run `env/bin/python _system/tools/validate.py` from `AI Native/` after any change. Zero errors.

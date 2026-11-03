# context/

The "why" layer. Read before authoring; don't author here.

| File | Origin | Editable |
|---|---|---|
| `tangible-story.md` | **Vendored** from `tangiblecareers/tangible-source` | **No** |
| `udaan-build-manual.md` | This program's own artifact | Yes |
| `udaan-context-and-sources.md` | This program's own artifact | Yes |
| `vocabulary-map.md` | Written here — reconciles the two | Yes |

## Reading order

1. **`tangible-story.md` §1–4** — the thesis and the substrate. Everything downstream is an
   instance of this. §4 is the data model; §13 is the decision rules.
2. **`vocabulary-map.md`** — how this program's vocabulary lands in that substrate, and the
   three places it doesn't. Shortest path to being useful here.
3. **`udaan-build-manual.md` Part III** — the design playbook. Read before making anything.
   Parts I–III record existing practice; Part IV is proposal only.
4. **`udaan-context-and-sources.md`** — only when explaining the program outward.

## On the vendored copy

`tangible-story.md` carries a DO-NOT-EDIT header from upstream. It is the published copy of a
document the founders maintain privately, and it is overwritten in full on every upstream publish.
Local edits are lost and put this repo out of sync with the canon.

**Disagreements go upstream**, to Alok or Bishesh, and come back through a re-vendor. Where this
repo has found genuine gaps in the canon, they are written up as
[open questions](vocabulary-map.md#5-open-questions-for-upstream) rather than patched locally.

**Re-vendor procedure.** Replace the body of `tangible-story.md` below the HTML comment header,
keep the header intact, and note the version in the commit message. Then re-read
`vocabulary-map.md` §2 and §4 — those sections are the ones a canon change is most likely to
invalidate.

## On Part II of the build manual

`udaan-build-manual.md` Part II (the AI Pyramid, literacy-to-nativity, the PBL evidence base)
derives from Khatri & Khanal (2026), arXiv:2601.06500 — authored by Tangible's CEO and CSO.
It is effectively shared theory between this repo and the canon, not repo-local material.
When it and `tangible-story.md` disagree, that is a real conflict worth escalating, not a
downstream mapping problem. One such conflict is live: see `vocabulary-map.md` §5 Q1.

## Confidentiality

`tangible-story.md` contains traction figures, capital architecture, named clients, and investor
framing. **This repo has no remote and should not get a public one.** Before adding any remote,
confirm it is private.

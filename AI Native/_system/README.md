# _system/

Maintainer material. Readers can skip this folder; the numbered folders cover the programme itself.

The programme is also expressed as a contribution to Tangible's typed capability graph
(`tangiblecareers/tangible-source`). This folder holds the machinery for that.

| Path | What it is | Editable |
|---|---|---|
| `vocabulary-map.md` | How UDAAN's vocabulary maps onto the graph, where it doesn't fit, and open questions for upstream | Yes |
| `graph/` | Machine-readable registries: domains, skills and typed edges, knowledge bases, problems, escalations | Yes |
| `tools/validate.py` | The structural gate. Run before claiming any change is done | Yes |
| `tools/seed_corpus.py` | One-time seed of the 63 sub-units, kept for auditability. `--force` destroys hand edits | Rarely |
| `source/` | Pointer and manifest for the original decks and spreadsheets. The binaries are not committed | Yes |
| `claude-project-memory.md` | Programme-level notes carried over from earlier Claude sessions | Yes |
| `tangible-story.md` | **Local only, never committed.** The vendored canon | **No** |

## Run the validator

From the `AI Native/` folder:

```sh
env/bin/pip install pyyaml      # once
env/bin/python _system/tools/validate.py
```

`INCOMPLETE` results are the honest record of missing work (see
[`5-roadmap/corpus-gaps.md`](../5-roadmap/corpus-gaps.md)), not failures to suppress.

## The canon is confidential

`tangible-story.md` carries traction figures, capital architecture, named clients and investor
framing. It is gitignored at this path and must never be pushed: this repository is public. Keep
your local copy here so the references in `CLAUDE.md` and `vocabulary-map.md` resolve.

It is vendored from upstream and overwritten on every publish, so **don't edit it**. Disagreements
go to `vocabulary-map.md` §5 as open questions, then to Alok or Bishesh. To re-vendor, replace the
body below its HTML comment header, note the version in the commit message, then re-read
`vocabulary-map.md` §2 and §4.

## Build manual Part II is shared theory

[Build manual](../1-how-we-built-it/build-manual.md) Part II (the AI Pyramid, literacy to nativity,
the problem-based-learning evidence) derives from Khatri & Khanal (2026), arXiv:2601.06500, written
by Tangible's CEO and CSO. When it and the canon disagree, that's a real conflict to escalate, not a
local mapping problem. One is live: `vocabulary-map.md` §5 Q1.

## The graph registries

`graph/` holds five registries: domains, skills (with typed edges), knowledge bases, problems and
escalations. They were rebuilt on 2026-11-05 after it turned out the originals had never been
committed. [`graph/README.md`](graph/README.md) records the source for each and what couldn't be
recovered.

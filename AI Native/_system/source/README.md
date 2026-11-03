# _system/source/

Original authoring artifacts. **Binaries are gitignored** — this directory holds the manifest and
the pointer, not the files.

Why: 63 `.pptx` + 63 `.pdf` decks plus consolidated per-unit decks is hundreds of megabytes of
binary that git cannot diff and that nothing in the pipeline reads programmatically. The
authoritative record of what exists is `../context/udaan-context-and-sources.md` Part II.

## Where the material currently is

```
/Users/drabidsubedi/Downloads/Course3_Reworked_FULL- Latest/
```

Not yet copied in. Two files from it are already vendored into `_system/`
(`udaan-build-manual.md`, `udaan-context-and-sources.md`); the rest is not.

## What is needed, in priority order

Per `../proposals/corpus-gaps.md`:

| # | File | Unblocks |
|---|---|---|
| 1 | `AI_Native_Skill_Mapper.xlsx` | Skill declarations on 62 SCUs — **the top blocker** |
| 2 | `AI_Native_Skill_Pool_and_Pyramid.xlsx` | Level-3 skill records, coverage densities |
| 3 | `Course{N}_FINAL_SubUnit_Slides/` | Correct type tags; the 24-vs-17 concept-cycle mismatch |
| 4 | `Course{N}_Unit{U}_Descriptions.docx` | Durations, learner-facing titles |
| 5 | `Course1_Unit{U}_Tangible_Reworked.pdf` | The only place the design method is stated in the program's own words |

Item 5 is worth flagging: `1-how-we-built-it/sources-and-context.md` Part II describes it as *"the
only place the design method is stated in the program's own words — the source of the 8-step flow
and the concept-cycle counts."* Build manual Part III is a reconstruction from it. If the two
disagree, that file wins.

## Copying material in

```sh
mkdir -p _system/source/course-1 _system/source/course-2 _system/source/course-3
cp -R "/Users/drabidsubedi/Downloads/Course3_Reworked_FULL- Latest/…" _system/source/…
```

Then record what landed in `MANIFEST.yaml` (create it — it is the one file besides this README
that is not gitignored) with, per file: path, what it carries, and which graph objects depend on
it. Binaries stay out of git; the manifest is how the repo knows what it is missing.

## Naming caveat, carried from upstream

`1-how-we-built-it/sources-and-context.md` Part II records that sub-unit deck titles differ between
the per-unit folder and the consolidated folder — e.g. `U3.1_Show-Dont-Describe` vs
`U3.1_The-Word-That-Never-Works-Example`. **The descriptions document is authoritative for
learner-facing titles.** The SCU titles in `4-courses/` follow the build manual's unit tables,
which follow the descriptions. Do not "correct" them against a deck filename.

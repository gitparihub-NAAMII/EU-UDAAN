# ai-training

The **UDAAN AI-Native program**, expressed as a capability-graph contribution.

Three shipped courses — Context Engineering, Agentic AI, Responsible AI — built by NAAMII's
Education & Outreach Division for the EU UDAAN programme, restructured here in the vocabulary of
[Tangible's](https://github.com/tangiblecareers/tangible-source) typed capability graph.

> ⚠️ **Private.** `context/tangible-story.md` carries traction figures, capital architecture,
> named clients, and investor framing. This repo has no remote. If you add one, make it private.

## What this repo is

A **downstream consumer** of `tangiblecareers/tangible-source`. It follows the canon's
conventions and vocabulary; it does not define them.

In Tangible's terms (story §6.1) this repo is one **teacher-persona** contribution — pedagogical
content, authored against problems, producing SCUs that thicken the shared substrate. It is not
the platform, not the graph itself, and not an operational deployment.

What it produces:

```
1 domain · 4 problems (3 shipped, 1 unbuilt) · 3 flows
15 CUs · 63 SCUs · 22 skills · 20 typed edges · 8 knowledge bases · 1 escalation point
```

## Layout

```
context/     The "why". Read before authoring; don't author here.
             ├─ tangible-story.md          VENDORED, read-only — the canon
             ├─ vocabulary-map.md          UDAAN ↔ Tangible, and where it doesn't fit
             ├─ udaan-build-manual.md      what was built, the theory, the playbook, the gaps
             └─ udaan-context-and-sources.md   institution, sources, bibliography

graph/       The machine-readable contribution. Cross-cutting registries only.
             domains · skills + typed edges · knowledge · problems · escalations

content/     The authored material, ordered. Flows, CUs, SCUs — the artifact lives with the SCU.
             <problem>/flow.yaml → cu-N-*/cu.yaml → scu-N.N-*/{scu.yaml, artifact.md}

proposals/   Drafts. Nothing here is established practice.
source/      Pointer + manifest for original binaries. Binaries are gitignored.
tools/       validate.py (the gate) · seed_corpus.py (one-time seed, kept for auditability)
```

## Start here

| You are | Read |
|---|---|
| New to the project | `context/README.md`, then `context/vocabulary-map.md` |
| About to author something | `WORKFLOW.md` |
| Looking for what's missing | `proposals/corpus-gaps.md` |
| An agent working in this repo | `CLAUDE.md` |

## Check it

```sh
env/bin/pip install pyyaml      # once
env/bin/python tools/validate.py
```

Zero errors expected. `INCOMPLETE` counts are the honest record of missing work — see
`proposals/corpus-gaps.md`. Suppressing them would be worse than showing them.

## Known state

**0 errors · 268 incomplete.** The corpus is structurally sound and substantively thin. The
single blocker is `AI_Native_Skill_Mapper.xlsx`: without it, 62 of 63 SCUs declare no skills,
and a skill no SCU exercises is invisible to every query the graph exists to answer.

Two things this restructuring surfaced that were not previously written down:

- **17 of the 63 sub-units carry the pedagogical invention** — the concept cycles. The other 46
  are connective tissue that a composition engine would later regenerate. That is a precise
  statement of what this contribution durably adds. (`context/vocabulary-map.md` §1.1 — note the
  current scaffold infers 24 and the discrepancy is unresolved.)
- **The program's hardest rule is an escalation point, and the banking engagement needs it.**
  *"For a decision about a person, AI recommends and a named human decides"* is a policy-rule
  trigger with a named-human target — exactly the primitive a loan-processing flow requires.
  (`graph/escalations.yaml`)

Three gaps in the canon itself are filed as open questions in `context/vocabulary-map.md` §5.
They need an answer upstream, not work here.

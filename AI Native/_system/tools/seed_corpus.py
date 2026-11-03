#!/usr/bin/env python3
"""Seed 4-courses/ with the 63 shipped sub-units as CUs and SCUs.

One-time seed, kept in-repo so the derivation is reproducible and auditable rather than
a pile of hand-written YAML nobody can trace. Re-running is safe: existing scu.yaml and
cu.yaml files are left alone unless --force is passed.

SOURCE OF TRUTH: 1-how-we-built-it/build-manual.md §1.3, §1.4, §1.5 — the unit tables listing
every unit title, sub-unit title, and the concept(s) each unit carries.

INFERENCE WARNING: the build manual states sub-unit *type tags* (EXPERIENCE THE PROBLEM /
DISCOVER IT YOURSELF / PUT IT TOGETHER / ...) only for a handful of sub-units. The tags
assigned below are inferred from sub-unit titles and the unit arc described in §3.1. Every
generated scu.yaml carries `type_tag_source: inferred` for this reason.

That inference does not currently reconcile with the manual: §3.1 records that `THE NAME
FOR IT` and `YOUR TURN` each appear exactly 17 times across the 63 decks — one per concept
cycle — and this script's tagging produces a different count (printed at the end). The
decks are authoritative. Reading them and correcting the tags is tracked in
5-roadmap/corpus-gaps.md.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent   # AI Native/
CONTENT = REPO / "4-courses"

# ── Type tags, per build manual §3.1 ─────────────────────────────────────────
EXPERIENCE = "experience-the-problem"
DISCOVER = "discover-it-yourself"
PUT_TOGETHER = "put-it-together"
TRY_YOURSELF = "try-it-yourself"       # course-opening variant
NAME_GENERALISE = "name-it-generalise"  # course-opening variant
PAYOFF = "the-payoff"                   # course-closing
WHOLE_JOURNEY = "the-whole-journey"     # course-closing

# Only DISCOVER and NAME_GENERALISE carry a concept cycle and are candidates for lifting
# into another flow. See _system/vocabulary-map.md §1.1.
LIFTABLE = {DISCOVER, NAME_GENERALISE}

# ── The shipped corpus ───────────────────────────────────────────────────────
# (problem_id, flow_id, course_key, [ (unit_no, unit_title, concept, [(sub_no, title, tag)]) ])

PROGRAM = [
    (
        "prob.context-engineering",
        "flow.context-engineering.udaan-v1",
        "c1",
        "1-context-engineering-brief",
        [
            (1, "Why the same AI treats you differently", "Context exists (B)", [
                ("1.1", "Meet Maya", EXPERIENCE),
                ("1.2", "Maya's first try", EXPERIENCE),
                ("1.3", "So Maya asked Ravi", TRY_YOURSELF),
                ("1.4", "So that's the difference", NAME_GENERALISE),
            ]),
            (2, "When the facts aren't enough", "Role, Intent", [
                ("2.0", "The message that broke the customer", EXPERIENCE),
                ("2.1", "The Role", DISCOVER),
                ("2.2", "The Intent", DISCOVER),
                ("2.3", "The Audience", DISCOVER),
                ("2.4", "Maya rewrites the message", PUT_TOGETHER),
            ]),
            (3, 'The endless "make it better"', "Examples, Format", [
                ("3.0", "The correction spiral", EXPERIENCE),
                ("3.1", "The word that never works", DISCOVER),
                ("3.2", "The shape, decided upfront", DISCOVER),
                ("3.3", "Maya ends the spiral", PUT_TOGETHER),
            ]),
            (4, "The answer it invented", "Grounding (B deepened)", [
                ("4.0", "The answer it invented", EXPERIENCE),
                ("4.1", "Why confident isn't correct", DISCOVER),
                ("4.2", "Fencing the AI inside the truth", DISCOVER),
                ("4.3", "Maya answers Sunita, safely", PUT_TOGETHER),
            ]),
            (5, "The Monday it forgot everything", "Statelessness -> the reusable BRIEF", [
                ("5.0", "Friday's genius, Monday's stranger", EXPERIENCE),
                ("5.1", "Why it forgets", DISCOVER),
                ("5.2", "Everything on one page", PAYOFF),
                ("5.3", "Look what you can do now", WHOLE_JOURNEY),
            ]),
        ],
    ),
    (
        "prob.agentic-ai",
        "flow.agentic-ai.udaan-v1",
        "c2",
        "2-agentic-ai-agent",
        [
            (1, "You fixed the writing. So why are you MORE tired?", "Aim (A)", [
                ("1.1", "A normal Monday", EXPERIENCE),
                ("1.2", "Count the cost", TRY_YOURSELF),
                ("1.3", "You've become the middleware", NAME_GENERALISE),
            ]),
            (2, "Why won't it just DO it for me?", "Go-signal (G)", [
                ("2.0", '"Just do it every Monday"', EXPERIENCE),
                ("2.1", "It still won't budge", EXPERIENCE),
                ("2.2", "What it takes to actually do a job", DISCOVER),
            ]),
            (3, "It did exactly what I said, and it was a disaster", "Explicit steps (E)", [
                ("3.0", "It did exactly what I said", EXPERIENCE),
                ("3.1", "Read it like a machine would", DISCOVER),
                ("3.2", "The gaps you didn't know you left", DISCOVER),
            ]),
            (4, "Who's watching while you sleep?", "Nod points, Tools & limits (N, T)", [
                ("4.0", "The three-week silent failure", EXPERIENCE),
                ("4.1", "Would you have caught it?", DISCOVER),
                ("4.2", "The failure you can't hear", DISCOVER),
            ]),
            (5, "The report that writes itself", "Assembly + judgment", [
                ("5.0", "Five parts, one word", PAYOFF),
                ("5.1", "Maya's report on one page", PAYOFF),
                ("5.2", "Build it in Gemini, free", PUT_TOGETHER),
                ("5.3", "What deserves an agent", DISCOVER),
            ]),
        ],
    ),
    (
        "prob.responsible-ai",
        "flow.responsible-ai.udaan-v1",
        "c3",
        "3-responsible-ai-trust",
        [
            (1, "Everything runs perfectly, so what could go wrong?", "Frames all five", [
                ("1.1", "The quiet empire", EXPERIENCE),
                ("1.2", "The shortlist she can't vouch for", EXPERIENCE),
                ("1.3", "What might already be wrong", TRY_YOURSELF),
                ("1.4", "The check nobody ran", TRY_YOURSELF),
                ("1.5", "The line that changes everything", NAME_GENERALISE),
            ]),
            (2, "The machine lied to a customer, who pays?", "Trace (T)", [
                ("2.0", "The machine that lied", EXPERIENCE),
                ("2.1", "The policy that never existed", EXPERIENCE),
                ("2.2", "Spot the invention", DISCOVER),
                ("2.3", "Why the machine makes things up", DISCOVER),
                ("2.4", "Checking what you can't read", PUT_TOGETHER),
            ]),
            (3, "Two identical CVs, two different scores. Why?", "Uncover (U)", [
                ("3.0", "Two CVs, one difference", EXPERIENCE),
                ("3.1", "Same CV, two verdicts", EXPERIENCE),
                ("3.2", "It wasn't a one-off", DISCOVER),
                ("3.3", "Where the bias actually comes from", DISCOVER),
                ("3.4", "The line that keeps it fair", PUT_TOGETHER),
            ]),
            (4, "Whose data did you just paste?", "Respect (R)", [
                ("4.0", "The paste you can't take back", EXPERIENCE),
                ("4.1", "What have you pasted this month?", EXPERIENCE),
                ("4.2", "Follow the records out the door", DISCOVER),
                ("4.3", "What you're really handing over", DISCOVER),
                ("4.4", "Classify first, paste second", PUT_TOGETHER),
            ]),
            (5, "Show your work, and sign it", "Show, Take (S, T)", [
                ("5.0", "The three she nearly sent unsigned", EXPERIENCE),
                ("5.1", "Show your work, and sign it", DISCOVER),
                ("5.2", "Everything spells TRUST", PAYOFF),
                ("5.3", "Your one-page AI policy", PAYOFF),
                ("5.4", "Point TRUST at what you built", PUT_TOGETHER),
                ("5.5", "The loop closes", WHOLE_JOURNEY),
            ]),
        ],
    ),
]

# Escalation points referenced by specific SCUs — _system/graph/escalations.yaml
ESCALATION_REFS = {
    "scu.c3.u1.5": ["esc.bright-line"],
    "scu.c3.u3.4": ["esc.bright-line"],
}


def slug(text: str) -> str:
    text = text.lower().replace("'", "").replace("’", "")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def yaml_str(text: str) -> str:
    """Quote a scalar safely for YAML."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write(path: Path, body: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing cu.yaml / scu.yaml (destroys hand edits)")
    args = ap.parse_args()

    written = 0
    skipped = 0
    tag_counts: dict[str, int] = {}

    for problem_id, flow_id, course_key, course_slug, units in PROGRAM:
        course_dir = CONTENT / course_slug

        # ── flow.yaml ──
        cu_ids = [f"cu.{course_key}.u{n}" for n, _, _, _ in units]
        flow_body = [
            "# Flow — Tangible story §4.8",
            '# "Flows are ordered CUs that take one approach to one problem."',
            "#",
            "# This is the shipped UDAAN sequence. A problem may carry more than one flow;",
            "# a proposed banking re-skin is in 5-roadmap/banking-reskin.md.",
            "",
            f"id: {flow_id}",
            f"problem: {problem_id}",
            "approach: >",
            "  Problem-based, narrative-driven. Five units, each opening on a failure created",
            "  by the previous unit's success. No jargon until earned; the framework is",
            "  assembled across the course and revealed in the final unit.",
            "  See 1-how-we-built-it/build-manual.md Part III.",
            "status: shipped",
            "mode: pedagogy",
            "actor: human",
            "",
            "cus:",
        ]
        flow_body += [f"  - {cid}" for cid in cu_ids]
        if write(course_dir / "flow.yaml", "\n".join(flow_body) + "\n", args.force):
            written += 1
        else:
            skipped += 1

        # ── each CU ──
        for unit_no, unit_title, concept, subs in units:
            cu_id = f"cu.{course_key}.u{unit_no}"
            cu_dir = course_dir / f"cu-{unit_no}-{slug(unit_title)}"
            scu_ids = [f"scu.{course_key}.u{s}" for s, _, _ in subs]

            cu_body = [
                "# Content Unit — Tangible story §4.8",
                '# "CUs are ordered sequences of SCUs forming one coherent unit."',
                "# In pedagogy mode a CU is a lesson. Here: one UDAAN unit.",
                "",
                f"id: {cu_id}",
                f"flow: {flow_id}",
                f"title: {yaml_str(unit_title)}",
                f"concept: {yaml_str(concept)}",
                "",
                "# The learner-facing title is the learner's complaint, in their voice.",
                "# Build manual §3.2 step 1: name the failure, not the topic.",
                "",
                "scus:",
            ]
            cu_body += [f"  - {sid}" for sid in scu_ids]
            cu_body += [
                "",
                "# Skills are declared per-SCU, not here. Empty until",
                "# AI_Native_Skill_Mapper.xlsx lands in _system/source/ — see _system/graph/README.md.",
            ]
            if write(cu_dir / "cu.yaml", "\n".join(cu_body) + "\n", args.force):
                written += 1
            else:
                skipped += 1

            # ── each SCU ──
            for sub_no, sub_title, tag in subs:
                scu_id = f"scu.{course_key}.u{sub_no}"
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
                liftable = tag in LIFTABLE
                # Everything earlier in this flow is assumed. Recorded honestly rather
                # than claiming more reusability than the pedagogy actually has.
                # See _system/vocabulary-map.md §4.1.
                idx = scu_ids.index(scu_id)
                assumes = scu_ids[:idx]

                scu_body = [
                    "# Sub-Content Unit — Tangible story §4.6",
                    '# "The atomic capability spec." Everything is keyed to this id.',
                    "",
                    f"id: {scu_id}",
                    f"cu: {cu_id}",
                    f"title: {yaml_str(sub_title)}",
                    "",
                    "# UDAAN type tag — build manual §3.1.",
                    f"type_tag: {tag}",
                    "type_tag_source: inferred   # from sub-unit title, NOT read from the deck",
                    "",
                    "# Story §4.6. Empty pending AI_Native_Skill_Mapper.xlsx — _system/graph/README.md.",
                    "skills: []",
                    "",
                    "knowledge:",
                    "  - kb.world.himalayan-getaways",
                    "",
                    "actor: human",
                    "mode: pedagogy",
                    "",
                    "# Story §6.1 compartmentalization, honestly declared.",
                    "# vocabulary-map.md §1.1: only concept-cycle SCUs are durable corpus assets;",
                    "# the rest is flow-local connective tissue.",
                    f"liftable: {str(liftable).lower()}",
                ]
                if assumes:
                    scu_body.append("assumes:")
                    scu_body += [f"  - {a}" for a in assumes]
                else:
                    scu_body.append("assumes: []")

                scu_body += [
                    "",
                    "# Story §6.1 artifact tier model.",
                    "artifact:",
                    "  tier: 1            # shipped as .pptx + .pdf slide decks",
                    "  target_tier: 1     # raise where the SCU runs a live experiment",
                    "  path: null         # set when authored in-repo",
                    "",
                    "duration_min: null   # declared per sub-unit in the source decks",
                ]
                if scu_id in ESCALATION_REFS:
                    scu_body += ["", "escalations:"]
                    scu_body += [f"  - {e}" for e in ESCALATION_REFS[scu_id]]

                scu_dir = cu_dir / f"scu-{sub_no}-{slug(sub_title)}"
                if write(scu_dir / "scu.yaml", "\n".join(scu_body) + "\n", args.force):
                    written += 1
                else:
                    skipped += 1

    total_scus = sum(tag_counts.values())
    cycles = tag_counts.get(DISCOVER, 0) + tag_counts.get(NAME_GENERALISE, 0)

    print(f"wrote {written} file(s), skipped {skipped} existing")
    print(f"\n{total_scus} SCUs by inferred type tag:")
    for tag, n in sorted(tag_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {tag:24s} {n:3d}")
    print(f"\nconcept cycles (liftable): {cycles}")
    if cycles != 17:
        print(
            f"  MISMATCH: build manual §3.1 records 17 concept cycles across the program\n"
            f"  (THE NAME FOR IT and YOUR TURN each appear 17 times in the 63 decks).\n"
            f"  This script infers {cycles}. The decks are authoritative — the tags above\n"
            f"  need correcting against them. Tracked in 5-roadmap/corpus-gaps.md."
        )


if __name__ == "__main__":
    main()

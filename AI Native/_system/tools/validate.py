#!/usr/bin/env python3
"""Validate this repo's capability-graph contribution.

Enforces the structural anchoring that Tangible story §8.3 calls "the price of admission
to the graph": no unanchored SCUs, no dangling references, no invented competency levels.

    env/bin/python _system/tools/validate.py          # errors + incompleteness
    env/bin/python _system/tools/validate.py --strict # incompleteness also fails

ERRORS are things that would corrupt the graph — a dangling skill ref, an invalid level,
an SCU no CU lists. They fail the run.

INCOMPLETE is honest missing work — 62 SCUs with no skills declared because the skill
mapper spreadsheet isn't in _system/source/ yet. Reported, not failed, because pretending the
corpus is fuller than it is would be the worse error (story §13, "provenance over
assertion").
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML required:  env/bin/pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent.parent   # AI Native/
GRAPH = REPO / "_system" / "graph"
CONTENT = REPO / "4-courses"

# Story §4.11. The only levels. The build manual Part IV §4.3 scale is retired —
# see _system/vocabulary-map.md §2.
LEVELS = {"awareness", "application", "mastery", "influence"}

# Story §4.5.
EDGE_TYPES = {"prereq", "part-of", "specializes", "uses", "alternative", "co-occurs", "extends"}

TYPE_TAGS = {
    "experience-the-problem", "discover-it-yourself", "put-it-together",
    "try-it-yourself", "name-it-generalise", "the-payoff", "the-whole-journey",
}

errors: list[str] = []
incomplete: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def inc(msg: str) -> None:
    incomplete.append(msg)


def load(path: Path) -> dict:
    if not path.exists():
        err(f"missing required file: {path.relative_to(REPO)}")
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        err(f"{path.relative_to(REPO)}: unparseable YAML — {e}")
        return {}


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="treat incompleteness as failure")
    args = ap.parse_args()

    # ── Load the registries ─────────────────────────────────────────────────
    domains_doc = load(GRAPH / "domains.yaml")
    skills_doc = load(GRAPH / "skills.yaml")
    knowledge_doc = load(GRAPH / "knowledge.yaml")
    problems_doc = load(GRAPH / "problems.yaml")
    escal_doc = load(GRAPH / "escalations.yaml")

    domain_ids = {d["id"] for d in domains_doc.get("domains", [])}
    scenario_ids = {d["id"] for d in domains_doc.get("scenario_domains", [])}
    skill_ids = {s["id"] for s in skills_doc.get("skills", [])}
    cluster_ids = {c["id"] for c in skills_doc.get("clusters", [])}
    kb_ids = {k["id"] for k in knowledge_doc.get("knowledge", [])}
    escal_ids = {e["id"] for e in escal_doc.get("escalations", [])}
    problems = problems_doc.get("problems", [])
    problem_ids = {p["id"] for p in problems}

    # ── Skills ──────────────────────────────────────────────────────────────
    for s in skills_doc.get("skills", []):
        if s.get("cluster") not in cluster_ids:
            err(f"skills.yaml: {s['id']} has unknown cluster {s.get('cluster')!r}")
        if s.get("provisional") and not s.get("provisional_reason"):
            err(f"skills.yaml: {s['id']} is provisional with no provisional_reason")

    for i, e in enumerate(skills_doc.get("edges", [])):
        where = f"skills.yaml edge[{i}]"
        if e.get("type") not in EDGE_TYPES:
            err(f"{where}: unknown edge type {e.get('type')!r}")
        for end in ("from", "to"):
            if e.get(end) not in skill_ids:
                err(f"{where}: {end} references unknown skill {e.get(end)!r}")
        if e.get("from") == e.get("to"):
            err(f"{where}: self-edge on {e.get('from')}")

    # ── Problems ────────────────────────────────────────────────────────────
    declared_flows: dict[str, str] = {}
    for p in problems:
        pid = p["id"]
        if p.get("domain") not in domain_ids:
            err(f"problems.yaml: {pid} has unknown domain {p.get('domain')!r}")
        sd = p.get("scenario_domain")
        if sd and sd not in scenario_ids:
            err(f"problems.yaml: {pid} has unknown scenario_domain {sd!r}")
        for k in p.get("knowledge") or []:
            if k not in kb_ids:
                err(f"problems.yaml: {pid} references unknown knowledge {k!r}")
        for e in p.get("escalations") or []:
            if e not in escal_ids:
                err(f"problems.yaml: {pid} references unknown escalation {e!r}")
        for pr in p.get("prereq_problems") or []:
            if pr not in problem_ids:
                err(f"problems.yaml: {pid} has unknown prereq_problem {pr!r}")
        flows = p.get("flows") or []
        if not flows and p.get("status") != "unbuilt":
            err(f"problems.yaml: {pid} is {p.get('status')} but has no flows")
        for f in flows:
            declared_flows[f] = pid

    # ── Escalations ─────────────────────────────────────────────────────────
    escal_backrefs: dict[str, list[str]] = {}
    for e in escal_doc.get("escalations", []):
        escal_backrefs[e["id"]] = e.get("referenced_by") or []

    # ── Walk the content tree ───────────────────────────────────────────────
    flow_files = sorted(CONTENT.glob("*/flow.yaml"))
    if not flow_files:
        err("4-courses/: no flow.yaml found")

    seen_flows: set[str] = set()
    all_cu_ids: set[str] = set()
    cu_listed_scus: set[str] = set()
    all_scu_ids: set[str] = set()
    scu_by_id: dict[str, dict] = {}
    liftable_count = 0

    for ff in flow_files:
        flow = load(ff)
        fid = flow.get("id")
        seen_flows.add(fid)
        if fid not in declared_flows:
            err(f"{rel(ff)}: flow {fid!r} is not listed by any problem")
        elif flow.get("problem") != declared_flows[fid]:
            err(f"{rel(ff)}: problem {flow.get('problem')!r} disagrees with "
                f"problems.yaml, which attaches this flow to {declared_flows[fid]!r}")

        listed_cus = flow.get("cus") or []
        if not listed_cus:
            err(f"{rel(ff)}: flow lists no CUs")

        found_cus: dict[str, Path] = {}
        for cf in sorted(ff.parent.glob("cu-*/cu.yaml")):
            cu = load(cf)
            cid = cu.get("id")
            if cid in all_cu_ids:
                err(f"{rel(cf)}: duplicate CU id {cid!r}")
            all_cu_ids.add(cid)
            found_cus[cid] = cf

            if cu.get("flow") != fid:
                err(f"{rel(cf)}: declares flow {cu.get('flow')!r}, found under {fid!r}")

            listed_scus = cu.get("scus") or []
            if not listed_scus:
                err(f"{rel(cf)}: CU lists no SCUs")
            cu_listed_scus.update(listed_scus)

            found_scus: dict[str, Path] = {}
            for sf in sorted(cf.parent.glob("scu-*/scu.yaml")):
                scu = load(sf)
                sid = scu.get("id")
                if sid in all_scu_ids:
                    err(f"{rel(sf)}: duplicate SCU id {sid!r}")
                all_scu_ids.add(sid)
                scu_by_id[sid] = scu
                found_scus[sid] = sf

                if scu.get("cu") != cid:
                    err(f"{rel(sf)}: declares cu {scu.get('cu')!r}, found under {cid!r}")

                tag = scu.get("type_tag")
                if tag not in TYPE_TAGS:
                    err(f"{rel(sf)}: unknown type_tag {tag!r}")
                if not scu.get("type_tag_source"):
                    err(f"{rel(sf)}: type_tag_source not declared")
                elif scu["type_tag_source"] == "inferred":
                    inc(f"{rel(sf)}: type_tag inferred from title, not read from the deck")

                # Skills — the core anchoring requirement (story §8.3).
                skills = scu.get("skills")
                if not skills:
                    inc(f"{rel(sf)}: no skills declared")
                else:
                    for entry in skills:
                        if not (isinstance(entry, list) and len(entry) == 2):
                            err(f"{rel(sf)}: skill entry {entry!r} is not [skill_id, level]")
                            continue
                        skid, level = entry
                        if skid not in skill_ids:
                            err(f"{rel(sf)}: unknown skill {skid!r}")
                        if level not in LEVELS:
                            err(f"{rel(sf)}: invalid level {level!r} "
                                f"(story §4.11: {'|'.join(sorted(LEVELS))})")

                for k in scu.get("knowledge") or []:
                    if k not in kb_ids:
                        err(f"{rel(sf)}: unknown knowledge {k!r}")
                for e in scu.get("escalations") or []:
                    if e not in escal_ids:
                        err(f"{rel(sf)}: unknown escalation {e!r}")
                    elif sid not in escal_backrefs.get(e, []):
                        err(f"{rel(sf)}: references {e!r} but escalations.yaml "
                            f"does not list it in referenced_by")

                if scu.get("liftable") is None:
                    err(f"{rel(sf)}: liftable not declared (story §6.1)")
                elif scu["liftable"]:
                    liftable_count += 1

                art = scu.get("artifact") or {}
                if art.get("tier") not in (1, 2, 3, 4, 5):
                    err(f"{rel(sf)}: artifact.tier {art.get('tier')!r} not in 1..5")
                path = art.get("path")
                if path:
                    if not (sf.parent / path).exists():
                        err(f"{rel(sf)}: artifact.path {path!r} does not exist")
                else:
                    inc(f"{rel(sf)}: no artifact authored in-repo")

                if scu.get("duration_min") is None:
                    inc(f"{rel(sf)}: duration not declared (build manual §3.5)")

            for sid in listed_scus:
                if sid not in found_scus:
                    err(f"{rel(cf)}: lists {sid!r} but no such scu.yaml under this CU")
            for sid in found_scus:
                if sid not in listed_scus:
                    err(f"{rel(found_scus[sid])}: exists but {cid} does not list it")

        for cid in listed_cus:
            if cid not in found_cus:
                err(f"{rel(ff)}: lists {cid!r} but no such cu.yaml under this flow")
        for cid in found_cus:
            if cid not in listed_cus:
                err(f"{rel(found_cus[cid])}: exists but {fid} does not list it")

    for fid, pid in declared_flows.items():
        if fid not in seen_flows:
            err(f"problems.yaml: {pid} declares flow {fid!r} with no flow.yaml in 4-courses/")

    # ── Cross-cutting: assumes must resolve ─────────────────────────────────
    for sid, scu in scu_by_id.items():
        for a in scu.get("assumes") or []:
            if a not in all_scu_ids:
                err(f"{sid}: assumes unknown SCU {a!r}")
            elif a == sid:
                err(f"{sid}: assumes itself")

    # ── Escalation back-references resolve ──────────────────────────────────
    for eid, refs in escal_backrefs.items():
        for r in refs:
            if r not in all_scu_ids:
                err(f"escalations.yaml: {eid} referenced_by unknown SCU {r!r}")
            elif eid not in (scu_by_id[r].get("escalations") or []):
                err(f"escalations.yaml: {eid} claims {r} but that SCU does not reference it")

    # ── Orphan skills: declared but never exercised ─────────────────────────
    exercised = {e[0] for s in scu_by_id.values() for e in (s.get("skills") or [])
                 if isinstance(e, list) and len(e) == 2}
    for skid in sorted(skill_ids - exercised):
        inc(f"_system/graph/skills.yaml: {skid} is declared but no SCU exercises it")

    # ── Report ──────────────────────────────────────────────────────────────
    print(f"problems {len(problems)}  flows {len(seen_flows)}  "
          f"CUs {len(all_cu_ids)}  SCUs {len(all_scu_ids)}  "
          f"(liftable {liftable_count})")
    print(f"skills {len(skill_ids)}  edges {len(skills_doc.get('edges', []))}  "
          f"knowledge {len(kb_ids)}  escalations {len(escal_ids)}")

    if errors:
        print(f"\n{len(errors)} ERROR(S):")
        for e in errors:
            print(f"  ✗ {e}")

    if incomplete:
        buckets: dict[str, int] = {}
        for m in incomplete:
            key = m.split(": ", 1)[1] if ": " in m else m
            buckets[key] = buckets.get(key, 0) + 1
        print(f"\n{len(incomplete)} INCOMPLETE (known missing work, not failures):")
        for k, n in sorted(buckets.items(), key=lambda kv: -kv[1]):
            print(f"  · {n:3d} × {k}")

    if errors:
        return 1
    if incomplete and args.strict:
        print("\n--strict: incompleteness treated as failure")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

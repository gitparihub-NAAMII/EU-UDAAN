#!/usr/bin/env python3
"""One-time scaffold for the health programme: five courses, five ways.

Writes flow.yaml, cu.yaml and scu.yaml for each course under 4-courses/. Skips files that
already exist, so hand edits survive a re-run. Kept for auditability, like seed_corpus.py.

    env/bin/python _system/tools/scaffold_health.py            # write what's missing
    env/bin/python _system/tools/scaffold_health.py --tables   # print README unit tables

The design is in 3-course-flow/health-programme.md; the ways in 1-how-we-built-it/five-ways.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
COURSES = REPO / "4-courses"
WORLD = "kb.world.bheri-corridor"

# ── The five ways (1-how-we-built-it/five-ways.md §3) ─────────────────────────
# liftable: the two durable sub-units per unit. concept: the one that names the concept and
# carries pedagogy.pattern. tier3: where a live artifact would make the way work on a page.
WAYS = {
    "udaan-8-step": dict(
        liftable={"discover-it-yourself", "name-it-generalise"},
        concept={"discover-it-yourself", "name-it-generalise"},
        tier3={"discover-it-yourself": "Step 4 is a 2–4 variant one-variable experiment that depends on model behaviour. As Tier 3 the learner runs it live and a failure to reproduce shows instead of silently making the lesson false (vocabulary-map.md §3.4)."},
    ),
    "rounds-staged-case": dict(
        liftable={"the-attending-question", "your-case"},
        concept={"the-attending-question"},
        tier3={"present-the-case": "The commit before the reveal is the way's mechanism (five-ways.md §4). On a page nothing stops the learner scrolling; as Tier 3 the record stays hidden until a commitment is written."},
    ),
    "drill-station": dict(
        liftable={"debrief", "station-with-the-check"},
        concept={"debrief"},
        tier3={"station-cold-run": "A station needs a clock and a hidden answer sheet (five-ways.md §4). Read without one it is a worked example.",
               "station-with-the-check": "Two timed reps scored against the rubric; browser-only state."},
    ),
    "audit-investigation": dict(
        liftable={"the-finding", "the-memo"},
        concept={"the-finding"},
        tier3={"dig": "The registers as a sandbox the learner can sort and trace in, so the dig is done rather than read (five-ways.md §4)."},
    ),
    "build-the-kit": dict(
        liftable={"spec", "build-and-test"},
        concept={"spec"},
        tier3={"build-and-test": "The test log on three items is the evidence move; as Tier 3 the learner runs the part on their own items and keeps the log."},
    ),
}
CLOSING = {"the-payoff", "the-whole-journey"}

TAG_LABEL = {
    "experience-the-problem": "Experience the problem", "try-it-yourself": "Try it yourself",
    "name-it-generalise": "Name it & generalise", "discover-it-yourself": "Discover it yourself",
    "put-it-together": "Put it together", "the-payoff": "The payoff", "the-whole-journey": "The whole journey",
    "present-the-case": "Present the case", "reveal-the-record": "Reveal the record",
    "the-attending-question": "The attending's question", "your-case": "Your case",
    "station-cold-run": "Station: cold run", "debrief": "Debrief",
    "station-with-the-check": "Station: with the check", "reflex-card": "Reflex card",
    "the-handover": "The handover", "dig": "Dig", "the-finding": "The finding", "the-memo": "The memo",
    "the-job": "The job", "spec": "Spec", "build-and-test": "Build and test", "ship-it": "Ship it",
}

# ── The five courses ──────────────────────────────────────────────────────────
# Each: (prefix, dir, flow id, problem id, way, rules kb, framework kb, approach, {scu: [esc]},
#        reference scu, units[(n, slug, title, concept, scus[(num, slug, title, tag)])])
COURSE_SPECS = [
    dict(
        prefix="h1", dir="health-h1-patient-instructions",
        flow="flow.health-patient-instructions.udaan-v1", problem="prob.health-patient-instructions",
        way="udaan-8-step", rules="kb.rules.practice-prescriptions", framework="kb.framework.safer",
        escalations={"4.3": ["esc.signer-checks-source"], "5.2": ["esc.fluent-reader-check"]},
        reference="2.1",
        approach=(
            "The Story way: problem-based, narrative-driven, on the shipped UDAAN shape. Five units, each\n"
            "  opening on a failure created by the previous unit's success. Pooja, a staff nurse at a\n"
            "  primary health care centre in Bardiya, learns to turn a prescription into instructions a\n"
            "  patient can act on without losing what matters. Outline:\n"
            "  5-roadmap/sector-courses/health-h1-patient-instructions.md. Way: 1-how-we-built-it/five-ways.md §3.1."),
        units=[
            (1, "it-reads-so-much-better-so-why-is-it-wrong", "It reads so much better. So why is it wrong?",
             "The source is fixed: a must-not-change list", [
                ("1.0", "the-slip-that-read-better", "The slip that read better", "experience-the-problem"),
                ("1.1", "four-runs-four-timings", "Four runs, four timings", "try-it-yourself"),
                ("1.2", "a-new-text-not-the-same-text", "A new text, not the same text", "name-it-generalise"),
                ("1.3", "poojas-must-not-change-list", "Pooja's must-not-change list", "put-it-together"),
            ]),
            (2, "every-number-matched-so-why-did-she-come-back-worse", "Every number matched. So why did she come back worse?",
             "Check both ways; a warning is an action", [
                ("2.0", "the-warning-that-went-quiet", "The warning that went quiet", "experience-the-problem"),
                ("2.1", "check-it-backwards", "Check it backwards", "discover-it-yourself"),
                ("2.2", "a-softened-warning-is-a-lost-action", "A softened warning is a lost action", "discover-it-yourself"),
                ("2.3", "the-two-way-check-on-the-whole-sheet", "The two-way check, on the whole sheet", "put-it-together"),
            ]),
            (3, "everythings-there-so-why-cant-he-follow-it", "Everything's there. So why can't he follow it?",
             "Fits the reader and the channel; read it back", [
                ("3.0", "five-lines-he-couldnt-follow", "Five lines he couldn't follow", "experience-the-problem"),
                ("3.1", "write-for-this-reader", "Write for this reader", "discover-it-yourself"),
                ("3.2", "the-channel-decides-the-shape", "The channel decides the shape", "discover-it-yourself"),
                ("3.3", "say-it-back", "Say it back", "discover-it-yourself"),
                ("3.4", "a-slip-and-a-voice-note-both-read-back", "A slip and a voice note, both read back", "put-it-together"),
            ]),
            (4, "it-sounds-so-caring-so-where-did-that-advice-come-from", "It sounds so caring. So where did that advice come from?",
             "Extras removed: fence it inside the slip", [
                ("4.0", "the-advice-nobody-prescribed", "The advice nobody prescribed", "experience-the-problem"),
                ("4.1", "why-caring-isnt-correct", "Why caring isn't correct", "discover-it-yourself"),
                ("4.2", "fence-it-inside-the-slip", "Fence it inside the slip", "discover-it-yourself"),
                ("4.3", "every-line-traced-one-question-sent", "Every line traced, one question sent", "put-it-together"),
            ]),
            (5, "it-looks-perfect-in-tharu-so-why-did-phulmati-laugh", "It looks perfect in Tharu. So why did Phulmati laugh?",
             "Read by a fluent person -> the one-page instruction sheet", [
                ("5.0", "the-word-that-meant-something-else", "The word that meant something else", "experience-the-problem"),
                ("5.1", "you-cant-check-what-you-cant-read", "You can't check what you can't read", "discover-it-yourself"),
                ("5.2", "a-fluent-person-is-the-check", "A fluent person is the check", "discover-it-yourself"),
                ("5.3", "five-checks-one-sheet", "Five checks, one sheet", "the-payoff"),
                ("5.4", "the-counter-before-and-after", "The counter, before and after", "the-whole-journey"),
            ]),
        ],
    ),
    dict(
        prefix="h2", dir="health-h2-hmis-reporting",
        flow="flow.health-hmis-reporting.audit-v1", problem="prob.health-hmis-reporting",
        way="audit-investigation", rules="kb.rules.practice-hmis-registers", framework="kb.framework.count",
        escalations={"5.2": ["esc.signer-checks-source"]},
        reference="1.2",
        approach=(
            "The Audit way: each unit is one investigation. A monthly report that reads as finished lands\n"
            "  on Sangita's desk with the registers it was made from, and the learner has to decide whether\n"
            "  to sign it. Five findings, one per unit, each a different way an AI-assembled report goes\n"
            "  wrong. Way: 1-how-we-built-it/five-ways.md §3.4."),
        units=[
            (1, "the-totals-added-up-so-why-didnt-they-match-the-register", "The totals added up. So why didn't they match the register?",
             "Counted, not predicted: every figure traces to a register line", [
                ("1.0", "the-report-that-balanced", "The report that balanced", "the-handover"),
                ("1.1", "follow-one-figure", "Follow one figure", "dig"),
                ("1.2", "the-figure-nobody-counted", "The figure nobody counted", "the-finding"),
                ("1.3", "the-first-finding-memo", "The first finding memo", "the-memo"),
            ]),
            (2, "the-numbers-were-right-so-why-was-the-story-wrong", "The numbers were right. So why was the story wrong?",
             "No cause without a source: say what the data shows", [
                ("2.0", "the-paragraph-that-explained-everything", "The paragraph that explained everything", "the-handover"),
                ("2.1", "find-the-sentences-source", "Find the sentence's source", "dig"),
                ("2.2", "the-reason-that-wasnt-in-the-data", "The reason that wasn't in the data", "the-finding"),
                ("2.3", "a-narrative-that-only-reports", "A narrative that only reports", "the-memo"),
            ]),
            (3, "everything-matched-so-why-was-it-last-months", "Everything matched. So why was it last month's?",
             "One month, one file, fresh chat: the report states its period", [
                ("3.0", "the-figures-that-looked-familiar", "The figures that looked familiar", "the-handover"),
                ("3.1", "which-month-is-this-line-from", "Which month is this line from?", "dig"),
                ("3.2", "last-month-carried-forward", "Last month, carried forward", "the-finding"),
                ("3.3", "a-report-that-states-its-month", "A report that states its month", "the-memo"),
            ]),
            (4, "the-figures-matched-the-register-so-why-was-the-indicator-wrong", "The figures matched the register. So why was the indicator wrong?",
             "Use the manual's definition: the formula and the lines it used", [
                ("4.0", "the-percentage-that-looked-right", "The percentage that looked right", "the-handover"),
                ("4.1", "rebuild-the-indicator", "Rebuild the indicator", "dig"),
                ("4.2", "the-denominator-it-borrowed", "The denominator it borrowed", "the-finding"),
                ("4.3", "every-indicator-its-definition", "Every indicator, its definition", "the-memo"),
            ]),
            (5, "the-report-was-complete-so-why-was-it-dishonest", "The report was complete. So why was it dishonest?",
             "Tell the gap: a missing figure is reported missing, and a person signs -> the audit protocol", [
                ("5.0", "the-day-that-filled-itself-in", "The day that filled itself in", "the-handover"),
                ("5.1", "find-the-page-that-isnt-there", "Find the page that isn't there", "dig"),
                ("5.2", "a-gap-is-a-gap", "A gap is a gap", "the-finding"),
                ("5.3", "the-memo-that-says-not-counted", "The memo that says \"not counted\"", "the-memo"),
                ("5.4", "five-findings-one-protocol", "Five findings, one protocol", "the-payoff"),
                ("5.5", "the-register-room-before-and-after", "The register room, before and after", "the-whole-journey"),
            ]),
        ],
    ),
    dict(
        prefix="h3", dir="health-h3-current-rule",
        flow="flow.health-current-rule.build-v1", problem="prob.health-current-rule",
        way="build-the-kit", rules="kb.rules.practice-circulars", framework="kb.framework.reply",
        escalations={"5.1": ["esc.signer-checks-source"]},
        reference="2.1",
        approach=(
            "The Build way: each unit adds one part to a kit the learner keeps. Nirmala, a public health\n"
            "  officer at the district health office, answers \"what is the current rule?\" from every\n"
            "  facility in Bardiya, and builds the circular desk part by part on her own calls: the\n"
            "  circular file, the answer template, the dated index, the ask-back, the signed answer.\n"
            "  Way: 1-how-we-built-it/five-ways.md §3.5."),
        units=[
            (1, "it-answered-straight-away-so-where-did-the-rule-come-from", "It answered straight away. So where did the rule come from?",
             "Read the circular first: no answer without the document in the chat", [
                ("1.0", "the-question-from-the-health-post", "The question from the health post", "the-job"),
                ("1.1", "the-circular-file", "The circular file", "spec"),
                ("1.2", "build-the-file-test-three-questions", "Build the file, test three questions", "build-and-test"),
                ("1.3", "version-1-dated", "Version 1, dated", "ship-it"),
            ]),
            (2, "it-had-the-circular-so-why-did-the-condition-change", "It had the circular. So why did the condition change?",
             "Exact words first: quote, then explain", [
                ("2.0", "promptly", "\"Promptly\"", "the-job"),
                ("2.1", "quote-before-you-explain", "Quote before you explain", "spec"),
                ("2.2", "build-the-template-test-three-answers", "Build the template, test three answers", "build-and-test"),
                ("2.3", "the-template-goes-in-the-kit", "The template goes in the kit", "ship-it"),
            ]),
            (3, "it-quoted-the-circular-so-why-was-it-the-old-one", "It quoted the circular. So why was it the old one?",
             "Pin the date: one current version, in a dated index", [
                ("3.0", "two-circulars-one-subject", "Two circulars, one subject", "the-job"),
                ("3.1", "the-dated-index", "The dated index", "spec"),
                ("3.2", "build-the-index-test-three-subjects", "Build the index, test three subjects", "build-and-test"),
                ("3.3", "the-index-goes-in-the-kit", "The index goes in the kit", "ship-it"),
            ]),
            (4, "the-answer-was-correct-so-why-was-it-wrong-for-them", "The answer was correct. So why was it wrong for them?",
             "Look at the asker's situation: three questions before any answer", [
                ("4.0", "the-right-answer-to-the-wrong-facility", "The right answer to the wrong facility", "the-job"),
                ("4.1", "the-ask-back", "The ask-back", "spec"),
                ("4.2", "build-the-ask-back-test-three-calls", "Build the ask-back, test three calls", "build-and-test"),
                ("4.3", "the-ask-back-goes-in-the-kit", "The ask-back goes in the kit", "ship-it"),
            ]),
            (5, "the-answer-became-the-rule-so-who-said-so", "The answer became the rule. So who said so?",
             "Your name on it: a person signs the answer, and the circular wins -> the circular desk", [
                ("5.0", "the-health-office-said", "\"The health office said\"", "the-job"),
                ("5.1", "your-name-on-it", "Your name on it", "spec"),
                ("5.2", "build-the-signed-answer-test-three-replies", "Build the signed answer, test three replies", "build-and-test"),
                ("5.3", "the-kit-version-1-0", "The kit, version 1.0", "ship-it"),
                ("5.4", "five-parts-one-desk", "Five parts, one desk", "the-payoff"),
                ("5.5", "the-phone-before-and-after", "The phone, before and after", "the-whole-journey"),
            ]),
        ],
    ),
    dict(
        prefix="h4", dir="health-h4-health-misinformation",
        flow="flow.health-misinformation.drill-v1", problem="prob.health-misinformation",
        way="drill-station", rules="kb.rules.practice-forwards", framework="kb.framework.share",
        escalations={"5.1": ["esc.signer-checks-source"]},
        reference="2.1",
        approach=(
            "The Drill way: each unit is one check, drilled at stations against the clock. Sunil, the\n"
            "  information officer at a private hospital in Nepalgunj, gets forwards all day and has\n"
            "  minutes to decide what to share and what to reply. Cold run, answer sheet, debrief, two\n"
            "  more stations, a card for the deck. Way: 1-how-we-built-it/five-ways.md §3.3."),
        units=[
            (1, "it-gave-a-verdict-so-why-was-there-nothing-behind-it", "It gave a verdict. So why was there nothing behind it?",
             "Source behind the verdict: a verdict without a source is an opinion", [
                ("1.0", "station-the-forward-about-the-kitchen-remedy", "Station: the forward about the kitchen remedy", "station-cold-run"),
                ("1.1", "a-verdict-is-not-a-source", "A verdict is not a source", "debrief"),
                ("1.2", "station-two-more-forwards", "Station: two more forwards", "station-with-the-check"),
                ("1.3", "card-where-is-that-written", "Card: \"Where is that written?\"", "reflex-card"),
            ]),
            (2, "it-gave-a-source-so-why-wasnt-it-there", "It gave a source. So why wasn't it there?",
             "Hold: open the link before you trust it", [
                ("2.0", "station-the-claim-with-three-references", "Station: the claim with three references", "station-cold-run"),
                ("2.1", "a-link-you-havent-opened", "A link you haven't opened", "debrief"),
                ("2.2", "station-two-more-reference-lists", "Station: two more reference lists", "station-with-the-check"),
                ("2.3", "card-open-it", "Card: \"Open it\"", "reflex-card"),
            ]),
            (3, "the-reply-was-correct-so-why-did-it-make-things-worse", "The reply was correct. So why did it make things worse?",
             "Answer the fear, not the claim: one action, plain words, no labels", [
                ("3.0", "station-write-the-reply", "Station: write the reply", "station-cold-run"),
                ("3.1", "the-reply-that-argued", "The reply that argued", "debrief"),
                ("3.2", "station-two-more-replies", "Station: two more replies", "station-with-the-check"),
                ("3.3", "card-who-is-scared-and-of-what", "Card: \"Who is scared, and of what?\"", "reflex-card"),
            ]),
            (4, "it-read-the-notice-so-why-did-it-verify-a-fake", "It read the notice. So why did it verify a fake?",
             "Read what it read: the screenshot, the fields, then the real notice", [
                ("4.0", "station-the-forwarded-notice", "Station: the forwarded notice", "station-cold-run"),
                ("4.1", "a-screenshot-is-not-a-notice", "A screenshot is not a notice", "debrief"),
                ("4.2", "station-two-more-screenshots", "Station: two more screenshots", "station-with-the-check"),
                ("4.3", "card-what-did-it-read", "Card: \"What did it read?\"", "reflex-card"),
            ]),
            (5, "the-rumour-was-about-us-so-who-speaks", "The rumour was about us. So who speaks?",
             "Ends with a person: the hospital speaks through a named person, with no invented figure and no patient exposed -> the card deck", [
                ("5.0", "station-the-post-about-the-hospital", "Station: the post about the hospital", "station-cold-run"),
                ("5.1", "a-person-speaks-for-the-hospital", "A person speaks for the hospital", "debrief"),
                ("5.2", "station-two-more-posts-about-us", "Station: two more posts about us", "station-with-the-check"),
                ("5.3", "card-who-signs-this", "Card: \"Who signs this?\"", "reflex-card"),
                ("5.4", "the-full-shift-five-cards", "The full shift: five cards", "the-payoff"),
                ("5.5", "the-page-before-and-after", "The page, before and after", "the-whole-journey"),
            ]),
        ],
    ),
    dict(
        prefix="h5", dir="health-h5-referral-notes",
        flow="flow.health-referral-notes.rounds-v1", problem="prob.health-referral-notes",
        way="rounds-staged-case", rules="kb.rules.practice-referral-records", framework="kb.framework.route",
        escalations={"5.2": ["esc.bright-line"]},
        reference="2.2",
        approach=(
            "The Rounds way: each unit is one case, presented in stages, and the learner commits before\n"
            "  each reveal. Ramesh, the health assistant in charge of a health post in rural Bardiya,\n"
            "  drafts referral notes with AI; Dr. Basnet, who reads them in the Nepalgunj emergency, asks\n"
            "  the one question that would have caught each failure. The note carries findings and the\n"
            "  question; the call stays with a person. Way: 1-how-we-built-it/five-ways.md §3.2."),
        units=[
            (1, "the-note-said-everything-so-why-did-nobody-read-the-line-that-mattered", "The note said everything. So why did nobody read the line that mattered?",
             "Reason first: the first line says why, and what you need", [
                ("1.0", "the-letter-that-said-everything", "The letter that said everything", "present-the-case"),
                ("1.1", "what-dr-basnet-read-first", "What Dr. Basnet read first", "reveal-the-record"),
                ("1.2", "what-do-you-need-from-me", "\"What do you need from me?\"", "the-attending-question"),
                ("1.3", "three-notes-first-line-first", "Three notes, first line first", "your-case"),
            ]),
            (2, "every-line-read-right-so-where-did-that-blood-pressure-come-from", "Every line read right. So where did that blood pressure come from?",
             "Observed only: nothing in the note that isn't in the register", [
                ("2.0", "the-note-with-the-normal-pressure", "The note with the normal pressure", "present-the-case"),
                ("2.1", "the-register-beside-the-note", "The register beside the note", "reveal-the-record"),
                ("2.2", "did-you-measure-that", "\"Did you measure that?\"", "the-attending-question"),
                ("2.3", "three-notes-nothing-added", "Three notes, nothing added", "your-case"),
            ]),
            (3, "the-note-was-urgent-so-why-did-he-wait-four-hours", "The note was urgent. So why did he wait four hours?",
             "Urgency as a time, not a courtesy", [
                ("3.0", "kindly-evaluate-at-your-earliest-convenience", "\"Kindly evaluate at your earliest convenience\"", "present-the-case"),
                ("3.1", "what-the-triage-desk-saw", "What the triage desk saw", "reveal-the-record"),
                ("3.2", "by-when", "\"By when?\"", "the-attending-question"),
                ("3.3", "three-notes-each-with-a-time", "Three notes, each with a time", "your-case"),
            ]),
            (4, "the-note-matched-the-register-so-why-was-the-time-wrong", "The note matched the register. So why was the time wrong?",
             "Transcription confirmed before the note is written", [
                ("4.0", "the-register-page-it-read", "The register page it read", "present-the-case"),
                ("4.1", "the-photo-beside-the-page", "The photo beside the page", "reveal-the-record"),
                ("4.2", "what-did-it-read", "\"What did it read?\"", "the-attending-question"),
                ("4.3", "three-pages-read-then-confirmed", "Three pages, read then confirmed", "your-case"),
            ]),
            (5, "i-asked-for-a-note-so-why-did-it-make-the-call", "I asked for a note. So why did it make the call?",
             "Explicit who decides: the note carries findings and the question, never the call -> the rounds book", [
                ("5.0", "the-impression-nobody-asked-for", "The impression nobody asked for", "present-the-case"),
                ("5.1", "what-a-line-like-that-does-at-the-desk", "What a line like that does at the desk", "reveal-the-record"),
                ("5.2", "whose-call-is-that", "\"Whose call is that?\"", "the-attending-question"),
                ("5.3", "three-notes-the-call-left-open", "Three notes, the call left open", "your-case"),
                ("5.4", "grand-round-five-questions", "Grand round: five questions", "the-payoff"),
                ("5.5", "the-health-post-before-and-after", "The health post, before and after", "the-whole-journey"),
            ]),
        ],
    ),
]


def q(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write(path: Path, text: str) -> None:
    if path.exists():
        print("skip ", path.relative_to(REPO))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("wrote", path.relative_to(REPO))


def scaffold(spec: dict) -> None:
    way = WAYS[spec["way"]]
    root = COURSES / spec["dir"]
    pre = spec["prefix"]
    flow_cus = []
    for u, uslug, utitle, concept, scus in spec["units"]:
        cid = f"cu.{pre}.u{u}"
        flow_cus.append(cid)
        cdir = root / f"cu-{u}-{uslug}"
        ids = [f"scu.{pre}.u{n}" for n, *_ in scus]
        write(cdir / "cu.yaml", f"""# Content Unit — Tangible story §4.8
# "CUs are ordered sequences of SCUs forming one coherent unit."
# In pedagogy mode a CU is a lesson. Here: one unit of a health programme course
# (3-course-flow/health-programme.md), taught the {spec['way']} way (1-how-we-built-it/five-ways.md).

id: {cid}
flow: {spec['flow']}
title: {q(utitle)}
concept: {q(concept)}

# The learner-facing title is the learner's complaint, in their voice.
# Build manual §3.2 step 1: name the failure, not the topic.

scus:
""" + "".join(f"  - {i}\n" for i in ids) + """
# Skills are declared per-SCU, not here. None assigned: no skill mapper row exists for this
# course yet (story §13, provenance over assertion).
""")
        seen: list[str] = []
        for (num, sslug, stitle, tag), sid in zip(scus, ids):
            liftable = tag in way["liftable"]
            is_concept = tag in way["concept"]
            kb = [WORLD, spec["rules"]]
            if is_concept or tag == "the-payoff":
                kb.append(spec["framework"])
            esc = spec["escalations"].get(num, [])
            a_line = ("assumes:\n" + "".join(f"  - {a}\n" for a in seen)) if seen else "assumes: []\n"
            e_line = ("escalations:\n" + "".join(f"  - {e}\n" for e in esc)) if esc else ""
            if tag in way["tier3"]:
                tier = (f"artifact:\n  tier: 1\n  target_tier: 3\n  target_tier_reason: >\n"
                        f"    {way['tier3'][tag]}\n  path: null\n")
            else:
                tier = "artifact:\n  tier: 1\n  target_tier: 1\n  path: null\n"
            ped = (f"\n# Story §8.2, \"how to learn it\". The concept-carrying sub-unit of the {spec['way']} way.\n"
                   f"pedagogy:\n  pattern: {spec['way']}\n  targets_habit: true   # vocabulary-map.md §2.3, upstream Q1\n") if is_concept else ""
            ref = ("\n# REFERENCE LESSON for this course and this way: the one sub-unit written out.\n"
                   if num == spec["reference"] else "")
            write(cdir / f"scu-{num}-{sslug}" / "scu.yaml", f"""# Sub-Content Unit — Tangible story §4.6
# "The atomic capability spec." Everything is keyed to this id.
{ref}
id: {sid}
cu: {cid}
title: {q(stitle)}

# Type tag from the {spec['way']} vocabulary, 1-how-we-built-it/five-ways.md §3.
# Set by design in the course README, not inferred from a title.
type_tag: {tag}
type_tag_source: health-programme-design

# Story §4.6. None assigned until a skill mapper row exists for this course.
skills: []

knowledge:
""" + "".join(f"  - {k}\n" for k in kb) + e_line + f"""
actor: human
mode: pedagogy

# Story §6.1 compartmentalization, declared honestly. vocabulary-map.md §1.1 and five-ways.md §5.
liftable: {str(liftable).lower()}
{a_line}
# Story §6.1 artifact tier model. Not yet authored unless artifact.path says otherwise.
{tier}
duration_min: null   # set when the lesson is written
{ped}""")
            seen.append(sid)

    write(root / "flow.yaml", f"""# Flow — Tangible story §4.8
# "Flows are ordered CUs that take one approach to one problem."
#
# Health programme, problem bank {pre.upper()}. One of five courses that each teach one health problem
# one way: 3-course-flow/health-programme.md. The way: 1-how-we-built-it/five-ways.md.

id: {spec['flow']}
problem: {spec['problem']}
pedagogy_pattern: {spec['way']}
approach: >
  {spec['approach']}
status: draft
mode: pedagogy
actor: human

cus:
""" + "".join(f"  - {c}\n" for c in flow_cus))


def tables(spec: dict) -> str:
    out = []
    for u, uslug, utitle, concept, scus in spec["units"]:
        cdir = f"cu-{u}-{uslug}"
        out.append(f"#### Unit {u} — {utitle}\n")
        out.append(f"Concept: **{concept}** · [`{cdir}/`]({cdir}/) · `cu.{spec['prefix']}.u{u}`\n")
        out.append("| # | Sub-unit | Type | Reusable | Lesson written |")
        out.append("|---|---|---|---|---|")
        way = WAYS[spec["way"]]
        for num, sslug, stitle, tag in scus:
            sdir = f"{cdir}/scu-{num}-{sslug}"
            lift = "yes" if tag in way["liftable"] else "no"
            written = f"[draft]({sdir}/artifact.md)" if num == spec["reference"] else "—"
            out.append(f"| {num} | [{stitle}]({sdir}/) | {TAG_LABEL[tag]} | {lift} | {written} |")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    if "--tables" in sys.argv:
        for spec in COURSE_SPECS:
            print(f"\n===== {spec['dir']} =====\n")
            print(tables(spec))
    else:
        for spec in COURSE_SPECS:
            scaffold(spec)

**Purpose & context**

Drabid is designing a multi-course AI literacy programme intended to build practical, evidence-backed competencies for AI-native knowledge workers. The programme is currently structured around three completed courses — **BRIEF** (Context Engineering), **AGENT** (Agentic AI), and **TRUST** (Responsible AI) — each containing five units built around a consistent experiential learning cycle. A fourth course is under active consideration.

The programme has a strong Nepal context: it references Nepal's National AI Policy 2082, local constraints around bandwidth, hardware, and free tooling, Nepali-language prompting, and a national target for AI professional training. Fictional protagonists (Maya, Suresh) set in Kathmandu are used to maintain narrative continuity across courses. The intended audience includes knowledge workers and, potentially, mixed technical cohorts requiring differentiated pathways.

Drabid appears to occupy a curriculum design and programme leadership role, with decisions about structure, pedagogy, and output format all originating from him. Materials are produced for both internal teams (research compendiums, structural diagrams) and learners (evidence submission guides, PDF packs).

---

**Current state**

- The three-course programme (BRIEF, AGENT, TRUST) is structurally complete, with 26 assessed checkpoints across the programme.
- A **practical evidence submission guide** has been developed for students — both a markdown version and a 31-page print-ready PDF — covering all 26 checkpoints with pass criteria, submission skeletons, and worked samples. A blank submission workbook (fillable PDF or Word) was proposed as a follow-up artifact.
- The **pedagogical architecture** has been visualised as SVG diagrams and a two-page shareable PDF, articulating the five-phase experiential learning cycle (Experience → Discover → Name → Apply → Generalise, with a Unit 5 Consolidate phase).
- A **CTEVT-style occupational analysis** has been completed, mapping AI-native knowledge worker duties and tasks across eleven duty areas, with Nepal-specific constraints noted.
- A **research compendium** (~17-page Word document, ~45 sources) has been produced as an evidence base for a three-hour workshop, covering AI adoption, business value, agentic AI, context engineering, and responsible AI.

---

**On the horizon**

- **Course 4** is the primary next frontier. It is scoped around six technical concepts: LangChain, Ollama, API keys, RAG, Hugging Face models, and n8n — organised into a proposed six-unit WIRED framework. Key open questions include: whether it serves as a continuation for existing learners or a standalone track for a new cohort, and how to handle mixed technical audiences (a cohort-split after Unit 2 has been proposed).
- Two **curriculum gaps** have been flagged as candidates for Course 4 coverage: ongoing agent monitoring (Duty G) and evaluation/observability design (Duty K / Tier 6 of the technical skills progression).
- A **blank student submission workbook** was offered but not yet produced.
- Formalising the experiential learning cycle for facilitators (potentially in Course 4) was flagged as a structural recommendation.

---

**Key learnings & principles**

- The programme's core pedagogical rule is **"problem first, name it after"** — learners encounter failure or friction before terminology is introduced. This applies at unit level and should be maintained in Course 4.
- Several checkpoints are **deliberately designed so the AI fails** (hallucination, bias, unsanctioned agent promises); submissions that demonstrate the learner caught the failure score higher than clean submissions. This is a principled design choice, not an oversight.
- The **experiential learning cycle** (mapped to Kolb's framework) is implicit in the writing but has not been named for facilitators — making it explicit is a recognised gap.
- The primary constraint on AI value in organisations has shifted from model capability to **organisational factors**: workflow redesign, _system/data engineering, governance maturity, and workforce literacy. This framing anchors the programme's positioning.
- For Nepal specifically: **no-code before code**, free-tool-first sequencing, and local language prompting are non-negotiable design constraints given infrastructure realities.

---

**Approach & patterns**

- Drabid works in a **build-then-validate** pattern: Claude produces full artefacts (SVGs, PDFs, Word documents, markdown guides), which are then reviewed and refined through clarification and correction.
- Outputs are consistently expected as **production-ready deliverables** (PDFs via WeasyPrint, Word via docx libraries, SVG diagrams) rather than drafts or outlines.
- Structural decisions are made at the **programme level first**, then propagated into course and unit design — maintaining consistency across the arc matters more than optimising any single unit.
- When producing research-backed content, Drabid expects **specific sourcing** (named frameworks, named studies, clickable citations) rather than general claims.
- Mnemonics and portable artifacts (BRIEF, AGENT, TRUST, WIRED) are a recurring design pattern for learner recall and course identity.

---

**Tools & resources**

- **Document generation**: WeasyPrint (PDF), Node.js `docx` library (Word), SVG/Canvas for diagrams
- **Reference frameworks**: UNESCO AI literacy framework, OECD/AILit, NIST AI RMF, Nepal National AI Policy 2082, CTEVT occupational analysis methodology, Kolb's experiential learning cycle, BCG jagged frontier study, WEF Future of Jobs 2030, Lightcast labour market data, Stanford HAI, McKinsey/Deloitte/Gartner survey series
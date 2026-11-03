# The UDAAN AI-Native Program

## Build Manual

*What has been built · why it works · how to build more · what is missing*

NAAMII Education & Outreach Division · EU UDAAN Programme

---

## How to read this document

Four parts, in the order a builder needs them.

**Part I — What has been built.** The three shipped courses, unit by unit, with their frameworks and skill mappings. Start here so the rest has something concrete to attach to.

**Part II — The theory.** Why the program is shaped this way. The AI Pyramid, the literacy-to-nativity distinction, and the evidence base for problem-based learning. Read this when you need to defend a design decision or explain the program to someone outside it.

**Part III — The playbook.** The design method reconstructed from the shipped courses: how a unit is structured, how a concept is taught, what earns a place on a slide, how the frameworks get built. **This is the part that exists nowhere else.** Read it before making anything.

**Part IV — Gaps and proposals.** What is missing, with drafts. Everything marked **[PROPOSAL]** is a draft, not established practice. Nothing in Part IV has been used in a delivered course.

**Companion document:** `UDAAN_AI_Native_Context_and_Sources.md` carries the institutional context (NAAMII, the UDAAN consortium, the problem statement), the source-material inventory, and the full bibliography. Read that one when you are explaining the program to a partner or funder rather than building in it.

A note on provenance: Parts I–III are derived from the shipped artifacts — the sub-unit slide decks, unit description documents, skill mapping spreadsheets, the Sunway outreach deck, the UDAAN Concept Brief, and Khatri & Khanal's AI Pyramid paper. Where a rule in Part III is inferred from observed practice rather than stated anywhere, it is marked *(inferred)*.

---

# PART I — WHAT HAS BEEN BUILT

## 1.1 Program shape

Three courses. Five units each. Three to five sub-units per unit. **One protagonist across all three.**

| | Course 1 | Course 2 | Course 3 |
|---|---|---|---|
| **Skill area** | Context Engineering | Agentic AI | Responsible AI |
| **Course capability** | Context Engineering & Effective Prompting | Agentic Automation Design | Responsible AI Governance |
| **Framework** | **BRIEF** | **AGENT** | **TRUST** |
| **Maya's condition entering** | Can't get good output | Gets good output, exhausted | Runs flawlessly, can't vouch for it |
| **Maya's condition leaving** | Output sounds like her | Monday runs without her | She can stand behind it |
| **Sub-units** | 21 | 16 | 26 |

These three are three of the **four AI-Native skill areas** the program is built on. The fourth — AI-Enabled Problem Solving — has no course. See Part II §2.4 for where the four come from, and Part IV §4.2 for a proposed build.

**Program-level capability (Skill Pyramid, Level 1):** *AI-Native Professional Fluency* — "Get original work from AI, delegate repeatable work to safe agents, and stand behind every [output]."

**The three-course chain is a single argument.** Each course's opening trap is created by the previous course's success:

- Course 1 teaches you to brief AI well → your output gets good → everything that needs writing lands on your desk
- Course 2 opens: *"You fixed the writing. So why are you MORE tired?"* → teaches delegation to agents → your department becomes the most reliable in the company
- Course 3 opens: *"Everything runs perfectly, so what could go wrong?"* → asks whether what the machines do in your name is *right*, or merely error-free
- Course 3 closes with *"The loop closes"* — three courses, three frameworks, one operator

## 1.2 The protagonist and world

**Maya Gurung**, trip coordinator at **Himalayan Getaways**, a mid-sized travel company in Kathmandu.

Characterised in 1.1 before AI is mentioned at all: *"She's the reliable one: the client who emails at 9 p.m. gets a reply; the booking that gets tangled — a flight moved, a group that changed its dates twice — lands on her desk, because everyone trusts her to fix it."*

Supporting cast and world objects, reused across courses:

| Element | Role |
|---|---|
| **Ravi Shrestha** | Colleague who gets better results from the same tool — the Course 1 inciting comparison |
| **Suresh** | Colleague whose well-built agent fails silently for three weeks (C2 U4) |
| **Sunita** | Customer asking a refund question — the hallucination case (C1 U4) |
| **CodeHimal** | 40-person Kathmandu software firm; the retreat booking that opens the program |
| **The Thapa family** | The proposal Maya loses on Monday when the chat forgets (C1 U5) |
| **Annapurna Base Camp / Ghorepani–Poon Hill / Ghandruk** | Treks; the landslide cancellation drives C1 U2 |
| **Tihar offer** | The Facebook post driving the correction spiral (C1 U3) |

Everything is Nepali-localised as a structural property, not decoration: Kathmandu, Pokhara, monsoon landslides, Tihar, trekking economics, WhatsApp as the reply channel. The rules that make this structural are in Part III §3.6.

## 1.3 Course 1 — Context Engineering → BRIEF

*Course-level skill: Context Engineering & Effective Prompting*

| Unit | Learner-facing title | Sub-units | Concept(s) |
|---|---|---|---|
| 1 | Why the same AI treats you differently | 1.1 Meet Maya · 1.2 Maya's first try · 1.3 So Maya asked Ravi · 1.4 So that's the difference | Context exists (**B**) |
| 2 | When the facts aren't enough | 2.0 The message that broke the customer · 2.1 The Role · 2.2 The Intent · 2.3 The Audience · 2.4 Maya rewrites the message | **R**, **I** |
| 3 | The endless "make it better" | 3.0 The correction spiral · 3.1 The word that never works · 3.2 The shape, decided upfront · 3.3 Maya ends the spiral | **E**, **F** |
| 4 | The answer it invented | 4.0 The answer it invented · 4.1 Why confident isn't correct · 4.2 Fencing the AI inside the truth · 4.3 Maya answers Sunita, safely | Grounding (**B** deepened) |
| 5 | The Monday it forgot everything | 5.0 Friday's genius, Monday's stranger · 5.1 Why it forgets · 5.2 Everything on one page · 5.3 Look what you can do now | Statelessness → the reusable BRIEF |

**The framework, as revealed in 5.2:**

| Letter | Meaning | Earned in |
|---|---|---|
| **B** — Background | The facts of your world, and grounding in real documents | Units 1 & 4 |
| **R** — Role | Who the AI should be — the voice | Unit 2 |
| **I** — Intent | The outcome you want — and who's reading | Unit 2 |
| **E** — Examples | Show your voice, don't describe it | Unit 3 |
| **F** — Format | The shape — length, structure, must & must-not | Unit 3 |

The reveal line: *"They spell BRIEF — because that's exactly what you've learned to do: brief the AI, the way you'd brief a capable new colleague before handing them a job. This is the framework promised way back in Unit 1. You didn't memorise it — you earned each letter by feeling the problem it solves."*

**The tangible:** a reusable one-page BRIEF, filled once per recurring job, pasted into any fresh chat. *"Fill it once. Paste it forever. The AI's forgetting stops being your problem."* Payoff dramatised: Maya's Monday goes from an hour of re-teaching to ten seconds.

**Skill pool coverage** (units out of 5): Designing Context-Aware AI Systems 5/5 · Structured Prompt Engineering 5/5 · AI Literacy 4/5 · AI Output Validation & Contextual Auditing 4/5 · AI Tool & Platform Literacy 3/5 · Reusable Prompt & Framework Design 2/5 · Audience-Aware AI Communication 1/5 · Secure AI Prompting Practices 1/5

## 1.4 Course 2 — Agentic AI → AGENT

*Course-level skill: Agentic Automation Design*

Opening frame: *"What she had not noticed was that being able to do everything with AI had quietly become doing everything herself, all day, by hand, around it."*

| Unit | Learner-facing title | Sub-units | Concept |
|---|---|---|---|
| 1 | You fixed the writing. So why are you MORE tired? | 1.1 A normal Monday · 1.2 Count the cost · 1.3 You've become the middleware | **A** — Aim |
| 2 | Why won't it just DO it for me? | 2.0 "Just do it every Monday" · 2.1 It still won't budge · 2.2 What it takes to actually do a job | **G** — Go-signal |
| 3 | It did exactly what I said, and it was a disaster | 3.0 It did exactly what I said · 3.1 Read it like a machine would · 3.2 The gaps you didn't know you left | **E** — Explicit steps |
| 4 | Who's watching while you sleep? | 4.0 The three-week silent failure · 4.1 Would you have caught it? · 4.2 The failure you can't hear | **N**, **T** |
| 5 | The report that writes itself | 5.0 Five parts, one word · 5.1 Maya's report on one page · 5.2 Build it in Gemini, free · 5.3 What deserves an agent | Assembly + judgment |

**The framework, as revealed in 5.0:**

| Letter | Meaning | Earned in |
|---|---|---|
| **A** — Aim | The outcome, and the quality bar | Unit 1 |
| **G** — Go-signal | What starts it: a time, an event, or you | Unit 2 |
| **E** — Explicit steps | The recipe, gaps removed | Unit 3 |
| **N** — Nod points | Where a human must say yes | Unit 4 |
| **T** — Tools & limits | What it may touch, and must never | Unit 4 |

Reveal line: *"You didn't learn this from a definition. You earned each letter by hitting the problem it solves."*

**The tangible:** a working agent, built free as a Google Gemini "Gem," step by step alongside Maya. The course then closes on judgment — 5.3 *What deserves an agent*: "the last skill is knowing when *not* to build one at all."

**Skill pool coverage:** AI Literacy 4/5 · Task Decomposition & Process Design 4/5 · Agent Design & Configuration 4/5 · Automation Judgment & ROI 3/5 · AI Tool & Platform Literacy 3/5 · AI Automation (Agent Building) 2/5 · AI Risk & Oversight Management 2/5 · Secure AI Prompting Practices 2/5 · Workflow & Automation Analysis 1/5 · AI Output Validation & Contextual Auditing 1/5

## 1.5 Course 3 — Responsible AI → TRUST

*Course-level skill: Responsible AI Governance*

Opening frame: *"What she has not thought to ask, not once, is whether everything these machines do in her name is actually right, or merely error-free. Nothing has broken, so nothing has prompted the question."*

| Unit | Learner-facing title | Sub-units | Check |
|---|---|---|---|
| 1 | Everything runs perfectly, so what could go wrong? | 1.1 The quiet empire · 1.2 The shortlist she can't vouch for · 1.3 What might already be wrong · 1.4 The check nobody ran · 1.5 The line that changes everything | Frames all five |
| 2 | The machine lied to a customer, who pays? | 2.0 The machine that lied · 2.1 The policy that never existed · 2.2 Spot the invention · 2.3 Why the machine makes things up · 2.4 Checking what you can't read | **T** — Trace |
| 3 | Two identical CVs, two different scores. Why? | 3.0 Two CVs, one difference · 3.1 Same CV, two verdicts · 3.2 It wasn't a one-off · 3.3 Where the bias actually comes from · 3.4 The line that keeps it fair | **U** — Uncover |
| 4 | Whose data did you just paste? | 4.0 The paste you can't take back · 4.1 What have you pasted this month? · 4.2 Follow the records out the door · 4.3 What you're really handing over · 4.4 Classify first, paste second | **R** — Respect |
| 5 | Show your work, and sign it | 5.0 The three she nearly sent unsigned · 5.1 Show your work, and sign it · 5.2 Everything spells TRUST · 5.3 Your one-page AI policy · 5.4 Point TRUST at what you built · 5.5 The loop closes | **S**, **T** |

**The framework, as revealed in 5.2:**

| Letter | Meaning | Earned in |
|---|---|---|
| **T** — Trace | Track every claim to a source; sample, quote, keep a trail | Unit 2 |
| **R** — Respect | Protect the data and the people it belongs to; classify, strip | Unit 4 |
| **U** — Uncover | Hunt the bias you can't see; swap-test, keep a human deciding | Unit 3 |
| **S** — Show | Be open that AI was involved, where it matters | Unit 5 |
| **T** — Take | Take the accountability; a named human signs | Unit 5 |

Reveal line: *"Run these five and you can look anyone in the eye — a customer, a candidate, a regulator, your boss — and say 'yes, I can stand behind what this machine did in my name.' You didn't memorise TRUST. You earned each letter from a real failure that could have cost someone something."*

**Notable design choices in this course:**

- **The only external real-world case in the program.** Unit 2 opens on Air Canada's chatbot inventing a bereavement fare policy in 2024 and the court making the company pay. Used as the *anchor of consequence* before the same failure appears in Maya's inbox.
- **The bright line.** Recurs twice (1.5, 3.4) as the program's single hardest rule: *for a decision about a person, AI recommends and a named human decides.* Unit 1.5 establishes when this level of care becomes non-optional — "Maya's shortlist is not a caption or a rough draft. It decides who gets a job."
- **The swap test** — same CV, only the name changed, run repeatedly to rule out flukes. A reproducible learner-runnable experiment, not an assertion about bias.
- **Three tangibles:** an audit sampling habit (2.4), a classify-before-paste protocol (4.4), and a one-page personal AI policy (5.3) — then 5.4 turns the policy on something the learner has already shipped.

**Skill pool coverage:** AI Literacy 5/5 · Responsible AI Use & Compliance 5/5 · AI Output Validation & Contextual Auditing 4/5 · AI Accountability & Transparency 3/5 · AI Governance & Risk Management 3/5 · Secure AI Prompting Practices 3/5 · AI Fairness & Bias Auditing 1/5 · Confidential Information Handling 1/5 · Data Sensitivity Classification 1/5

## 1.6 The skill ontology

Two spreadsheets carry the measurement layer.

**`AI_Native_Skill_Pool_and_Pyramid.xlsx`** — three-level capability pyramid:

- **Level 1** — after the whole program: *AI-Native Professional Fluency*
- **Level 2** — after each course: the three course-level capabilities
- **Level 3** — after each content unit: 3–5 named skills per unit

Plus one sheet per course listing that course's **skill pool** with coverage density (*"assigned to N of 5 units"*). The density figure is how you see at a glance whether a skill is a spine of the course or a one-unit visit.

**`AI_Native_Skill_Mapper.xlsx`** — finer grain: one row per *sub-unit*, mapping Course → Unit → Sub-unit → Title → General Skill. This is where a sub-unit's single primary skill is declared (e.g. 2.1 The first missing landmark → *Role & Persona Specification*; 4.2 Fencing the AI inside the truth → *Source Grounding & Hallucination Control*).

Both files are duplicated into each course folder so the ontology travels with the material.

## 1.7 The outreach layer

The **AI Nativity** session (delivered at Sunway College) is the top of the funnel. Its structure is itself a design artifact worth reusing.

Six-beat flow:

1. **The hook** — *"5 questions about AI you probably can't answer"*
2. **The big shift** — why AI is not just another tool
3. **AI around the world** — the global picture in numbers
4. **The AI Pyramid** — the core idea
5. **The core of AI Nativity** — five habits
6. **What it means for you** — skills, learning, where to go next

**The hook doubles as a diagnostic and a course map.** Each of the five questions is answered, then explicitly routed:

| Q | Question | Routes to |
|---|---|---|
| 1 | What does "GPT" in ChatGPT actually stand for? | How AI works — the foundation |
| 2 | Open a brand-new chat. Does it remember you? | **Context Engineering** |
| 3 | Difference between a chatbot and an agent? | **Agentic AI** |
| 4 | Why does it give confident wrong answers? | **Responsible AI** — judgment |
| 5 | AI gives wrong advice, you act on it. Who's responsible? | **Responsible AI** — accountability |

Then the payoff slide: *"Those weren't random trivia."*

**The five habits** — the AI-Native habit loop, the public-facing compression of all three courses:

```
Frame → Feed → Let it work → Verify → Own
the task    the right    across      before      the
clearly     context      steps       you trust   decision
```

Each habit is taught with a **weak vs. strong** pair and a one-line *"The habit:"* statement, then routed to a course. Two audience-specific closing slides (student / educator) precede the call to action.

---

# PART II — THE THEORY

Everything the program does traces back to one paper: **Khatri, A., & Khanal, B. (2026). *The AI Pyramid: A Conceptual Framework for Workforce Capability in the Age of AI.* arXiv:2601.06500.**

Read that paper before building anything. This part is a summary of what it commits the program to.

## 2.1 Why AI is categorically different

Technological change has historically amplified distinct dimensions of human capability:

| Wave | Extended |
|---|---|
| Industrial machinery | Physical strength |
| Digital computation | Numerical processing |
| The internet | Coordination of information |
| **AI** | **Cognitive labor itself** |

Contemporary AI performs writing, summarising, pattern recognition, communication, ideation, and prediction — forms of reasoning that were, until recently, exclusively human.

**The inversion that matters.** Automation historically concentrated on routine work. Felten, Raj & Seamans (2023) show generative AI disproportionately affects *highly educated, white-collar occupations engaged in non-routine cognitive tasks*. This reverses the standard assumption about who is exposed, and it is the reason AI capability cannot be confined to technical roles.

## 2.2 From AI literacy to AI nativity

**AI literacy** (Long & Magerko, 2020 — 17 competencies across five themes) is a foundational understanding of AI: what it is, what it can do, how it works, how it should be used, how people perceive it. Necessary, but it treats AI as an external instrument.

**AI nativity** is the capacity to integrate AI fluidly into everyday reasoning, problem-solving, and decision-making — treating AI as part of the environment in which reasoning occurs, not a system you occasionally consult.

The paper is explicit that this is **not a linear progression but a qualitative transformation** — "analogous to the difference between studying a foreign language and achieving native fluency." Theoretical grounding: Lave & Wenger's (1991) situated learning — AI-native individuals treat AI systems as collaborators within their communities of practice.

**The observable definition, which is what makes it teachable:** AI nativity "is observable not in what individuals know about AI, but in how they habitually incorporate, interrogate, and govern AI use in task formulation, iteration, and problem resolution across diverse contexts."

This single sentence is the reason the courses teach habits through failure rather than concepts through explanation.

### The before/after table

Used verbatim in both the Concept Brief and the Sunway deck:

| Before | AI-Native |
|---|---|
| Searches and compiles manually | Defines the problem, guides AI, verifies the output |
| Accepts or ignores AI output wholesale | Evaluates, cross-checks, and refines it |
| Uses AI for isolated tasks | Orchestrates AI across a workflow |
| Treats AI as a novelty | Treats AI as part of the working environment |

## 2.3 The AI Pyramid

Three interdependent capability layers. Built on Lepak & Snell's (1999) Human Resource Architecture theory — organizations should differentiate investment based on strategic value and uniqueness of human capital segments.

**AI Native capability — the base.** The broad population that works and reasons in AI-mediated environments but does not design, train, or engineer AI systems. It is a *behavioral orientation*: routinely framing problems AI can engage with, evaluating and contextualising outputs critically, integrating machine suggestions into human judgment, and knowing when AI output should be questioned, constrained, or excluded.

**AI Foundation capability — the middle.** Those who design, build, integrate, and maintain AI-enabled systems: engineers, technical generalists, applied data practitioners, developers. Defined by *what they can build*, not what they know. This layer faces the sharpest skill obsolescence — Deming & Noray (2020) show returns to applied STEM degrees decline sharply within the first decade of working life. Cannot be secured by static credentials.

**AI Deep capability — the apex.** Those advancing the frontier: new architectures, algorithms, training methods, plus those applying frontier techniques for breakthroughs in health, education, science, energy, policy. **Not required in every organization.** Operates at the level of research ecosystems and national innovation systems; its value reaches organizations through spillovers.

### Two things the shape is telling you

Both are stated on the Sunway slide, and both must be repeated whenever the pyramid is shown:

1. **The base is the most critical layer.** Just as ancient pyramids required massive foundations to support narrow peaks, AI-enabled societies require broad AI Native capability to support smaller populations of Foundation builders and Deep researchers. Visual convention suggests the apex is the achievement; the framework inverts that.

2. **It is NOT a career ladder.** Nobody has to climb. The layers describe how capability is distributed across a *system* — scale, function, and dependency — not a ranking of people. Everyone needs Native; only some roles need the rest.

Overinvesting in one layer produces systemically imbalanced organizations: sophisticated research capacity with no deployment expertise, or widespread tool adoption with no technical infrastructure to sustain it.

## 2.4 The four AI-Native skill areas

AI Native capability decomposes into four interconnected areas. These define the program's course map.

| Area | Definition | Status |
|---|---|---|
| **Context Engineering** | Structuring information, instructions, and data to guide AI toward better outcomes | **Course 1 — shipped** |
| **Agentic AI** | Autonomous task execution, workflow management, goal-oriented actions | **Course 2 — shipped** |
| **Responsible AI** | Fairness, privacy, transparency; knowing when to constrain or reject AI | **Course 3 — shipped** |
| **AI-Enabled Problem Solving** | Research, analysis, planning, and decision support with AI in the loop | **Not yet built** — see Part IV |

The underlying five core skills the paper names: formulating tasks in alignment with how models interpret and reason; evaluating reliability and limits of outputs; orchestrating AI-enabled workflows; integrating machine suggestions into human judgment; and exercising responsible AI awareness.

## 2.5 From programs to infrastructure

The paper's structural argument: historically, capability building operated as *discrete programs* transferring stable skillsets. AI breaks that model, because the skills evolve continuously. If the whole population needs to be AI-native and multiple sectors are transforming simultaneously, program-based training cannot keep pace.

Capability building must therefore be **infrastructure**, comprising three interdependent systems:

- **Measurement infrastructure** — defining, assessing, and updating what it means to be Native / Foundation / Deep across roles and sectors
- **Learning infrastructure** — continuous, problem-embedded pathways, not episodic interventions
- **Credentialing and verification infrastructure** — capabilities recognised, transferred, and trusted across organizations and labor markets

This is why the program has a skill ontology (Part I §1.6) and not just a syllabus.

## 2.6 Problem-Based Learning as the named mechanism

**PBL is not a stylistic choice. The paper names it as the core mechanism of learning infrastructure**, on this reasoning: AI-related skills are not abstract technical knowledge but *contextual practices intertwined with specific workflows and roles*. PBL adapts to the problems learners actually need to solve.

Evidence base cited:

- **Strobel & van Barneveld (2009)** — meta-synthesis of PBL meta-analyses: PBL is superior to traditional instruction for long-term retention, skill development, and satisfaction. (Traditional instruction wins on short-term retention for standardized exams.)
- **Gijbels et al. (2005)** — strongest positive effects at the level of *"understanding principles that link concepts"*, which is precisely the kind of understanding AI-augmented work requires.
- **Lave & Wenger (1991)** — legitimate peripheral participation; expertise develops by participating in authentic practices within communities.

**The inversion PBL requires:** rather than beginning with AI concepts and then seeking applications, start with the real tasks and challenges individuals face in their roles. AI concepts enter *when they are relevant to solving those specific problems*.

The canonical loop, drawn identically in the Concept Brief and the Sunway deck:

```
Problem → AI Exploration → Human Judgment → Reflection → Capability Growth
```

Sunway slide caption: *"Not lectures first, then applications. Start with a real problem — AI ideas arrive exactly when you need them."*

**This loop is the source of everything in Part III.** Every design rule in the playbook is an operationalisation of it.

## 2.7 The evidence set worth memorising

These figures recur across the Concept Brief, the Sunway deck, and the paper. They are the program's standing arguments.

**The productivity and equity argument**
Brynjolfsson, Li & Raymond (2025), *Generative AI at Work*, QJE 140(2) — customer support agents with AI assistance: **+15% average productivity, +30% for novice workers.** AI disseminates expert practice to less experienced workers. Two implications the program leans on: (a) AI could reduce skill-based wage gaps, but only if lower-skilled populations gain access *and competency*; (b) the 15% depends on *widespread* adoption — organizations cannot deploy AI-native capability to a subset of roles and expect system-level benefit.

**The exposure argument**
Cazzaniga et al. (2024), IMF — ~60% of employment exposed to AI in advanced economies vs. **26% in low-income countries**. Exposure means both opportunity and displacement risk; advanced economies are better positioned to capture the benefit.

**The obsolescence argument**
Deming & Noray (2020), QJE — returns to applied STEM degrees decline sharply within the first decade of working life due to rapid turnover in skill content. Static credentials do not hold.

**The dependency argument**
Hosseinioun et al. (2025) — skills exhibit hierarchical dependency structures; foundational skills are prerequisite to advanced skills in nested patterns. Supports the pyramid's functional-dependency logic and implies that assessing advanced capability requires first verifying prerequisites.

**Adoption and market figures** (Sunway deck)

- 1 billion+ monthly AI tool users; ~1.5 billion counting AI embedded in other products
- ~800 million weekly ChatGPT users — largest user base of any single product
- 37% of people in richer economies used AI in 2025, up from 19% in 2023
- 91% of businesses use AI in some way, up from 78% in 2024
- 280× cheaper to run AI in 18 months — the same answer that cost $20 now costs ~$0.07
- $252 billion global company investment in AI (2024), an all-time high
- **+56% average pay premium for AI skills**
- 4× faster productivity growth in AI-intensive industries

**The Nepal / Global South figures**

- AI use: **27% Global North vs 15% Global South** — the gap is widening
- UAE highest at 64% of working adults; Singapore ~61%
- AI's share of South Asian job postings: **2.9% → 6.5%** from 2023 to 2025
- **August 2025: Nepal endorsed its first National AI Policy.** Nepal has South Asia's lowest AI exposure today.

The framing that follows: *the map is uneven — and that's the opportunity.*

Full source list for these figures is in the companion document.

---

# PART III — THE PLAYBOOK

*This is the build manual proper. Everything here is derived from the three shipped courses. If you are making a new unit, a new course, or a new session, work from this part.*

## 3.0 The six commitments

Everything below is downstream of these. If a design decision is unclear, resolve it against these six.

**1. The problem comes before the concept. Always.**
Never open with a definition. Open with someone doing the sensible thing and it going wrong. The concept is the *answer to a question the learner is already asking* — which means they have to be made to ask it first.

**2. No jargon until it is earned.**
Course 1 Unit 1 states the rule explicitly: *"no technical terms until phase 4"* and *"We will not use a single piece of jargon until you have earned it by experiencing the problem yourself."* A term is only introduced after the learner has felt the gap it names. Naming too early converts a discovery into a vocabulary lesson.

**3. The framework is assembled, never issued.**
Five problems produce five letters. The acronym is *revealed* in the final unit as a discovery, not printed in the syllabus. *"You didn't memorise TRUST. You earned each letter from a real failure."*

**4. Everything lives in the slides.**
Repeated in every unit spec: *"everything in the slides · no separate downloads"* and *"written to be understood fully by reading alone, no facilitator needed."* Self-paced comprehension is a hard constraint, not a preference. If a learner needs an instructor to understand a slide, the slide is broken.

**5. Show the artifact, never summarise it.**
The failed email appears in full. Both CVs appear word-for-word. The run log appears line by line. The WhatsApp reply appears as a chat bubble. If a claim can be shown as a thing the learner reads with their own eyes, it must be — because the learner has to *catch it themselves* for the lesson to land.

**6. One variable at a time.**
Every experiment holds everything constant and changes one thing. *"Maya keeps every fact the same. She only adds one line at the start."* This is what makes the causal claim visible rather than asserted, and it is why the experiments are repeated 2–4 times — one change could be luck; four is a mechanism.

## 3.1 The two-level structure

There are two nested structures. Confusing them is the most common way to get the design wrong.

### Level 1 — the unit arc, expressed as sub-unit types

Each sub-unit carries a **type tag** on its opening slide. The tag declares the sub-unit's job.

| Position | Tag | Job |
|---|---|---|
| **X.0** | `EXPERIENCE THE PROBLEM` | Live the failure through real prompts, emails, replies. Nothing labels it a problem. |
| **X.1 … X.n** | `DISCOVER IT YOURSELF` | One concept cycle each — one landmark, one part, one check |
| **X.last** | `PUT IT TOGETHER` | Maya's combined prompt → the result → your turn → a takeaway |

**Course-opening units** run a lighter variant, because there is no prior concept to stack on:
`EXPERIENCE THE PROBLEM → TRY IT YOURSELF → NAME IT & GENERALISE`

**Course-closing units** add:
`THE PAYOFF` (the acronym reveal + the reusable tangible) → `THE WHOLE JOURNEY` (look how far you've come)

So the standard unit is:

```
Experience the problem  →  Discover ×n  →  Put it together
```

**The number of Discover cycles is set by how many concepts the unit carries, not by a target length.** Observed: C1 U2 carries 3 (Role · Intent · Audience), U3 carries 2 (Examples · Format), U4 carries 2 (hallucination → grounding & verify), U5 carries 1. Each unit spec states this explicitly — *"deep discovery arc, 3 concept cycles each following the 8-step flow."*

### Level 2 — the 8-step flow inside one DISCOVER IT YOURSELF sub-unit

This is the atomic teaching unit of the whole program.

| # | Step | What it must do |
|---|---|---|
| 1 | **Think first** | An everyday-life brainstorm question. **AI is not mentioned.** Then hold the answer — force the learner to commit before any reveal. |
| 2 | **Experience** | Live the problem multiple times through real prompts, emails, replies. **No label tells you it's a problem.** |
| 3 | **Look again** | Re-read the failure with new eyes. The evidence was always on the page; now it becomes visible. |
| 4 | **Discover the fix** | A baseline is shown, then *add this → the result changes.* Repeated 2–4 times so it reads as systematic, not lucky. |
| 5 | **Name it** | The term arrives — **only now** — with the mechanism for why it works. |
| 6 | **The intuition / the mental picture** | An analogy from ordinary life that makes the concept portable. |
| 7 | **Your turn** | Three quick applications in different contexts. |
| 8 | **Generalise + bridge** | "This works for everything you write" — then open the next problem. |

### The canonical slide-header vocabulary

Observed frequency across the 63 shipped sub-unit decks:

| Header | Count | Step |
|---|---|---|
| `FIRST, A QUESTION` / `THINK FIRST` | — | 1 |
| `REFLECT BEFORE WE GO ON` / *"Hold your answer"* | — | 1 (device) |
| `LOOK AGAIN AT…` | — | 3 |
| `EXPERIMENT · [what changed]` | — | 4 |
| `NOW WE CAN NAME IT` / `THE NAME FOR IT` | **17** | 5 |
| `THE INTUITION` / `THE MENTAL PICTURE` | — | 6 |
| `YOUR TURN` | **17** | 7 |
| `THE BIGGER PICTURE` | **12** | 8 |

`THE NAME FOR IT` and `YOUR TURN` both appear 17 times — one per concept cycle across the program. That symmetry is the integrity check: **every named concept gets a practice, and every practice names a concept.**

### Worked example — C1 U2.1, "The Role"

The reference implementation. Study this one before writing a new sub-unit.

1. **Think first** — *"You have a money problem. You could ask a bank officer, a shopkeeper, or your grandmother — same question. Would the three answers sound the same? Why not?"* No AI in the question.
2. **Hold your answer** — *"Take ten seconds."* Then the pivot: *"Now here's the question that cracks Maya's problem open: when she asked ChatGPT to write the message, who did it think it was?"*
3. **Look again** — Maya's failed message in full. *"Read it out loud. It sounds like a lawyer. Or an insurance form. Or a government notice."*
4. **Discover the fix** — Four experiments, identical facts, one line added each time:
   - *"You are a warm, caring local trekking guide"* → warm, human, on your side
   - *"You are a calm operations manager"* → clear, organised, reassuring
   - *"You are a corporate legal officer"* → cold, defensive — **"(This is the default!)"**
   - *"You are an excited travel host"* → upbeat, persuasive
   Closing line: *"Same facts every time. Four completely different messages. The only thing that changed was who you told it to be."*
5. **Name it** — *"This landmark is called the Role."* Plus the mechanism: *"the AI has read millions of examples of how a caring guide writes… When you name the role, you're pointing it at the right shelf of examples."*
6. **The intuition** — *"You explain the same problem differently to your boss, your best friend, and a child."* **The mental picture** — *"a brilliant actor who can play anyone, standing on stage with no script, waiting. 'You are a warm local guide' is the director's note."*
7. **Your turn** — three situations, each with a suggested role, and *"There's no single right answer."*
8. **Generalise + bridge** — *"Every time you ask AI to write anything, quietly ask: who should be saying this?"* Then: *"Role is landmark number one. But Maya's message still has a problem — it tells people what happened, but it isn't really trying to achieve anything. That's the next discovery."*

Note step 4's third experiment. It doesn't just add a variant — it **reveals that the learner's original failure was one of these roles all along**. The default *is* the corporate legal officer. That reframing is what turns four examples into an explanation.

## 3.2 How to design a unit from scratch

Work in this order. Do not skip to step 4.

**Step 1 — Name the failure, not the topic.**
Ask: *what does a competent person do that seems entirely reasonable and produces a bad outcome?* That is the unit. Write it as the learner's complaint, in their voice.

Right: *"You fixed the writing. So why are you MORE tired?"* · *"It did exactly what I said, and it was a disaster."* · *"Two identical CVs, two different scores. Why?"*
Wrong: *"Unit 3: Task Decomposition."*

**Step 2 — Find the trap the previous unit set.**
The best failure is one *caused by the previous lesson's success*. Course 1 makes your output good, so everything lands on your desk. Course 2 makes your agents reliable, so nobody questions them. Within Course 1: Unit 1 teaches facts; Unit 2 opens with *"Unit 1's lesson worked… until a Tuesday in monsoon season."* This is the strongest structural device in the program and should be the default.

**Step 3 — Decide the concept cycles.**
List every concept the failure implies. Each becomes one `DISCOVER IT YOURSELF` sub-unit. Two or three is typical; more than three and the unit is really two units.

**Step 4 — For each cycle, find the everyday analogy first.**
Before designing the AI experiment, find the ordinary-life question that has the same shape. *Money advice from a bank officer vs. a grandmother* is the Role. *Asking a friend for a real favour* is what it takes to act. *A doctor who says "your result is abnormal" vs. one who says "here's what we found and exactly what we'll do"* is the Intent. If you cannot find this analogy, the concept is not yet understood well enough to teach.

**Step 5 — Design the one-variable experiment.**
Hold the entire scenario constant. Change exactly one thing. Show the before and after in full. Repeat with 2–4 variants, and make at least one variant reveal the learner's *own* default behaviour.

**Step 6 — Write the naming slide last.**
Only after steps 4 and 5 exist. The naming slide has two obligations: give the term, and explain the mechanism in plain language. Never give the term without the mechanism.

**Step 7 — Build the Put It Together sub-unit.**
Maya's combined artifact (the full prompt, the full spec, the full policy) → the result it produces → the learner's turn to do the same → a one-line takeaway. This is where the unit's concepts stop being separate.

**Step 8 — Write the bridge.**
The last line of the unit must open the next problem. *"But Maya's message still has a problem…"* The learner should finish a unit already curious rather than merely satisfied.

## 3.3 The acronym method

Every course ends in a five-letter word. This is a deliberate mechanism, not branding.

**The rules:**

1. **One letter per unit's core concept.** Five units, five letters. If a unit teaches two concepts they may share a letter's territory (C1 U2 yields both R and I; C1 U3 yields E and F), but every letter must trace to a specific problem the learner suffered.
2. **The word must describe the *act*, not the topic.** BRIEF is what you do — brief the AI like a capable new colleague. AGENT is what you build. TRUST is what you earn. A word that merely names the subject is a wasted acronym.
3. **Never announce it in advance.** C1 U1 *promises* a framework without naming it; U5.2 delivers. The promise creates a small open loop across the whole course.
4. **The reveal has a fixed shape:**
   - Slide 1: *"Five problems, five [landmarks/parts/checks]"* — each listed with the unit that produced it
   - Slide 2: *"Now read the first letters"* — the word, then *"You didn't memorise this — you earned each letter by feeling the problem it solves"*
   - Slide 3: the reusable one-page version
   - Slide 4: the payoff, dramatised (Maya's Monday: an hour → ten seconds)
   - Slide 5: *"Your turn — build yours"*, in 3–4 numbered steps
5. **Letter order serves the word, not the teaching order.** TRUST is taught Units 2, 4, 3, 5, 5 but presented T-R-U-S-T. State the source unit beside each letter so the learner can trace it back.

## 3.4 Curation criteria — what earns a place

**Include when:**

- **It is an artifact the learner can inspect.** The full email, both CVs verbatim, the agent's run log, the WhatsApp reply, the exact prompt. If it can be shown, show it.
- **It is a real case with real consequences, and one exists.** Air Canada's chatbot and the court ruling — used once, at maximum leverage, to establish that this is not hypothetical. Used sparingly; the program is otherwise fictional-but-true-to-life.
- **It is a figure that changes a decision.** +30% for novices. 27% vs 15%. 2.9% → 6.5%. Each is load-bearing for an argument. No decorative statistics.
- **It is an everyday analogy.** Bank officer / shopkeeper / grandmother. The actor with no script. Asking a friend for a favour. Freely.
- **It is the learner's own behaviour, turned on them.** *"What have you pasted this month?"* — before the concept is named. This is the highest-value slide type in the program and is underused outside Course 3.

**Exclude when:**

- **It is a definition arriving before its problem.**
- **It is a summary of something that could be shown.**
- **It requires a facilitator to interpret.**
- **It is a downloadable.** *"No separate downloads."* If it matters, it is on the slide.
- **It is a technical term whose gap the learner has not yet felt.**
- **It is a second example that varies nothing.** Variants must each change one thing and prove one thing.

**Sourcing rules:**

- Framework claims cite Khatri & Khanal by footnote, every time.
- Public-facing figures carry a labelled, clickable source list. The Sunway deck's convention: *"Where a report cites an original study, the linked report carries the reference."*
- Academic evidence is used to justify *method* (PBL, situated learning) and *urgency* (exposure, wage premium), not to decorate the learner-facing story. **Maya's story contains no citations.** Keep the evidence layer and the narrative layer separate.

## 3.5 Voice and writing rules

Derived from the shipped copy *(inferred where not stated)*.

**Sentence-level:**

- Second person for the learner, third person for Maya. Never "one" or "the user."
- Short declaratives at moments of impact. *"Confidence is not evidence."* *"Plausible ≠ true."* *"AI advises. You decide."*
- Long, warm, specific sentences in narrative. The 9 p.m. email. The group that changed its dates twice. Specificity is what makes Maya real.
- Contractions throughout. This is spoken register, not institutional register.
- Direct address at the turn: *"Before you read what happened, stop and do one thing — this matters more than it sounds."*

**Structural:**

- Every unit description is written *"learner-facing — paste as is"*, meaning it must survive being read cold, out of context, in an LMS field.
- Sub-unit descriptions are written *"to be read alone"* — each is self-contained enough that a learner arriving mid-course is not lost.
- Durations are declared per sub-unit (6 min, 20 min, 30 min) and per unit (35 min for C1 U1, ~2 hours for C1 U2).
- Two-column **before/after** or **weak/strong** tables are the standard comparison device.

**Forbidden:**

- Jargon before its earning moment.
- The word "simply."
- Any claim about what AI "understands" or "knows." The program consistently describes mechanism instead — *predicts, borrows, points at a shelf of examples*.
- Blaming the learner. Maya is competent throughout; the failures are structural, and the reader is told so: *"this is about you, not just Maya."*

## 3.6 Localisation rules

Nepali localisation in this program is structural. It is not a translation layer or a change of names.

**What makes it structural, observed:**

- **The industry is locally legible.** Trekking and travel — an economy every Nepali learner understands without explanation, with real stakes (a landslide closing a route two days before departure) that need no setup.
- **Geography does narrative work.** Annapurna Base Camp closed → Ghorepani–Poon Hill offered. The substitution is only meaningful if the reader knows both are real treks of different difficulty.
- **The calendar is local.** Tihar drives the promotional post. Monsoon drives the cancellation.
- **The money is local in scale.** A 40-person corporate booking "makes a good month" for a mid-sized Kathmandu operator.
- **The channels are local.** WhatsApp for the customer reply, not email.
- **The tools are free-tier.** Free ChatGPT, free Google Gemini Gems. Nothing in the program requires a paid subscription — this is an access decision, not an incidental one.
- **The comparison is peer-level.** Ravi is *"no more talented than Maya"*, at the same company, using the same free tool. The lesson cannot be attributed to resources or seniority.

A proposed enforceable version of this is in Part IV §4.4.

## 3.7 Pre-ship checklist

Run against every sub-unit before release.

**Structure**

- [ ] The sub-unit carries a type tag: `EXPERIENCE THE PROBLEM` / `DISCOVER IT YOURSELF` / `PUT IT TOGETHER` / `TRY IT YOURSELF` / `NAME IT & GENERALISE` / `THE PAYOFF` / `THE WHOLE JOURNEY`
- [ ] If `DISCOVER IT YOURSELF`, all eight steps are present and in order
- [ ] The unit ends with a `PUT IT TOGETHER` that combines every concept in the unit
- [ ] The final slide bridges to the next problem

**Pedagogy**

- [ ] The problem is experienced before any concept is named
- [ ] Step 1's question does not mention AI
- [ ] No technical term appears before its naming slide
- [ ] The naming slide gives both the term *and* the mechanism
- [ ] There is an everyday analogy or mental picture
- [ ] There is a `YOUR TURN` with three applications
- [ ] Every named concept has a practice; every practice names a concept

**Evidence**

- [ ] Every experiment changes exactly one variable
- [ ] There are 2–4 variants, not one
- [ ] At least one variant reveals the learner's own default
- [ ] Every artifact is shown in full, not summarised
- [ ] Every figure is load-bearing

**Self-containment**

- [ ] Readable and fully comprehensible with no facilitator
- [ ] No external downloads required
- [ ] The sub-unit description survives being read cold, out of order
- [ ] Duration is declared

**Localisation and access**

- [ ] Scenario, geography, calendar, and channel are locally legible
- [ ] Every tool used is available on a free tier
- [ ] Any peer comparison is genuinely peer-level

**Ontology**

- [ ] The sub-unit is mapped to a primary skill in `AI_Native_Skill_Mapper.xlsx`
- [ ] The unit's 3–5 skills are recorded in `AI_Native_Skill_Pool_and_Pyramid.xlsx` Level 3
- [ ] Course skill-pool coverage densities are updated

**Framework integrity** *(unit 5 only)*

- [ ] Each letter traces to a specific unit and a specific suffered problem
- [ ] The acronym was never announced in advance
- [ ] The reveal follows the five-slide shape
- [ ] A reusable one-page tangible is produced
- [ ] The payoff is dramatised with a concrete before/after

---

# PART IV — GAPS AND PROPOSALS

*Everything in this part marked **[PROPOSAL]** is a draft. None of it has been used in a delivered course. It is written to be argued with, edited, or discarded — not to be treated as established practice.*

## 4.1 The gaps, stated plainly

| # | Gap | Why it matters |
|---|---|---|
| 1 | **AI-Enabled Problem Solving has no course.** | One of the four named AI-Native skill areas. Advertised in the Concept Brief and the Sunway deck; three of four are shipped. The Sunway slide even omits the "A UDAAN course" label under it, making the gap visible to prospects. |
| 2 | **No assessment instruments exist.** | The Pyramid paper's central methodological claim is that AI capability must be measured by *competency-based assessment along proficiency continua*, not course completion. The program has a skill ontology but no rubrics, no proficiency scales, and no evidence collection. This is the largest gap between the theory and the build. |
| 3 | **No facilitator layer.** | Everything is built for solo reading, correctly. But live delivery happens (Sunway). There is no facilitator guide, no timing plan, no discussion prompts, no guidance on what to do when a room answers a Think First question wrongly. |
| 4 | **Localisation is asserted, never specified.** | Every unit spec says "Nepali-localised." No checklist defines what that requires, so it cannot be enforced in review or handed to a new writer. Part III §3.6 is a reconstruction, not a standard. |
| 5 | **The delivery platform is unnamed.** | "Paste as is" implies an LMS with unit and sub-unit description fields, plus duration fields. Which platform, and what its constraints are, is nowhere recorded. |
| 6 | **No Foundation or Deep curriculum artifacts.** | The Concept Brief points to ANAIS and "structured training tracks." Nothing in the material set specifies them. Two of three pyramid layers have no build. |
| 7 | **No cohort or feedback loop.** | The infrastructure argument requires capability definitions to be *updated* as AI evolves. There is no recorded mechanism for feeding delivery experience back into the courses. |

## 4.2 [PROPOSAL] Course 4 — AI-Enabled Problem Solving

The skill area is defined as *"research, analysis, planning, and decision support."* Applying the method in Part III:

**Maya's condition entering.** She briefs well (C1), delegates safely (C2), and can stand behind the output (C3). The trap the previous courses set: *she has become excellent at executing tasks someone else framed.* Her manager asks a question that isn't a task — *"should we open a Pokhara branch?"* — and every skill she has assumes the problem already exists.

**Candidate course question:** *"What do you do when nobody has told you what the task is?"*

**Candidate framework — SOLVE** (letters must be earned, so this is provisional and should change as the units are built):

| Letter | Concept | Candidate unit failure |
|---|---|---|
| **S** — Split | Decompose a vague question into answerable sub-questions | Maya asks the AI the big question and gets a confident, useless essay |
| **O** — Observe | Gather evidence; know what you actually have vs. what you assume | She builds a case on three numbers she never checked the source of |
| **L** — Lay out options | Generate and structure genuine alternatives, not one plan and two strawmen | The AI agrees with whatever she proposes; she mistakes agreement for validation |
| **V** — Verify the reasoning | Stress-test the logic, not just the facts — the argument can be wrong when every fact is right | A perfectly sourced recommendation with a broken inference chain |
| **E** — Explain the call | Make a decision defensible to someone who wasn't in the room | She's right, and cannot get anyone to act on it |

**Sycophancy is the strongest available unit.** *"The AI agreed with me"* is a failure every learner has experienced, almost none can name, and it can be demonstrated with a one-variable experiment: present the same proposal twice, once as your own and once as a colleague's you're skeptical of, and compare the responses. It fits the method exactly.

**Sequencing question to settle:** whether this course belongs *before* Responsible AI rather than after. The current chain (write → delegate → govern) is causally tight. Problem-solving may sit better as Course 2, since framing precedes both delegation and governance. Argues against: TRUST's "the loop closes" is written as a program finale.

## 4.3 [PROPOSAL] A competency assessment layer

To close gap 2 without violating commitment 4 ("everything lives in the slides").

**Principle.** Assess the *artifact the learner already produces*. Every unit already ends in a tangible — a filled BRIEF, an agent spec, a classify-first protocol, a one-page AI policy. Those are the evidence. No separate exam.

**Proposed four-point proficiency scale**, applied per skill in the ontology:

| Level | Name | Description |
|---|---|---|
| 0 | **Unaware** | Does not recognise the situation as one where the skill applies |
| 1 | **Prompted** | Applies the skill correctly when told to; does not initiate |
| 2 | **Habitual** | Applies it unprompted in familiar contexts |
| 3 | **Transferring** | Applies it in a context the course never showed, and can say why |

Level 3 is the operational definition of AI nativity — *"observable not in what individuals know about AI, but in how they habitually incorporate, interrogate, and govern AI use… across diverse contexts."* Level 2 is the pass bar for a course; Level 3 is the pass bar for the program.

**Proposed evidence per course:**

| Course | Artifact | Level 3 test |
|---|---|---|
| 1 | A filled BRIEF for the learner's own recurring job | Produces a second BRIEF for a job type not resembling any course example |
| 2 | An AGENT spec plus a working Gemini Gem | Correctly argues that a proposed task should *not* get an agent (5.3 already teaches this) |
| 3 | A one-page personal AI policy plus a TRUST audit of something already shipped | Identifies a bright-line decision in their own work that no course example covered |

**Swap-test as a generalisable assessment device.** C3 U3's method — hold everything constant, change one attribute, compare outputs — is already a reproducible instrument. It could be standardised as the program's house evaluation technique across all four courses, not just bias.

**What this deliberately does not do:** issue a completion certificate. The paper is explicit that static credentials lose relevance. If credentialing is required for UDAAN reporting, it should record *demonstrated level per skill with a date*, so it can be re-verified rather than treated as permanent.

## 4.4 [PROPOSAL] Localisation standard

To turn Part III §3.6 from a reconstruction into an enforceable checklist. A scenario is Nepali-localised when all seven hold:

1. **Sector** — the industry is one a Nepali learner understands without explanation, with visible stakes
2. **Geography** — real named places, where the *relationship between* places carries meaning
3. **Calendar** — the timing is driven by a local season or festival, not a generic quarter
4. **Scale** — money and headcount are realistic for a mid-sized local organisation, and their significance is stated in local terms
5. **Channel** — communication happens where it actually happens (WhatsApp, Viber), not a default assumption
6. **Access** — every tool works on a free tier, on a laptop, on ordinary connectivity
7. **Parity** — any comparison between two people holds resources, seniority, and talent constant, so the lesson cannot be attributed to advantage

Failing any one is a review blocker. *(Item 7 matters most: it is what makes the program's core promise — that this is learnable — credible.)*

## 4.5 [PROPOSAL] Facilitator layer

The self-contained-slides constraint should not be relaxed for live delivery. Instead, add a thin parallel layer that never becomes required reading.

Per unit, one page:

- **Timing plan** — which sub-units to run live and which to assign, with a target minute count
- **The Think First questions**, with the two or three wrong answers a room typically gives and what each reveals
- **Which experiment to run live** — the one variant worth doing together rather than reading
- **The moment of maximum silence** — the point in the unit where a facilitator should stop and wait (e.g. Maya's cursor over Forward; "what have you pasted this month?")
- **The one thing not to say early** — the term, named, with the slide number where it is allowed

**Design constraint:** if the facilitator page were lost, the unit must still work. That is the test of whether this layer has stayed thin.

## 4.6 [PROPOSAL] Feedback loop

Minimum viable version of the "infrastructure not programs" commitment:

- **After every cohort**, record: which sub-unit produced the most confusion, which experiment failed to land, and which learner example was better than the one in the slides. Three fields.
- **Quarterly**, review the figures in Part II §2.7 — adoption, cost, wage premium, Nepal's position. Several will be stale within a year, and they are the program's standing arguments.
- **Per model generation**, re-run every experiment in the shipped slides. The four-role experiment in C1 U2.1 and the swap test in C3 U3 depend on model behaviour that will change. **This is the highest-risk maintenance item in the program:** if a shipped experiment stops reproducing, the sub-unit built on it silently becomes false.

---

# QUICK REFERENCE

## The three frameworks, side by side

| | BRIEF (Course 1) | AGENT (Course 2) | TRUST (Course 3) |
|---|---|---|---|
| | **B**ackground | **A**im | **T**race |
| | **R**ole | **G**o-signal | **R**espect |
| | **I**ntent | **E**xplicit steps | **U**ncover |
| | **E**xamples | **N**od points | **S**how |
| | **F**ormat | **T**ools & limits | **T**ake |
| **Answers** | What do I hand the AI? | What makes it safe to run without me? | How do I stand behind what it did? |
| **Tangible** | A reusable one-page BRIEF | An agent spec + a working Gemini Gem | A one-page AI policy + a TRUST audit |

## The bright line

The single hardest rule in the program, stated twice in Course 3 (1.5 and 3.4):

> **For a decision about a person, AI recommends and a named human decides.**

---

*Build Manual · version 1.0 · Reconstructed from shipped artifacts. Parts I–III are records of existing practice; Part IV is proposal only.*
*Companion: `UDAAN_AI_Native_Context_and_Sources.md` — institutional context, source inventory, bibliography.*

# Sector problem statements

One problem statement per sector, for the 11 sectors in the problem bank. Each one is
written in the challenge-sheet format used in Tangible's problem-based AI productivity
course.

**Status:** draft, 2026-11-13. Not reviewed by Alok or Bishesh, and not tested with anyone
from these sectors.

## Sources

| Source | What it gave |
|---|---|
| Problem bank: build order | 11 sectors, 65 candidate problems, evidence, confidence, and the reason for each |
| Tangible's AI productivity course design | How a problem is chosen and framed: the six problem shapes, the five-week ladder, the challenge-sheet format |

**Evidence is the problem bank's own.** Figures and dates below are copied from the board
and were not checked again here. Its confidence ratings (High, Medium, Low) are carried over
unchanged.

## How each problem was chosen

The AI productivity course picks a problem by the **shape of the work**, not by topic. A
participant carries one real problem through five weeks: workspace, then finding the right
material, then a document to standard, then the finished format, then making it repeat. So
a sector's problem has to survive all five weeks. Each candidate was tested against six
questions taken from that course's design:

| # | Test | Why it matters in that course |
|---|---|---|
| 1 | **Recurring** on a fixed cycle (daily, weekly, monthly) | The work between sessions is the person's real job, and week 5 needs a cycle to repeat |
| 2 | **Owed anyway**: someone expects the output | People keep working between sessions only on work they owe someone |
| 3 | **Fits one of the six shapes** | Every shape walks the same five-week ladder; a shape is what makes the weekly walls appear |
| 4 | **Has a standard and a reviewer** | Week 3's wall is a draft that reads well but cannot be sent; without a standard there is no wall |
| 5 | **Safe material exists** | Invented or published material the person can work on with no real personal data |
| 6 | **A clear human line** | Every challenge sheet ends with what stays a human decision |

The six shapes:

| Shape | In one line |
|---|---|
| **A · The daily exception** | Data arrives on a cycle; find the few items that need attention and say why |
| **B · The periodic report** | Same reader, same structure, new numbers every cycle |
| **C · The document to standard** | Inputs become a document its reviewer will accept |
| **D · The process explained once** | The same questions, answered again and again by the same person |
| **E · The follow-up that never forgets** | Many open items, each waiting on someone, each with a deadline |
| **F · The checker** | A document set reviewed against a checklist; every gap flagged with its reason |

## The eleven at a glance

| Sector | Chosen | Shape | Confidence | Runner-up |
|---|---|---|---|---|
| Health | H2 · HMIS and DHIS2 monthly reporting | B, with A | High | H1 · Plain-Nepali patient instructions |
| Health-tech | D1 · Insurance claims and rejections | F | High | D2 · Electronic records and clinical notes |
| Education | E1 · CDC-aligned lesson plans | C | High | E2 · Feedback for mixed-ability classes |
| Fintech | F2 · Spotting and explaining scams | D | High | F4 · Tracking NRB directives and circulars |
| Agri-tech | A1 · Farmer advisory in Nepali voice and text | D | High | A3 · Crop and livestock insurance explained |
| Municipality | M3 · Grievance triage | E | High | M2 · Ward demands to annual plan |
| Small business | B1 · Social media marketing without a designer | B | High | B3 · Customer messages and fraud attempts |
| Government offices | G1 · Tippani and formal Nepali drafting | C | High | G4 · Citizen questions and RTI responses |
| Policy makers and MPs | P1 · Reading bills and budgets | C | High | P5 · Deepfakes and misinformation |
| Hospitality | T1 · Multilingual reviews | E, with C | Medium | T4 · Permits, routes and altitude information |
| Science and engineering | S1 · Literature reviews and academic English | C | High | S2 · DPRs, BOQs and cost estimates |

**The board's pilot picks held up.** In every sector, the problem marked `pilot` on the
board also scored best on the six tests above. The reasons are the shape fit, not the
label. Where a pick is weaker, the sector section says so.

**Shape balance.** Four of eleven are shape C (Education, Government, Policy, Science). If
the 11 are taught side by side, one group per shape, C will dominate the room. The first
swap to consider is Science to S2 (DPRs and BOQs, which is shape B), then Policy to P5.

---

## Health · H2 · HMIS and DHIS2 monthly reporting

**Shape:** B · The periodic report, with A · The daily exception for the error checks ·
**Confidence:** High · **Who:** health post in-charges, HMIS focal persons, municipal health
coordinators

### The problem

Every month, register entries are counted by hand into the HMIS forms and entered into
DHIS2. The structure and the reader stay the same; only the numbers change. Errors slip in
during tallying, and there is little time left to say what the numbers mean.

**Tasks like this:** Monthly HMIS form · facility trend summary · checking for figures that
look wrong.

### Your challenge

How could you make the monthly report quicker to assemble, easier to check, and more useful
to the person who reads it?

Choose one report from your own work and a small part you can explore today.

**Safe starting material:** A monthly table with invented values in the real HMIS layout,
including a few planted errors. No register pages and no patient identifiers.

**Responsibility:** Check every figure against the source table, and mark any trend you
cannot verify. AI can get sums wrong and can describe trends that are not there. The
in-charge signs the report.

### Why this one

- **Evidence:** 74% on-time reporting, but only about 38% of facilities report online
  themselves; DHIS2 data is often incomplete or inconsistent.
- It is a fixed monthly duty at every facility, so the work between sessions is always
  there. The work is tables and short summaries, so the course's report weeks (3 and 4)
  fit directly.
- AI arithmetic mistakes are easy to show live, so the week-3 wall arrives on its own.
- **Runner-up:** H1 (plain-Nepali patient instructions) is high value but shape C. H5 was
  reframed by the board so that AI never makes a triage decision; keep that framing if it
  is ever chosen.

---

## Health-tech · D1 · Insurance claims and rejections

**Shape:** F · The checker · **Confidence:** High · **Who:** insurance desk staff, medical
recorders, hospital finance teams

### The problem

Claims to the Health Insurance Board go out in large numbers, and a missing document or a
mismatch with the package rules gets a claim rejected. Payment can then be delayed for
months. Today a person reads each claim file in full to find the few gaps.

**Tasks like this:** Checking a claim file before submission · summarising why claims were
rejected · drafting an appeal.

### Your challenge

How could you make a first check of a claim file show every gap and its reason, without
treating silence as proof the file is complete?

Choose one kind of claim from your own work and a small part you can explore today.

**Safe starting material:** An invented claim pack with planted gaps, and package rules you
supply yourself. No real patient or claim data.

**Responsibility:** AI must never help inflate or fake a claim. Mark every finding you are
unsure of. Submitting or appealing a claim stays a human decision.

### Why this one

- **Evidence:** unpaid claims owed to hospitals were reported at Rs10 billion to over Rs16
  billion during 2026; about one claim in five has been reported rejected; major hospitals
  suspended insurance services.
- It is the course's checker shape, so the walls are already known: scanned documents read
  badly, and a checker that misses a gap and says "complete" is worse than none.
- It carries the strongest ethics lesson in the set: honest claims only.
- **Runner-up:** D2 (electronic records). D3 and D4 overlap with Health's H5 and H2.

---

## Education · E1 · CDC-aligned lesson plans

**Shape:** C · The document to standard · **Confidence:** High · **Who:** community school
teachers

### The problem

Teachers, often temporary or relief staff, plan lessons for multi-grade classes with little
support. Every plan has to meet a standard, the CDC learning outcome, and the plans are due
every week.

**Tasks like this:** Weekly lesson plan · a plan for a multi-grade class · a plan in Nepali
or English.

### Your challenge

How could you get from a CDC learning outcome to a lesson plan you would teach from, faster,
without drifting away from the syllabus?

Choose one subject and grade from your own teaching and a small part you can explore today.

**Safe starting material:** A published CDC learning outcome and your own past plans. No
student names or marks.

**Responsibility:** Check every plan against the CDC outcome it claims to meet. Watch for
content invented by the AI or taken from a foreign syllabus. The teacher decides what is
taught.

### Why this one

- **Evidence:** community schools are short of more than 50,000 subject teachers; no new
  permanent quotas since 2000.
- Weekly, owed, and the standard is published, so week 3 has a real reviewer. The CDC
  curriculum is a large body of material, so learning to find only the relevant part
  (week 2) comes up naturally.
- Low confidentiality risk: curriculum documents are public.
- **Runner-up:** E2 (practice and feedback for mixed-ability classes). E6 overlaps with E2.

---

## Fintech · F2 · Spotting and explaining scams

**Shape:** D · The process explained once · **Confidence:** High · **Who:** branch staff,
wallet agents, customer-education teams

### The problem

Customers lose money to OTP, fake-prize and impersonation scams. Staff are asked the same
questions every day: is this message real, what should I do now? Each answer is given from
memory, and the customer waits until someone with the answer is free.

**Tasks like this:** "Is this SMS genuine?" · explaining an OTP scam to a customer · a
warning notice in Nepali.

### Your challenge

How could a colleague or customer get a reliable answer about a suspicious message with less
repeated explanation from you?

Choose one kind of scam you see in your own work and a small part you can explore today.

**Safe starting material:** Invented scam messages written in the style of real ones, and
published warnings. No real customer messages, numbers or account details.

**Responsibility:** AI may wrongly call a scam legitimate, so a "looks fine" answer is never
a clearance. Mark any answer you cannot verify. Contacting customers and blocking accounts
stay human decisions.

### Why this one

- **Evidence:** 20,526 cybercrime complaints in FY2025/26; wallet hacking and OTP phishing
  are the top fraud types.
- Shape D, fewer repeated explanations, is the aim the AI productivity course was first
  built around.
- Every learner is a potential victim too, so the skill pays off outside work.
- **Not chosen:** F3 (AML and KYC narratives) is high evidence, but its real material is
  suspicious-transaction content, which must never go into a public tool. That makes safe
  practice material hard to build. **Runner-up:** F4 (NRB circulars), also shape D.

---

## Agri-tech · A1 · Farmer advisory in Nepali voice and text

**Shape:** D · The process explained once · **Confidence:** High · **Who:** agronomists,
agritech call-centre advisors, extension staff

### The problem

Advisors answer the same crop, pest and weather questions from thousands of farmers, often
by voice and in local languages. The answers change with the season, and wrong advice on a
pesticide dose can cause real harm.

**Tasks like this:** Seasonal advisory · answer script for a common pest question · an
SMS or voice-note version of advice.

### Your challenge

How could farmers get a correct answer to a common question with less repeated
explanation from you, while every answer stays checked against an official source?

Choose one crop or season from your own work and a small part you can explore today.

**Safe starting material:** Official advisories and published crop guides, plus invented
farmer questions. No farmer names or phone numbers.

**Responsibility:** Never send AI crop or chemical advice without checking it against an
official source. Watch for advice written for Indian conditions rather than Nepal's
varieties. Outbreaks and dose decisions need a technician.

### Why this one

- **Evidence:** agriculture is about 24% of GDP and involves about 62% of households; NAAMP
  and Connect Kisan agreed in February 2026 to provide voice and text AI advisory to
  farmers.
- It is the core daily job in the sector, it is already being rolled out nationally, and the
  key habit (check against the official source) is exactly week 3's lesson.
- **Runner-up:** A3 (insurance explained) has the most striking evidence: 2,107 crop
  policies against 164,211 livestock and fish policies. But claims are seasonal, not weekly.

---

## Municipality · M3 · Grievance triage

**Shape:** E · The follow-up that never forgets · **Confidence:** High · **Who:**
information officers, grievance focal persons

### The problem

Complaints arrive by phone, Facebook, Hello Sarkar and in person, with no single list. Each
one has a deadline, an owner and a next step, and that information sits across messages,
registers and memory. Complaints slip when the officer is busy.

**Tasks like this:** Sorting incoming complaints · tracking each one against its response
deadline · drafting an acknowledgement.

### Your challenge

How could you keep every open complaint and its next action visible, and stop deadlines
being missed?

Choose one channel or type of complaint from your own work and a small part you can explore
today.

**Safe starting material:** Invented complaints with invented names, wards and dates. No
real complainant details.

**Responsibility:** Send no replies. Check that no urgent case is filed as routine. Decisions
on urgency, escalation and the response stay human. Never expose who complained.

### Why this one

- **Evidence:** Hello Sarkar complaints rose 321% to 69,724 in FY2025/26; fixed response
  times are now required.
- It is the course's follow-up shape, so the known walls carry over: inputs arrive by phone
  and in person, and the tracker is only as good as what reaches it.
- It is daily, deadline-driven and measurable.
- **Runner-up:** M2 (ward demands to annual plan) is annual, which does not suit a five-week
  cycle. M5 (disaster warnings) is high value but seasonal, and safety-critical text needs a
  person.

---

## Small business · B1 · Social media marketing without a designer

**Shape:** B · The periodic report, applied to content: the same kind of post every week,
new products · **Confidence:** High · **Who:** shop owners, home producers, local brands

### The problem

Owners must post to sell, but have no designer, copywriter or budget. Every week brings new
stock or a new offer, and each post is written and designed again from scratch.

**Tasks like this:** Weekly product posts · a festival offer · captions in Nepali and
English.

### Your challenge

How could you produce this week's posts faster, in your own voice, without starting from a
blank page each time?

Choose one product line from your own business and a small part you can explore today.

**Safe starting material:** Your own product photos and descriptions. These are yours and
are already public.

**Responsibility:** Make no claim about a product that you cannot stand behind. Do not use
images you do not have the rights to. The owner decides what gets posted.

### Why this one

- **Evidence:** 14.8 million social media identities; social sellers must now register under
  the E-Commerce Act.
- It is the safest entry point in the set: the material is the owner's own and already
  public, so there is no confidentiality problem. Results are quick and visible.
- It fits the course's split between writing the content and producing the formatted
  version: one set of product content, many posts.
- **Weaker on:** the reviewer (test 4). The owner is their own reviewer, so week 3 needs
  a stand-in standard, such as a past post that sold well. **Runner-up:** B3 (customer
  messages and fraud) is shape D or E and also daily.

---

## Government offices · G1 · Tippani and formal Nepali drafting

**Shape:** C · The document to standard · **Confidence:** High · **Who:** section
officers, nayab subbas

### The problem

Officers spend hours on tippani, letters and minutes in formal Nepali. Each one has to meet
the office's register and format, and drafts come back from the reviewer for rework.

**Tasks like this:** Tippani · official letter · meeting minutes.

### Your challenge

How could you get from your notes to a tippani your reviewer will accept, with less rework?

Choose one document type from your own work and a small part you can explore today.

**Safe starting material:** A past, non-confidential tippani or an invented one in the same
structure. No live or classified files.

**Responsibility:** Mark any fact, figure or commitment you cannot trace to its source. AI
often gets formal Nepali wrong, so check the register line by line. The signing officer is
responsible for what goes out.

### Why this one

- **Evidence:** the Auditor General found Rs36.28 billion in spending without supporting
  documents.
- Tippani writing is the core daily task of the civil service, and it is the clearest case
  of the course's document-to-standard shape: little of the time goes on the thinking, and
  most goes on register, rework and format.
- Formal Nepali is hard for AI, so the week-3 wall (a draft that reads well but cannot be
  sent) is guaranteed.
- **Runner-up:** G4 (citizen questions and RTI) is shape D or E and overlaps with
  Municipality's M3.

---

## Policy makers and MPs · P1 · Reading bills and budgets

**Shape:** C · The document to standard · **Confidence:** High · **Who:** MPs, committee
staff

### The problem

Many first-time MPs must read long bills and budget documents quickly. Each bill is a large
document, and what a member needs is a short, faithful brief: what each clause changes and
what to ask about it.

**Tasks like this:** Clause-by-clause summary · briefing note before a committee meeting ·
budget-line comparison.

### Your challenge

How could you get from a long bill to a brief you trust enough to speak from, without
missing a clause?

Choose one bill or budget document you are working on and a small part you can explore
today.

**Safe starting material:** A published bill or budget PDF. These are public.

**Responsibility:** Check every summary line against the clause it cites. Mark anything
left out. Watch for a summary that leans one way. The member's position is theirs.

### Why this one

- **Evidence:** RSP won 182 of 275 seats with many first-time MPs; the IT and Cyber
  Security Bill is pending.
- It is the course's week-2 problem in its plainest form: finding the one part you need in
  a very long document, without reading all of it.
- The material is public, so there is no confidentiality problem.
- **Weaker on:** recurrence and who attends. Bills arrive in waves rather than weekly, and
  the person doing the work between sessions is more likely to be committee staff than the
  MP. Confirm who the learner is before building. **Runner-up:** P5 (deepfakes).

---

## Hospitality · T1 · Multilingual reviews

**Shape:** E · The follow-up that never forgets (reviews left waiting), with C for the
reply itself · **Confidence:** Medium · **Who:** hotel owners, front-office managers

### The problem

Reviews arrive in many languages across several sites. Some go unanswered for days, and
the ones that are answered vary in tone. Unanswered or badly answered reviews hurt bookings.

**Tasks like this:** This week's new reviews · a reply to a complaint · a reply in the
guest's language.

### Your challenge

How could every review get a timely reply in your property's voice, with less effort from
you?

Choose one review site or language from your own property and a small part you can explore
today.

**Safe starting material:** Your property's own public reviews, or invented ones. No guest
booking details.

**Responsibility:** Check every translation, especially anything about allergies, safety or
refunds. Post nothing without reading it. Compensation and complaints stay human decisions.

### Why this one

- **Evidence:** 1.16 million foreign visitors in 2025 from varied markets. This is
  **Medium**: the board found no data on how many reviews go unanswered.
- Daily, owed, public material, and quick results for properties of any size.
- **The weakest evidence of the eleven.** Validate with two or three hotels before
  building. **Runner-up:** T4 (permits, routes and altitude) is shape D and higher stakes,
  since outdated permit rules can endanger lives. T3 (crisis communication) has High
  evidence but is episodic, so a five-week cycle may not include a crisis.

---

## Science and engineering · S1 · Literature reviews and academic English

**Shape:** C · The document to standard · **Confidence:** High · **Who:** researchers,
lecturers, postgraduate students

### The problem

Reviews, papers and grant proposals take months, with limited access to journals. The
document has a demanding reader, a reviewer or a funder, and every claim in it must trace to
a real source.

**Tasks like this:** Literature review section · paper draft · grant proposal.

### Your challenge

How could you get to a review section you would submit, faster, with every reference real
and every claim traceable?

Choose one section of a paper or proposal you are writing now and a small part you can
explore today.

**Safe starting material:** Open-access papers and your own notes. No unpublished data
belonging to other people.

**Responsibility:** Check that every reference exists and says what your text says it does.
AI can invent references that look real. Authorship and the argument are yours.

### Why this one

- **Evidence:** R&D is about 0.03% of GDP; only 325 of 1,853 UGC grants led to published
  papers.
- Week 3's lesson on tracing every sentence to its source is the whole job here, and an
  invented reference is the clearest example of AI being wrong in the set.
- **Runner-up, and the swap to consider:** S2 (DPRs, BOQs and cost estimates) is shape B,
  which would ease the set's lean toward C. S6 (scripting) was moved out by the board
  because it breaks the no-code rule.

---

## Open questions

- **Who decides the final eleven.** These are recommendations and need Alok's or
  Bishesh's call.
- **Validation.** Low- and Medium-confidence items need a practitioner conversation before
  building (the board says so for each). Hospitality is the only Medium pick.
- **Learner fit for Policy.** Confirm whether MPs or their staff would be the participants.
- **Shape balance.** Four C problems out of eleven. Decide whether that matters for how
  the sectors will be taught.
- **Evidence currency.** Figures come from the board as written; several are 2026 news
  reports, which can change quickly.

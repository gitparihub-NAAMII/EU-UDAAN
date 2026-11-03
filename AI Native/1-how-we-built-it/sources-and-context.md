# The UDAAN AI-Native Program

## Context and Sources

*Who runs it · why it exists · what it is built from*

NAAMII Education & Outreach Division · EU UDAAN Programme

---

## How to read this document

This is the companion to `UDAAN_AI_Native_Build_Manual.md`.

Use **this** document when you are explaining the program to someone outside it — a partner, a funder, a new hire on their first day, an institution considering a cohort. It carries the institutional context, the problem statement, the source-material inventory, and the full bibliography.

Use the **Build Manual** when you are making something. It carries what has been built, the theory behind it, the design playbook, and the gaps.

| Question | Document |
|---|---|
| Who is NAAMII? What is UDAAN? | This document, Part I |
| Why does this program exist at all? | This document, §1.3 |
| What courses exist and what's in them? | Build Manual, Part I |
| Why is it designed this way? | Build Manual, Part II |
| How do I build a new unit? | Build Manual, Part III |
| What's missing? | Build Manual, Part IV |
| Where did a given file or figure come from? | This document, Parts II and III |

---

# PART I — WHAT THIS IS

## 1.1 The institution

**NAAMII** — Nepal Applied Mathematics and Informatics Institute for Research — is a multidisciplinary AI Center of Excellence (profit-not-distributing), founded by Nepali researchers. Its mission is to build a self-sustaining AI ecosystem in emerging economies: advancing AI research, developing talent, and driving innovation against high-impact challenges locally and globally.

Track record cited in the Concept Brief:

- USD 2.5M+ in research grants
- 70+ publications at leading international AI venues
- R&D services, startup incubation, and technology transfer with academia, industry, and government
- **ANAIS** (Annual Nepal AI School) — flagship winter school, six editions, participants from 40+ countries, faculty from Oxford, Stanford, ETH Zurich

ANAIS curriculum, as described in the Concept Brief: fundamentals forming the essential toolkit for understanding AI models, then deep neural networks, computer vision, natural language processing, geometric deep learning, generative modeling, neuro-symbolic AI, vision-language models, and large multimodal models.

The **Education & Outreach Division** delivers structured AI capacity-building for students, professionals, technical teams, and leaders. The AI-Native program is its work.

## 1.2 The programme

**UDAAN** — Unleashing Digital Acceleration and Ambition of Nepali Youth — is a four-year, EU-supported national initiative preparing young Nepalis for the digital economy.

Consortium: **Youth Innovation Lab · Heifer Project Nepal · NAAMII**

Four connected components:

| Component | Purpose |
|---|---|
| **PATHSHALA** | Builds digital skills in AI, coding, animation, and emerging technologies |
| **KARYASHALA** | Fosters innovation through internships, hackathons, mentorship, and incubation |
| **KARMASHALA** | Connects youth to fellowships and career opportunities |
| **NITISHALA** | Advances digital governance through policy engagement and local collaboration |

NAAMII leads the AI components of **PATHSHALA** and **KARMASHALA**.

The positioning line from the Concept Brief: *"When you partner with NAAMII, you are connecting to more than a single training provider. You are tapping into a national network built to make Nepal's workforce ready for the digital economy."*

**Programme contact**
Pradip Chaudhary, Community Manager — EU UDAAN Programme, NAAMII
pradip.chaudhary@naamii.org.np · +977-9802378540 · Jwagal Galli, Lalitpur · www.naamii.org

## 1.3 The problem statement

From the Concept Brief, stated in three moves:

1. **AI is not another software tool.** Previous waves extended physical strength or sped up calculation. AI extends *cognitive labor itself*.
2. **"Digital literacy" and one-off "AI awareness" workshops treat AI as an external instrument to be understood.** That prepares people to recognise AI. It does not prepare them to think and work with it.
3. **Therefore:** organizations need a structured, durable way to make their people genuinely *capable* with AI, not just aware of it.

The theoretical elaboration of this argument — the AI Pyramid, the literacy-to-nativity distinction, and the case for problem-based learning — is in the Build Manual, Part II.

## 1.4 The two audiences

The Concept Brief and the Sunway session close on different calls to action, and the program is positioned for both.

**Organizations.** *"If your organization wants to prepare its workforce for an AI-mediated world, register your interest and we will follow up with a tailored scope and pricing."*

**Individuals.** *"If you want to build the AI skills your role now demands, register your interest and we will let you know when the next cohort opens."*

The Sunway session adds two audience-specific closing positions:

| If you're a student | If you're an educator |
|---|---|
| AI nativity is the new baseline employers assume | The base layer is a whole-institution goal, not an IT elective |
| It's behavioural — you can build it now, in your coursework | Design AI into assignments; keep your judgment central |
| You don't need to code. You need to think and judge well with AI | Model responsible use — that's the lesson students copy |

---

# PART II — SOURCE MATERIAL INVENTORY

Everything in the Build Manual is derived from these artifacts. This table is the provenance record.

| Artifact | What it carries |
|---|---|
| `Course{N}_FINAL_SubUnit_Slides/` | 63 sub-unit decks, `.pptx` + `.pdf`. The primary teaching material. |
| `Course{N}_Unit{U}_Descriptions.docx` | Learner-facing unit and sub-unit descriptions, marked "paste as is" |
| `Course1_Unit{U}_Tangible_Reworked.pdf` | Unit build specs: arc type, concept cycles, duration, sub-unit minutes, resources. **The only place the design method is stated in the program's own words** — the source of the 8-step flow and the concept-cycle counts. |
| `Course{N}_FINAL_Content/` | Consolidated per-unit decks (`.pptx` + `.pdf`) |
| `Course{N}/Unit{U}/` | Working folders — per-unit slides, descriptions, and tangibles |
| `AI_Native_Skill_Pool_and_Pyramid.xlsx` | Three-level capability pyramid + per-course skill pools with coverage density |
| `AI_Native_Skill_Mapper.xlsx` | Sub-unit → primary skill mapping |
| `Course{N}_Editable_Canvas.html` | Editable working canvas |
| `AI_Nativity_Sunway_Session.pdf` | 40-slide outreach session delivered at Sunway College; top of funnel |
| `CONCEPT NOTE [DRAFT] V4` | Organisational concept brief for partners and funders |
| Khatri & Khanal (2026), arXiv:2601.06500 | The theoretical foundation |

**Note on duplication.** The two skill spreadsheets are copied into each course folder so the ontology travels with the material. `Course{N}_FINAL_SubUnit_Slides/` and the per-unit `Unit{U}/` folders contain overlapping copies of the same decks; the per-unit folders carry the tangible specs, which the consolidated folder does not.

**Note on file naming.** Sub-unit decks follow `U{unit}.{sub}_{Title-In-Title-Case}.pdf`. Some titles differ slightly between the per-unit folder and the consolidated folder (e.g. `U3.1_Show-Dont-Describe` vs `U3.1_The-Word-That-Never-Works-Example`) — the descriptions document is authoritative for learner-facing titles.

---

# PART III — BIBLIOGRAPHY

## 3.1 Framework

Khatri, A., & Khanal, B. (2026). *The AI Pyramid: A Conceptual Framework for Workforce Capability in the Age of AI.* arXiv preprint arXiv:2601.06500.

NAAMII / UDAAN. *AI Skills Pyramid Concept Brief.* naamii.org

## 3.2 Learning method

Strobel, J., & van Barneveld, A. (2009). When is PBL more effective? A meta-synthesis of meta-analyses comparing PBL to conventional classrooms.

Gijbels, D., Dochy, F., Van den Bossche, P., & Segers, M. (2005). Effects of problem-based learning: A meta-analysis from the angle of assessment.

Lave, J., & Wenger, E. (1991). *Situated Learning: Legitimate Peripheral Participation.* Cambridge University Press.

Long, D., & Magerko, B. (2020). What is AI literacy? Competencies and design considerations.

## 3.3 Economics, exposure, and workforce

Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044
*(Also cited in earlier form as NBER Working Paper 31161, 2023.)*

Felten, E. W., Raj, M., & Seamans, R. (2023). Occupational heterogeneity in exposure to generative AI. SSRN Working Paper No. 4414065. https://doi.org/10.2139/ssrn.4414065

Cazzaniga, M., Jaumotte, F., Li, L., Melina, G., Panton, A. J., Pizzinelli, C., Rockall, E. J., & Tavares, M. M. (2024). Gen-AI: Artificial intelligence and the future of work. *IMF Staff Discussion Notes, 2024*(001). https://doi.org/10.5089/9798400262548.006

Deming, D. J., & Noray, K. (2020). Earnings dynamics, changing job skills, and STEM careers. *The Quarterly Journal of Economics, 135*(4), 1965–2005. https://doi.org/10.1093/qje/qjaa021

Hosseinioun, M., et al. (2025). Skill dependency structures.

Lepak, D. P., & Snell, S. A. (1999). The human resource architecture: Toward a theory of human capital allocation and development.

Clark (2025). *Cited in the Pyramid paper on the transformation of the cognitive environment when large population segments become AI-native.*

## 3.4 Adoption and market data

Microsoft. *State of Global AI Diffusion* (2026). blogs.microsoft.com

Microsoft / OECD. *Global AI Adoption* (2025). microsoft.com

Stanford HAI. *2025 AI Index Report.* hai.stanford.edu

PwC. *2025 Global AI Jobs Barometer.* pwc.com

World Bank. *AI Adoption in South Asia* (2025). blogs.worldbank.org

Government of Nepal. *National AI Policy 2082* (2025). Endorsed August 2025.

**Citation convention used in the outreach material:** *"Where a report cites an original study (e.g. OECD adoption, OpenAI usage), the linked report carries the reference."*

## 3.5 Case material

Air Canada chatbot / bereavement fare ruling (2024). Used in Course 3 Unit 2 as the program's single external real-world case.

---

*Context and Sources · version 1.0*
*Companion: `UDAAN_AI_Native_Build_Manual.md` — what has been built, the theory, the playbook, the gaps.*

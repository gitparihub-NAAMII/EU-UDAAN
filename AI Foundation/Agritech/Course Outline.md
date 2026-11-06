# Agentic AI for Agriculture (Agri-tech) Course

## 1. Course Overview

The Agri-tech course teaches learners to improve agricultural workflows with Agentic AI. Learners move from understanding an agricultural problem, to formulating it in an evidence-aware way, to building the intelligence needed to investigate it, to transforming the workflow with an evaluated prototype.

The course follows four steps:

1. **Understand** the agricultural system.
2. **Formulate** the problem.
3. **Build** the intelligence.
4. **Transform** the workflow.

Analytical work follows the Agri-tech framework U0 to U4: problem formulation, descriptive, diagnostic and predictive analytics, and decision and action. Learners specify the work in familiar documents (Markdown, CSV and Excel files), and an AI agent helps carry it out. Learners review and validate the results before accepting them.

The course is 60 hours: 40 hours of self-study and 20 hours of workshops. A single teaching example, fruit fly in cucumber production, runs through the whole course.

## 2. Course Goals

After 60 hours, learners progress from problem understanding to an evaluated prototype. By the end of the course, learners should be able to:

- **Understand** agricultural systems, stakeholders, value chains and operational context.
- **Formulate** and document evidence-based problems using Agri-tech U0.
- **Structure** a reusable Agricultural Problem Bank.
- **Specify** data, analytical and knowledge requirements.
- **Design** specialized agents, tools, orchestration and human checkpoints.
- **Implement** and test an integrated Agentic AI prototype.
- **Evaluate** limitations, usability, safety and measurable operational outcomes.

## 3. Target Learners and Learning Needs

Four proposed categories provide a starting point for learner profiling and cohort design.

| Category | Who | Strength | Learning need |
|---|---|---|---|
| A. Agriculture Professionals | Agronomists, extension officers, agriculture graduates, researchers | Agricultural context | Data, analytics and AI translation |
| B. IT & AI Professionals | Developers, data scientists, AI engineers, computer science graduates | Computational skills | Agricultural systems and operations |
| C. Interdisciplinary Professionals | Agritech entrepreneurs, digital agriculture teams, project and innovation leads | Cross-domain exposure | End-to-end integration |
| D. Institutional & Policy Professionals | Agricultural officers, municipal planners, NGOs, development organizations | Institutional and service context | AI-enabled decision workflows |

Each group needs to bridge a different gap to contribute to agricultural workflow transformation.

| Category | Learning challenge | Expected capability |
|---|---|---|
| Agriculture Professionals | Agricultural problems are not always translated into structured data and intelligence requirements. | Formulate problems; specify evidence and analytical needs. |
| IT & AI Professionals | Technical solutions may be designed without sufficient understanding of farm operations. | Translate agricultural workflows into technical architectures. |
| Interdisciplinary Professionals | Agricultural data, knowledge, services and decisions may be fragmented. | Design integrated, multi-agent workflows. |
| Institutional Professionals | Agricultural service delivery, monitoring and coordination may lack connected information. | Identify institutional opportunities and decision-support workflows. |

## 4. Learning Approach and Framework

**Learning progression.** The Agritech Agentic AI learning framework has four phases:

1. **Foundation: understand the agricultural problem.** Understanding agricultural systems, U0 Problem Formulation, and infrastructure setup.
2. **Analytical Intelligence.** U1 Descriptive Analytics, U2 Diagnostic Analytics, and U3 Predictive Analytics (optional).
3. **AI Technology Foundation.** Local LLM, RAG and Agentic AI.
4. **Integration and Implementation.** Markdown-driven instructions, analytical agents, agricultural workflow transformation, testing and deployment.

**Agri-tech analytical framework (U0 to U4).**

| Unit | Stage | Key question | Purpose |
|---|---|---|---|
| U0 | Problem Formulation | What is the problem? | Define the agricultural problem and investigation questions. |
| U1 | Descriptive Analytics | What is happening? | Summarize, quantify and visualize the current situation. |
| U2 | Diagnostic Analytics | Why is it happening? | Identify and evaluate possible factors and explanations. |
| U3 | Predictive Analytics | What might happen next? | Estimate future risk, damage and trends using past evidence. |
| U4 | Decision & Action | What should be done? | Recommended actions, implementation plan and monitoring. |

**Two tracks, one learning outcome.** The tracks differ in technical depth, not in the analytical objective.

- **Agriculture background.** Learners focus on writing clear Markdown instructions, organizing agricultural datasets and documents, asking meaningful descriptive questions, directing the AI agent, and checking whether outputs make agricultural sense.
- **Computer Science / IT background.** Learners may additionally focus on understanding data-processing code, implementing statistical functions, building or extending agent capabilities, testing technical execution, and improving reproducibility and performance.

The common deliverable is a validated analytical report with tables, charts, findings and limitations.

**Course design rules.**

- Do not confuse exploration with formulation. Presentation introduces the problem. Exploration builds the knowledge needed to understand the agricultural context. Formulation defines the problem systematically and establishes what must be investigated.
- Keep the agriculture track simple. Focus on using AI agents and project documents, not on building software infrastructure.
- Introduce advanced infrastructure only when learners are ready: first an AI agent with Markdown and CSV or Excel files (U1 to U3), then RAG and a local LLM in a later unit, then the complete Agritech Agentic AI system in integration.
- Evaluate the ability to improve an agricultural workflow, not coding alone.

## 5. Suggested 60-Hour Allocation

The target is 40 hours of self-study plus 20 hours of workshops.

| Stage | Self study (h) | Workshop (h) | Total (h) |
|---|---|---|---|
| 1. Understanding Agriculture/AI | 6 | 2 | 8 |
| 2. U0 Problem Formulation | 4 | 2 | 6 |
| 3. Infrastructure | 2 | 2 | 4 |
| 4. U1 Descriptive Analytics | 5 | 2 | 7 |
| 5. U2 Diagnostic Analytics | 5 | 2 | 7 |
| 6. U3 Predictive Analytics | 5 | 2 | 7 |
| 7. RAG, Local LLM and Agent Basics | 6 | 2 | 8 |
| 8. Integration, Markdown-driven Workflow and Deployment | 5 | 2 | 7 |
| 9. Capstone and Evaluation | 2 | 4 | 6 |
| **Total** | **40** | **20** | **60** |

U3 can be replaced with additional U1/U2 investigation and agentic workflow work if suitable historical data is unavailable.

This allocation revises an earlier 10-stage draft that summed to 46 hours. Agentic AI and the Markdown-driven workflow are folded into stages 7 and 8. The capstone workshop is 4 hours, taken from stages 7 and 8. Workshop hours stay at 20, so trainer load is unchanged.

## 6. Course Modules

### Module 1: Understanding Agriculture

**Time:** 8 hours (6 self-study, 2 workshop)

Learners present the problem, explore and understand the agricultural system, and only then formulate (Module 2). Learners should understand the agricultural reality before formalizing it for analytical and AI-supported investigation.

- **Stage 1, Problem Presentation** (guiding question: What is the problem?). Introduce the agricultural problem and encourage initial questions.
  - Example: farmers cultivating cucumber report fruit fly-related crop damage and difficulties managing the infestation. The extent of infestation, pest species and effectiveness of existing management practices have not yet been systematically established.
  - Discussion questions: What do you understand from this problem? Why might farmers be concerned? What information would you want to know? Have you encountered similar problems in agricultural production?
  - Expected output: a preliminary understanding and initial questions. No formal problem definition or technical solution is expected yet.
- **Stage 2, Problem Exploration** (guiding question: What do we need to understand about the agricultural system behind this problem?). Investigate processes, stakeholders, practices, resources and information needs.
  - Crop and production: what cucumber is and how it is cultivated, crop growth stages, what farmers do from planting to harvest, resources needed, and how farmers monitor crop health.
  - Pest and management: what fruit fly is, how it damages cucurbit crops, how infestation is identified and monitored, which management practices are used, and what advice and resources exist.
  - Stakeholders: farmers (practices and challenges), agriculture technicians (field inspection, advice), extension officers (support and training), agro-vets (inputs and advice), researchers (pest identification, evidence).
  - These are topics for investigation, not assumptions that a particular cause or management failure has been established.
- **Exploration output: the Agricultural System Understanding Document.** It covers the crop production process, crop growth stages, farm operations and resources, pest and management context, stakeholders and their roles, farmers' information and decision needs, and initial knowledge gaps requiring further investigation. Exploration builds contextual understanding. It does not replace formal problem formulation.
- **Evidence rule.** The cucumber fruit fly scenario is a teaching example. Do not invent infestation rates, pest species, causes, locations or intervention effectiveness. Record instead what is reported, what is supported by evidence, what is assumed, and what remains unknown. Reports of damage are not confirmed measurements.

**Learning outcome:** Explain the agricultural system behind a problem, and distinguish presenting a problem from exploring it and formulating it.

### Module 2: U0 Problem Formulation

**Time:** 6 hours (4 self-study, 2 workshop)

**Key question:** What exactly is the problem, and what needs to be investigated?

Problem formulation transforms a broad agricultural concern into a clearly defined, structured and evidence-based problem. It establishes what should happen, what is actually happening, the gap between them, and what evidence is still needed.

- **The eight elements of problem formulation**, taking a broad concern to a bounded, evidence-aware and investigable problem:
  1. Context: where and under what conditions?
  2. Stakeholders: who experiences, influences or addresses the problem?
  3. Expected condition: what should happen?
  4. Observed condition: what is actually happening or measured?
  5. Gap and significance: what is the difference, and why does it matter?
  6. Evidence and uncertainty: what is known, assumed or unknown?
  7. Scope and constraints: what boundaries and limitations apply?
  8. Formulated problem: what exactly needs investigation?
- **Key questions:** What is happening, where and when? Who is affected? What should be happening versus what is observed? What evidence do we have, and what remains unknown? What exactly should we investigate?
- **Expected outputs:** Problem Identification Brief (a clear description), Evidence and Uncertainty Register (known and unknown), Investigation Questions, and next-stage questions.
- **Worked example: fruit fly infestation in cucurbit production** (cucumber, bitter gourd and summer squash).
  - Broad concern: farmers report fruit fly-related crop damage and difficulties managing infestation.
  - Formulated problem: the extent of infestation, pest species, current management practices and contributing factors have not yet been systematically established. A structured investigation is required to understand the extent of the problem, identify operational and information gaps, assess existing management practices, and determine what evidence and decision-support capabilities are needed.
  - What must be investigated: where and when infestation occurs; incidence and severity; which pest species are involved; what practices farmers currently follow; what factors may contribute; what information farmers need.
  - Eight-element check: context (cucumber production and growing season); stakeholders (farmers, workers and extension officers); expected (monitoring, identification and timely management); observed (farmers report damage and management difficulties); gap (evidence and decision-support needs remain unclear); evidence (infestation level and species need validation); scope (selected farms and study period to be defined).
  - Reported concerns are not confirmed measurements; validate the situation through field evidence.
- **Formulated problem record.** Problem ID AG-U0-001, titled "Fruit Fly Infestation and Management Challenges in Cucumber Production". Problem statement: farmers cultivating cucumber report fruit fly-related crop damage and difficulties in managing infestation effectively. However, the extent and distribution of infestation, pest species involved, existing monitoring practices, contributing factors and effectiveness of current management approaches have not yet been systematically established.

**The three stages compared**

| Dimension | Problem Presentation | Problem Exploration | Problem Formulation (U0) |
|---|---|---|---|
| Starting point | Broad agricultural concern | Presented problem | Explored agricultural context |
| Main activity | Recognize the problem | Investigate and learn | Structure and define |
| Main question | What is happening? | How does the agricultural system work? | What exactly needs investigation? |
| Learner role | Discuss and ask initial questions | Investigate processes and context | Define the problem systematically |
| Evidence | Initial reports or scenario | Contextual information gathered | Evidence assessed; uncertainty recorded |
| Main output | Initial questions | Agricultural System Understanding Document | Problem Identification Brief, Evidence and Uncertainty Register, Investigation Questions |

**How the problem evolves.** Presentation: "Farmers report fruit fly damage in cucumber." Exploration: "We need to understand cucumber production, fruit fly biology, crop growth, farm management and farmers' existing practices." Formulation: "The extent of infestation, pest species, management practices and contributing factors have not been systematically established. A structured investigation is required."

**What learners bring from Understanding Agriculture:**

- Farm and production system (land, season, cultivation method).
- Crop production lifecycle (seed, planting, growth, flowering, fruiting, harvest).
- Agricultural resources (soil, water, inputs, tools, labour).
- Farmers and stakeholders (farmers, workers, extension, agro-vets, buyers).
- Crop monitoring and management (plant health, pests and diseases, control practices).
- Production, harvesting and marketing (yield, grading, market, income).
- Agricultural data and records (field observation, input use, production and sales records).

**Learning outcome:** Turn a broad agricultural concern into a structured, evidence-aware problem using the eight elements, and record what is known, assumed and unknown.

### Module 3: Development Infrastructure Setup

**Time:** 4 hours (2 self-study, 2 workshop)

Workshop content:

- Introduction to Git and GitHub.
- Repository creation and project initialization.
- README.md and project documentation.
- Folder structures and Markdown files.
- Git add, commit, push and pull.
- Basic collaboration and version control.

**Learning outcome:** Set up a version-controlled project folder with Markdown documentation, ready to hold the course's instructions, data and outputs.

### Module 4: U1 Descriptive Analytics

**Time:** 7 hours (5 self-study, 2 workshop)

**Key question:** What is happening? Summarize, quantify and visualize the current situation.

- **Purpose:** summarize and describe the current situation using data.
- **Objective (example):** describe the extent, pattern and distribution of fruit fly damage in cucumber farms.
- **Key questions:** How many are affected? How much damage is there? What percentage is damaged? How is it distributed? Where and when does it occur?
- **Typical methods:** frequency and percentage; mean, median and range; distribution and summary tables; simple visualizations.
- **Example data:** farm records (10 farms), fruits inspected and damaged, farm location and date.
- **Workshop (2 h):** identify data, variables, evidence gaps and suitable analytical questions.
- **Self-study (5 h):** agricultural data types, statistics and analytical methods.

**Working environment (agriculture track).** A document-driven AI agent workflow for agricultural professionals.

- Learners use an AI coding agent (Claude Code or OpenAI Codex), Markdown files for instructions and specifications, CSV and Excel files for agricultural data, PDF, Word and other documents for reference material, and a project folder to keep all files organized.
- This unit does not cover building APIs with FastAPI, programming statistical functions, setting up PostgreSQL databases, agent orchestration frameworks such as LangGraph, or RAG and local LLM deployment (covered in a later unit).
- Design principle: agricultural learners specify the work in familiar documents; the AI agent helps carry it out.

Example project folder, `U1_Cucumber_Analysis/`:

| File | Purpose |
|---|---|
| Agent_Instructions.md | Defines the agent's role, objective, rules and expected output |
| Problem_Definition.md | Explains the cucumber fruit fly problem and its scope |
| Data_Description.md | Describes columns, units, categories and missing values |
| Analysis_Requirements.md | Lists descriptive questions, calculations and charts |
| Workflow.md | Specifies the order in which the agent should work |
| Data/cucumber_fruit_fly.csv | Agricultural dataset |
| Outputs/ | Reports, tables and charts |
| U1_Results.md | Records findings, limitations and interpretation |

The flow is: give instructions, provide data and documents, then review the generated tables, charts, findings and report. Markdown is the instruction and documentation format; it is not the statistical calculation engine.

**Example agent instruction.** Analyse the supplied cucumber fruit fly dataset: count the farms represented; calculate the number and percentage of affected farms; summarize damage levels; compare damage across farms; generate appropriate charts; prepare a descriptive analytics report. Rules: use only the supplied data, do not assume results, do not invent missing values, identify incomplete data, and explain limitations.

**Example data used for teaching: fruit damage on 10 farms**

| Farm ID | Fruits inspected | Damaged fruits | Damage (%) |
|---|---|---|---|
| Farm 1 | 100 | 5 | 5.0% |
| Farm 2 | 100 | 8 | 8.0% |
| Farm 3 | 100 | 0 | 0.0% |
| Farm 4 | 100 | 12 | 12.0% |
| Farm 5 | 100 | 6 | 6.0% |
| Farm 6 | 100 | 15 | 15.0% |
| Farm 7 | 100 | 3 | 3.0% |
| Farm 8 | 100 | 10 | 10.0% |
| Farm 9 | 100 | 0 | 0.0% |
| Farm 10 | 100 | 9 | 9.0% |
| **Total** | **1,000** | **68** | **6.8%** |

**Summary of the example data:** 10 farms investigated; 8 (80%) with damage; 1,000 fruits inspected; 68 damaged; overall damage 6.8%; mean damage per farm 6.8%; median 7.0%; range 0% to 15%. Farm 6 had the highest damage (15%); Farms 3 and 9 had no damaged fruits in this sample.

**Example descriptive report.** In a sample of 10 cucumber farms, 8 farms (80%) had at least one damaged fruit. Among 1,000 inspected fruits, 68 were damaged, representing 6.8% damage. The average farm-level damage was 6.8%, with a median of 7.0% and a range of 0% to 15%. Damage varied across farms, with the highest damage observed in Farm 6 (15%).

**U1 agent architecture (IT track).** A practical hybrid architecture of agent, APIs and tools. A single Descriptive Analytics Agent acts as orchestrator: it understands the U0 questions, plans the descriptive analysis, selects and calls the right tools and APIs, interprets results in agricultural terms, and generates the U1 report. Separate agents for every action are not necessary.

| Component | Role |
|---|---|
| Data API | Access and collect data (CSV, Excel, databases, farm and field records) |
| Data Quality API | Validate: missing values, duplicates, consistency |
| Data Profiling API | Understand: variables and types, ranges and summary, completeness |
| Statistics API | Compute: frequency and percentage, mean, median, range, distribution |
| Visualization API | Present: charts (bar, line, pie), tables and dashboards by farm, location and time |
| Reporting API | Generate the U1 report (Markdown or PDF) with findings, limitations, evidence and methods |

Example technology stack: Python (data and statistics), FastAPI (APIs and services), LangGraph (agent orchestration), Gemma or another open LLM (reasoning and interpretation), PostgreSQL (database), Plotly (visualization), with pandas, NumPy, SciPy, statsmodels and Matplotlib as supporting libraries.

**Seven-step strategy for agentic U1:** (1) Define: U0 scope and questions. (2) Prepare: collect and validate data. (3) Plan: select descriptive methods. (4) Execute: compute and visualize via APIs. (5) Explain: interpret results. (6) Report: generate the U1 report. (7) Review: human approval before U2.

**Learning outcome:** A clear picture of the current situation, patterns and distribution of fruit fly damage in cucumber production, delivered as a validated Descriptive Analytics Report with tables, charts, findings and limitations.

### Module 5: U2 Diagnostic Analytics

**Time:** 7 hours (5 self-study, 2 workshop)

**Key question:** Why is it happening? Identify and evaluate possible factors and explanations.

- **Purpose:** investigate the possible reasons and contributing factors behind the problem, and find and evaluate possible explanations.
- **Key questions:** What factors are associated with higher damage? How do environmental, crop and management conditions relate to damage? Which factors are most influential?
- **Typical methods:** correlation analysis, regression analysis, group comparison, pattern and relationship analysis, and evidence from domain knowledge.
- **Diagnostic factors for cucumber fruit fly:**
  - Environmental: temperature, rainfall, humidity, season.
  - Crop: variety, crop stage, plant density, flowering and fruiting.
  - Pest: trap count, pest species, infestation level, damage pattern.
  - Management: monitoring, field sanitation, trap use, other control practices.
  - Also resource and information factors (advice, knowledge) and operational factors (timing, practices).
- **Treat factors as investigation candidates, not established causes.**
- **Diagnostic workflow:** (1) understand the problem and get U1 results; (2) identify diagnostic questions; (3) select relevant data and factors; (4) perform analysis (for example regression and tests); (5) interpret findings; (6) generate the diagnostic report.
- **The U2 agent** identifies potential factors, selects analysis methods, runs diagnostic analyses, interprets results with evidence, and creates a clear report. Input from U1: 8 of 10 farms affected, overall damage 6.8%, damage varies 0% to 15%. Tools and APIs: Data Integration, Diagnostic Profiling, Association Analysis (correlation), Statistical Modelling (regression and advanced models), Knowledge Retrieval (agricultural expertise), and Visualization and Reporting.

**Example diagnostic results (teaching example).** Trap count versus fruit damage: r = 0.78, p = 0.003, a strong positive relationship.

| Factor | Effect on damage | p-value |
|---|---|---|
| Trap count (+10 flies) | +4.2% | 0.003 |
| Temperature (+1 °C) | +1.1% | 0.021 |
| Humidity (+10%) | +1.6% | 0.047 |
| Crop stage (Fruiting) | +5.3% | 0.018 |
| Trap use (Yes) | -4.8% | 0.027 |

Effect on damage is the change in fruit damage associated with each factor; p < 0.05 indicates statistical significance.

**Key findings (example).** Higher trap counts are strongly associated with higher fruit fly damage. Warmer and more humid conditions are linked with increased damage. The fruiting stage has significantly higher damage than earlier stages. Use of traps is associated with lower damage (about 4.8% less). Higher damage was also seen in farms with poor pest management (p = 0.03), and environmental conditions may contribute.

**Possible explanation (example).** Fruit fly infestation is higher under warmer, more humid conditions, especially during the fruiting stage. Regular trap use and field sanitation likely reduce damage by lowering the fruit fly population.

**Learning outcome:** An evidence-based explanation of the key factors contributing to fruit fly damage in cucumber production, delivered as a U2 Diagnostic Analytics Report covering key factors and patterns, statistical evidence, possible explanations and recommendations for further investigation.

### Module 6: U3 Predictive Analytics

**Time:** 7 hours (5 self-study, 2 workshop). Optional: U3 can be replaced with additional U1/U2 investigation and agentic workflow work if suitable historical data is unavailable.

**Key question:** What might happen in the future? Estimate future risk, damage and trends using past evidence.

- **Objective:** predict future fruit fly infestation risk and fruit damage in cucumber production.
- **Key prediction tasks:** infestation risk (farm-wise), expected fruit damage (%), future trap counts (pest population), seasonal risk periods, crop stage vulnerability, potential yield loss, and early warning for high-risk farms.
- **Inputs:** historical data (farm, pest, crop), weather data (temperature, rainfall, humidity), management data (trap, sanitation, practices), and crop data (variety, growth stage).
- **Execution steps:** (1) understand the objective: what to predict; (2) use U0 to U2 evidence: problem, patterns, factors; (3) prepare data: select, clean, create variables; (4) build and evaluate the model: train, test, measure performance; (5) generate predictions: risk, damage, trends, uncertainty; (6) write the U3 report: findings, interpretation, limitations, next steps.

**Markdown files for the U3 agent** (in `Agri-tech/U3_Predictive_Analytics/`):

| File | Purpose |
|---|---|
| U3_Instructions.md | What the agent must do |
| Prediction_Objectives.md | What to predict |
| Prediction_Variables.md | Input and target variables |
| Data_Requirements.md | Data needed (historical and current) |
| Prediction_Methods.md | Suitable prediction methods (for example regression, time-series, ML) |
| Model_Training.md | How to train the model |
| Model_Evaluation.md | How to evaluate performance (for example accuracy, RMSE) |
| Prediction_Results.md | Forecasts and risk estimates |
| U3_Predictive_Report.md | Final predictive analytics report (with uncertainty and limitations) |

**Example: predicting fruit fly damage for the next 7 days (teaching example)**

| Farm | Trap count (flies/week) | Temp (°C) | Humidity (%) | Crop stage |
|---|---|---|---|---|
| F1 | 5 | 24 | 78 | Flowering |
| F2 | 12 | 26 | 82 | Fruiting |
| F3 | 3 | 23 | 75 | Vegetative |
| F4 | 20 | 28 | 85 | Fruiting |
| F5 | 8 | 25 | 80 | Fruiting |

| Farm | Predicted damage (%) | Risk level |
|---|---|---|
| F1 | 4.2% | Low |
| F2 | 8.9% | Medium |
| F3 | 2.1% | Low |
| F4 | 14.6% | High |
| F5 | 7.8% | Medium |

Risk levels group each farm's predicted damage into Low, Medium and High to support early warning, targeted monitoring and timely pest management.

**Suitable methods by prediction need**

| Prediction need | Suitable methods (examples) |
|---|---|
| Predict damage percentage (numerical) | Linear regression, Random Forest regression, Gradient Boosting |
| Predict risk category (low/medium/high) | Logistic regression, Random Forest classification |
| Predict future trap counts (time series) | Time-series models (ARIMA, Prophet) |
| Predict seasonal risk patterns | Time-series and seasonal analysis |
| Capture complex relationships | Machine learning (for example XGBoost, LightGBM) |
| Estimate uncertainty | Prediction intervals, probabilistic models |

**Key deliverables:** Prediction Objectives Document, Prediction Variables Register, Historical Data Requirements, Model Training and Evaluation Report, Prediction Results (forecasts and risk), and the U3 Predictive Analytics Report.

**Learning outcome:** Estimate future risk, damage and trends from evidence, with clear model evaluation and uncertainty, building on U1 (what is happening) and U2 (why it is happening), in support of U4 (Decision and Action) such as targeted monitoring and timely pest management.

### Module 7: RAG, Local LLM and Agent Basics

**Time:** 8 hours (6 self-study, 2 workshop)

This module introduces the advanced infrastructure that the earlier units deliberately leave out, once learners are ready for it.

- **RAG (Retrieval-Augmented Generation) pipeline:** ingest and chunk, embed (vector), vector database (FAISS), retrieve top-k.
- **Knowledge sources for RAG:** agricultural manuals (PDF or Markdown), research papers (PDF), extension advisories (Markdown or HTML), local practices and SOPs (Markdown), and Agri-tech U0 to U2 results (Markdown).
- **Local LLM** (for example Gemma 4 or Llama), run locally for privacy, offline use and low connectivity.
- **Agentic orchestration:** a Data Agent (prepare and validate), an Analysis Agent (modeling and prediction), a RAG Agent (retrieve domain knowledge), and a Report Agent (interpret and generate the report).
- **Local deployment** in a school, municipal or extension office setting: local LLM, FAISS vector database, and PostgreSQL data storage, running the Agri-tech agents.
- **Execution steps (agentic, RAG and local LLM):** (1) understand the objective; (2) retrieve knowledge through RAG (agronomic practices, research, SOPs); (3) prepare data; (4) train and evaluate the model (regression, classification or time-series); (5) generate predictions with risk, damage, trends and uncertainty; (6) explain with the local LLM, using evidence from retrieved sources; (7) write the report with findings, limitations and next steps.

**Learning outcome:** Explain how RAG, a local LLM and a small set of cooperating agents bring trusted agricultural knowledge into an analytical workflow, and where such a system can be deployed.

### Module 8: Integration, Markdown-driven Workflow and Deployment

**Time:** 7 hours (5 self-study, 2 workshop)

Markdown-driven agentic analytics takes agricultural problem solving from problem to action (U0 to U4). Agricultural experts specify the problem, data, methods and expectations in simple structured files, and the AI agent executes the analysis and generates evidence-based reports, without the experts needing to work with APIs or complex programming.

- **Agri-tech project structure:** `Agri-tech/` holds `U0_Problem_Formulation.md` and one folder per unit (`U1_Descriptive_Analytics/`, `U2_Diagnostic_Analytics/`, `U3_Predictive_Analytics/`), each with its instruction, requirement, method and results files.
- **How the agent performs U2 (worked example):**

| Step | Agent action (Markdown file) | Purpose |
|---|---|---|
| 1 | Read U0_Problem_Formulation.md | Understand the agricultural problem |
| 2 | Read U1_Results.md | Understand what is happening (descriptive evidence) |
| 3 | Read Diagnostic_Questions.md | Understand what needs explanation |
| 4 | Read Potential_Factors.md | Identify possible explanatory factors |
| 5 | Read Data_Requirements.md | Identify available and missing information |
| 6 | Follow Analysis_Methods.md | Select appropriate diagnostic approaches |
| 7 | Generate U2_Diagnostic_Report.md | Present findings, explanations, evidence and uncertainty |

- **U2 files and their purpose:** U2_Instructions.md (what the diagnostic agent must do), Diagnostic_Questions.md (questions to investigate, such as why damage is higher on some farms), Potential_Factors.md (possible factors: environment, crop, pest, management), Data_Requirements.md (for example trap count, temperature, crop stage), Analysis_Methods.md (for example correlation, regression, group analysis), Knowledge_Base.md (fruit fly biology, management guidelines), and U2_Diagnostic_Report.md (factors, evidence, uncertainty, recommendations).
- **Example diagnostic question:** Is fruit damage associated with trap counts? Required analysis: examine the relationship between trap counts and fruit damage, consider correlation analysis, report the correlation coefficient (r) and its significance (p-value), and explain the results and their limitations.

**Standardized Markdown structure across stages**

| Stage | Key question | Main Markdown documents (examples) | Outcome |
|---|---|---|---|
| U0 Problem Formulation | What exactly is the problem? | Problem_Definition.md, Evidence_Register.md | A clear, evidence-based problem statement |
| U1 Descriptive Statistics | What is happening? | U1_Instructions.md, Data_Description.md, U1_Results.md | Current situation, patterns and key summaries |
| U2 Diagnostic Analytics | Why might it be happening? | U2_Instructions.md, Diagnostic_Questions.md, Potential_Factors.md, Data_Requirements.md, Analysis_Methods.md, Knowledge_Base.md, U2_Diagnostic_Report.md | Likely contributing factors, evidence and explanations |
| U3 Predictive Analytics | What might happen in the future? | U3_Objectives.md, Variables.md, Model_Requirements.md, Evaluation.md | Forecasts, risk estimates and scenarios |
| U4 Decision and Action | What should be done? | Decision_Requirements.md, Alternatives.md, Constraints.md, Action_Plan.md | Recommended actions, implementation plan and monitoring |

**Learning outcome:** Design and run an Agri-tech analytical workflow from U0 to U4 using structured Markdown documents, with human checkpoints before each stage's results are accepted.

### Module 9: Capstone and Evaluation

**Time:** 6 hours (2 self-study, 4 workshop)

Learners progress from problem understanding to an evaluated prototype, and are assessed on their ability to improve an agricultural workflow (see Section 7).

**Expected result:** a validated problem brief, a Problem Bank record, an architecture, and a functional learning prototype.

**Learning outcome:** Present an integrated Agentic AI prototype for an agricultural workflow, with its problem brief, requirements, agent design, evaluation and limitations.

## 7. Assessment Strategy

Assessment covers domain understanding, problem formulation, intelligence design and practical implementation.

| Assessment component | Weight |
|---|---|
| Agricultural reality and value chain | 10% |
| Operational workflow mapping | 10% |
| Agri-tech U0 problem formulation | 15% |
| Problem Bank construction | 15% |
| Intelligence requirements | 15% |
| Agent design and architecture | 15% |
| Working prototype and evaluation | 20% |
| **Total** | **100%** |

**Assessment principle:** evaluate the ability to improve an agricultural workflow, not coding alone.

## 8. Expected Course Outputs

By the end of the course, learners should have:

- A validated problem brief.
- A Problem Bank record, as part of a reusable Agricultural Problem Bank.
- Data, analytical and knowledge requirements for their problem.
- An architecture specifying agents, tools, orchestration and human checkpoints.
- A functional, tested learning prototype, with an assessment of its limitations, usability, safety and measurable operational outcomes.
- Along the way: an Agricultural System Understanding Document, an Evidence and Uncertainty Register, and U1 to U3 reports for the chosen problem.

## 9. Items to Confirm

The source slides contain a few inconsistencies and gaps that should be settled before delivery:

- **Unit numbering.** The learning-progression slide numbers Descriptive, Diagnostic and Predictive as Units 2, 3 and 4 (with infrastructure as Unit 1). All later slides use U1 Descriptive, U2 Diagnostic and U3 Predictive, with infrastructure as a separate stage. This document follows the later numbering.
- **U4 Decision and Action.** It is part of the framework and the Markdown structure, but has no stage or hours in the 60-hour allocation and no teaching content of its own.
- **Stage 1 title.** The allocation calls it "Understanding Agriculture/AI", but the slides for this stage cover only agriculture. Decide whether an AI-concepts component belongs here.
- **Correlation value.** The U2 results slides give r = 0.78 for trap count versus damage; one insight slide gives r = 0.72. This document uses 0.78.
- **Placement of RAG and local LLM.** The slides titled "U3 Architecture: RAG-Based, Local LLM System" and "U3 Execution Steps (Agentic + RAG + Local LLM)" are placed in Module 7, because other slides say RAG and local LLM come in a later unit.
- **Problem Bank, intelligence requirements and agent design.** They are assessed and listed as graduate capabilities, but no slides teach them.
- **Datasets.** The U1 to U3 numbers are teaching examples. Real datasets are needed for delivery, in line with the evidence rule in Module 1.
- **Module learning outcomes.** Outcomes for U1, U2 and U3 follow the slides' own outcome statements. Those for Modules 1, 3, 7, 8 and 9 are worded from the slide content.

---

**Document status:** Course specification derived from the Naamii Agritech teaching-strategy deck (56 slides)
**Next step:** Resolve the items in Section 9, then convert each module into session-wise objectives, activities and rubrics.

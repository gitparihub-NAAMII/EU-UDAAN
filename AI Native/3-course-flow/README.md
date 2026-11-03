# Course flow

The three courses are one argument, told through one person. Each course opens on a problem the
previous course's success created.

```
 COURSE 1 · Context Engineering         COURSE 2 · Agentic AI              COURSE 3 · Responsible AI
 ────────────────────────────           ─────────────────────────          ──────────────────────────
 Maya can't get good output       ──▶   Her output is good, so all   ──▶   Her agents never fail, so
                                        the writing lands on her desk      nobody asks if they're right
 Learns to brief the AI                 Learns to hand AI a job            Learns to stand behind it
 Leaves with: a one-page BRIEF          Leaves with: a working agent       Leaves with: an AI policy
                                                                           ── "The loop closes" ──
```

1. **Course 1** teaches Maya to brief AI well. Her output gets good, so everything that needs
   writing lands on her desk.
2. **Course 2** opens: *"You fixed the writing. So why are you MORE tired?"* It teaches delegation
   to agents, and her department becomes the most reliable in the company.
3. **Course 3** opens: *"Everything runs perfectly, so what could go wrong?"* It asks whether what
   the machines do in her name is right, or only error-free. It closes with *"The loop closes"*:
   three courses, three frameworks, one operator.

The same device works inside each course. Course 1, Unit 2 opens with *"Unit 1's lesson
worked… until a Tuesday in monsoon season."*

## The world

**Maya Gurung**, trip coordinator at **Himalayan Getaways**, a mid-sized travel company in
Kathmandu. She is introduced as the reliable one before AI is mentioned at all, and she stays
competent throughout. The failures are structural, never hers.

| Character or object | Role in the story |
|---|---|
| **Ravi Shrestha** | Colleague who gets better results from the same tool (Course 1's opening comparison) |
| **Suresh** | Colleague whose well-built agent fails silently for three weeks (C2 Unit 4) |
| **Sunita** | Customer whose refund question the AI answers with an invented policy (C1 Unit 4) |
| **CodeHimal** | 40-person Kathmandu software firm; the retreat booking that opens the programme |
| **The Thapa family** | The proposal Maya loses when the chat forgets (C1 Unit 5) |
| **Annapurna Base Camp, Poon Hill, Ghandruk** | Treks; a landslide cancellation drives C1 Unit 2 |
| **The Tihar offer** | The Facebook post behind the correction spiral (C1 Unit 3) |

Local setting is structural, not decoration: Kathmandu, Pokhara, monsoon landslides, Tihar,
trekking economics, WhatsApp as the reply channel.

## Inside a course

Each course has five units. Each unit takes one failure and turns it into one or two letters of the
course framework. The framework is never announced: it is revealed in the final unit, when the
learner reads the first letters of the five things they've already learned.

| Course | Unit 1 | Unit 2 | Unit 3 | Unit 4 | Unit 5 |
|---|---|---|---|---|---|
| **BRIEF** | **B** Background | **R** Role · **I** Intent | **E** Examples · **F** Format | **B** grounding | Reveal + reusable brief |
| **AGENT** | **A** Aim | **G** Go-signal | **E** Explicit steps | **N** Nod points · **T** Tools & limits | Reveal + build the agent |
| **TRUST** | Frames all five | **T** Trace | **U** Uncover | **R** Respect | **S** Show · **T** Take + reveal |

Inside each unit, the shape is always the same: *experience the problem → discover each concept
→ put it together.* See [How we built it](../1-how-we-built-it/README.md#the-unit-arc).

## Files

| File | What it is |
|---|---|
| [`course-map.md`](course-map.md) | All 15 units on one page: the learner's complaint, the concept, and the sub-units |
| `../4-courses/*/flow.yaml` | The machine-readable unit order for each course |

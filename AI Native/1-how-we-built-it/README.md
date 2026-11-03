# How we built it

The whole programme follows one rule, and everything else is a consequence of it:

> **Problem first, name it after.** The learner meets a failure before they meet the word for it.

Every unit opens with someone competent doing the sensible thing and it going wrong. The concept
arrives as the answer to a question the learner is already asking.

## The six commitments

1. **The problem comes before the concept.** Never open with a definition.
2. **No jargon until it is earned.** A term is introduced only after the learner has felt the gap it names.
3. **The framework is assembled, never issued.** Five problems produce five letters; the acronym is
   revealed in the last unit as a discovery, not printed in the syllabus.
4. **Everything lives in the slides.** Readable alone, no facilitator, no separate downloads.
5. **Show the artifact, never summarise it.** The failed email in full, both CVs word for word, the
   run log line by line. The learner has to catch it with their own eyes.
6. **One variable at a time.** Every experiment holds everything constant and changes one thing,
   two to four times, so the result reads as a mechanism rather than luck.

## The unit arc

Every unit has the same shape. Each sub-unit has one job, shown as a tag on its first slide.

```
EXPERIENCE THE PROBLEM  →  DISCOVER IT YOURSELF  ×n  →  PUT IT TOGETHER
   live the failure          one concept per cycle       combine, then your turn
```

- **Course-opening units** are lighter, because there is nothing to stack on yet:
  `EXPERIENCE → TRY IT YOURSELF → NAME IT & GENERALISE`
- **Course-closing units** add `THE PAYOFF` (the framework reveal and the reusable tool) and
  `THE WHOLE JOURNEY` (look how far you've come).
- The number of Discover cycles is set by how many concepts the unit carries, not by a target length.

## The 8-step lesson

Inside every `DISCOVER IT YOURSELF` sub-unit:

| # | Step | What it must do |
|---|---|---|
| 1 | **Think first** | An everyday question. AI is not mentioned. The learner commits to an answer. |
| 2 | **Experience** | Live the problem. Nothing labels it as one. |
| 3 | **Look again** | Re-read the failure. The evidence was on the page all along. |
| 4 | **Discover the fix** | A baseline, then *add this → the result changes*, two to four times. |
| 5 | **Name it** | The term arrives now, with the mechanism. |
| 6 | **The intuition** | An ordinary-life analogy that makes it portable. |
| 7 | **Your turn** | Three applications in different contexts. |
| 8 | **Generalise + bridge** | "This works for everything you write", then open the next problem. |

The reference implementation is
[C1 2.1 *The Role*](../4-courses/1-context-engineering-brief/cu-2-when-the-facts-arent-enough/scu-2.1-the-role/artifact.md).

## How a new unit is designed

1. **Name the failure, not the topic.** Write it as the learner's complaint:
   *"It did exactly what I said, and it was a disaster"*, not *"Unit 3: Task Decomposition"*.
2. **Find the trap the previous unit set.** The best failure is caused by the last lesson's success.
3. **Decide the concept cycles.** Each concept the failure implies becomes one Discover sub-unit.
4. **Find the everyday analogy first.** If you can't, the concept isn't understood well enough to teach.
5. **Design the one-variable experiment.** At least one variant should reveal the learner's own default.
6. **Write the naming slide last.**
7. **Build the Put It Together sub-unit.** Maya's combined artifact, its result, the learner's turn.
8. **Write the bridge** into the next problem.

## Documents in this folder

| File | What it is |
|---|---|
| [`build-manual.md`](build-manual.md) | The full build manual. Part I is what was built, Part II the theory, Part III the playbook, Part IV proposals |
| [`authoring-workflow.md`](authoring-workflow.md) | Step-by-step pipeline for adding a unit or sub-unit to this repo, and the checks it must pass |
| [`sources-and-context.md`](sources-and-context.md) | The institution, the source material, and the bibliography |

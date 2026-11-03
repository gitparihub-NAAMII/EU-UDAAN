---
scu: scu.c1.u2.1
tier: 1
pattern: udaan-8-step
status: reference-implementation
---

# The Role

> **DISCOVER IT YOURSELF**

*Build manual §3.1 calls this the reference implementation: "Study this one before writing a new
sub-unit." It is reproduced here as the worked example of the 8-step flow, transcribed from the
build manual rather than from the shipped deck — the deck is authoritative for exact slide copy.*

---

## 1 · Think first

> **FIRST, A QUESTION**

You have a money problem. You could ask a bank officer, a shopkeeper, or your grandmother — same
question.

Would the three answers sound the same? Why not?

*(No AI in the question. That is the rule, not an accident — build manual §3.0 commitment 1.)*

## 2 · Hold your answer

> **REFLECT BEFORE WE GO ON**

Take ten seconds.

Now here's the question that cracks Maya's problem open: when she asked ChatGPT to write the
message, **who did it think it was?**

## 3 · Look again

> **LOOK AGAIN AT MAYA'S MESSAGE**

*(Maya's failed message appears in full. Build manual §3.0 commitment 5: show the artifact, never
summarise it — the learner has to catch it themselves.)*

Read it out loud. It sounds like a lawyer. Or an insurance form. Or a government notice.

## 4 · Discover the fix

> **EXPERIMENT · One line added, everything else identical**

Same facts every time. One line added at the start.

| The line added | What comes back |
|---|---|
| *"You are a warm, caring local trekking guide"* | Warm, human, on your side |
| *"You are a calm operations manager"* | Clear, organised, reassuring |
| *"You are a corporate legal officer"* | Cold, defensive — **(This is the default!)** |
| *"You are an excited travel host"* | Upbeat, persuasive |

Same facts every time. Four completely different messages. The only thing that changed was who you
told it to be.

> **The move that makes this work.** The third experiment doesn't just add a variant — it reveals
> that the learner's original failure *was one of these roles all along*. The default **is** the
> corporate legal officer. That reframing is what turns four examples into an explanation.
> Build manual §3.2 step 5 requires at least one variant do this.

## 5 · Name it

> **NOW WE CAN NAME IT**

This landmark is called the **Role**.

And the mechanism, which arrives with the term and never after it: the AI has read millions of
examples of how a caring guide writes, and millions of how a legal officer writes. When you name
the role, you're pointing it at the right shelf of examples.

*(Note the phrasing. Not what the AI "understands" or "knows" — what it predicts, borrows, points
at. Build manual §3.5, forbidden list.)*

## 6 · The intuition

> **THE INTUITION**

You explain the same problem differently to your boss, your best friend, and a child.

> **THE MENTAL PICTURE**

A brilliant actor who can play anyone, standing on stage with no script, waiting.
*"You are a warm local guide"* is the director's note.

## 7 · Your turn

> **YOUR TURN**

Three situations, each with a suggested role. There's no single right answer.

1. …
2. …
3. …

*(Three applications in different contexts — build manual §3.1 step 7. The exact three are in the
shipped deck.)*

## 8 · Generalise and bridge

> **THE BIGGER PICTURE**

Every time you ask AI to write anything, quietly ask: *who should be saying this?*

Role is landmark number one. But Maya's message still has a problem — it tells people what
happened, but it isn't really trying to achieve anything.

That's the next discovery.

---

## Authoring notes

Kept because this SCU is the pattern reference, not because every SCU needs them.

- **What makes step 4 work** is that everything is held constant. Build manual §3.0 commitment 6:
  one variable at a time. Four variants, not one, because *"one change could be luck; four is a
  mechanism."*
- **The acronym is not named here.** BRIEF is revealed in 5.2. This SCU may teach the letter's
  concept and must not name the word — `kb.framework.brief`, `disclosure_rule`.
- **This experiment is model-dependent.** Build manual §4.6 names re-running the shipped
  experiments per model generation as *"the highest-risk maintenance item in the program: if a
  shipped experiment stops reproducing, the sub-unit built on it silently becomes false."* The
  four-role experiment is one of the two named instances. This is the case for raising it to
  Tier 3 — see `../../../../context/vocabulary-map.md` §3.4.

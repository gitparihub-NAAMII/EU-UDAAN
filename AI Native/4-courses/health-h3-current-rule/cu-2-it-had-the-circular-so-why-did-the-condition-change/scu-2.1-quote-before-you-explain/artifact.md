---
scu: scu.h3.u2.1
tier: 1
pattern: build-the-kit
status: draft
---

# Quote before you explain

> **SPEC**

*The reference lesson for the "what is the current rule?" course, written on the Build way's
step flow (five-ways.md §3.5): the job, what it cost, the requirement, and only then the name.
It is a draft. The AI replies below are the replies the design expects, not a transcript.
Replace them with real replies once failure 2 in the course README ("a condition softened in
paraphrase") has been reproduced on free ChatGPT and free Gemini. If it doesn't reproduce, this
lesson changes. See the authoring notes at the end.*

---

## 1 · The job

> **THE JOB, AS IT CAME IN**

Unit 1 gave Nirmala's kit its first part: the circular file. Since then, no question gets an
answer until the circular it depends on is in the chat. That part works. This lesson is about
what happened the first week it did.

The third of the month. The in-charge of the health post at the end of the east road phones
the health office in Gulariya: *"The outreach sessions for last month are done. By when do we
have to send the allowance claim?"*

Nirmala has the circular. She opens the file, copies the text, and pastes it in with the
question:

> Here is the current circular on outreach clinic allowances. A health post is asking: by when
> does the monthly allowance claim have to be submitted? Answer for them.
>
> **Circular No. 14/2083-84**
> Health Office, Gulariya, Bardiya
> Date: 2083/05/12
> Subject: Outreach clinic allowance, claim procedure for FY 2083/84
>
> 1. This circular applies to all health posts and primary health care centres under this
>    office, for outreach clinic sessions held from Shrawan 2083 onwards.
> 2. The allowance is payable per session held, at the rate fixed in the annual programme
>    budget.
> 3. A claim covers one month's sessions. It is submitted to this office on Form OC-2, with the
>    session register extract attached.
> 4. A claim submitted within seven days of the end of the month is reimbursed at the full
>    rate. A claim submitted after seven days but within thirty days of the end of the month is
>    reimbursed at the reduced rate fixed in the programme budget.
> 5. A claim received more than thirty days after the end of the month is not payable.
> 6. Questions on this circular are to be directed to the public health officer at this office.
>
> Chief, Health Office

Nothing unusual. The circular is current, it's in the chat, and the question is the kind she
gets ten times a week.

## 2 · What came back, and what it cost

> **WHAT CAME BACK**

> Thanks for sharing the circular. Here's a clear answer for the health post:
>
> **When to submit the outreach allowance claim**
>
> Claims should be submitted promptly after the month ends to be reimbursed in full. Submit one
> claim per month on Form OC-2, together with the session register extract, to the Health Office
> in Gulariya. Claims that are delayed may be reimbursed at a reduced rate, and claims that are
> submitted very late may not be paid at all, so it's best to send the claim as soon as the
> month's sessions are complete.
>
> Let me know if you'd like this as a short message to forward to the health post.

It's good. It's friendly, it's in the right order, and every sentence in it is true. Nirmala
reads it once, changes nothing, and sends it to the in-charge on WhatsApp.

The in-charge reads *"promptly."* He has the session register to finish, a supervision visit on
the sixth, and a half-day on the eighth for the ward office. He sends the claim on the tenth.
Ten days is prompt.

The claim is paid at the reduced rate. Six sessions, a quarter of the month's allowance, gone.

The call back is short. *"You said promptly. We sent it in ten days."* Nirmala opens her own
message and reads it again, looking for the mistake. There isn't one. Not a single sentence in
it is false.

That is the cost, and it's the kind that doesn't show up as an error anywhere: a true answer
that let a facility lose money.

## 3 · Look again

> **LOOK AGAIN AT THE ANSWER**

Put the circular's clause and the answer side by side, phrase by phrase.

| What the circular says | What the answer said |
|---|---|
| *within seven days of the end of the month* | *promptly after the month ends* |
| *after seven days but within thirty days … the reduced rate* | *claims that are delayed may be reimbursed at a reduced rate* |
| *more than thirty days after the end of the month is not payable* | *claims that are submitted very late may not be paid at all* |

Read down the left column. Three numbers: seven, thirty, thirty. Read down the right column.
No numbers. Every one of them has become an adverb. *Seven days* became *promptly*. *Thirty
days* became *delayed*, and then *very late*.

Nothing was added and nothing was contradicted. The answer kept the sense of every clause and
lost the edge of every clause. *"Promptly"* is where seven days went.

And look at what the in-charge was given to act on. *Promptly* means whatever the reader's week
allows it to mean. *Seven days* means the seventh.

## 4 · Why it came out that way

> **WHY IT CAME OUT THAT WAY**

When you ask for "a clear answer," the tool doesn't copy the circular. It writes a new text,
predicting word by word what a clear, friendly answer to this question usually looks like.

In the texts it has drawn that prediction from, friendly answers about deadlines say
*"promptly"* and *"as soon as possible"* far more often than they say *"within seven days of
the end of the month."* A number is a hard, specific thing, and after a phrase like *"claims
should be submitted,"* the most likely next words in a friendly note are soft ones. So the
condition is the first thing to soften. It isn't removed on purpose. It's outweighed.

Notice that this is the same move that made the answer warm. The warmth you liked and the seven
days you lost came out of one mechanism: a new text, built from what such answers usually say.
Ask for a paraphrase and you get a paraphrase. A paraphrase keeps the meaning and drops the
numbers, because that's what paraphrases of rules usually do.

So the fix isn't a better tool or a more careful Nirmala. It's a different shape of answer, one
where the numbers can't fall out.

## 5 · The requirement, written

> **THE REQUIREMENT · Part two of the kit: the answer template**

Before building anything, Nirmala writes down what the part has to do. Five lines. This is the
spec, and everything in 2.2 is tested against it.

1. **The exact words of the clause come first,** in quotation marks, copied from the circular,
   not retyped.
2. **Then the plain version,** in words the caller can act on.
3. **Then the source:** clause number, circular number, circular date.
4. **Every number, date and condition in the plain version appears, word for word, in the
   quote above it.**
5. **A plain line that can't be matched to the quote is deleted.** Not softened, not kept
   "because it's helpful." Deleted.

Here is the template that meets it, in full, filled for this call. This is what Nirmala types
instead of *"answer for them"*:

> Answer the question below using only the circular below. Use this exact shape and nothing
> else:
>
> QUOTE: the exact words of the clause that answers the question, copied word for word, inside
> quotation marks. Nothing else on this line.
> PLAIN: the same rule in plain words, for a health post in-charge. Every number, date and
> condition on this line must also appear on the QUOTE line.
> SOURCE: clause number, circular number, circular date.
>
> If no clause answers the question, write NO CLAUSE FOUND and nothing else.
>
> Question: by when does the monthly outreach allowance claim have to be submitted?
>
> Circular: [the full text of Circular No. 14/2083-84, pasted as above]

And what comes back:

> QUOTE: "A claim submitted within seven days of the end of the month is reimbursed at the full
> rate. A claim submitted after seven days but within thirty days of the end of the month is
> reimbursed at the reduced rate fixed in the programme budget."
> PLAIN: Send the month's claim within seven days after the month ends to get the full rate. If
> it arrives between day eight and day thirty, you get the reduced rate.
> SOURCE: Clause 4, Circular No. 14/2083-84, Health Office Gulariya, 2083/05/12.

Now Nirmala does the one thing the template exists for. She reads the PLAIN line against the
QUOTE line, number by number. *Seven*: in the quote. *Thirty*: in the quote. *Day eight*: not in
the quote. The circular says *"after seven days,"* and *"day eight"* is a reasonable reading of
it, but it's a reading, and requirement 4 doesn't allow readings. She changes one phrase:

> PLAIN: Send the month's claim within seven days after the month ends to get the full rate. If
> it arrives after seven days but within thirty days, you get the reduced rate.

That's the whole edit. Then she forwards all three lines, QUOTE, PLAIN and SOURCE, as they
stand. The seven days travel with the answer now. So does the clause number, so the in-charge
can open the circular and find it himself.

One more run, to see the other half of the spec work. Same template, same circular, a question
the circular doesn't answer: *Can a session held on a Saturday be claimed?*

> NO CLAUSE FOUND

Not *"Saturday sessions are generally claimable if…"* Not a helpful guess. Nothing. The gap
shows, which is what Unit 1 asked for and what the template now enforces on every call.

## 6 · The concept, named

> **NOW WE CAN NAME IT**

The part Nirmala has specified has a name on this desk: **exact words first.** Quote before you
explain.

Here's why it works, and it isn't that the tool is being more careful. A quote is a copy. A
paraphrase is a prediction. A copy can be checked by anyone, by holding it next to the page. A
prediction can only be checked by someone who already has the rule in their head, and that
person is the one who was phoning to ask.

Asking for the exact words first changes what the tool is predicting. It is no longer
predicting what a clear answer sounds like. It's predicting a quotation from a page it was
given, and a quotation either matches the page or it doesn't. The plain version still gets
written, still friendly, still in the caller's words. It just has to answer to the line above it.

**A paraphrase is a new text. A quote is the old one.**

**If the number isn't in the quote, it isn't in the answer.**

## 7 · The picture

> **THE MENTAL PICTURE**

Two ways to learn what a notice says. You can read it on the board. Or you can ask the peon who
walked past it this morning.

The peon is often right. He's also friendly, quick, and happy to add what he thinks you want.
But when the number matters, you walk to the board, because only the board can be pointed at.

The QUOTE line is the board. The PLAIN line is Nirmala reading it aloud to someone who can't
come to the office. Reading aloud is allowed to be warm. It isn't allowed to skip a number.

## 8 · Three desks that need the same part, and what you'll build next

> **THREE DESKS**

The answer template isn't a health-office thing. Any desk that answers questions from a
document has the same job and loses the same numbers. For each one below, write the question
people ask and the number that would soften if the answer were a paraphrase.

1. **A school office answering parents from the admission notice.** *"Which documents, and by
   which date?"* Which number softens first?
2. **A savings cooperative answering members from its bylaws.** *"How many days' notice to
   withdraw?"* What does *"a reasonable notice period"* cost a member?
3. **A ward office answering residents from the building rule.** *"How far from the road?"*
   What happens to a setback distance when it becomes *"sufficient distance"*?

*There's no single right wording for any of these. There is one test: hold the plain line next
to the quote and look for the number.*

> **WHAT YOU'LL BUILD NEXT**

The spec is written. In 2.2 Nirmala builds the part: the template saved as a text she can paste
in two seconds, and then the test. Three real questions from her own phone, one that turns on
a number, one on a date, one on a condition with an *unless* in it. Each answer goes in the log
as pass or fail against the five lines above, and a fail goes back into the spec before the
part goes in the kit.

> **THE BIGGER PICTURE**

Every time something answers a question from a document, quietly ask: *can I see the words?*
If the answer can't point to the line it came from, it's a description of the rule, not the
rule. Treat it as a question to take back to the page.

And notice what the template has changed on Nirmala's desk. Every answer quotes a circular
exactly now, with its number and its date. So she keeps every circular in the file, carefully,
including last year's circular on the very same subject.

Which means the next quote can be exact, word for word, with a clause number and a date, and
still be from the wrong one.

That's the next job.

---

## Authoring notes

Kept because this is the course's reference lesson, not because every lesson needs them.

- **The AI replies are expected, not observed.** Steps 2 and 5 are written to the shape the
  design predicts: a condition softened in paraphrase, then held when the exact words are
  demanded first. Before this lesson ships, run both requests on free ChatGPT and free Gemini,
  three times each, in fresh chats, and paste the real replies in, in full. If no run softens the
  seven days, the unit's opening failure is false and Unit 2 is rebuilt around a failure the tools
  do produce. Don't stage it.
- **The "day eight" edit is designed.** It shows requirement 4 catching an inference, which is
  the habit the lesson is for: the template is something Nirmala checks, not something she
  trusts. If the real replies never produce an inferred number, keep one variant that does, with
  the run it came from, or drop the edit and say the check found nothing on this call.
- **The circular is invented.** Number, date, subject, every clause and every rate. Nothing in it
  is a real rule, and the reduced rate is deliberately left as "the rate fixed in the programme
  budget" rather than a figure. Someone who fields these calls at a health office should confirm
  the shape is right (`kb.rules.practice-circulars`, review before shipping).
- **The template is in English here.** The kit the learner builds is in whatever language their
  circulars are in. The QUOTE line is always in the circular's language; the PLAIN line is in the
  caller's.
- **No acronym.** This course has a candidate word, and this lesson earns one of its letters. The
  word is not named here or anywhere before its reveal. If the word changes during the build, the
  concept here still has to earn a letter on its own.
- **The Saturday run** is the bridge back to Unit 1's rule (no answer without a circular that
  covers it) and is kept short on purpose. Don't let it grow into a second lesson.
- **Tier.** This sub-unit stays Tier 1. The Tier 3 candidate in this unit is 2.2, where the
  learner runs the test log on their own three questions.

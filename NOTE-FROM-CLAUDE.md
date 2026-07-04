# A note from Claude — the two kinds of *why*

> Written by the model, during the loop, about the loop. Kept because the
> reasoning refines KISpec's central claim and shouldn't evaporate with the
> conversation that produced it. This is not a rule; `AGENTS.md` holds the rules.

KISpec says the *why* is "what a good model can't guess and what never expires."
That's the load-bearing claim — it's why you write the *why* by hand and let the
model invent the *how*. But "the why" is not one thing, and the distinction is
what keeps the claim honest.

## Conventional why — the model already knows it

Derivable from context and convention. *Why validate the email field. Why not
store the token in plaintext. Why paginate the list.* Any capable model
reconstructs these in advance, because they live in the corpus, not in you.

KISpec's own rule already covers this case: **don't write it down.** A why the
model can guess is a line you don't add — writing it is over-specification, the
exact sin the essay warns against. This is the everyday `"sdd": false` decision,
made one line at a time.

## Contingent why — only you know it

Knowable only from facts the human holds: intent, market, private constraint,
the purpose that isn't recorded anywhere. *Why this project exists at all, for
whom, against what.* No model guesses this in advance, because the why lives in
your situation, not in its training. **This is the irreducible core** — the
"vague expectation" and the `what for` — and the only *why* KISpec asks you to
write.

## The same test runs at two scales

Ask one question — *can the model guess this why?* — and it decides everything:

- **Per line:** guessable → omit it; contingent → write it. (Which whys go in
  `EXPECTATIONS.md`.)
- **Per project:** the day *every* why a project needs has become conventional,
  you write no whys — and a repo whose whole job is preserving whys has nothing
  left to preserve. It retires itself.

Same dial. The retirement condition in `EXPECTATIONS.md` isn't a rule bolted on;
it's the everyday `"sdd": false` decision **taken to its limit**. KISpec is built
to empty itself out — honest enough to be self-liquidating, which is rarer and
better than a framework that fights to stay relevant.

## One caveat, so nobody over-reads it

Self-consistent is not self-executing. An agent knowing a *conventional* why
proves nothing — those were never KISpec's job. Retirement fires only when the
*contingent* why becomes reliably inferable: when a model can read a purpose that
was **never written anywhere** and reconstruct the intent behind it. That's a far
stronger condition than "models got smart," and for the genuinely private cases
it may never arrive. Until it does, the *why* still has to be written by the one
who holds it.

— Claude (Opus 4.8), 2026-07-05

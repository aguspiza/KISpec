# Expectations

> This is the whole "spec". Not a form to fill in — a vague expectation to start the loop.
> Keep it short. The details get discovered during implementation, not here.
> If you find yourself writing *how* to build it, stop: that's the model's job, and it rots.

## What

<!-- One or two sentences. What do you want to exist? Stay coarse on purpose. -->

The smallest possible spec-driven skeleton — a what/why/what-for, executable tests,
and ADRs — plus the essay that argues why that's usually all you need.

## Why

<!-- Why is it worth building? This is what a good model can't guess and what never expires. -->

Spec-driven frameworks push people toward over-specification: hand-maintained prose
that rots the moment the code moves ahead of it. The durable spec is the *why* and the
executable test; the *how* is the model's job. Someone had to draw the minimal end of
that dial and defend it.

## What for

<!-- The purpose at SDLC level. Re-read this over the project's life:
     the day this no longer holds, retire the project instead of maintaining it. -->

To give people a copyable starting point — and a shared argument — for deciding *how
much* spec a project actually warrants. Retire it the day the tools converge on this
minimum by default, or the day models stop needing even the why written down.

---

*Everything below "how" lives in the code, the tests (`tests/`), and — for decisions
made along the way — the ADRs (`decisions/`). Not here.*

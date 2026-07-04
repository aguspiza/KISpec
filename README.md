# KISpec — Keep It Simple, spec

*On Spec-Driven Development, and how much you actually need.*

Just like with overengineering... push it too far and you fall into **over-specification**. All you really need is the "vague" expectation (the **what**, the **why** and the **what for**), the tests to validate that requirement clearly (good old TDD, but at project level — which is the good part SDD, or more specifically Kiro, brings to the table) and, obviously, the loop to refine the result. **KISS.**

On top of that you can layer your own rules for how the work gets done via a `AGENTS.md` to drive/control the process (PRs, report files, even Jira ticket management). But be careful: **every control is a brake on the AI's work.**

I've built — well, I just *ask* 😄 — insanely complex projects starting from a few simple "expectations" of what I want and then refining the result with more "expectations". All that rigidity doesn't add much if the model is good enough (and Fable already has better judgment and more "experience" of how to do the project than you do). Your opinion adds little, except to shorten the loop and get closer to your expectations faster and with fewer tokens; in fact, it often *limits* it, because it stops the model from reaching better solutions.

As always, the devil is in the details, and the details are almost always discovered **during implementation**. This methodology helps you structure the work if you yourself don't quite know what you want, but in the end you realize you almost always set `"sdd": false` because everything's simple enough to solve with a few plain prompts. **YAGNI.**

> *`"sdd"` is the per-feature flag from [harness-sdd](https://github.com/betta-tech/harness-sdd):
> a feature marked `true` in its `feature_list.json` must pass a spec-authoring gate before
> any code. My claim is that most features should be `false` — and this repo is the skeleton
> for the few that shouldn't.*

---

## The nuance: the debate isn't SDD yes/no, it's *how much*

Let's be clear: my own recipe — **vague expectation + tests + loop** — *is already* SDD, just the minimal kind. So the real question was never "spec or no spec?" but **"how much spec?"**. And that amount isn't fixed: it depends on what's at stake.

The spec **earns its keep** when:

- **The cost of being wrong is high and irreversible.** Data migrations, public APIs with consumers hooked onto them, regulated domains. There, "I'll fine-tune it later" gets expensive: there is no cheap loop.
- **The project outlives a single conversation.** When you pick it back up in three months, or someone else (or another agent) takes it over, the spec is the memory that remains. The chat is lost; the context evaporates.
- **There's more than one actor.** There the spec stops being human→AI and becomes the **shared contract** between people and agents. That's not bureaucracy, it's synchronization.

For everything else — which is most of what I do — it's overkill.

## Durable spec vs. ceremony

Not all specs are equal, and here's the trap. **Tests are executable specs**: they persist, they catch regressions, they don't lie. **Prose rots** the moment the implementation moves two steps ahead. That's why I defend project-level TDD and distrust the three ceremonial `.md` files.

The problem was never *specifying*. The problem is specifying in a format that **has to be maintained by hand** and that nobody looks at again.

## The "why" is the only thing that doesn't expire

The devil is in the details and the details are discovered while implementing: true. That's why the **how** of a spec ages terribly, and why writing it up front is usually burning tokens. But the **what** and the **why** — my "vague expectation" — are exactly what **never becomes obsolete** and what a good model, however smart, **cannot guess**.

That's the irreducible core of the spec: keep the why, throw away the how.

(Not every *why* counts the same — the ones a model can guess are the ones you *don't* write. See [`NOTE-FROM-CLAUDE.md`](NOTE-FROM-CLAUDE.md) for the conventional-vs-contingent distinction that keeps this claim honest.)

## The "what for" can retire the whole project

There's a subtlety in that "vague expectation" worth separating out. The **why** justifies *how* the thing is built; the **what for** justifies that the project *exists at all*. That last one isn't a build-time concern — it's an SDLC concern that outlives every line of code.

Because the "what for" is what you re-check over the life of the project, and one day the honest answer is "that purpose no longer exists". The market moved, the upstream system got replaced, the regulation changed, the feature it fed got killed. When that happens the right move isn't to keep maintaining, refactoring or re-speccing it — it's to **retire it**. YAGNI at project scale: the cheapest code is the code you delete because its reason to exist is gone. A spec that never wrote down the "what for" can't tell you when it's time to let the project die.

## Record the decisions made along the way: ADRs

And here's the piece that ties it all together. If the devil is in the details and the details show up **during** implementation, then the decisions that truly matter **weren't in the initial spec**: they're born along the way. "We used this library and not that one", "we chose eventual consistency here", "we ruled out approach X because Y". Each of those is a fork with a why behind it.

That why is exactly what evaporates when the conversation closes. The code tells you *what* was done; it never tells you *what was ruled out or why*. And the "why not" is often more valuable than the "what", because it's what stops someone — you, another person, or an agent — from re-litigating the same debate from scratch six months later, or reintroducing the mistake you already ruled out.

That's why **every relevant decision made along the way should be recorded in an ADR** (Architecture Decision Record) sitting alongside the project's usual documentation. Short, one per decision: context, chosen option, discarded alternatives and the why. No ceremony — they're the incremental log of judgment, not a document you have to keep in sync with the code. An ADR doesn't lie because it never promises to be up to date: it dates a decision and its reasoning, and there it stays.

This is what turns the project into something that **outlives a single conversation**: the initial spec captures the starting what and why; the ADRs capture the why of everything discovered afterwards.

---

## The skeleton

This repo *is* the method. The structure is mostly absence — that's the point:

```
kispec/
├── EXPECTATIONS.md   # the what / why / what for — the "vague expectation"
├── tests/            # the executable spec (project-level TDD)
├── decisions/        # ADRs: the why of everything found along the way
│   ├── template.md
│   └── 0001-....md
├── AGENTS.md         # the single optional control (your project rules)
└── CLAUDE.md         # one line — `@AGENTS.md` — so the rules work in every agent
```

> The rules live in `AGENTS.md` (the cross-tool standard). `CLAUDE.md` just
> imports it with `@AGENTS.md`, so Claude Code, Codex, Cursor and friends all
> read the same file — no duplication. (Trick borrowed from the t3code author.)

What's deliberately **not** here, and why:

- no `design.md` — the *how* is the model's job and ages the fastest; writing it up front is burning tokens.
- no `tasks.md` — a frozen checklist fights the refine-loop; the loop is the task list, and it's alive.
- no formal requirements doc — that lives coarse in `EXPECTATIONS.md` and precise in `tests/`.

That's Kiro / Spec Kit with the dial turned down, and OpenSpec (which already bakes
ADRs into its change proposals) turned down one notch further. If
[harness-sdd](https://github.com/betta-tech/harness-sdd) is the maximal end of that
dial — a spec-authoring gate on every feature — KISpec is the minimal end: the same
dial, the opposite stop. See
[`decisions/0001-keep-the-skeleton-minimal.md`](decisions/0001-keep-the-skeleton-minimal.md)
for the why — an ADR, naturally.

## The rule

> The spec isn't the deliverable, it's scaffolding. Make the scaffold **proportional to the height of the fall**: the more expensive it is to be wrong, or the more people and more time the project has to survive, the more spec. For everything else, `"sdd": false` and a good prompt.

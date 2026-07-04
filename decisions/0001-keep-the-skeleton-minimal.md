# ADR 0001 — Keep the skeleton minimal: no design.md, no tasks.md

- **Date:** 2026-07-04
- **Status:** accepted

## Context

KISpec needed a reference structure people could copy. The obvious move was to
mirror existing spec-driven frameworks (Kiro, GitHub Spec Kit, OpenSpec), which
ship four artifacts: a proposal, specs, a `design.md` (technical approach) and a
`tasks.md` (implementation checklist).

But this repo's whole argument is that the *how* is discovered during
implementation and that a good model doesn't need it dictated up front. A
skeleton that preaches minimalism while carrying the same file count as the
tools it criticizes would contradict itself.

## Decision

Ship the smallest structure that still captures what doesn't expire:

- `EXPECTATIONS.md` — the what / why / what for (the "vague expectation")
- `tests/` — the executable spec (project-level TDD)
- `decisions/` — ADRs for the why of everything found along the way
- `AGENTS.md` — the single optional control (project rules)

## Alternatives discarded

- **Include `design.md`.** Rejected: the technical approach is the *how*. It
  ages the fastest and is exactly what a capable model produces better than a
  pre-written plan. Writing it up front is burning tokens.
- **Include `tasks.md`.** Rejected: a frozen checklist fights the refine-loop.
  The loop *is* the task list, and it's alive, not a stale document to sync.
- **Adopt OpenSpec wholesale.** Rejected as the default, but noted as the sane
  middle ground: it already bakes ADRs into its change proposals. KISpec is the
  same idea with the dial turned further down.

## Consequences

- The repo embodies its own thesis: the structure is mostly *absence*.
- Newcomers from heavier frameworks may miss `design.md`/`tasks.md` — the README
  has to make the omission explicit, or it reads as incompleteness rather than a
  choice. Hence this ADR.

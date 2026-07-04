# AGENTS.md — project rules (the one optional control)

> This is the single "control" KISpec allows: your rules for how the work gets
> done. Keep it short — every rule here is a brake on the AI's work, so add one
> only when its absence actually costs you.

- The spec is `EXPECTATIONS.md`. Read it first. If a request contradicts the
  "what for", say so before building.
- Tests are the spec of record. Add/adjust tests in `tests/` for any behavior
  change, and keep them green.
- When you make a non-obvious decision along the way — a library choice, a
  trade-off, an approach you ruled out — record it as an ADR in `decisions/`
  using `template.md`. Capture the *why not*, not just the what.
- Don't write a `design.md` or a `tasks.md`. The how lives in the code; the plan
  lives in the loop.

# Work Routing

How to decide who handles what.

## Routing Table

| Work Type | Route To | Examples |
|-----------|----------|----------|
| Spec-kit workflow (all of it) | Spec-kit Expert | constitution, specify, clarify (if ambiguous), plan, tasks, implement — owns the whole SDD process |
| Architecture & planning | Planner | Turn a spec into a plan/design, sequencing, load-bearing design decisions |
| Writing code | Implementer | Implement from `tasks.md`, wire up the CLI, make the happy path run |
| Smoke testing | Tester | Quick happy-path smoke test — run it, confirm it works, move on |
| Housekeeping / ops | Admin | File organization, `.gitignore`, README stubs, routine repo chores |
| Code review | Spec-kit Expert / Planner | Check work against spec and plan |
| Scope & priorities | Spec-kit Expert | Owns what's in-scope for the spec; enforces no gold-plating |
| Session logging | Scribe | Automatic — never needs routing |
| RAI review | Rai | Content safety, bias checks, credential detection, ethical review |
| Fact-check / devil's advocate | Fact Checker | Verify claims, challenge assumptions before shipping |

## Spec-Kit Gate (hard rule)

**No work happens outside spec-kit.** The Spec-kit Expert drives the workflow; everyone else follows the artifacts.

- ❌ No planning before a spec exists.
- ❌ No code before `tasks.md` exists.
- ⏭️ `analyze` is always skipped. `clarify` runs only when a spec is genuinely ambiguous.
- ✅ Definition of done: the app runs and the happy path works end-to-end. No gold-plating.

## Issue Routing

| Label | Action | Who |
|-------|--------|-----|
| `squad` | Triage: analyze issue, assign `squad:{member}` label | Spec-kit Expert |
| `squad:{name}` | Pick up issue and complete the work | Named member |

### How Issue Assignment Works

1. When a GitHub issue gets the `squad` label, the **Spec-kit Expert** triages it — analyzing content, assigning the right `squad:{member}` label, and commenting with triage notes.
2. When a `squad:{member}` label is applied, that member picks up the issue in their next session.
3. Members can reassign by removing their label and adding another member's label.
4. The `squad` label is the "inbox" — untriaged issues waiting for Spec-kit Expert review.

## Rules

1. **Eager by default** — spawn all agents who could usefully start work, including anticipatory downstream work.
2. **Scribe always runs** after substantial work, always as `mode: "background"`. Never blocks.
3. **Quick facts → coordinator answers directly.** Don't spawn an agent for "what port does the server run on?"
4. **When two agents could handle it**, pick the one whose domain is the primary concern.
5. **"Team, ..." → fan-out.** Spawn all relevant agents in parallel as `mode: "background"`.
6. **Anticipate downstream work.** If a feature is being built, spawn the tester to write test cases from requirements simultaneously.
7. **Issue-labeled work** — when a `squad:{member}` label is applied to an issue, route to that member. The Spec-kit Expert handles all `squad` (base label) triage.

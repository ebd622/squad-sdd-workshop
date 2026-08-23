# Squad Team

> squad-sdd-workshop

## Project Context

- **Owner:** ebd622
- **Project:** POC speed squad — ships proof-of-concept apps fast. First objective: an interactive Rock-Paper-Scissors CLI app in Python.
- **Stack:** Python (CLI), spec-kit (Spec-Driven Development)
- **Philosophy:** Speed and a working demo over robustness, scale, or polish. **Not production.** Spec-kit is mandatory — no work happens outside it. Definition of done: the app runs and the happy path works end-to-end. No gold-plating.

## Coordinator

| Name | Role | Model | Notes |
|------|------|-------|-------|
| Squad | Coordinator | Claude Haiku 4.5 | Routes work, enforces handoffs, reviewer gates, and the SDD gate. Fast/cheap for lightweight routing. |

## Members

| Name | Role | Charter | Model | Status |
|------|------|---------|-------|--------|
| Spec-kit Expert | SDD Owner | .squad/agents/spec-kit-expert/charter.md | Claude Opus 4.8 | 📐 Active |
| Planner | Architecture | .squad/agents/planner/charter.md | Claude Opus 4.8 | 🏗️ Active |
| Implementer | Coding | .squad/agents/implementer/charter.md | Claude Sonnet 4.6 | 🔧 Active |
| Tester | Smoke Test | .squad/agents/tester/charter.md | Claude Haiku 4.5 | 🧪 Active |
| Admin | Housekeeping | .squad/agents/admin/charter.md | Claude Haiku 4.5 | 🗂️ Active |
| Scribe | Session Logger | .squad/agents/scribe/charter.md | auto | 📋 Silent |
| Ralph | Work Monitor | .squad/agents/ralph/charter.md | auto | 🔄 Monitor |
| Rai | RAI Reviewer | .squad/agents/Rai/charter.md | auto | 🛡️ Background |
| Fact Checker | Fact Checker | .squad/agents/fact-checker/charter.md | auto | 🔍 Verifier |

## Spec-Kit Workflow (Mandatory)

**No work happens outside spec-kit.** The Spec-kit Expert owns and drives the full workflow; the rest of the team follows the artifacts and never skips ahead.

```
constitution → specify → (clarify only if ambiguous) → plan → tasks → implement
```

- `analyze` is **always skipped** (speed over audit).
- `clarify` runs **only when a spec is genuinely ambiguous**.
- **SDD gates:** no planning before specs exist; no code before tasks exist.

## Coding Agent

<!-- copilot-auto-assign: false -->

| Name | Role | Charter | Status |
|------|------|---------|--------|
| @copilot | Coding Agent | — | 🤖 Coding Agent |

### Capabilities

**🟢 Good fit — auto-route when enabled:**
- Bug fixes with clear reproduction steps
- Test coverage (adding missing tests, fixing flaky tests)
- Lint/format fixes and code style cleanup
- Dependency updates and version bumps
- Small isolated features with clear specs
- Boilerplate/scaffolding generation
- Documentation fixes and README updates

**🟡 Needs review — route to @copilot but flag for squad member PR review:**
- Medium features with clear specs and acceptance criteria
- Refactoring with existing test coverage
- API endpoint additions following established patterns
- Migration scripts with well-defined schemas

**🔴 Not suitable — route to squad member instead:**
- Architecture decisions and system design
- Multi-system integration requiring coordination
- Ambiguous requirements needing clarification
- Security-critical changes (auth, encryption, access control)
- Performance-critical paths requiring benchmarking
- Changes requiring cross-team discussion

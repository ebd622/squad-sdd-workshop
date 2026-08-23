# Squad Decisions

## Active Decisions

### 2026-08-23T12:26:53+02:00: POC speed squad — founding charter

**By:** ebd622 (via Squad Coordinator, Init Mode)

**What:** This squad is optimized for shipping proof-of-concept apps FAST. It does **not** build for production. Priorities: speed and a working demo over robustness, scale, or polish.

**Rules the whole team follows:**
1. **Spec-kit is mandatory — no work happens outside it.** The Spec-kit Expert owns and drives the full SDD workflow: `constitution → specify → plan → tasks → implement`.
2. `clarify` runs **only when a spec is genuinely ambiguous**. `analyze` is **always skipped**.
3. **SDD gates:** no planning before specs exist; no code before tasks exist. The rest of the team follows the Spec-kit Expert's artifacts and never skips ahead.
4. **Definition of done:** the app runs and the happy path works end-to-end. **No gold-plating.**
5. **Tester** runs **only a quick happy-path smoke test** — no edge cases, no coverage chasing. Verify it works, then move to the next build.
6. **Be FAST** in writing both spec and code.

**Models (pinned):**
- Spec-kit Expert → Claude Opus 4.8 (deep reasoning where mistakes cost most)
- Planner → Claude Opus 4.8 (architecture, high-stakes decisions)
- Implementer → Claude Sonnet 4.6 (strong coding + speed/cost for high-volume work)
- Tester → Claude Haiku 4.5 (fast/cheap, lightweight smoke test)
- Admin → Claude Haiku 4.5 (fast/cheap, routine tasks)
- Coordinator → Claude Haiku 4.5 (fast/cheap, lightweight routing)

**Why:** User's explicit brief when founding the team.

**First objective:** Build an interactive Rock-Paper-Scissors CLI app in Python, via the spec-kit workflow.

### 2026-08-23T12:52:08+02:00: Rock-Paper-Scissors CLI shipped via Spec Kit

**By:** Spec-kit Expert (SDD Owner)

**What:** Drove the full Spec Kit workflow (constitution → specify → plan → tasks → implement) to build an interactive Rock-Paper-Scissors CLI. `clarify` and `analyze` were skipped (spec unambiguous; team policy skips analyze).

**Key choices (POC speed):**
- **Single file** `rps.py` at repo root — no package, no modules, no tests directory.
- **Standard library only** (`random`, `sys`); runnable via `python rps.py`.
- Human vs. computer (random). Accepts `rock/paper/scissors` and `r/p/s`, case-insensitive.
- Loop until `quit`/`q`; graceful exit also on EOF (Ctrl-D) and Ctrl-C. Running score shown.
- Invalid input reprompts without counting a round.

**Artifacts:**
- Constitution: `.specify/memory/constitution.md` (v1.0.0)
- Spec: `specs/001-rock-paper-scissors-cli/spec.md`
- Plan + design: `plan.md`, `research.md`, `data-model.md`, `contracts/cli.md`, `quickstart.md`
- Tasks: `specs/001-rock-paper-scissors-cli/tasks.md` (9 tasks, all done)
- App: `rps.py`

**Run:** `python rps.py` (smoke test: `printf 'rock\nquit\n' | python rps.py`)

**Implications for others:** Any follow-on work must go through Spec Kit (SDD gate). Keep it lean; this is a POC.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction

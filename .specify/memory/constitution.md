<!--
Sync Impact Report
- Version change: (template) → 1.0.0
- Ratification: initial adoption of project constitution
- Modified principles: none (initial authoring; all placeholders replaced)
- Added sections:
  - Core Principles: I. POC Speed First, II. Spec-First & Phase-Gated,
    III. Happy-Path Definition of Done, IV. No Gold-Plating
  - Delivery Constraints
  - Development Workflow
  - Governance
- Removed sections: none (template placeholders fully replaced)
- Follow-up TODOs: none
-->

# Squad POC Constitution

## Core Principles

### I. POC Speed First

Every decision optimizes for a fast, working demo over robustness, scale, or polish. We build
proof-of-concept apps to prove an idea end-to-end, not production systems. When a choice trades
speed for hardening the team does not strictly need, speed MUST win. Rationale: the team's mission
is to ship POCs quickly; premature engineering is the primary risk to that mission.

### II. Spec-First & Phase-Gated (NON-NEGOTIABLE)

No work happens outside the Spec Kit workflow. Phases run in strict order —
constitution → specify → plan → tasks → implement — and each phase gates the next: no plan before a
spec exists, no tasks before a plan exists, no code before tasks exist. `clarify` runs ONLY when a
spec is genuinely ambiguous; `analyze` is ALWAYS skipped. Rationale: mistakes at the spec/plan stage
are the most expensive downstream, so the artifacts are the single source of truth everyone follows.

### III. Happy-Path Definition of Done

A build is done when the app runs and the happy path works end-to-end. Testing is a single quick
happy-path smoke test — no edge-case matrices, no coverage targets. Rationale: for a POC, a working
demonstrated path is the proof we need; anything beyond it is effort spent past the point of value.

### IV. No Gold-Plating

If a requirement does not serve the happy-path demo, it is cut before it reaches implementation.
No speculative features, no configurability "for later", no persistence/networking/scaling work
unless the demo itself requires it. Every artifact — spec, plan, tasks — MUST stay as lean as the
POC needs. Rationale: scope creep is the enemy of speed; trimming ruthlessly keeps builds shippable.

## Delivery Constraints

- Prefer the simplest runnable form: a single-file app run with the language's native toolchain.
- Do NOT introduce build tools, frameworks, or dependencies unless they are essential to compile or
  run the app.
- No persistence, networking, or multi-module structure unless the feature explicitly requires it.
- Standard library / built-in runtime only wherever feasible.

## Development Workflow

- Sloth (Spec-kit Expert) owns and drives constitution → specify → plan → tasks, and gatekeeps the
  phase order.
- The Implementer writes code only against an approved tasks list; the Tester runs only the
  happy-path smoke test, then moves on.
- Team decisions live in `.squad/decisions.md`; meaningful changes require team consensus.
- Reviews, when they happen, check work against the spec and tasks — rejections go back to the
  original author with specific, artifact-tied notes.

## Governance

This constitution supersedes ad-hoc practices for all POC builds. Amendments require team consensus,
a recorded rationale in `.squad/decisions.md`, and a version bump per the policy below.

Versioning policy (semantic):
- MAJOR: backward-incompatible governance or principle removals/redefinitions.
- MINOR: a new principle/section or materially expanded guidance.
- PATCH: clarifications, wording, and non-semantic refinements.

Compliance: every spec, plan, and tasks artifact MUST be checkable against these principles.
Complexity or hardening beyond the happy path MUST be justified against Principle IV or cut.

**Version**: 1.0.0 | **Ratified**: 2026-08-23 | **Last Amended**: 2026-08-23

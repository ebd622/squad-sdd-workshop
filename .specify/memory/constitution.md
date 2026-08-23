<!--
Sync Impact Report
- Version change: (template) → 1.0.0
- Ratification: initial adoption
- Modified principles: template placeholders → concrete POC-speed principles
  - [PRINCIPLE_1_NAME] → I. Speed Over Polish
  - [PRINCIPLE_2_NAME] → II. Happy Path Is Done
  - [PRINCIPLE_3_NAME] → III. Standard Library Only
  - [PRINCIPLE_4_NAME] → IV. Spec-Driven Development Gate
- Added sections: Technology Constraints; Development Workflow
- Removed sections: none (5th template principle folded into IV — POC needs 4)
- Deferred TODOs: none
-->

# Rock-Paper-Scissors POC Constitution

## Core Principles

### I. Speed Over Polish
Optimize for a working demo, not production. Ship the shortest path to a runnable app.
No scale, robustness hardening, config systems, packaging, or abstractions the happy
path does not need. Rationale: this is a POC speed squad — time-to-demo is the metric.

### II. Happy Path Is Done
Definition of done: the app runs and the happy path works end-to-end. Do not gold-plate
with extra features, exhaustive error handling, or edge-case coverage beyond graceful
quit. Rationale: a demonstrable happy path is the entire deliverable.

### III. Standard Library Only
Pure Python 3, standard library only. No pip installs, no external dependencies. The
entry point MUST be runnable with `python <file>.py`. Rationale: zero-setup runs on any
machine keep the demo friction-free.

### IV. Spec-Driven Development Gate (NON-NEGOTIABLE)
All work happens inside the spec-kit workflow in strict order: constitution → specify →
plan → tasks → implement. No planning before a spec exists; no code before tasks exist.
`clarify` runs only when a spec is genuinely ambiguous; `analyze` is always skipped.
Rationale: the spec is the source of truth and prevents rework.

## Technology Constraints

- Language: Python 3 (standard library only).
- Interface: interactive command-line app.
- Distribution: a single runnable file or a tiny module; no packaging.

## Development Workflow

- Artifacts are produced by spec-kit and kept lean — the minimum to unblock the next step.
- Implementation must satisfy the spec's happy path and be verified by running the app
  (input may be piped for non-interactive verification).

## Governance

This constitution supersedes ad-hoc practices for this POC. Amendments are made by
updating this file with a version bump. Versioning: MAJOR for principle
removals/redefinitions, MINOR for added principles/sections, PATCH for clarifications.
Compliance is verified by confirming the app runs and the SDD gate order was followed.

**Version**: 1.0.0 | **Ratified**: 2026-08-23 | **Last Amended**: 2026-08-23

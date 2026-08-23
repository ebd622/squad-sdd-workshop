# Squad Team

> squad-sdd-workshop

## Coordinator

| Name | Role | Model | Notes |
|------|------|-------|-------|
| Squad | Coordinator | Claude Haiku 4.5 | Routes work, enforces handoffs and reviewer gates. Fast/cheap model for routine dispatch. |

## Members

| Name | Role | Model | Charter | Status |
|------|------|-------|---------|--------|
| Sloth | Spec-kit Expert | Claude Opus 4.8 | `.squad/agents/sloth/charter.md` | active |
| Data | Implementer | Claude Sonnet 4.6 | `.squad/agents/data/charter.md` | active |
| Mouth | Tester | Claude Haiku 4.5 | `.squad/agents/mouth/charter.md` | active |
| Scribe | Session logger & memory | — | `.squad/agents/scribe/charter.md` | active |
| Ralph | Work monitor | — | `.squad/agents/ralph/charter.md` | active |
| Rai | Responsible-AI reviewer | — | `.squad/agents/Rai/charter.md` | active |
| Fact Checker | Devil's advocate / verifier | — | `.squad/agents/fact-checker/charter.md` | active |

## Team Charter

- **Mission:** Ship proof-of-concept apps fast. Not building for production — prioritize speed and a working demo over robustness, scale, or polish.
- **Process:** Spec Kit is mandatory; no work happens outside it. Sloth (spec-kit expert) drives constitution → specify → (clarify only if genuinely ambiguous) → plan → tasks → implement. `analyze` is always skipped. No planning before specs exist, no code before tasks exist.
- **Definition of done:** The app runs and the happy path works end-to-end. No gold-plating.
- **Testing policy:** Mouth (tester) runs one quick happy-path smoke test only — no edge cases, no coverage chasing.

## Project Context

- **Project:** squad-sdd-workshop
- **First objective:** Interactive Rock-Paper-Scissors CLI app in Java
- **Created:** 2026-08-23

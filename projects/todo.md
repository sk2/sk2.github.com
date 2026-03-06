---
layout: default
section: projects
---

# Rust TUI GTD Todo (OmniFocus-inspired)

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Keyboard-driven Rust TUI task manager built around a GTD workflow. Stores tasks in a local SQLite database with support for projects, hierarchical tags, and availability-based next-action computation. Optimized for rapid inbox processing — single-key field mode for triage, project/tag assignment, and batch operations with sub-second interactions at 10,000+ actions.

Includes a one-time importer for OmniFocus 4 `.ofocus-package` files, mapping projects, folders, tasks, tags, notes, and dates into the local database.

---

## Features

- GTD views: Inbox, Projects, Tags/Contexts, Next, Waiting, Someday/Maybe, Review
- Single-key field mode for fast inbox triage with overlay selectors
- Hierarchical tags with descendant-inclusive filtering
- Next actions computed from availability rules (active, not completed, defer date, not blocked)
- Per-project review intervals with review screen
- OmniFocus 4 one-time import (read-only, `.ofocus-package`)
- Architecture hooks for future local-only, opt-in LLM processing suggestions

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust |

---

## What This Is

A fast, keyboard-driven Rust text UI (TUI) task manager inspired by OmniFocus, built around a GTD workflow. It stores data in an owned SQLite database, supports projects and hierarchical contexts/tags, and is optimized for rapid inbox processing (triage + tagging) with minimal friction.

An OmniFocus 4 `.ofocus-package` importer provides one-time migration into the local database so the tool can replace OmniFocus for day-to-day use.

---

## Core Value

Process an inbox full of captures into correctly-organized next actions (project + tags + defer/due) at high speed, with sub-second interactions.

---

## Requirements

---

## # Validated

(None yet  ship to validate)

---

## # Active

- [ ] Keyboard-first TUI with OmniFocus-like navigation: Inbox, Projects, Tags/Contexts, Next, Waiting, Someday/Maybe, Review
- [ ] Fast inbox processing sprint: single-key field mode with overlays for project/tag/date assignment and batch operations
- [ ] Owned SQLite data model supporting projects + actions + hierarchical tags, with filtering that includes descendants by default
- [ ] Next actions computed via availability rules (active + not completed + defer<=today + not blocked), with performant list queries
- [ ] OmniFocus 4 one-time import from `.ofocus-package` mapping projects/folders, tasks, tags, notes, and core dates into SQLite
- [ ] Per-project review interval and review screen showing projects due for review
- [ ] Foundation for future local-only, opt-in LLM suggestions (initial target: inbox processing suggestions)
- [ ] Claude Code integration for batch inbox processing: export inbox items, auto-suggest projects/tags/contexts with confidence levels, thematic grouping, and batch acceptance UI

---

## # Out of Scope

- Ongoing sync with OmniFocus  one-time import only for v1
- Web/mobile UI  terminal-only for v1
- LLM features shipping in v1  only architecture hooks and data needed for later

---

## Context

- Motivation: OmniFocus is powerful but painful to work with; the goal is a replacement that keeps the familiar mental model while prioritizing speed and ergonomics.
- Platform: macOS-only initially.
- Scale expectation: up to ~10k actions.
- UX emphasis: vim-like keyboard navigation; single-key field mode for triage; tag selection must be extremely fast.

---

## Constraints

- **Performance**: Sub-second UI response; queries and filtering must remain snappy at ~10k actions.
- **Tech stack**: Rust TUI application with SQLite persistence.
- **Import**: OmniFocus 4 `.ofocus-package` supported; importer is read-only and one-time.
- **Privacy**: Future LLM integration must be local-only and opt-in by default.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| GTD-first with OmniFocus feel | Own the workflow + speed while keeping familiar lists/navigation; import lands cleanly |  Pending |
| Single-key field mode for inbox triage | Optimize the highest-leverage moment (processing sprint) |  Pending |
| Projects contain actions | Matches GTD/OmniFocus model and keeps project views coherent |  Pending |
| Hierarchical tags with descendant-inclusive filtering | Organize contexts while keeping filtering powerful and fast |  Pending |
| Next actions computed from availability flags/dates | Avoid manual next-action bookkeeping; keep lists actionable |  Pending |
| One-time OmniFocus import | Avoid complexity of sync; focus on primary UX |  Pending |
| Per-project review interval | Supports weekly review without forcing one cadence |  Pending |
| LLM posture: local-only, opt-in; first use-case = processing suggestions | Preserve privacy while enabling future assistance |  Pending |

*Last updated: 2026-02-20 after initialization*

---

## Current Status

2026-02-25 - Completed 13-01-PLAN.md

---

[← Back to Projects](/projects)

---
layout: default
section: data-analytics
---

# Rust TUI Task Manager

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

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

[← Back to Data Analytics](../data-analytics)

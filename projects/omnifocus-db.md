---
layout: default
section: projects
---

# OmniFocus DB CLI

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-02-16</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Stated Constraints](#stated-constraints)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-16 |

---

## Concept

A Python CLI that reads directly from the OmniFocus SQLite database on macOS, bypassing AppleScript/TypeScript layers. Provides structured, token-efficient data (JSON/Text) for project listing, inbox analysis, and context gathering.

- **Near-instant retrieval** of projects and tasks without the overhead of the OmniFocus app or AppleScript.
- **Agent-optimized:** dense, low-token representations of the user's task list.
- **Read-only access** by default to prevent database corruption while OmniFocus is active.

---

## Stated Constraints

- **Platform:** macOS (Darwin) only.
- **Target App:** OmniFocus 4 (Direct Version).
- **Language:** Python (for ease of development and robust SQLite/Agent library support).
- **Access:** Direct SQLite reading (bypassing Official APIs).

---

## Requirements



---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] **Discovery:** Locate and verify the OmniFocus 4 SQLite database path for the Direct version.
- [ ] **Schema Mapping:** Identify the key tables and relations for Projects, Inbox, Tasks, and Tags.
- [ ] **Read-Only CLI:** Implement a Python CLI that outputs project lists and inbox items in a token-efficient format.
- [ ] **Safety Check:** Implement a check to detect if OmniFocus has an active write lock on the DB.
- [ ] **MCP Integration:** Provide an entry point for use as a Model Context Protocol (MCP) server.

---

## # Out of Scope

- **Write Operations (v1):** Direct DB writing is deferred to ensure stability; triage will be advisory in v1.
- **Legacy Support:** No support for OmniFocus 2 or 3 unless the schema is identical.
- **UI/GUI:** This is a headless CLI/API tool only.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Python | Faster iteration than Rust for DB schema discovery and easier integration with existing agent toolchains. | — Pending |
| Read-Only | Direct writes to an active SQLite DB managed by a complex app like OmniFocus risk corruption. | — Pending |
| Direct Version | User explicitly mentioned using the non-App Store version. | — Pending |

*Last updated: 2026-02-13 after initialization*

---

## Current Status

** 2026-02-16 - Closed out phase 7 (summaries, state update)

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

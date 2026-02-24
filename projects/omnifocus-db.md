---
layout: default
section: projects
---

# OmniFocus DB CLI (omnifocus-db)

<span class="status-badge status-active">Last Active: 2026-02-16</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Use Cases](#use-cases)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)

## Concept

### What This Is

A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.

### Core Value

- **Zero-Latency Context:** Near-instant retrieval of projects and tasks without the overhead of the OmniFocus app or AppleScript.
- **Agent-Optimized:** Focused on providing dense, low-token representations of the user's task list.
- **Safety First:** Read-only access by default to prevent database corruption while OmniFocus is active.

---

## Use Cases

**AI Agent Context:**
```bash
$ omnifocus-db inbox --format json
{
  "inbox_count": 3,
  "items": [
    {"id": "abc123", "name": "Review PR #456", "added": "2026-02-13T10:30:00Z"},
    {"id": "def456", "name": "Book dentist appointment", "added": "2026-02-13T09:15:00Z"},
    {"id": "ghi789", "name": "Research Rust async patterns", "added": "2026-02-12T14:20:00Z"}
  ]
}
```

**Fast Project Overview:**
```bash
$ omnifocus-db projects --active --format compact
• Work (5 active)
  - Q1 Product Launch (3 tasks)
  - Documentation Update (2 tasks)
• Personal (2 active)
  - Home Renovation Planning (2 tasks)
```

**Agent Triaging:**
```
User: "What's urgent in my OmniFocus?"
Agent: [omnifocus-db query in 5ms]
Agent: "You have 3 flagged items due today: PR review, dentist appointment, and team standup prep."
```

---

## Architecture





```
┌────────────────────────────────┐
│    OmniFocus 4 Application     │
│         (Running)              │
└────────┬───────────────────────┘
         │ Manages
         ↓
┌────────────────────────────────┐
│   OmniFocus.sqlite Database    │
│    ~/Library/Group Containers/ │
└────────┬───────────────────────┘
```


```
         │ Direct Read
         ↓
┌────────────────────────────────┐
│    omnifocus-db CLI            │
│    (Python + SQLite)           │
└────────┬───────────────────────┘
         │
    ┌────┼────┬─────────┐
    │    │    │         │
┌───▼──┐ │ ┌──▼───┐ ┌──▼────┐
```



```
│ CLI  │ │ │ MCP  │ │Future │
│      │ │ │Server│ │ Web   │
└──────┘ │ └──────┘ └───────┘
         │
    ┌────▼─────┐
    │  Agents  │
    │(Claude)  │
    └──────────┘
```

---

## Tech Stack

- **Language**: Python (fast iteration, robust SQLite support)
- **Database**: Direct SQLite3 access
- **Platform**: macOS (OmniFocus 4 Direct Version)
- **Output**: JSON, compact text, or MCP protocol
- **Safety**: Read-only, lock detection

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

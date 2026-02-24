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
- [Integration with Agents](#integration-with-agents)
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Key Features](#key-features)
- [Requirements](#requirements)

## Concept

A Python-based CLI that bypasses slow AppleScript/TypeScript layers to read directly from the OmniFocus SQLite database on macOS. It provides structured, token-efficient data (JSON/Text) to agents for lightning-fast project listing, inbox analysis, and context gathering.

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

## Integration with Agents

**Direct MCP Server:**
```python
from mcp import use_tool

inbox = use_tool("omnifocus_db", action="inbox")
```

**Claude Desktop Integration:**
- Add to `claude_desktop_config.json` MCP servers
- Instant OmniFocus context in every conversation
- "What should I work on next?" answered from live database

---

## The Problem

**Traditional OmniFocus Access:**
- AppleScript: 500-2000ms per query
- OmniFocus app API: Requires app launch, 300-1000ms
- Web/Sync API: Network latency, authentication overhead

**For AI Agents:**
- Need instant context: "What's in my inbox?"
- Token efficiency matters: Raw OmniFocus XML is verbose
- Real-time triaging: Can't wait seconds for each query

---

## The Solution

**Direct SQLite Access:**
```
Traditional Path:          Direct DB Path:
Agent → AppleScript        Agent → SQLite
  ↓ 1000ms                   ↓ 5ms
OmniFocus App →            JSON Output
  ↓ 500ms
XML/Text Output
```

**Performance Improvement:** ~200x faster for typical queries

---

## Key Features

### Lightning-Fast Queries
- **Project Listing**: < 10ms for complete project hierarchy
- **Inbox Analysis**: < 5ms for all inbox items
- **Task Search**: Direct SQL queries on indexed fields

### Agent-Optimized Output
- **JSON Format**: Structured, parseable task data
- **Token Efficiency**: Minimal overhead, dense information
- **Context Selection**: Configurable depth (inbox only, active projects, complete hierarchy)

### Safety Mechanisms
- **Read-Only by Default**: No write operations in v1
- **Lock Detection**: Check for OmniFocus write locks before reading
- **Backup Validation**: Verify database integrity before access

### MCP Integration
- **Model Context Protocol Server**: Direct integration with Claude and other LLM tools
- **Streaming Context**: Real-time task list updates in agent conversations

---

## Requirements

**Active:**
- Discover and verify OmniFocus 4 SQLite database path
- Map database schema (Projects, Inbox, Tasks, Tags tables)
- Implement read-only CLI with token-efficient output
- Add safety checks for active write locks
- Provide MCP server integration

**Out of Scope (v1):**
- **Write Operations**: Deferred to ensure stability; triaging is advisory only
- **Legacy Support**: No OmniFocus 2 or 3 support
- **UI/GUI**: Headless CLI/API tool only

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

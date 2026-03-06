---
layout: default
section: data-analytics
---

# OmniFocus DB CLI

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Concept

Python CLI that reads directly from the OmniFocus 4 SQLite database on macOS, bypassing AppleScript and Omni Automation layers. Provides near-instant retrieval of projects, inbox items, and tasks in structured, token-efficient formats (JSON/text) for agent consumption. Read-only access by default to prevent database corruption while OmniFocus is active.

---

## Features

- Direct SQLite access to OmniFocus 4 database (macOS only)
- Dense, low-token output for LLM agent integration
- MCP server entry point for Model Context Protocol workflows
- Write-lock detection to avoid conflicts with the running application

---

[← Back to Data Analytics](../data-analytics)

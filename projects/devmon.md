---
layout: default
section: data-analytics
---

# GSD Project Monitor

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

---

## Concept

TUI dashboard that scans multiple development directories for projects with `.planning` structures, tracking health and progress across workspaces. Detects recent activity from state files, git commits, and source changes, then visualizes each project's pipeline stage (discuss, research, planning, ready, active, done). Highlights at-risk projects — those marked active with no ready plans in the queue.

---

## Features

- Multi-workspace scanning with automatic project discovery
- Activity detection from state files, git history, and file modification times
- Pipeline stage visualization with phase progression tracking
- At-risk alerting for active projects with empty plan queues
- TOML-based configuration for workspace paths and settings

---

[← Back to Data Analytics](/data-analytics)

[← Back to Projects](/projects)

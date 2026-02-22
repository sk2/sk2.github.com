---
layout: default
---

# GSD Project Monitor

<span class="status-badge status-active">Stable</span>

[← Back to Projects](../projects)

---

## The Insight

Developing...

## Quick Facts

| | |
|---|---|
| **Status** | Stable |
| **Language** | Python |
| **Started** | 2026 |

---
## Features

### Multi-Workspace Scanning
Scans multiple development directories for GSD projects, identifying those with a `.planning` structure. It tracks project health across different environments without requiring manual registration.

### Smart Activity Detection
Intelligently detects recent activity by checking `STATE.md` updates, git commits, and scanning source directories for recent changes. This ensures the "Last Activity" status is accurate even before code is committed.

### Phase Pipeline Tracking
Visualizes the progress of projects through the GSD pipeline:
- **Discuss**: Needs initial context.
- **Research**: Needs domain investigation.
- **Planning**: Needs task breakdown.
- **Ready**: Planned and ready to execute.
- **Active**: Currently in progress.
- **Done**: Completed.

### At-Risk Alerting
Automatically highlights projects that are "Active" but have zero "Ready" plans. This serves as a leading indicator that a project's pipeline is running dry and requires planning attention.

---

## Architecture

**Language**: Python 3.10+
**UI Framework**: `ratatui` / `textual` for the TUI dashboard
**Scanning**: Integrated `ripgrep` support for high-performance file discovery
**Configuration**: TOML-based project and workspace configuration

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

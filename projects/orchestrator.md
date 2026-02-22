---
layout: default
---

# Orchestrator (Device Interaction Runner)

<span class="status-badge status-active">Phase 1/5 (0%)</span>

[← Back to Projects](../projects)

---

## The Insight

Run the same device workflow reliably across lab/real targets, with deterministic execution semantics and replayable artifacts.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 1/5 (0%) |
| **Language** | N/A |
| **Started** | 2026 |

---
## What This Is

An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives. The orchestrator owns run coordination, persistence, and event streaming.

This is inspired by Tower/AWX-style job execution, but it is purpose-built for our use case: reliable, replayable device runs with clean integration boundaries and a clear path to future expansion (including broader workflow graphs) without making AI a dependency.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

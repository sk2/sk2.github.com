---
layout: default
section: network-automation
---

# Orchestrator (Device Interaction Runner)

<span class="status-badge status-updated">Recently Updated</span>



[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives. The orchestrator owns run coordination, persistence, and event streaming.

This is inspired by Tower/AWX-style job execution, but it is purpose-built for our use case: reliable, replayable device runs with clean integration boundaries and a clear path to future expansion (including broader workflow graphs) without making AI a dependency.

---

## What This Is

An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

v1 is explicitly **device-focused** and **uses `deviceinteraction` as a library** for transports/parsing/test primitives. The orchestrator owns run coordination, persistence, and event streaming.

This is inspired by Tower/AWX-style job execution, but it is purpose-built for our use case: reliable, replayable device runs with clean integration boundaries and a clear path to future expansion (including broader workflow graphs) without making AI a dependency.

---

## Core Value

Run the same device workflow reliably across lab/real targets, with deterministic execution semantics and replayable artifacts.

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

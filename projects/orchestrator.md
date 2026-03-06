---
layout: default
section: network-automation
---

# Device Interaction Runner

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Concept

Orchestration engine for coordinating device interactions across real and testbed networks. Executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots). Uses [Device Interaction Framework](../deviceinteraction) as a library for transports, parsing, and test primitives — the orchestrator owns run coordination, persistence, and event streaming.

Inspired by Tower/AWX-style job execution, but purpose-built for reliable, replayable device runs with clean integration boundaries.

---

## Architecture

The runner exposes an HTTP API as a headless execution engine. Clients (Network Automation Workbench, CLI, CI pipelines) submit device workflows as declarative YAML. The engine handles:

- **Bounded concurrency**: configurable parallelism across device targets
- **Retry semantics**: exponential backoff with configurable limits
- **Timeouts and cancellation**: per-step and per-run deadlines
- **Durable artifacts**: structured logs, command outputs, and device snapshots persisted per run

---

## Features

- API-first design — multiple clients share the same execution engine
- Declarative YAML workflow definitions
- Structured event streaming for real-time run monitoring
- Integration with the broader network automation ecosystem

---

[← Back to Network Automation](../network-automation)

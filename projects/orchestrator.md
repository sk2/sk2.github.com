---
layout: default
section: network-automation
---

# Orchestrator (Device Interaction Runner)

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Features](#features)
- [Current Status](#current-status)

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

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Python |

---

## What This Is

An orchestration runner for coordinating **device interactions** across real/testbed networks. It executes runs with retries, timeouts, bounded concurrency, and durable artifacts (logs, results, snapshots) that plug into the broader automation ecosystem.

v1 is explicitly **device-focused** and **uses `[deviceinteraction](../deviceinteraction)` as a library** for transports/parsing/test primitives. The orchestrator owns run coordination, persistence, and event streaming.

This is inspired by Tower/AWX-style job execution, but it is purpose-built for our use case: reliable, replayable device runs with clean integration boundaries and a clear path to future expansion (including broader workflow graphs) without making AI a dependency.

---

## Core Value

Run the same device workflow reliably across lab/real targets, with deterministic execution semantics and replayable artifacts.

---

## Requirements

---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Provide an API service that can execute a device run and return status + artifacts
- [ ] Use `[deviceinteraction](../deviceinteraction)` to execute commands/triggers/verifications against targets and stream structured events
- [ ] Support core run semantics: bounded concurrency, retries/backoff, timeouts, and cancellation

---

## # Out of Scope

- Full Tower/AWX replacement — not the goal; we only need the orchestration engine semantics and our adapters
- Vendor-specific config generation logic — belongs in modeling/config tooling, not the orchestrator

---

## Context

- This project is part of a larger network automation ecosystem (toolchain + workbench + simulators + device interaction).
- v1 focuses on real/testbed device interaction; simulator integration is a future extension.
- Must support core orchestration primitives: retries/backoff, timeouts/cancellation, and bounded parallel execution.
- Runs should be authorable as a small declarative YAML DSL and/or a Python SDK (TBD), but v1 can start with one.
- Future direction: optionally integrate with an LRM for step selection, retry strategies, and run summarization; engine must remain reliable without AI.

---

## Constraints

- **Operator experience**: API service first — headless execution engine with an HTTP API (CLI/UI can come later as clients)
- **Integration**: Device-first — v1 integrates with `[deviceinteraction](../deviceinteraction)` to talk to devices; other targets come via adapters later
- **Portability**: Must work on a laptop against a small lab, then scale out via concurrency controls and durable run state

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| API-first service | Align with engine role; enables multiple clients (Workbench/CLI/CI) | — Pending |
| Device-first scope (v1) | Prevent scope creep; ship a useful runner for device interactions | — Pending |
| Use `[deviceinteraction](../deviceinteraction)` as a library | Avoid duplicating transports/parsers; keep clean ownership boundaries | — Pending |
| Workflow definitions | Start simple; add YAML and/or Python SDK as needed | — Pending |

---

## Future Direction (Explicitly Not v1)

- Global/toolchain orchestration (multi-tool DAGs across [topogen](../topogen)/[autonetkit](../autonetkit)/[netsim](../netsim)/[netvis](../netvis))
- Simulator-first adapters (e.g. `[network-simulator](../netsim)/`) and environment lifecycle management
- Scheduling, RBAC, approval gates

*Last updated: 2026-02-22 after initialization*

---

## Current Status

2026-03-05 - Completed 02-05-PLAN.md

---

[← Back to Network Automation](/network-automation)

[← Back to Projects](/projects)

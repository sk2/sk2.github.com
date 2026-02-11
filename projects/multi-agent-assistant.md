---
layout: default
---

# multi-agent-assistant

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active Development |
| **Language** | Python, Rust, NATS, Swift |
| **Started** | 2025 |

---

## The Insight

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

## What This Is

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

## Security Model

- **Containerized isolation**: Each agent runs with seccomp deny-by-default, read-only filesystem, no-new-privileges.
- **NATS broker**: TLS 1.3, per-subject ACLs, JetStream for durable messaging.
- **Capability-based authorization**: Short-lived signed tokens per action with one-time nonce validation.
- **Complete audit trail**: All agent actions, message flows, security events logged to SQLite WAL.
- **Per-agent network policies**: Sensitive agents get no internet, API agents get scoped access only.

## Architecture

- **Orchestrator**: LLM planning (GPT-4/Claude), workflow DAG execution, NATS dispatch.
- **Agents**: Lightweight and deterministic; orchestrator does reasoning.
- **macOS collectors**: Swift binaries for HealthKit/EventKit (host-only integrations).
- **Observability**: Structured logs with correlation IDs, OpenTelemetry traces to Jaeger.

## Current Agents

Health monitoring (HealthKit), home automation (Hue), data aggregation (calendar/weather/RSS), screen time tracking, backup integrity monitoring, financial summaries.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
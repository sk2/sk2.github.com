---
layout: default
section: agentic-systems
---

# Secure Multi-Agent Personal Assistant

<div class="badges-row">
  <span class="status-badge status-active">Recently Updated</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

A security-first multi-agent system that coordinates specialized containerized agents through a NATS message broker. Each agent runs in isolation with minimal privileges — separate containers, scoped credentials, no direct agent-to-agent communication. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

The core principle is defense-in-depth: compromise of one agent cannot cascade to others or the orchestrator. All actions are auditable through capability-based authorization with time-limited, signed tokens.

---

## Architecture

- **Orchestrator**: central coordinator with LLM reasoning, manages approval workflows for sensitive actions
- **Message broker**: NATS over LAN (TLS 1.3, per-queue ACLs, message signing)
- **Agent isolation**: Docker containers with seccomp profiles, read-only filesystems, capability dropping
- **Authorization**: Ed25519-signed capability tokens with time limits and scope restrictions
- **Infrastructure**: Mac mini M4 Pro (primary) + Mac mini (secondary) for distributed agent hosting

Agents communicate only through validated message queues — no direct network access between agents. Per-agent egress policies control which agents can reach the internet.

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Python |

---

## What This Is

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

---

## Core Value

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

---

## Requirements

---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Orchestrator coordinates agents via message broker (NATS or RabbitMQ)
- [ ] Each agent runs in isolated container with scoped credentials
- [ ] Agent-to-agent communication blocked by network policies
- [ ] Capability-based authorization with time-limited, signed tokens
- [ ] Complete audit trail of all agent actions and message flow
- [ ] Pre-approval workflow for sensitive agent actions
- [ ] Real-time monitoring dashboard showing agent activity
- [ ] Agents explain reasoning for proposed actions
- [ ] Health monitoring agent that tracks Apple Health metrics
- [ ] Home automation agent that controls Hue lights
- [ ] Data aggregation agent that queries across services
- [ ] Screen Time agent (macOS native usage metrics)
- [ ] Backup Integrity agent (Time Machine/Arq monitoring)
- [ ] Daily Burn agent (Financial transaction summaries)
- [ ] Readwise agent (Reading highlights recall)
- [ ] Unified Notification agent (iMessage/Telegram/Slack gateway)
- [ ] Audit Anomaly agent (Security monitoring of agent activity)
- [ ] One complete end-to-end workflow (e.g., bedtime routine)
- [ ] Per-agent network policies (some internet access, some isolated)
- [ ] Security validation demonstrating isolation guarantees
- [ ] Documentation as case study for infrastructure agent deployment

---

## # Out of Scope

- MCP protocol integration — Message broker provides better security boundaries and audit trail for zero-trust architecture
- Local LLMs in agents (v1) — Keep agents lightweight and deterministic; orchestrator does reasoning via cloud API
- Agent-to-agent direct communication — Violates isolation model; all coordination through orchestrator
- Real-time event streaming from services — Start with polling and request/response patterns; event-driven can come later
- Mobile interface — macOS-native focus initially
- Multi-user support — Single-user personal assistant for v1

---

## Context

**Security Research Background:**

Three reference documents inform this architecture:
1. Agent Communication Patterns - Message Brokers and Event Systems
2. Agent Container Isolation - Security Best Practices
3. Multi-Agent Workflow Architecture - Secure Orchestration Patterns

These establish proven patterns for air-gapped agents, defense-in-depth isolation, and capability-based security.

**Technical Environment:**

- Primary Node: Mac mini M4 Pro (Main orchestrator, NATS server, high-priority agents)
- Secondary Node: Mac mini (Distributed agent node, resource-heavy or specialized integrations)
- Connectivity: NATS over LAN (TLS 1.3 secured)
- macOS native deployment with Docker containers for agent isolation

**Key Architectural Decisions:**

- Message broker over MCP: Better security primitives (per-queue ACLs, TLS enforcement, message signing)
- Lightweight agents over autonomous: Orchestrator centralization allows better audit and approval workflows
- Containerized agents: Each agent in separate container with seccomp profiles, read-only filesystems, capability dropping
- Hybrid integration: Some agents poll APIs, some react to events, orchestrator coordinates timing

---

## Constraints

- **Resource**: Mac mini M4 Pro limits simultaneous container count and memory usage — lightweight agent design is essential
- **Security**: Zero-trust isolation model is non-negotiable — agents treated as potentially compromised at all times
- **Observability**: All actions must be auditable — no agent operations without logging
- **Language**: Agents can be Go, Python, or Rust — whatever fits the integration best
- **Network**: Per-agent egress policies — sensitive agents get no internet, API agents get scoped access only

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Message broker for communication | Provides validated intermediary, prevents direct agent-to-agent contact, enables fine-grained ACLs and audit logging | — Pending |
| Cloud LLM for orchestrator reasoning | Mac mini resources reserved for running containers; orchestrator needs sophisticated planning | — Pending |
| Lightweight deterministic agents | Reduces attack surface, simplifies security analysis, concentrates intelligence in auditable orchestrator | — Pending |
| Docker containers for isolation | Provides namespaces, cgroups, seccomp, network policies on macOS | — Pending |
| Capability tokens for authorization | Time-limited signed tokens prevent privilege escalation and enable fine-grained access control | — Pending |

*Last updated: 2026-02-02 after initialization*

---

## Current Status

2026-02-21 — Completed  (Dashboard milestone achievements included in snapshot payload)

---

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

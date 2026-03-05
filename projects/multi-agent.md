---
layout: default
section: agentic-systems
---

# Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Recently Updated</span>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Concept

Multi-agent coordination requires strict security boundaries to prevent lateral movement. This assistant demonstrates **containerized isolation** where agents (HealthKit, Home Automation, etc.) coordinate via a NATS message broker. By using per-subject ACLs and a "deny-by-default" security posture, the system ensures that compromise of a single agent cannot cascade through the infrastructure.

A security-first framework for coordinating specialized agents. It uses NATS for communication and Docker for isolated execution. The orchestrator handles high-level reasoning and workflow execution, while agents perform deterministic tasks.

The system includes 13+ specialized agents: HealthKit, HealthyPi, Hue (home automation), Climate, Calendar, Weather, RSS, Backup Monitor, Screen Time, Network Monitor, Workflow Engine, Notification Gateway, and Audit Anomaly detection. See [Individual Agents](#individual-agents) section below for details.

AI agent systems need strong security boundaries to prevent compromise from cascading:

**Monolithic Agent Systems:**
- Single point of failure
- Compromise spreads to all capabilities
- Difficult to audit actions
- No privilege separation

**Direct Agent-to-Agent Communication:**
- Attack surface grows with agent count
- Difficult to enforce security policies
- No centralized audit trail
- Trust relationships complex to manage

**Weak Isolation:**
- Shared memory or filesystem
- Credential leakage between agents
- No network segmentation
- Resource contention

**Multi-Agent Assistant provides:**
- Complete agent isolation via containers
- Message broker enforces communication boundaries
- Capability-based authorization with time-limited tokens
- Network policies prevent direct agent-to-agent contact
- Complete audit trail via OpenTelemetry
- Pre-approval workflow for sensitive actions
- Lightweight deterministic agents with cloud LLM orchestrator

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

A security-first multi-agent system that coordinates specialized containerized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues, demonstrating production-ready patterns for deploying AI agents in security-critical infrastructure environments. The orchestrator uses cloud LLM reasoning (GPT-4/Claude) while agents remain lightweight and deterministic.

Complete isolation between agents such that compromise of one agent cannot cascade to others or the orchestrator—demonstrating that secure multi-agent systems are practical for both personal and production infrastructure use cases.

---

## Quick Facts

| | |
|---|---|
| **Status** |  () |
| **Language** | Agents can be Go, Python, or Rust |

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

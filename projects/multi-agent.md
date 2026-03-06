---
layout: default
section: agentic-systems
---

# Secure Multi-Agent Personal Assistant

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Python</span>
</div>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Agents](#agents)
- [Status](#status)

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

## Agents

- **Health monitoring** — Apple HealthKit integration via Swift collector
- **Home automation** — Hue lighting control
- **Screen Time** — macOS usage metrics
- **Backup integrity** — Time Machine/Arq monitoring
- **Financial** — transaction summaries
- **Reading** — Readwise highlights recall
- **Notifications** — unified iMessage/Telegram/Slack gateway
- **Audit anomaly** — security monitoring of agent activity

---

## Status

**Current**: building out the agent roster and end-to-end workflows (bedtime routine as first complete workflow).

**Completed:**
- NATS broker infrastructure with TLS 1.3 and ACLs
- Orchestrator with LLM planning and approval workflows
- Container isolation architecture with capability tokens
- Dashboard with agent activity monitoring

---

[← Back to Autonomous Systems](../agentic-systems)

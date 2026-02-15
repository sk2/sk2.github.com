---
layout: default
section: agentic-systems
---

# Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Phase 18/20 (84%)</span>

[← Back to Agentic Systems](../agentic-systems)

---


## Concept

Multi-agent coordination requires strict security boundaries to prevent lateral movement. This assistant demonstrates **containerized isolation** where agents (HealthKit, Home Automation, etc.) coordinate via a NATS message broker. By using per-subject ACLs and a "deny-by-default" security posture, the system ensures that compromise of a single agent cannot cascade through the infrastructure.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 18/20 (84%) |
| **Language** | Agents can be Go, Python, or Rust |
| **Started** | 2026 |

---

## What This Is

A security-first framework for coordinating specialized agents. It uses NATS for communication and Docker for isolated execution. The orchestrator handles high-level reasoning and workflow execution, while agents perform deterministic tasks.

The system includes 13+ specialized agents: HealthKit, HealthyPi, Hue (home automation), Climate, Calendar, Weather, RSS, Backup Monitor, Screen Time, Network Monitor, Workflow Engine, Notification Gateway, and Audit Anomaly detection. See [Individual Agents](#individual-agents) section below for details.

## Problem It Solves

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

## Features

### Pre-Approval Workflow

Sensitive actions require user confirmation:

```
1. Agent requests capability token for sensitive action
2. Orchestrator prompts user via macOS notification
3. User approves/denies with reason
4. Orchestrator issues token or rejects request
5. Action logged to audit trail
```

**Sensitive Actions:**
- Financial transactions
- Home automation commands
- Message sending
- Data deletion

### Real-Time Monitoring

macOS-native dashboard shows agent activity:

**Displayed Information:**
- Active agents and container status
- Message throughput on NATS
- Recent agent actions
- Pending approvals
- Anomaly alerts

**Controls:**
- Start/stop individual agents
- View logs per agent
- Revoke capability tokens
- Manual workflow triggers

### Explanation of Actions

Agents provide reasoning for proposed actions:

```
Health Agent: "Suggesting 10-minute walk break"
Reason: "Sedentary for 3 hours, heart rate variability declining"
Data: { sitting_time: 180, hrv_trend: -15%, step_count: 450 }
Confidence: 0.85
```

---

## Architecture

### Message Broker: NATS

NATS provides security primitives and communication infrastructure:

**Security Features:**
- TLS 1.3 encryption in transit
- Per-queue ACL (Access Control Lists)
- Subject-based routing and filtering
- Message signing and verification
- Connection authentication

**Communication Patterns:**
- Request/response for agent queries
- Publish/subscribe for events
- Queue groups for load balancing
- Key-value store for state

### Orchestrator

Central coordination with cloud LLM reasoning:

**Responsibilities:**
- Plans multi-agent workflows
- Routes requests to appropriate agents
- Coordinates complex multi-step operations
- Enforces pre-approval for sensitive actions
- Maintains audit log

**LLM Integration:**
- GPT-4 or Claude API for reasoning
- Lightweight agent design offloads intelligence
- Mac mini resources dedicated to running containers

### Containerized Agents

Each agent runs in isolated Docker container:

**Isolation Mechanisms:**
- Separate network namespace
- Read-only root filesystem
- Dropped Linux capabilities
- Seccomp profiles
- Resource limits (CPU/memory)

**Communication:**
- NATS client only
- No direct agent-to-agent contact
- Scoped credentials per agent
- Network policies enforce boundaries

**Agent Types:**
- Stateless: Process requests and return results
- Stateful: Maintain internal state via NATS KV
- Polling: Periodic queries to external services
- Reactive: Respond to events on message queue

## Security Model

### Capability-Based Authorization

Agents receive time-limited signed tokens:

```python
capability_token = {
    "agent": "health-monitoring",
    "allowed_subjects": ["health.data.read", "health.insights.write"],
    "expiration": 1234567890,
    "signature": "ed25519_signature_here"
}
```

**Properties:**
- Ed25519 signing prevents tampering
- Expiration limits compromise window
- Scoped to specific NATS subjects
- Orchestrator issues tokens on-demand

### Network Isolation

Per-agent network policies:

**Internet Access Tiers:**
- **Isolated**: No internet (data aggregation, sensitive agents)
- **Scoped**: Specific API endpoints only (home automation, health)
- **Full**: General internet (notification gateway, backup monitor)

**Agent-to-Agent:**
- Blocked by default
- All communication via NATS
- No direct connections allowed

### Audit Trail

OpenTelemetry tracing for all operations:

**Logged Information:**
- All agent actions with timestamps
- Message flow between agents
- Capability token issuance
- Pre-approval decisions
- Failures and errors

**Analysis:**
- Audit anomaly agent monitors logs
- Detection of unusual patterns
- Security incident investigation
- Compliance reporting

## Individual Agents

**The system includes 13+ specialized agents**, each designed for a specific domain with minimal privileges and explicit security boundaries:

### Health & Biometrics
- **HealthKit Agent** (Swift): Extracts metrics from Apple Health (heart rate, sleep, activity). Runs on macOS host only (no container) due to HealthKit framework requirements.
- **HealthyPi Agent** (Python): Processes real-time biometric signals (ECG, PPG, EDA) from HealthyPi hardware, performs HRV analysis, and publishes health events.

### Home & Environment
- **Hue Agent** (Python): Controls Philips Hue lights based on time of day, presence detection, and automation rules. Scoped network access to Hue Bridge API only.
- **Climate Agent** (Python): Monitors temperature, humidity, and adjusts HVAC settings. Isolated network tier.

### Data Aggregation
- **Calendar Agent** (Swift): Reads upcoming events from Apple Calendar/EventKit. macOS host execution only.
- **Weather Agent** (Python): Fetches forecasts and current conditions. Scoped to weather API endpoints.
- **RSS Agent** (Python): Aggregates news feeds and notifies on keywords. Full internet tier with content filtering.

### Monitoring & Maintenance
- **Backup Monitor** (Rust): Verifies Time Machine and NAS backup integrity. Checks disk usage and staleness. Alerts on failures.
- **Screen Time Agent** (Swift): Tracks application usage patterns from macOS. Host-only execution.
- **Network Monitor** (Rust): Tracks bandwidth, latency, and detects anomalies in local network traffic.

### Automation & Coordination
- **Workflow Engine** (Python): Executes multi-step workflows involving multiple agents. Coordinates approval flow for sensitive actions.
- **Notification Gateway** (Python): Sends notifications via multiple channels (iOS, email, Slack). Full internet access.
- **Audit Anomaly Agent** (Python): Monitors OpenTelemetry logs for security events and unusual patterns.

All agents communicate exclusively via NATS with subject-based ACLs. Each agent's capabilities are explicitly defined, and actions requiring elevated privileges trigger the pre-approval workflow.

---

[← Back to Agentic Systems](../agentic-systems)

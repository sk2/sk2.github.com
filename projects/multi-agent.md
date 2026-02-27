---
layout: default
section: agentic-systems
---

# Secure Multi-Agent Personal Assistant

<span class="status-badge status-active">Active</span>

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

---

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

---

## Quick Facts

| | |
|---|---|
| **Status** |  () |
| **Language** | Agents can be Go, Python, or Rust |

---

## # Pre-Approval Workflow

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

---

## # Real-Time Monitoring

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

---

## # Explanation of Actions

Agents provide reasoning for proposed actions:

```
Health Agent: "Suggesting 10-minute walk break"
Reason: "Sedentary for 3 hours, heart rate variability declining"
Data: { sitting_time: 180, hrv_trend: -, step_count: 450 }
Confidence: 0.85
```

---

## # Message Broker: NATS

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

---

## # Orchestrator

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

---

## # Containerized Agents

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

---

## # Capability-Based Authorization

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

---

## # Network Isolation

Per-agent network policies:

**Internet Access Tiers:**
- **Isolated**: No internet (data aggregation, sensitive agents)
- **Scoped**: Specific API endpoints only (home automation, health)
- **Full**: General internet (notification gateway, backup monitor)

**Agent-to-Agent:**
- Blocked by default
- All communication via NATS
- No direct connections allowed

---

## # Audit Trail

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

---

[← Back to Autonomous Systems](../agentic-systems)

[← Back to Projects](../projects)

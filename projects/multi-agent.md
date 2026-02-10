---
layout: default
---

# Multi-Agent Assistant

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active development |
| **Language** | Python · Go · Rust · Swift |
| **Stack** | Docker · NATS · OpenTelemetry |
| **Architecture** | Security-first containerized agents |
| **Agents** | 10+ specialized agents |
| **Started** | 2025 |
| **License** | Open Source |

---

## Overview

Security-first multi-agent system that coordinates specialized containerized agents through a message broker architecture. Each agent runs in isolation with minimal privileges and communicates only through validated message queues. Demonstrates production-ready patterns for deploying AI agents in security-critical infrastructure environments.

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

## Implemented Agents

### Health Monitoring Agent
- Tracks Apple Health metrics (steps, heart rate, sleep)
- Analyzes trends and patterns
- Sends interventions for health goals
- Integrates with HealthyPi ecosystem

### Home Automation Agent
- Controls Philips Hue lights
- Schedules automations
- Responds to conditions (time, occupancy)
- Part of bedtime routine workflow

### Data Aggregation Agent
- Queries across multiple services
- Correlates information
- Provides unified responses
- No internet access (isolated agent)

### Screen Time Agent
- Tracks macOS usage metrics
- Application time monitoring
- Focus session tracking
- Daily/weekly summaries

### Backup Integrity Agent
- Monitors Time Machine status
- Checks Arq backup completion
- Verifies backup freshness
- Alerts on failures

### Daily Burn Agent
- Summarizes financial transactions
- Categorizes spending
- Budget tracking
- Trend analysis

### Readwise Agent
- Retrieves reading highlights
- Surfaces relevant quotes
- Spaced repetition scheduling
- Knowledge recall

### Unified Notification Agent
- Gateway for iMessage/Telegram/Slack
- Message routing and delivery
- Notification preferences
- Rate limiting

### Audit Anomaly Agent
- Security monitoring of agent activity
- Detects unusual patterns
- Privilege escalation attempts
- Unauthorized access detection

### Additional Planned Agents
- Calendar integration
- Email processing
- Task management
- Weather and environment

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

## Use Cases

**Bedtime Routine Workflow:**
1. Screen Time agent detects 9 PM
2. Orchestrator plans routine
3. Home Automation dims lights
4. Notification agent sends goodnight messages
5. Backup Integrity checks completion
6. Health agent suggests wind-down activity

**Security Monitoring:**
Audit Anomaly agent detects backup agent attempting unauthorized health data access. Alerts user, revokes token, logs incident.

**Daily Briefing:**
Data Aggregation queries Health, Screen Time, Daily Burn, Readwise agents. Compiles report without internet access. Delivers via Notification agent.

## Technical Details

### Performance

- Container startup: <2s per agent
- Message latency: <10ms on LAN
- NATS throughput: 100k+ messages/sec
- Resource usage: ~100MB per agent

### Deployment

**Primary Node:** Mac mini M4 Pro
- NATS server
- Orchestrator
- High-priority agents

**Secondary Node:** Mac mini
- Resource-heavy agents
- Specialized integrations
- Distributed workload

### Development

**Local Testing:**
- Mock NATS server for unit tests
- Docker Compose for integration tests
- Pre-commit hooks for security checks
- Capability token validation

## Development Status

**Active Development:**
- Core framework complete
- 10+ agents implemented
- Security model validated
- End-to-end workflows functional

**Next Steps:**
- Additional agent implementations
- Enhanced monitoring dashboard
- Mobile interface (future)
- Multi-user support (future)

**Out of Scope for v1:**
- MCP protocol integration (message broker provides better security)
- Local LLMs in agents (keep agents lightweight)
- Agent-to-agent direct communication (violates isolation)
- Real-time event streaming (start with polling)

## Comparison

| Feature | Multi-Agent Assistant | AutoGPT | LangChain Agents |
|---------|----------------------|---------|------------------|
| Agent Isolation | Full (containers) | None | None |
| Security Model | Capability tokens | API keys | API keys |
| Audit Trail | Complete | Logs only | Logs only |
| Pre-Approval | Built-in | Manual | Manual |
| Network Policies | Per-agent | No | No |
| Resource Limits | Enforced | No | No |
| Agent Language | Any | Python | Python |

## Links

- **GitHub:** [github.com/sk2/multi-agent-assistant](https://github.com/sk2/multi-agent-assistant)
- **Documentation:** See repository docs/ directory
- **Related:** [HealthyPi Ecosystem](healthypi) integrates as health monitoring agent

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Architecture diagram showing NATS + containers
- macOS dashboard with agent status
- Pre-approval notification example
- Audit trail visualization
- Agent logs with OpenTelemetry
- Docker container security config
- Network policy diagram
- Capability token structure
- Bedtime routine workflow diagram
- Anomaly detection alert
-->

---
layout: default
---

# Agentic Systems Ecosystem

Security-first multi-agent architectures for personal and infrastructure automation. Specialized agents coordinate through message brokers with strict isolation boundaries, capability-based authorization, and comprehensive audit trails.

---

## The Vision

AI agent systems promise automation and intelligence, but most implementations fail on security. A single compromised agent shouldn't cascade to the entire system. This ecosystem demonstrates production-ready patterns for deploying AI agents in security-critical environments—both personal infrastructure (home automation, health monitoring) and enterprise contexts.

**Core Philosophy:**
- **Isolation by default**: Each agent runs in a separate container with minimal privileges
- **Communication through brokers**: No direct agent-to-agent contact, all coordination via NATS
- **Capability-based authorization**: Time-limited tokens scope what each agent can do
- **Pre-approval for sensitive actions**: User confirms financial transactions, home automation, data deletion
- **Lightweight agents, cloud reasoning**: Agents remain deterministic, orchestrator uses GPT-4/Claude for planning

## Architecture Overview

```
┌────────────────────────────────────────────────────────────┐
│                   Orchestrator (Cloud LLM)                  │
│              GPT-4/Claude for planning & reasoning          │
└────────────┬───────────────────────────┬───────────────────┘
             │                           │
    ┌────────▼─────────┐        ┌────────▼─────────┐
    │   NATS Broker    │◄──────►│  Security Layer  │
    │  (Message Bus)   │        │  (Token Mgmt)    │
    └────────┬─────────┘        └──────────────────┘
             │
   ┌─────────┼─────────┬─────────┬─────────┬─────────┐
   │         │         │         │         │         │
┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│Health│  │ Hue │  │ Cal │  │Bkup │  │ RSS │  │Work │
│Agent │  │Agent│  │Agent│  │Agent│  │Agent│  │Engine│
└─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘
```

Each agent:
- Runs in isolated Docker container (or macOS host for framework access)
- Communicates only through NATS message broker
- Receives time-limited capability tokens
- Logs all actions to OpenTelemetry

---

## The Systems

### Multi-Agent Personal Assistant

<span class="status-badge status-active">Phase 17/20 (79%)</span> · [Full Details →](projects/multi-agent)

**What It Is:**
A security-first framework for coordinating 13+ specialized agents (health monitoring, home automation, data aggregation, workflow automation) through a message broker architecture. Demonstrates production-ready patterns for deploying AI agents in security-critical infrastructure.

**The Security Problem:**

Traditional agent systems fail on security:
- **Monolithic agents**: Single point of failure, compromise spreads to all capabilities
- **Direct agent-to-agent**: Attack surface grows quadratically with agent count
- **Weak isolation**: Shared memory/filesystem enables credential leakage
- **No audit trail**: Can't reconstruct what happened after compromise

**The Solution:**

Complete isolation with message-broker coordination:
- **Container isolation**: Each agent in separate Docker container with dropped capabilities
- **Network segmentation**: Agents can't communicate directly, only through NATS
- **Capability tokens**: Time-limited Ed25519-signed tokens scope agent permissions
- **Pre-approval workflow**: Sensitive actions require user confirmation
- **Audit trail**: OpenTelemetry logs all agent actions for forensic analysis

**Individual Agents:**

### Health & Biometrics

**HealthKit Agent** (Swift)
- **Purpose**: Extract metrics from Apple Health (heart rate, sleep, activity)
- **Execution**: macOS host only (HealthKit framework requirement)
- **Capabilities**: Read-only access to Health data
- **Use case**: "Your resting heart rate is 5% above baseline this week"

**HealthyPi Agent** (Python)
- **Purpose**: Process real-time biometric signals from HealthyPi hardware
- **Protocols**: ECG, PPG (photoplethysmography), EDA (electrodermal activity)
- **Analysis**: HRV (heart rate variability) calculation, stress detection
- **Use case**: "Elevated stress detected (low HRV), suggest 5-minute breathing exercise"

### Home & Environment

**Hue Agent** (Python)
- **Purpose**: Control Philips Hue lights based on automation rules
- **Network**: Scoped access to Hue Bridge API only (no general internet)
- **Triggers**: Time of day, presence detection, sleep schedule
- **Use case**: "Dim lights to 20% at 9 PM for wind-down routine"

**Climate Agent** (Python)
- **Purpose**: Monitor temperature/humidity, adjust HVAC
- **Network**: Isolated tier for smart thermostat communication
- **Intelligence**: Learn comfort patterns, optimize for efficiency
- **Use case**: "Pre-heat home 30 minutes before arrival based on calendar"

### Data Aggregation

**Calendar Agent** (Swift)
- **Purpose**: Read upcoming events from Apple Calendar/EventKit
- **Execution**: macOS host only (EventKit framework)
- **Capabilities**: Read-only calendar access
- **Use case**: "Meeting in 15 minutes, start focus mode and prepare notes"

**Weather Agent** (Python)
- **Purpose**: Fetch forecasts and current conditions
- **Network**: Scoped to weather API endpoints only
- **Integration**: Informs clothing suggestions, commute planning
- **Use case**: "Rain expected in 2 hours, suggest early departure"

**RSS Agent** (Python)
- **Purpose**: Aggregate news feeds, notify on keywords
- **Network**: Full internet with content filtering
- **Intelligence**: Keyword matching, topic clustering, importance scoring
- **Use case**: "3 articles about Rust 2.0 release, curated digest ready"

### Monitoring & Maintenance

**Backup Monitor** (Rust)
- **Purpose**: Verify Time Machine and NAS backup integrity
- **Checks**: Disk usage, backup staleness, consistency verification
- **Alerts**: Notify on backup failures or degradation
- **Use case**: "Time Machine backup hasn't run in 5 days, investigate"

**Screen Time Agent** (Swift)
- **Purpose**: Track application usage patterns from macOS
- **Execution**: Host-only (macOS framework dependency)
- **Intelligence**: Detect productivity patterns, context switching
- **Use case**: "4 hours in Slack today, 30% above weekly average"

**Network Monitor** (Rust)
- **Purpose**: Track bandwidth, latency, detect anomalies
- **Monitoring**: Local network traffic analysis, ISP performance
- **Alerts**: Connection degradation, unusual traffic patterns
- **Use case**: "Upload bandwidth dropped 60%, possible ISP issue"

### Automation & Coordination

**Workflow Engine** (Python)
- **Purpose**: Execute multi-step workflows involving multiple agents
- **Coordination**: Orchestrates approval flow for sensitive actions
- **Example workflow**: "Low energy detected → suggest walk → check weather → send notification"
- **Use case**: Chains agents together for complex automation

**Notification Gateway** (Python)
- **Purpose**: Send notifications via multiple channels
- **Channels**: iOS push, email, Slack, webhook
- **Network**: Full internet access for delivery
- **Use case**: Route urgent alerts to appropriate channel

**Audit Anomaly Agent** (Python)
- **Purpose**: Monitor OpenTelemetry logs for security events
- **Detection**: Unusual patterns, privilege escalation attempts, anomalous access
- **Alerting**: Real-time notification on suspicious activity
- **Use case**: "HealthKit agent requested home automation capability (unusual)"

---

## Security Model in Depth

### Containerized Isolation

Each agent runs in Docker with strict constraints:

**Resource Limits:**
```yaml
memory: 256MB
cpu_shares: 512
pids_limit: 128
```

**Security Options:**
```yaml
read_only: true
no_new_privileges: true
cap_drop: [ALL]
cap_add: [NET_BIND_SERVICE]  # Only if needed
seccomp: default
```

**Network Policies:**
```yaml
# Health agents: NATS only
healthkit:
  allow: [nats:4222]
  deny: [0.0.0.0/0]

# Weather agent: Scoped internet
weather:
  allow: [nats:4222, api.weather.com:443]
  deny: [0.0.0.0/0]
```

### Capability-Based Authorization

Agents receive time-limited signed tokens:

Request capability:
```json
{
  "agent": "health-monitoring",
  "requested_subjects": ["health.data.read", "health.insights.write"],
  "duration_seconds": 3600,
  "reason": "Scheduled HRV analysis"
}
```

Orchestrator issues token:
```json
{
  "agent": "health-monitoring",
  "allowed_subjects": ["health.data.read", "health.insights.write"],
  "issued_at": 1234567890,
  "expires_at": 1234571490,
  "signature": "ed25519_signature_prevents_tampering"
}
```

Agent presents token on NATS connection:
```python
nats_client.connect(
    servers=["nats://broker:4222"],
    user_jwt=capability_token
)
```

### Pre-Approval Workflow

Sensitive actions require user confirmation:

```
1. Hue Agent: "Turn off all lights"
   ↓
2. Orchestrator: "Light control requires approval"
   ↓
3. macOS Notification: "Hue Agent wants to turn off all lights. Approve?"
   ↓
4. User: [Approve] or [Deny with reason]
   ↓
5. Orchestrator: Issue capability token (if approved)
   ↓
6. Action logged to audit trail
```

**Sensitive action categories:**
- Financial transactions
- Home automation (lights, locks, climate)
- Message sending
- Data deletion
- External API writes

### Audit Trail

All agent actions logged to OpenTelemetry:

```json
{
  "timestamp": "2026-02-12T19:30:45Z",
  "agent": "hue-agent",
  "action": "set_light_state",
  "resource": "living_room_lights",
  "parameters": {"brightness": 0, "on": false},
  "user_approved": true,
  "capability_token_id": "cap_abc123",
  "result": "success"
}
```

Query audit trail:
```bash
# Find all hue agent actions in last hour
otel query --agent hue-agent --since 1h

# Find actions requiring approval
otel query --filter "user_approved=true"

# Detect anomalies
otel query --anomalies
```

---

## Real-World Workflow Examples

### Morning Routine Automation

```
06:30 - Calendar Agent: "Meeting at 09:00"
  ↓
06:30 - Weather Agent: "Rain expected, 42°F"
  ↓
06:35 - Workflow Engine: Execute morning routine
  ├─ Climate Agent: Pre-heat home to 68°F
  ├─ Hue Agent: Gradual light fade-in (sunrise simulation)
  └─ Notification Gateway: "Morning briefing ready"
  ↓
06:45 - HealthKit Agent: Sleep quality summary
  ├─ "7.2 hours sleep, 85% quality"
  └─ "Resting HR 5% elevated, suggest light exercise"
```

### Health Alert Flow

```
14:00 - HealthyPi Agent: Low HRV detected
  ↓
14:01 - Workflow Engine: Trigger wellness intervention
  ├─ Screen Time Agent: "3 hours continuous work"
  ├─ Calendar Agent: "No meetings until 15:30"
  └─ Notification Gateway: "Suggest 10-minute walk break"
  ↓
User: [Accept suggestion]
  ↓
14:05 - Hue Agent: Dim lights (encourage leaving desk)
14:05 - Notification Gateway: "Timer started: 10 minutes"
```

### Backup Monitoring

```
Weekly - Backup Monitor: Check integrity
  ├─ Time Machine: Last backup 2 days ago [FAIL]
  ├─ NAS: Last backup 3 hours ago [OK]
  └─ Disk usage: 85% [WARN]
  ↓
Audit Anomaly Agent: Detect pattern
  ├─ "Time Machine backups failing for 2 weeks"
  └─ Notification Gateway: [HIGH PRIORITY]
  ↓
User: Investigate Time Machine configuration
```

---

### Cycle Agent — AI-Driven Training

<span class="status-badge status-active">Phase 1/5 (80%)</span> · [Full Details →](projects/cycle)

**What It Is:**
A native SwiftUI training application for iPad and Apple TV that bridges professional cycling hardware (KICKR Core smart trainer) with dynamic AI-driven workout logic via NATS, visualized in a high-performance SceneKit 3D environment.

**The Training Problem:**
- **Static workouts**: Pre-programmed intervals don't adapt to real-time performance
- **Manual adjustment**: Stopping to change resistance breaks flow state
- **No real-time feedback**: Can't adjust difficulty based on fatigue or heart rate
- **Disconnected platforms**: TrainerRoad/Zwift don't integrate with custom logic

**The Solution:**
AI agent dynamically adjusts workout based on rider performance:

**Agent Architecture:**
- **Fitness Agent** (Swift): Manages workout state, adjusts resistance in real-time
- **Data Collection Agent** (Swift): Captures power, cadence, heart rate from KICKR
- **Visualization Agent** (Swift/SceneKit): Renders 3D training environment
- **Planning Agent** (Cloud): Uses Claude/GPT-4 to adapt workout strategy

**Real-Time Adaptation:**
```
Current: 300W target, rider producing 310W at 75 RPM cadence
  ↓
Fitness Agent: "Rider exceeding target comfortably"
  ↓
Planning Agent (LLM): "Rider has capacity, increase to 320W"
  ↓
Fitness Agent: Adjust KICKR resistance
  ↓
Visualization: Update 3D terrain gradient
```

**Training Modes:**
- **FTP Test**: Automated 20-minute threshold detection
- **Interval Training**: AI-adjusted work/rest ratios
- **Endurance**: Maintain heart rate zones with dynamic resistance
- **Sweet Spot**: Hold 88-94% FTP with auto-correction

**Integration:**
- **NATS messaging**: Fitness agent publishes metrics, planning agent consumes
- **Bluetooth LE**: Direct KICKR communication via iOS Core Bluetooth
- **Apple TV**: Mirror workout to TV with SceneKit visualization
- **HealthKit**: Export workout summary to Apple Health

**Current Status:** Phase 1 complete (KICKR integration + basic workouts), building AI adaptation layer.

**Tech Stack:** Swift, SwiftUI, SceneKit, Core Bluetooth, NATS

---

## Philosophy: Why This Approach?

### Security Through Isolation
Containers provide hard isolation boundaries. A compromised RSS agent (full internet access) cannot access HealthKit data (host-only, scoped API). This is impossible with monolithic architectures.

### Explainability Through Logging
Every agent action is logged with reasoning. When something goes wrong, you can reconstruct the decision chain: "Hue agent dimmed lights because Calendar agent reported meeting, and Workflow Engine inferred focus mode."

### Modularity Through Message Brokers
Adding a new agent requires:
1. Write agent code
2. Define NATS subjects it publishes/subscribes to
3. Request capability tokens from orchestrator
4. Deploy container

No changes to existing agents. The broker enforces boundaries.

### Cloud LLM for Planning, Local Execution
Orchestrator uses GPT-4/Claude for high-level reasoning ("user seems stressed, what interventions make sense?"). Agents remain lightweight and deterministic ("dim lights to 20%"). This splits intelligence (cloud) from execution (local), optimizing for both capability and latency.

---

## Open Source & Contributions

- **Multi-Agent Assistant**: [github.com/sk2/multi-agent-assistant](https://github.com/sk2/multi-agent-assistant)
- **Cycle Agent**: [github.com/sk2/cycle-agent](https://github.com/sk2/cycle-agent)

---

[← Back to Projects](projects) | [View CV](cv) | [Network Automation](network-automation) | [Signal Processing](signal-processing) | [Data Analytics](data-analytics)

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
.status-planning {
  background-color: #ffc107;
  color: #343a40;
}
</style>

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

## Agent Catalog

### Health & Wellness Agents

**Health Monitoring Agent**
- **Purpose:** Tracks Apple Health metrics and integrates with HealthyPi ecosystem
- **Data Sources:** Apple Health API, HealthyPi NATS streams (ECG, PPG, EDA, EEG)
- **Capabilities:**
  - Monitors key metrics: sleep quality, activity levels, heart rate, HRV
  - Detects anomalies in biometric trends
  - Analyzes patterns across multiple data sources
  - Sends interventions for health goals (e.g., "Take a walk, sedentary for 3 hours")
- **Network Policy:** Scoped internet access (Apple Health API only)
- **Integration:** Subscribes to `healthypi.*` NATS subjects for real-time biometrics

**Bio-Feedback Prompter**
- **Purpose:** Links health metrics to journaling prompts
- **Capabilities:**
  - Correlates physiological data with activities
  - Generates contextual prompts based on stress/recovery indicators
  - Tracks mind-body connections over time
- **Network Policy:** Isolated (no internet)

**Ergonomic Sentinel Agent**
- **Purpose:** Monitors posture and ergonomics using Vision framework
- **Capabilities:**
  - Local webcam analysis (no recording, privacy-first)
  - Detects poor posture patterns
  - Reminds to adjust seating or take breaks
  - Integrates with Screen Time for sedentary alerts
- **Network Policy:** Isolated (local processing only)
- **Privacy:** All processing local, no data leaves container

### Home Automation Agents

**Hue Controller Agent**
- **Purpose:** Controls Philips Hue smart lighting system
- **API Integration:** Hue Bridge local API (HTTP)
- **Capabilities:**
  - Set light states (on/off, brightness, color temperature, RGB)
  - Query current status of all lights and groups
  - Schedule automations based on time or conditions
  - Part of bedtime/morning workflows
- **Example Actions:**
  - Dim lights at 9 PM for bedtime routine
  - Set warm colors in morning, cool colors during work hours
  - Flash lights for notifications (package delivery, important alert)
- **Network Policy:** Scoped LAN access (Hue Bridge only)

**IoT Bridge Agent**
- **Purpose:** Connects ESPHome/MQTT devices to NATS ecosystem
- **Protocols:** MQTT, ESPHome native API
- **Capabilities:**
  - Translate MQTT messages to NATS subjects
  - Expose ESP32 sensors (temperature, motion, door/window contacts)
  - Control ESP-based switches and relays
  - Unified interface for heterogeneous IoT devices
- **Network Policy:** Scoped LAN access (MQTT broker only)

**BLE Presence Agent**
- **Purpose:** Tracks device proximity via Bluetooth RSSI
- **Capabilities:**
  - Detects when paired devices are nearby (phone, watch, keys)
  - Occupancy detection for automation triggers
  - "Home/Away" state for lighting and climate control
  - Security: Alert if unknown BLE devices detected
- **Network Policy:** Isolated (local Bluetooth only)

### Productivity & Context Agents

**Screen Time Agent**
- **Purpose:** Tracks macOS digital usage and focus patterns
- **Data Sources:** macOS Screen Time API, application usage logs
- **Capabilities:**
  - Application time tracking (development tools, browsers, entertainment)
  - Focus session monitoring (Deep Work mode)
  - Daily/weekly productivity summaries
  - Detects context switches and distraction patterns
  - Integration with Habit Engine for streak tracking
- **Network Policy:** Isolated (no internet)
- **Privacy:** Stores aggregated metrics only, not screenshots

**Screen Context Agent**
- **Purpose:** Provides workflow awareness via local OCR
- **Capabilities:**
  - On-demand screen text extraction (not continuous monitoring)
  - Recognizes active project/task context
  - Suggests relevant agents based on visible content
  - Example: Detects terminal with SSH session, offers Backup Integrity check
- **Network Policy:** Isolated (local processing only)
- **Privacy:** OCR runs locally, never uploads screenshots

**Ambient Audio Agent**
- **Purpose:** Classifies local sound events without recording
- **Technology:** CoreML audio classification
- **Capabilities:**
  - Detects environmental context (music playing, people talking, silent focus)
  - No audio recording or storage (classification only)
  - Adjusts notifications based on audio environment
  - Example: Suppress non-urgent alerts during meetings
- **Network Policy:** Isolated (local processing only)
- **Privacy:** Zero-knowledge audio classification, no recordings

**Soundscape Agent**
- **Purpose:** Generates procedural ambient noise for focus/relaxation
- **Inspired By:** WatchNoise app (white/brown/pink noise, rain, ocean)
- **Capabilities:**
  - Procedurally generated soundscapes
  - Adaptive audio based on heart rate variability
  - Integration with Health Agent for stress response
- **Network Policy:** Isolated

### Data & Information Agents

**Data Aggregation Agent**
- **Purpose:** Queries multiple services and correlates information
- **Architecture:** Isolated agent that queries other agents (not external APIs directly)
- **Capabilities:**
  - Unified interface to query Health, Screen Time, Finance, Backup agents
  - Correlates data across domains (e.g., "Sleep quality vs. productivity")
  - Generates morning/evening briefings
  - Natural language query interface
- **Network Policy:** Isolated (no internet, NATS only)
- **Security Model:** Cannot directly access external services, must request via other agents

**Readwise Agent**
- **Purpose:** Surfaces reading highlights for knowledge recall
- **API Integration:** Readwise API (HTTPS)
- **Capabilities:**
  - Retrieves book/article highlights
  - Spaced repetition scheduling (surface old highlights periodically)
  - Context-aware suggestions (relevant quotes based on current work)
  - Daily knowledge review workflow
- **Network Policy:** Scoped internet (Readwise API only)

**Logistics Tracker**
- **Purpose:** Polls delivery APIs for package status
- **Integrations:** USPS, UPS, FedEx, Amazon tracking
- **Capabilities:**
  - Unified view of all in-transit packages
  - Delivery day alerts
  - Integration with BLE Presence (notify when home for delivery)
- **Network Policy:** Scoped internet (delivery APIs only)

**GSD Observer Agent**
- **Purpose:** Monitors NATS results and maps to planning requirements
- **Capabilities:**
  - Watches for completed tasks in GSD workflow
  - Updates `.planning/STATE.md` automatically
  - Tracks requirement fulfillment
  - Generates progress reports
- **Network Policy:** Isolated (NATS only)

### Financial & Productivity Agents

**Daily Burn Agent**
- **Purpose:** Summarizes financial transactions and spending
- **Data Source:** Daily Burn API (if available) or Banktivity Bridge
- **Capabilities:**
  - Fetches recent transactions
  - Categorizes spending automatically
  - Budget tracking and alerts (overspending warnings)
  - Weekly/monthly trend analysis
  - Anomaly detection (unusual charges)
- **Network Policy:** Scoped internet (financial API only)
- **Security:** Requires pre-approval for transaction queries

**Banktivity Bridge Agent**
- **Purpose:** Extracts finance data from Banktivity app
- **Integration:** AppleScript automation or direct SQLite DB access
- **Capabilities:**
  - Read account balances
  - Export transaction history
  - Query budget categories
  - Local-first alternative to cloud finance APIs
- **Network Policy:** Isolated (local filesystem only)
- **Security:** Read-only filesystem access to Banktivity database

**Habit Engine Agent**
- **Purpose:** Tracks cross-domain habit streaks
- **Data Sources:** Health, Screen Time, Finance, Backup agents
- **Capabilities:**
  - Tracks multi-faceted habits (e.g., "Healthy day" = 8hr sleep + 10k steps + <2hr screen time)
  - Maintains streak counters
  - Sends encouragement/warnings
  - Visualizes long-term trends
- **Network Policy:** Isolated (NATS only)

### System & Infrastructure Agents

**Backup Integrity Agent**
- **Purpose:** Monitors local backup systems
- **Integrations:** Time Machine API, Arq backup logs
- **Capabilities:**
  - Checks Time Machine last successful backup timestamp
  - Verifies Arq backup completion and upload status
  - Tests backup freshness (warns if >24 hours old)
  - Alerts on backup failures or missing destinations
  - Validates backup integrity (checksums if available)
- **Network Policy:** Isolated (local filesystem only)

**Update Manager Agent**
- **Purpose:** Reports on host and container update status
- **Capabilities:**
  - Checks macOS system updates
  - Docker image updates for all agent containers
  - Homebrew formula updates
  - Generates update summary without applying changes
  - Pre-approval required to trigger updates
- **Network Policy:** Scoped internet (update servers only)

**Infrastructure Balancer**
- **Purpose:** Manages agent placement across distributed nodes
- **Capabilities:**
  - Monitors resource usage per container
  - Migrates agents between Mac mini hosts based on load
  - Ensures high-priority agents on primary node
  - Handles failover if node goes offline
- **Network Policy:** Scoped LAN (NATS and Docker API)

### Communication Agents

**Unified Notification Agent**
- **Purpose:** Secure gateway for iMessage/Telegram/Slack
- **Architecture:** Reduces attack surface by centralizing external communication
- **Capabilities:**
  - Send messages via iMessage (AppleScript)
  - Telegram bot integration
  - Slack webhook posting
  - Message routing based on urgency/context
  - Rate limiting (prevent spam)
  - Template-based formatting
- **Network Policy:** Scoped internet (Telegram/Slack APIs only)
- **Security:** All outbound messages logged to audit trail

**Push Gateway Agent**
- **Purpose:** Bridges NATS to Apple Push Notification service (APNs)
- **Capabilities:**
  - Sends push notifications to iPhone/Apple Watch
  - Handles APNs authentication and token management
  - Priority-based delivery (time-sensitive vs. background)
  - Rich notifications with actions (approve/reject workflows)
- **Network Policy:** Scoped internet (APNs only)

**Mobile API Agent**
- **Purpose:** Secure ingestion endpoint for iPhone/Watch data
- **Capabilities:**
  - Receives context updates from mobile apps
  - Ingests real-time Focus mode status
  - Location updates (when relevant)
  - Health metrics from Apple Watch
  - Publishes to NATS for other agents
- **Network Policy:** Scoped LAN (mobile devices on local network)
- **Security:** mTLS client authentication required

### Security & Privacy Agents

**Audit Anomaly Agent**
- **Purpose:** Security monitoring of all agent activity
- **Data Source:** OpenTelemetry audit logs from all agents
- **Capabilities:**
  - Detects unusual agent behavior patterns
  - Identifies privilege escalation attempts
  - Alerts on unauthorized NATS subject access
  - Monitors for excessive resource usage (possible compromise)
  - Tracks capability token expiration violations
  - Generates security incident reports
- **Network Policy:** Isolated (NATS audit stream only)
- **Response:** Automatically revokes suspicious agent capabilities

**Privacy Auditor Agent**
- **Purpose:** Continuous secret scanning of logs and notes
- **Capabilities:**
  - Scans logs for accidentally leaked credentials
  - Detects PII in audit trails
  - Identifies API keys or tokens in plaintext
  - Alerts on potential GDPR/privacy violations
  - Redaction suggestions
- **Network Policy:** Isolated (local log files only)

### Native Apps & UI Agents

**Mac Menu Bar App**
- **Purpose:** Native macOS status and approval interface
- **Technology:** Swift + SwiftUI
- **Capabilities:**
  - Real-time NATS connection status
  - Pending approval requests (HITL workflow)
  - Quick approve/reject with reasoning display
  - Agent health monitoring (container status)
  - Manual workflow triggers
  - OpenTelemetry trace viewer
- **Network Policy:** Local NATS connection only

**Watch/iPhone Context Apps**
- **Purpose:** Gather real-time context from mobile devices
- **Data Collected:**
  - Focus mode status (Work, Sleep, Driving, etc.)
  - Coarse location (Home/Office/Away, not GPS)
  - Apple Watch biometrics (heart rate, HRV)
  - Activity state (stationary, walking, running)
- **Network Policy:** Local network (publishes to Mobile API Agent)
- **Privacy:** Minimal data collection, user-controlled

**Agent Terminal**
- **Purpose:** Bridge to external CLI agents like Claude Code
- **Capabilities:**
  - Spawn Claude Code sessions for complex tasks
  - Relay NATS messages to CLI tools
  - Capture tool output and publish to NATS
  - Integration with GSD workflow
- **Network Policy:** Scoped internet (Anthropic API)
- **Security:** Sandboxed execution with read-only access by default

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

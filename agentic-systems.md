---
layout: default
---

# Autonomous Systems

Multi-agent coordination and real-time adaptive control — secure systems where specialized agents work together within strict isolation boundaries.

## Contents
- [Principles](#principles)
- [How They Work Together](#how-they-work-together)
- [Systems](#systems)

---

## Principles

- **Security by Design**: Every agent runs in its own container with minimal privileges. No direct agent-to-agent communication — all coordination flows through the NATS broker.
- **Clear Coordination**: The orchestrator uses cloud LLM reasoning (Claude/GPT-4) for task planning while agents remain lightweight and deterministic.
- **User Control**: Sensitive actions require explicit approval. The system explains its reasoning and provides a clear audit trail.
- **Composable Architecture**: New capabilities are added by deploying new agent containers, not by modifying the orchestrator.

---

## How They Work Together

```
┌────────────────────────────────────────────────────────┐
│                    Orchestrator                         │
│            (LLM Reasoning + Task Planning)             │
└──────────┬────────────────────────────────┬────────────┘
           │         NATS Broker            │
     ┌─────▼──────┐  ┌──────────┐  ┌───────▼────────┐
     │  Health     │  │  Home    │  │  Monitoring    │
     │  Agent      │  │  Agent   │  │  Agent         │
     │ (Biometrics)│  │ (HomeKit)│  │ (Backups/Infra)│
     └─────────────┘  └──────────┘  └────────────────┘
```

Each agent subscribes to NATS topics matching its domain. The orchestrator breaks complex requests into domain-specific tasks, publishes them, and aggregates results. Agents can trigger other agents through the broker but never communicate directly.

---

## Systems

### Multi-Agent Personal Assistant

<span class="status-badge status-active">Recently Updated</span> · <span class="stack-badge">Python</span> · [Full Details →](projects/multi-agent)

Security-first multi-agent system coordinating specialized containerized agents through a NATS message broker. Each agent runs in isolation with scoped credentials — separate containers, no shared state. The orchestrator uses cloud LLM reasoning while agents remain lightweight and deterministic.

**Domains covered:**
- **Health**: Monitor and analyze biometric data from [HealthyPi](/projects/healthypi) and Apple HealthKit
- **Home**: Control environment via HomeKit integration
- **Monitoring**: Verify system integrity, backup status, and infrastructure health
- **Analysis**: Process and summarize information from multiple sources

---

### Training Assistant

<span class="status-badge status-active">Recently Updated</span> · <span class="stack-badge">Swift</span> · [Full Details →](projects/cycle)

Native SwiftUI training application for iPad and Apple TV that bridges a Wahoo KICKR Core smart trainer with AI-driven workout logic. The app communicates with the trainer over Bluetooth (FTMS protocol) for real-time resistance control and telemetry, while a NATS message bridge connects to an external agent for dynamic workout decisions.

**Capabilities:**
- Real-time power, cadence, and heart rate telemetry
- Dynamic resistance adjustment based on training goals
- Adaptive interval programming via agent reasoning
- Session recording and performance tracking

---

[← Back to Projects](projects) | [Network Automation](network-automation) | [Signal Processing](signal-processing) | [Photography](photography) | [Data & Analytics](data-analytics)

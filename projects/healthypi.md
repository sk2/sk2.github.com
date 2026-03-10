---
layout: default
section: agentic-systems
description: "Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (Pi HAT and wearable) into structured metrics for agent-driven…"
---

# HealthyPi Ecosystem

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-02-20</span>
  <span class="stack-badge">Python</span>
</div>

---

## Contents

- [Concept](#concept)
- [Architecture](#architecture)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Modular health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (Pi HAT and wearable) into structured metrics for agent-driven analysis. Swift collectors on Apple devices capture HealthKit data, publish to a NATS broker, and Python agents in containers run analysis pipelines — all coordinated by the [multi-agent](../multi-agent) orchestrator.

---

## Architecture

- **HealthyPi 6** (Pi HAT): ECG, PPG, SpO2, temperature via serial/USB
- **HealthyPi Move** (wearable): accelerometer, PPG via BLE
- **Ingest path**: hardware stream, normalize, publish to NATS (`biometric.raw.*`)
- **Agent integration**: leverages the [multi-agent](../multi-agent) framework (NATS broker, TLS 1.3, capability tokens)
- **Visualization**: desktop (menu bar) and Apple ecosystem (iOS/Watch)

---

## Features

- Standardized data models for multi-modal biometrics
- Synthetic "Virtual Patient" for hardware-free development
- Real-time and historical analysis via agent pipeline
- Unified visualization across desktop and mobile

---

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-20 |
| **Stack** | Python |

---

## Core Value

A modular, agent-aware health monitoring ecosystem that translates raw biometric data from HealthyPi hardware (6 and Move) into actionable insights and automated interventions.

---

## Vision

To bridge the gap between high-fidelity biometric hardware and daily health management through synthetic data simulation, advanced analysis, and agentic intelligence.

---

## Constraints

- Must support HealthyPi 6 (Pi HAT) and HealthyPi Move (Wearable).
- Modular architecture to allow agents to consume trends.
- Integration with existing `./agent-framework` (security-first [multi-agent](../multi-agent) system).
  - **Key Discovery:** Framework already includes Health Agent with HealthKit integration
  - Leverages: NATS broker (TLS 1.3 + ACLs), Orchestrator (LLM planning), Capability tokens (Ed25519)
  - Pattern: Swift collectors (host) → NATS → Python agents (containers) → Orchestrator
- Target platforms: Desktop (Menu Bar) and Apple Ecosystem (iOS/Watch).
- Security-first design: capability-based authorization, audit trail, container isolation.

---

## Target Outcomes

- Standardized data models for multi-modal biometrics.
- A "Virtual Patient" for hardware-free development.
- Agentic tools for real-time health coaching.
- Seamless visualization across desktop and mobile.

---

## Current Milestone: v1.1 Hardware Ingest (HealthyPi 6 + Move)

**Goal:** Connect real HealthyPi hardware streams into the existing NATS-first pipeline so analysis, agents, and Apple/Desktop clients can run on live data (not just simulator output).

**Target features:**
- HealthyPi 6 ingest path (serial/USB) -> normalize -> publish to `biometric.raw.*` and/or `health.healthypi.*`
- HealthyPi Move ingest path (BLE) -> normalize -> publish to `biometric.raw.*` and/or `health.healthypi.*`
- A unified ingest CLI/service with reconnection, timestamping, and device metadata
- Minimal end-to-end verification: hardware -> NATS -> analysis -> at least one UI client

*Last updated: 2026-02-20 after starting milestone v1.1 planning*

---

## Current Status

** 2026-02-20 - v1.1 roadmap created

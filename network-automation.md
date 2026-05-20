---
layout: default
title: Network Automation
description: A modular toolchain from whiteboard sketch to validated network configuration — topology engine, protocol simulator, configuration compiler, and visualization.
---

# Network Automation

A modular toolchain that takes a network design from whiteboard sketch to
validated, deployable configuration. Each tool handles one stage of the
lifecycle; together they form an end-to-end pipeline. The work grew from PhD
research on automated network configuration and is the largest body of
engineering on this site.

<div class="callout">
<p><strong>This toolchain has a dedicated site.</strong> Network Automation is
now its own project, documented in depth — per-tool detail, demos, and
architecture — at its <a href="/projects"><!-- TODO: replace /projects with the dedicated automation site URL -->dedicated site</a>.
The summary below covers the shape of the system; the full treatment lives
there.</p>
</div>

![Network Simulator running OSPF convergence](/images/netsim-basic-demo.gif)
*OSPF convergence in the Network Simulator — one stage in the pipeline.*

---

## Pipeline

<div class="mermaid">
flowchart TD
    BF["Brownfield CLI"] --> TG
    GF["Greenfield Design"] --> TG
    TG["Topology Generation<br/><small>TopoGen · Config Parsing</small>"]
    TG --> MOD["Modeling &amp; Queries<br/><small>Modeling Library + NTE</small>"]
    MOD --> CFG["Config Generation<br/><small>Config Framework</small>"]
    MOD --> SIM["Protocol Simulation<br/><small>Simulator</small>"]
    CFG --> DEP["Device Deploy &amp; Test"]
    SIM --> PERF["Performance Simulation"]
    DEP --> VIS["Visualization &amp; Analysis<br/><small>Visualization Engine · Workbench · Analysis Engine</small>"]
    PERF --> VIS
</div>

---

## The Toolchain in Brief

Four Rust engines form the core:

- **[Network Topology Engine](/projects/ank-nte)** — a graph engine (14-crate
  workspace, petgraph `StableDiGraph`) that keeps every topological mutation
  structurally sound.
- **[Network Simulator](/projects/netsim)** — a deterministic, tick-based
  protocol simulator that validates OSPF, IS-IS, and BGP routing before
  deployment.
- **[Network Configuration Framework](/projects/ank-netcfg)** — compiles
  vendor-neutral graph models into device configurations for Arista EOS and
  Cisco IOS-XR.
- **[Network Visualization Engine](/projects/netvis)** — a layout engine for
  dense, multi-layer topologies, with SVG, PDF, and PNG output and browser
  embedding via WASM.

Seven supporting tools cover brownfield ingestion, topology generation, device
interaction, performance simulation, and formal analysis. [Browse the network
projects →](projects)

---

## Foundations

The toolchain compiles declarative intent into validated device configurations
through formal graph transformations — an idea that started in the thesis-era
research.

- **[Network Modeling Foundations](/projects/autonetkit-foundation)** — the
  original research establishing the core abstractions.
- **[AutoNetKit](/projects/autonetkit)** — legacy configuration generation from
  that work.
- **[Tick-Based Determinism vs. Full Emulation](/insights/tick-based-determinism)**
  — why the simulator uses a custom Rust tick engine instead of Containerlab.

---

[← Back to Projects](projects) | [Signal Processing](signal-processing) | [Photography](photography) | [Data & Analytics](data-analytics) | [Autonomous Systems](agentic-systems)

---
layout: default
---

# Simon Knight

Telecommunications and software engineer based in Adelaide, South Australia. I build tools for modeling, simulating, and coordinating complex systems — turning architectural intent into working infrastructure.

My focus is structural clarity at scale: deterministic protocol simulators, graph topology engines, and multi-agent coordination systems. Each project starts from research (my PhD work on automated network configuration) and ships as working software.

**[Explore the Network Automation Toolchain](network-automation)**

## Featured Work

<div class="project-grid">
<div class="project-card">
  <h3 class="card-title"><a href="/projects/ank-nte">Network Topology Engine</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Graph engine (14-crate workspace, petgraph StableDiGraph) ensuring every topological mutation is structurally sound. Pluggable datastores: Polars, DuckDB, Lite.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netsim">Network Simulator</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Deterministic, tick-based protocol simulator that validates routing configurations (OSPF, IS-IS, BGP) before deployment. Same topology, same results — every time.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/ank-netcfg">Network Configuration Framework</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Compiles vendor-neutral graph models into device-specific configurations (Arista EOS, Cisco IOS-XR) through a deterministic blueprint-to-template pipeline.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/netvis">Visualization Engine</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
  <p class="card-description">Layout engine for dense, multi-layer network topologies. Edge bundling, hierarchical stacking, and SVG/PDF/PNG output with browser embedding via WASM.</p>
</div>
</div>

## Background

Bachelor of Engineering (Telecommunications, First Class Honours) and Bachelor of Economics from the University of Adelaide. PhD in Computer Science (2017) from the University of South Australia, where I developed the AutoNetKit modeling framework for automated network configuration.

- [Read my PhD thesis](thesis)
- [View CV](cv)

[View all projects](projects)

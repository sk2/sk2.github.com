---
layout: default
section: network-automation
---

# Topology Generator

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

## Contents

- [Interactive Playground (WASM Mock Demo)](#interactive-playground-wasm-mock-demo)
- [Technical Reports](#technical-reports)
- [Code Samples](#code-samples)
- [Quick start](#quick-start)
- [Examples (by use case)](#examples-by-use-case)
- [Python examples (by use case)](#python-examples-by-use-case)
- [Topology type mapping](#topology-type-mapping)
- [Validation policy](#validation-policy)
- [Usage](#usage)
- [Concept](#concept)
- [Current Milestone: v1.5 - Intent-Based Overlays & Schematic Enrichment](#current-milestone-v15-intent-based-overlays-schematic-enrichment)
- [Latest Release: v1.4 Interactive Editing & Incremental Validation (shipped 2026-03-02)](#latest-release-v14-interactive-editing-incremental-validation-shipped-2026-03-02)
- [Next Milestone Goals](#next-milestone-goals)
- [Requirements](#requirements)
- [Context](#context)
- [Constraints](#constraints)
- [Key Decisions](#key-decisions)
- [Ecosystem Context](#ecosystem-context)

## Interactive Playground (WASM Mock Demo)

This interactive widget demonstrates the core generation algorithms, running locally in your browser. 

<div class="playground-container" style="background: #1e1e2e; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <div style="display: flex; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px;">
      <h4 style="margin-top: 0; color: #cdd6f4;">Generator Settings</h4>
      <label style="color: #a6adc8; font-size: 14px; display: block; margin-bottom: 5px;">Algorithm</label>
      <select id="topo-algo" style="width: ; padding: 8px; border-radius: 4px; border: 1px solid #45475a; background: #313244; color: #cdd6f4; margin-bottom: 15px;">
        <option value="spine-leaf">Spine-Leaf Data Center</option>
        <option value="barabasi">Barabási-Albert (Scale-Free)</option>
        <option value="erdos">Erdős-Rényi (Random)</option>
      </select>
      
      <label style="color: #a6adc8; font-size: 14px; display: block; margin-bottom: 5px;">Node Count: <span id="node-count-val">50</span></label>
      <input type="range" id="topo-nodes" min="10" max="200" value="50" style="width: ; margin-bottom: 15px;">
      
      <button id="topo-gen-btn" style="background: #89b4fa; color: #11111b; border: none; padding: 10px 20px; border-radius: 4px; font-weight: 600; cursor: pointer; width: ;">Generate Topology</button>
    </div>
    
    <div style="flex: 2; min-width: 300px; background: #11111b; border-radius: 6px; position: relative; height: 300px; overflow: hidden;">
       <canvas id="topo-canvas" width="600" height="300" style="width: ; height: ;"></canvas>
       <div id="topo-stats" style="position: absolute; bottom: 10px; left: 10px; color: #a6adc8; font-size: 12px; font-family: monospace;">
         Nodes: 0 | Edges: 0 | Gen Time: 0ms
       </div>
    </div>
  </div>
</div>

<script>
  // Simple force-directed graph simulation to mock the WASM output visually
  document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('topo-canvas');
    const ctx = canvas.getContext('2d');
    const btn = document.getElementById('topo-gen-btn');
    const algoSelect = document.getElementById('topo-algo');
    const nodesInput = document.getElementById('topo-nodes');
    const nodesVal = document.getElementById('node-count-val');
    const stats = document.getElementById('topo-stats');
    
    let nodes = [];
    let edges = [];
    let animationId;
    
    const resize = () => {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    };
    window.addEventListener('resize', resize);
    resize();
    
    nodesInput.addEventListener('input', (e) => { nodesVal.textContent = e.target.value; });
    
    const generate = () => {
      cancelAnimationFrame(animationId);
      const numNodes = parseInt(nodesInput.value);
      const algo = algoSelect.value;
      const start = performance.now();
      
      nodes = Array.from({length: numNodes}, (_, i) => ({
        id: i,
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: 0, vy: 0
      }));
      edges = [];
      
      if (algo === 'barabasi') {
        for (let i = 1; i < numNodes; i++) {
          const targets = Math.min(i, 2);
          for (let j = 0; j < targets; j++) {
            const target = Math.floor(Math.random() * i);
            edges.push({source: i, target: target});
          }
        }
      } else if (algo === 'spine-leaf') {
        const spines = Math.max(2, Math.floor(numNodes * 0.2));
        const leaves = numNodes - spines;
        for (let i = 0; i < leaves; i++) {
          for (let j = 0; j < spines; j++) {
            edges.push({source: i, target: leaves + j});
          }
        }
      } else {
        const p = 4 / numNodes;
        for (let i = 0; i < numNodes; i++) {
          for (let j = i + 1; j < numNodes; j++) {
            if (Math.random() < p) edges.push({source: i, target: j});
          }
        }
      }
      
      const end = performance.now();
      stats.textContent = `Nodes: ${nodes.length} | Edges: ${edges.length} | Gen Time: ${(end-start).toFixed(2)}ms`;
      
      simulate();
    };
    
    const simulate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          let dx = nodes[j].x - nodes[i].x;
          let dy = nodes[j].y - nodes[i].y;
          let dist = Math.sqrt(dx*dx + dy*dy) || 1;
          if (dist < 80) {
            let force = 60 / (dist * dist);
            nodes[i].vx -= (dx/dist) * force;
            nodes[i].vy -= (dy/dist) * force;
            nodes[j].vx += (dx/dist) * force;
            nodes[j].vy += (dy/dist) * force;
          }
        }
      }
      
      edges.forEach(e => {
        let n1 = nodes[e.source];
        let n2 = nodes[e.target];
        let dx = n2.x - n1.x;
        let dy = n2.y - n1.y;
        let dist = Math.sqrt(dx*dx + dy*dy) || 1;
        let force = (dist - 40) * 0.05;
        n1.vx += (dx/dist) * force;
        n1.vy += (dy/dist) * force;
        n2.vx -= (dx/dist) * force;
        n2.vy -= (dy/dist) * force;
      });
      
      ctx.strokeStyle = 'rgba(166, 173, 200, 0.3)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      
      nodes.forEach(n => {
        n.vx += (canvas.width/2 - n.x) * 0.02;
        n.vy += (canvas.height/2 - n.y) * 0.02;
        n.x += n.vx * 0.5;
        n.y += n.vy * 0.5;
        n.vx *= 0.8;
        n.vy *= 0.8;
      });
      
      edges.forEach(e => {
        ctx.moveTo(nodes[e.source].x, nodes[e.source].y);
        ctx.lineTo(nodes[e.target].x, nodes[e.target].y);
      });
      ctx.stroke();
      
      ctx.fillStyle = '#f38ba8';
      nodes.forEach(n => {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 3, 0, Math.PI * 2);
        ctx.fill();
      });
      
      animationId = requestAnimationFrame(simulate);
    };
    
    btn.addEventListener('click', generate);
    setTimeout(generate, 500);
  });
</script>

---

## Technical Reports

- [Download Technical Report: topogen-techreport.pdf](/assets/docs/topogen-topogen-techreport.pdf)

---

## Code Samples

### README.md

```markdown
# TopoGen Example Gallery

Curated config examples live under `examples/configs/`.
They are organized primarily by use case (directory) and are safe to copy/paste.

Each config starts with an annotated header block showing how to run it and which knobs to tweak.

## Quick start

```bash
topogen generate examples/configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml --output topology.yaml
topogen validate topology.yaml
```

## Examples (by use case)

### `datacenter-lab/`

- `examples/configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml`
  - Small fat-tree (k=4) with `vendor: cisco` to demonstrate interface renaming.
- `examples/configs/datacenter-lab/leaf-spine--lab-2spine-4leaf-100g--seed42.yaml`
  - Tiny leaf-spine fabric for quick validation and iteration.
- `examples/configs/datacenter-lab/fat-tree--lab-k4--seed42.toml`
  - Same basic fat-tree lab scenario in TOML format.

### `datacenter-scale/`

- `examples/configs/datacenter-scale/fat-tree--scale-k8--seed7.yaml`
  - Larger fat-tree (k=8) for scale/perf testing.
- `examples/configs/datacenter-scale/leaf-spine--prod-4spine-16leaf-400g--seed99.yaml`
  - Higher-capacity leaf-spine with a redundant spine layer.

### `regional-backbone/`

- `examples/configs/regional-backbone/ring--na-8nodes-modern--seed42.yaml`
  - Regional WAN ring constrained to NA with a modern bandwidth profile.

### `global-backbone/`

- `examples/configs/global-backbone/mesh--global-6nodes-tier1-modern--seed42.yaml`
  - Small Tier-1 full-mesh backbone for all-to-all connectivity experiments.

### `enterprise-wan/`

- `examples/configs/enterprise-wan/hierarchical--na-eu-20nodes-variable-standard--seed4242.yaml`
  - Multi-region (NA+EU) hierarchical WAN with variable bandwidth and standard redundancy.

### `modeling/`

- `examples/configs/modeling/barabasi-albert--scale-free-n100-m3--seed42.yaml`
  - Scale-free (hub-heavy) random graph model.
- `examples/configs/modeling/watts-strogatz--small-world-n100-k6-beta0.1--seed42.yaml`
  - Small-world random graph model with rewiring.
- `examples/configs/modeling/erdos-renyi--gnp-n50-p0.2--seed42.yaml`
  - Baseline Erdos-Renyi G(n, p) model.

## Python examples (by use case)

Runnable scripts live under `examples/python/` and are organized by the same use-case directory names as the config gallery.

Notes:

- Scripts print stable stdout: `nodes=... edges=...` or `OK`.
- If a script writes outputs, it respects `TOPOGEN_EXAMPLE_OUT_DIR` (otherwise uses a temp dir).

### `datacenter-lab/`

- `examples/python/datacenter-lab/generate_fat_tree__k4_cisco_seed42.py`
  - Small fat-tree (k=4) with Cisco interface naming.
- `examples/python/datacenter-lab/generate_leaf_spine__2spine_4leaf_100g_seed42.py`
  - Tiny leaf-spine fabric for quick experiments.

### `datacenter-scale/`

- `examples/python/datacenter-scale/generate_fat_tree__k8_seed7.py`
  - Larger fat-tree (k=8) for scale/perf sanity checks.
- `examples/python/datacenter-scale/generate_leaf_spine__4spine_16leaf_400g_seed99.py`
  - Higher-capacity leaf-spine with 400G spine links.

### `regional-backbone/`

- `examples/python/regional-backbone/generate_ring__na_8nodes_seed42.py`
  - Regional WAN ring constrained to NA.

### `global-backbone/`

- `examples/python/global-backbone/generate_mesh__global_6nodes_seed42.py`
  - Small WAN mesh topology (all-to-all).

### `enterprise-wan/`

- `examples/python/enterprise-wan/generate_hierarchical_wan__na_eu_20nodes_seed4242.py`
  - Multi-region (NA+EU) hierarchical WAN with standard redundancy.

### `modeling/`

- `examples/python/modeling/generate_barabasi_albert__n100_m3_seed42.py`
  - Scale-free random graph model.
- `examples/python/modeling/generate_watts_strogatz__n100_k6_beta0.1_seed42.py`
  - Small-world random graph model.
- `examples/python/modeling/generate_erdos_renyi__n50_p0.2_seed42.py`
  - Baseline Erdos-Renyi G(n, p) model.

### `workflows/`

- `examples/python/workflows/workflow_generate_export_restore_isomorphic.py`
  - End-to-end: generate -> export YAML -> restore -> isomorphism check.

### `parity/` (manual-only)

- `examples/python/parity/seeded_cli_vs_python_isomorphism.py`
  - Seeded parity demo comparing `topogen generate <config>` output with Python API output.

## Topology type mapping

Use-case directories map back to roadmap topology types as follows:

- Datacenter: `datacenter-lab/`, `datacenter-scale/`
  - Generators: `fat-tree`, `leaf-spine`
- WAN: `regional-backbone/`, `global-backbone/`, `enterprise-wan/`
  - Generators: `ring`, `mesh`, `hierarchical`
- Random graphs: `modeling/`
  - Generators: `barabasi-albert`, `watts-strogatz`, `erdos-renyi`

## Validation policy

By default, CI runs a smoke subset of example configs driven by `examples/SMOKE.yaml`.

Maintainers can run the full suite (including ignored tests) locally:

```bash
cargo test --test examples_configs -- --ignored
```

Python example validation is opt-in (to keep CI fast):

```bash
TOPOGEN_RUN_ALL_EXAMPLES=1 python -m pytest -q
```

```

### SMOKE.yaml

```yaml
# Authoritative smoke subset of example artifacts executed in CI by default.
#
# Paths are repo-relative.

configs:
  # Datacenter
  - examples/configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml
  # Multi-layer
  - examples/configs/multi-layer-pop-backbone.yaml
  # WAN
  - examples/configs/regional-backbone/ring--na-8nodes-modern--seed42.yaml
  # Access ISP
  - examples/configs/access-isp/eyeball--regional-1k-subscribers--seed42.yaml
  # Random
  - examples/configs/modeling/barabasi-albert--scale-free-n100-m3--seed42.yaml
  - examples/configs/modeling/erdos-renyi--gnp-n50-p0.2--seed42.yaml

python:
  # Datacenter
  - examples/python/datacenter-lab/generate_fat_tree__k4_cisco_seed42.py
  - examples/python/datacenter-lab/generate_leaf_spine__2spine_4leaf_100g_seed42.py
  # WAN
  - examples/python/regional-backbone/generate_ring__na_8nodes_seed42.py
  - examples/python/global-backbone/generate_mesh__global_6nodes_seed42.py
  - examples/python/enterprise-wan/generate_hierarchical_wan__na_eu_20nodes_seed4242.py
  # Access ISP
  - examples/python/access-isp/generate_eyeball__regional_1k_seed42.py
  # Random
  - examples/python/modeling/generate_barabasi_albert__n100_m3_seed42.py
  - examples/python/modeling/generate_watts_strogatz__n100_k6_beta0.1_seed42.py
  - examples/python/modeling/generate_erdos_renyi__n50_p0.2_seed42.py
  # Workflow
  - examples/python/workflows/workflow_generate_export_restore_isomorphic.py
  - examples/python/workflows/workflow_multilayer_pop_to_containerlab.py
  - examples/python/workflows/workflow_eyeball_to_autonetkit.py

```

### eyeball--regional-1k-subscribers--seed42.yaml

```yaml
# Title: Eyeball access ISP (regional template, 1k subscribers)
# Goal: Access ISP hierarchy (access -> aggregation -> core) with peering/transit endpoints.
# Run:
#   topogen generate --config examples/configs/access-isp/eyeball--regional-1k-subscribers--seed42.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - subscriber_count: number of subscriber host nodes.
#   - template: small-isp|regional-isp|large-isp|mobile-network.
#   - tiers: 3|4.

name: eyeball-regional-1k
seed: 42

type: eyeball
template: regional-isp
subscriber_count: 1000
tiers: 3
redundancy: standard
peering_to_transit_split: 0.7

```

### fat-tree--lab-k4-cisco--seed42.yaml

```yaml
# Title: Fat-tree lab (k=4, Cisco interface names)
# Goal: Small, realistic datacenter topology for labs and demos.
# Run:
#   topogen generate examples/configs/datacenter-lab/fat-tree--lab-k4-cisco--seed42.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - k: even >= 2; controls size (pods and switch counts).
#   - vendor: cisco|arista|juniper|default (interface naming convention).
#   - core_bandwidth_gbps / agg_bandwidth_gbps: link bandwidths in Gbps.

name: dc-lab-fat-tree-k4-cisco
seed: 42
vendor: cisco

type: fat-tree
k: 4
core_bandwidth_gbps: 400.0
agg_bandwidth_gbps: 100.0

```

### leaf-spine--lab-2spine-4leaf-100g--seed42.yaml

```yaml
# Title: Leaf-spine lab (2 spines, 4 leaves, 100G)
# Goal: A compact 2-tier Clos for lab validation and quick iteration.
# Run:
#   topogen generate examples/configs/datacenter-lab/leaf-spine--lab-2spine-4leaf-100g--seed42.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - spines / leaves: scale the fabric size.
#   - spine_bandwidth_gbps: leaf<->spine bandwidth in Gbps.
#   - full_mesh: set false for partial connectivity experiments.

name: dc-lab-leaf-spine-2s-4l-100g
seed: 42

type: leaf-spine
spines: 2
leaves: 4
full_mesh: true
spine_bandwidth_gbps: 100.0

```

### fat-tree--scale-k8--seed7.yaml

```yaml
# Title: Fat-tree scale (k=8)
# Goal: Production-scale fat-tree to test larger fabrics and performance.
# Run:
#   topogen generate examples/configs/datacenter-scale/fat-tree--scale-k8--seed7.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - k: even >= 2; k=8 creates 80 switches.
#   - core_bandwidth_gbps / agg_bandwidth_gbps: link bandwidths in Gbps.

name: dc-scale-fat-tree-k8
seed: 7

type: fat-tree
k: 8
core_bandwidth_gbps: 400.0
agg_bandwidth_gbps: 400.0

```

### leaf-spine--prod-4spine-16leaf-400g--seed99.yaml

```yaml
# Title: Leaf-spine production (4 spines, 16 leaves, 400G)
# Goal: Modern, redundant spine layer with higher-speed fabric links.
# Run:
#   topogen generate examples/configs/datacenter-scale/leaf-spine--prod-4spine-16leaf-400g--seed99.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - spines / leaves: scale redundancy and rack count.
#   - spine_bandwidth_gbps: leaf<->spine bandwidth in Gbps.

name: dc-prod-leaf-spine-4s-16l-400g
seed: 99

type: leaf-spine
spines: 4
leaves: 16
full_mesh: true
spine_bandwidth_gbps: 400.0

```

### hierarchical--na-eu-20nodes-variable-standard--seed4242.yaml

```yaml
# Title: Enterprise WAN (hierarchical, NA+EU, 20 nodes)
# Goal: Multi-region 3-tier WAN (access/distribution/core) with realistic link profiles.
# Run:
#   topogen generate examples/configs/enterprise-wan/hierarchical--na-eu-20nodes-variable-standard--seed4242.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - node_count: total WAN sites/POPs.
#   - regions: which geo regions are included.
#   - bandwidth_profile: modern|variable.
#   - redundancy: minimal|standard|high.

name: enterprise-wan-na-eu-20
seed: 4242

type: hierarchical
node_count: 20
regions: ["NA", "EU"]
bandwidth_profile: variable
redundancy: standard

```

### mesh--global-6nodes-tier1-modern--seed42.yaml

```yaml
# Title: Global backbone mesh (6 nodes, Tier-1, modern)
# Goal: Small full-mesh backbone for CDN / Tier-1 interconnect experiments.
# Run:
#   topogen generate examples/configs/global-backbone/mesh--global-6nodes-tier1-modern--seed42.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - node_count: size of the mesh.
#   - city_tier: 1|2|3 (Tier-1 are major global hubs).
#   - bandwidth_profile: modern|variable.

name: wan-global-mesh-6-tier1-modern
seed: 42

type: mesh
node_count: 6
city_tier: 1
bandwidth_profile: modern

```

### barabasi-albert--scale-free-n100-m3--seed42.yaml

```yaml
# Title: Scale-free graph (Barabasi-Albert, n=100, m=3)
# Goal: Model a hub-heavy network with a power-law-ish degree distribution.
# Run:
#   topogen generate examples/configs/modeling/barabasi-albert--scale-free-n100-m3--seed42.yaml --output topology.yaml
#   topogen validate topology.yaml
# Tweak:
#   - n: number of nodes.
#   - m: new edges per node (higher m -> denser graph).

name: modeling-ba-n100-m3
seed: 42

type: barabasi-albert
n: 100
m: 3

```

---

## Usage

### Topology DSL Example

```yaml
# Example: Multi-layer POP underlay with mesh overlay
name: multi-layer-pop-backbone
type: multi-layer

layers:
  - name: physical
    type: pop
    count: 5
    redundancy: n+1

  - name: backbone
    type: mesh
    node_count: 4
    underlay: physical
    strategy: shortest-path
```

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |

---

## Concept

A Rust-based network topology generator with Python bindings that consolidates scattered topology generation logic from AutoNetKit, simulation tools, and visualization tools. Generates realistic data center, WAN, and random graph topologies with proper structure, design patterns, and realistic parameters. Outputs custom YAML format for use across the network engineering tool ecosystem.

Network engineers can quickly generate realistic, validated network topologies without implementing complex algorithms from scratch.

---

## Current Milestone: v1.5 - Intent-Based Overlays & Schematic Enrichment

**Goal:** Transform topologies from simple graphs into rich semantic models by formalizing intent-based "overlays" and hierarchical design patterns.

**Target features:**
- **Multi-Overlay Tagging**: Formalize `BGP`, `OSPF`, and `Physical` overlay properties on nodes/edges.
- **Intent-Based Role Assignment**: Automatically tag roles (`spine`/`leaf`, `p`/`pe`/`rr`, `provider`/`customer`) in all generators.
- **Schematic Grouping**: Formalize "Site", "Pod", and "Zone" hierarchies to support downstream visual grouping.
- **Relationship Intent**: Tag edges with semantic relationships (`peering`, `upstream`, `transit`) and `SRLG` (fate-sharing) intent.
- **Whiteboard-Level Property Mapping**: Ensure property names and structures align with AutoNetKit (ANK) whiteboard expectations.

---

## Latest Release: v1.4 Interactive Editing & Incremental Validation (shipped 2026-03-02)



---

## Next Milestone Goals

- Define v1.1 requirements (fresh `.planning/REQUIREMENTS.md`)
- Execute v1.1 Perf+Stability milestone

---

## Requirements



---

## # Validated

**v1.0-alpha :**
- ✓ Generate data center topologies (fat-tree, leaf-spine) — v1.0-alpha
- ✓ Generate WAN/backbone topologies (ring, mesh, hierarchical) — v1.0-alpha
- ✓ Generate random graph topologies (Erdős-Rényi, Barabási-Albert, Watts-Strogatz) — v1.0-alpha
- ✓ Output custom YAML format with nodes, edges, interfaces, and attributes — v1.0-alpha
- ✓ YAML format stores interfaces under nodes (not edge-centric) — v1.0-alpha
- ✓ Python bindings for programmatic topology generation — v1.0-alpha
- ✓ Validate generated topologies (structural correctness) — v1.0-alpha
- ✓ Validate graph properties (degree distribution, clustering, diameter) — v1.0-alpha
- ✓ Validate design pattern compliance (topology-specific rules) — v1.0-alpha
- ✓ Realistic parameters (bandwidth, latency appropriate for DC vs WAN) — v1.0-alpha
- ✓ Topologies follow network design best practices — v1.0-alpha

**v0.9 :**
- ✓ CLI tool for command-line topology generation — v0.9
- ✓ Config file driven generation (YAML/TOML input) — v0.9
- ✓ Vendor-specific interface naming conventions — v0.9
- ✓ Example topology gallery with sample configs — v0.9
- ✓ Algorithm documentation with parameter guidance — v0.9
- ✓ Typed Python exception hierarchy for better error handling — v0.9
- ✓ Installation guide and quickstart tutorial — v0.9
- ✓ Complete user documentation (CLI, Python API, config files) — v0.9
- ✓ Technical documentation with algorithm formulations and complexity analysis — v0.9
- ✓ Enhanced CLI help text with parameter ranges and examples — v0.9
- ✓ Shell completions for bash, zsh, and fish — v0.9
- ✓ Improved error messages with JSON diagnostics — v0.9
- ✓ Cross-interface parity tests and consistency validation — v0.9

**v0.10 :**
- ✓ Expose Erdos-Renyi generator via CLI, config, and Python API — v0.10
- ✓ Integrate topology-specific structural validators into validation flows — v0.10
- ✓ Complete .10

---

## # Active

**v1.1 Perf+Stability:**
- [ ] Improve large-topology performance across generators, validation, and exporters
- [ ] Add stable performance regression coverage (non-flaky, budgeted)
- [ ] Reduce memory spikes in large runs (generation + export)
- [ ] Improve CLI-level predictability for large workflows (clear limits, consistent diagnostics)

---

## # Deferred / Tech Debt

- Stderr/diagnostics contract consistency: make "stderr empty on success" true everywhere; migrate remaining ad-hoc stderr output into structured warning/reporting.

---

## # Out of Scope

- GNN-based topology generation — Future: graph neural network based generation (research-heavy)
- AutoNetKit loop-back integration — Future: use AutoNetKit itself to generate multi-layer topologies
- Interactive visualization — Handled by separate visualization tool in ecosystem
- Real-time topology updates — Future: dynamic topology modification APIs
- Topology diff/merge — Future: version control for topology configs

---

## Context

**Consolidation:** Topology generation code currently exists in three separate places:
- AutoNetKit (graph-based topology generation)
- Simulation engine (topology setup for network simulation)
- Visualization tool (topology generation for network diagrams)

This tool unifies that logic into a single, high-performance library.

**Integration:** Will likely become a dependency or part of the AutoNetKit workflow engine in the future. Designed to be the "whiteboard view" that other tools build from.

**Architecture Model:** Following AutoNetKit's "whiteboard" concept - one graph with annotations where interfaces are stored under nodes in the YAML format rather than edge-centric representation. This is more extensible than classical graph interchange formats.

**Users:**
- Primary: Network engineers who need realistic topologies for testing, validation, and simulation
- Secondary: Research community (though they often have their own methodologies)
- Internal: The tool ecosystem (AutoNetKit, simulation engine, visualization tools)

**Inspirations:**
- NetworkX AS-level graph generation
- Topology Zoo examples
- Network design best practices and patterns
- ContainerLab YAML format (but defining our own optimized structure)

---

## Constraints

- **Tech Stack - Core**: Rust for performance (fast generation of large topologies) and cross-platform binary distribution
- **Tech Stack - Bindings**: Python bindings required for integration with existing Python-based tools in the ecosystem
- **Output Format**: Custom YAML format (not constrained to existing formats, can design ideal structure)

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust core + Python bindings | Performance for large topology generation + cross-platform binary, while maintaining Python integration for existing tool ecosystem | ✓ Good - PyO3 FFI works well, maturin build smooth |
| Custom YAML format for v1 | Design ideal format for this use case, build converters to other formats (ContainerLab, AutoNetKit) later | ✓ Good - Interface-centric model proved extensible |
| Interfaces under nodes (not edge-centric) | Following AutoNetKit whiteboard model - more extensible than classical graph formats for network topologies with device types, interface naming, future BGP sessions/VPNs | ✓ Good - More natural for network topology use cases |
| All three interfaces (CLI, Python API, config-driven) | Maximum flexibility - engineers want CLI for quick generation, Python API for workflow integration, config files for complex/repeatable setups | ✓ Good - Parity tests ensure consistency |
| Documentation-first for v0.9 | Focus on making existing functionality discoverable rather than adding new features | ✓ Good - mdBook + doc-tests prevent drift |
| InterfaceSpec source-of-truth | Centralized parameter metadata prevents interface drift | ✓ Good - Parity tests validate automatically |

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. topogen provides topology generation — the "generate" stage of the pipeline.

**Role:** Generate realistic, validated network topologies with vendor naming, geographic placement, and traffic matrices. Feed topologies into [ank-pydantic](../ank-pydantic) (modeling), [netsim](../netsim) (simulation), [netflowsim](../netflowsim) (traffic analysis), and [netvis](../netvis) (visualization).

**Key integration points:**
- Exports to [ank-pydantic](../ank-pydantic) via AutoNetKit YAML (with topology_type, tier, role, region metadata)
- Exports to [netsim](../netsim) directly ([netsim](../netsim) YAML with device/wire/traffic structure)
- Exports to ContainerLab YAML for lab deployment
- Traffic matrix (CSV/JSON) feeds [netflowsim](../netflowsim)
- GeoJSON export for geographic visualization in [netvis](../netvis)

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities
- [Cross-Project Data Contracts](ARCHITECTURE.md) — ownership boundaries and format specifications

*Last updated: 2026-02-21 after v1.1 milestone start*

---

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

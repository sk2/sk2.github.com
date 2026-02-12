---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 59/62 (100%)</span>

[← Back to Projects](../projects)

---


## The Insight

Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **ank-pydantic** eliminates this trade-off by using Pydantic for schema validation and a high-performance Rust core (`petgraph`) for graph traversals.

## Quick Facts

| | |
|---|---|
| **Status** | Phase 59/62 (99%) |
| **Language** | Python, Rust |
| **Started** | 2026 |

---

## What This Is

A Python library for modeling and querying network topologies with type-safe Pydantic models and a high-performance Rust core. Think of it as SQLAlchemy for network topologies — expressive Python API backed by blazing-fast graph algorithms.

## Key Features

- **Two-Stage Transformation Model**: Whiteboard (sketch) → Plan (logical) → Protocol Layers (physical)
- **Type-Safe Models**: Pydantic validation ensures correct topology structure at design time
- **Lazy Query API**: Composable queries with Rust-backed execution (powered by `petgraph`)
- **Batteries-Included Blueprints**: Pre-built domain models for ISIS, MPLS, EVPN, L3VPN, IXP
- **Rust Core (`ank_nte`)**: Graph operations run at native speed with Python FFI bindings

## Examples

### Service Provider Core: IS-IS + MPLS + iBGP

Build a multi-vendor service provider topology with protocol layers:

```python
from ank_pydantic import Topology
from ank_pydantic.blueprints.designs.isis import build_isis_layer
from ank_pydantic.blueprints.designs.mpls import build_mpls_layer

# Load topology from YAML (16 devices: 8 core, 6 PE, 2 RR)
topology = Topology.from_yaml("transitnet.yaml")

# Build IS-IS Layer 2 flat domain
isis_layer = build_isis_layer(
    topology,
    level=2,
    area="49.0001",
    parent_layer="physical"
)

# Build MPLS/LDP following IS-IS adjacencies
mpls_layer = build_mpls_layer(
    topology,
    igp_layer="isis",
    layer_name="mpls"
)

# Verify layers created
print(f"IS-IS routers: {isis_layer.nodes().count()}")  # 16
print(f"MPLS nodes: {mpls_layer.nodes().count()}")     # 16
print(f"LDP sessions: {mpls_layer.edges().count()}")   # 14
```

**Protocol Stack Generated:**
- **Physical Layer**: 16 routers, 14 links across 4 PoPs
- **IS-IS Layer**: Level 2 adjacencies, auto-generated NETs from loopbacks
- **MPLS Layer**: LDP sessions on all IS-IS adjacencies
- **iBGP Layer**: Route reflector topology (PEs → RRs)

### L3VPN Configuration

Build L3VPN service layers with VRF assignments:

```python
from ank_pydantic.blueprints.designs.l3vpn import build_l3vpn_layer

# Build L3VPN service for customer NetCorp
l3vpn_layer = build_l3vpn_layer(
    topology,
    service_name="NetCorp-L3VPN",
    customer="NetCorp",
    customer_asn=65100,
    provider_asn=65000,
    vpn_id=100
)

# VRF configuration automatically applied to PE nodes
# PE-CE links identified and marked with BGP session data
print(f"PE nodes with VRF: {l3vpn_layer.nodes().where(role='pe').count()}")
print(f"PE-CE links: {l3vpn_layer.edges().count()}")
```

**Generated Configuration:**
- **VRF Name**: `NETCORP`
- **Route Distinguisher**: `65000:100`
- **Route Targets**: `65000:100` (import/export)
- **PE-CE Sessions**: eBGP with customer ASN 65100

### Containerlab Deployment

Export topology to Containerlab and deploy:

```python
from ank_pydantic.blueprints.environments import get_environment

# Get Containerlab compiler
env = get_environment('containerlab')

# Generate Containerlab topology file
artifacts = env.generate(topology)

# Write topology file
with open("transitnet.clab.yml", "w") as f:
    f.write(artifacts.files['topology.clab.yml'])
```

Deploy to Containerlab:

```bash
# Deploy topology
sudo containerlab deploy -t transitnet.clab.yml

# Verify deployment
sudo containerlab inspect -t transitnet.clab.yml

# Test IS-IS neighbors on P1
docker exec -it clab-transitnet-P1 show isis neighbors

# Verify LDP sessions
docker exec -it clab-transitnet-P1 show mpls ldp neighbor

# Test end-to-end connectivity (PE1 → PE6)
docker exec -it clab-transitnet-PE1 ping 10.0.0.16
```

**Output Format:**
- Multi-vendor support (Cisco IOS-XR, Juniper Junos)
- Management network auto-configured (172.20.20.0/24)
- Volume mounts for configs
- Interface mappings preserved

### Query API Usage

Composable queries with Rust-backed execution:

```python
# Find all core routers in North PoP
core_routers = topology.query.nodes().where(
    lambda n: n.data.role == "core" and n.data.pop == "North"
).models()

# Get links between specific sites
inter_pop_links = topology.query.links().where(
    lambda l: l.data.link_type == "long-haul"
).count()

# Find devices requiring MPLS
mpls_devices = topology.layer("mpls").nodes().where(
    mpls_enabled=True
).ids()
```

### Integration with NetVis

Export for visualization:

```python
# Export topology with layout hints
topology.export_for_netvis(
    "output.json",
    layout="hierarchical",
    node_metadata=True
)
```

NetVis applies advanced layout algorithms to produce publication-quality diagrams.

---

## YAML Topology Format

Define topologies in YAML for rapid prototyping:

```yaml
topology:
  - metadata:
      name: TransitNet SP Core
      organisation: TransitNet
      asn: 65000

  - nodes:
      - P1:
          role: core
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.1/32
          endpoints:
            - Gi0/0/0/0  # to P3
            - Gi0/0/0/1  # to P5

      - PE1:
          role: pe
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.11/32
          endpoints:
            - Gi0/0/0/0  # to P1
            - Gi0/0/0/1  # customer-facing

  - links:
      - [P1, Gi0/0/0/0, P3, Gi0/0/0/0]   # West-East
      - [P1, Gi0/0/0/1, P5, Gi0/0/0/0]   # West-North
      - [P1, Gi0/0/0/2, PE1, Gi0/0/0/0]  # Core-PE
```

Load and process:

```python
topology = Topology.from_yaml("transitnet.yaml")

# Apply design functions to derive protocol layers
isis_layer = build_isis_layer(topology, level=2, area="49.0001")
mpls_layer = build_mpls_layer(topology, igp_layer="isis")

# Export to Containerlab
env = get_environment('containerlab')
artifacts = env.generate(topology)
```

---

## Available Blueprints

Pre-built design functions for common network patterns:

| Blueprint | Purpose | Key Features |
|-----------|---------|--------------|
| **IS-IS** | IGP routing | Multi-level (L1, L2, L1/L2), area assignment, NET generation |
| **MPLS/LDP** | Label switching | Follows IGP adjacencies, label range configuration, targeted LDP |
| **L3VPN** | VPN services | VRF configuration, RD/RT generation, PE-CE sessions |
| **EVPN** | L2/L3 overlay | VXLAN, MAC/IP routes, multi-tenancy |
| **IXP** | Peering fabric | Route server, bilateral peering, BGP communities |
| **Data Center** | Spine-leaf | CLOS topology, ECMP, BGP unnumbered |

Each blueprint provides:
- **Layer builder functions** for protocol derivation
- **Pydantic models** for type-safe configuration
- **Query helpers** for network analysis
- **Config templates** for multi-vendor export

---

## Current Status

Feature-complete, final polish and documentation before 1.0 release.

## Tech Stack

Python (Pydantic), Rust core (`petgraph`-backed), PyO3 bindings

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)

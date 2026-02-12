---
layout: default
---

# ank_pydantic

<span class="status-badge status-active">Phase 59/62 (100%)</span>

[← Back to Projects](../projects)

---


## The Concept

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

**Input Topology** (transitnet.yaml):

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
            - Gi0/0/0/2  # to PE1

      - P3:
          role: core
          data:
            pop: East
            platform: iosxr
            loopback: 10.0.0.3/32
          endpoints:
            - Gi0/0/0/0  # to P1
            - Gi0/0/0/2  # to PE3

      - PE1:
          role: pe
          data:
            pop: West
            platform: iosxr
            loopback: 10.0.0.11/32
          endpoints:
            - Gi0/0/0/0  # to P1

  - links:
      - [P1, Gi0/0/0/0, P3, Gi0/0/0/0]   # West-East core
      - [P1, Gi0/0/0/2, PE1, Gi0/0/0/0]  # Core-PE
```

**Build Protocol Layers:**

```python
from ank_pydantic import Topology
from ank_pydantic.blueprints.designs.isis import build_isis_layer
from ank_pydantic.blueprints.designs.mpls import build_mpls_layer

# Load topology from YAML
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
```

**Generated Configuration** (P1 - Cisco IOS-XR):

```cisco
hostname P1
!
interface Loopback0
 ipv4 address 10.0.0.1 255.255.255.255
!
interface GigabitEthernet0/0/0/0
 description to P3
 ipv4 address 10.1.0.1 255.255.255.252
!
interface GigabitEthernet0/0/0/2
 description to PE1
 ipv4 address 10.1.0.5 255.255.255.252
!
router isis CORE
 is-type level-2-only
 net 49.0001.0100.0000.0001.00
 address-family ipv4 unicast
  metric-style wide
 !
 interface Loopback0
  passive
  address-family ipv4 unicast
 !
 interface GigabitEthernet0/0/0/0
  point-to-point
  address-family ipv4 unicast
   metric 10
  !
 !
 interface GigabitEthernet0/0/0/2
  point-to-point
  address-family ipv4 unicast
   metric 10
  !
 !
!
mpls ldp
 router-id 10.0.0.1
 interface GigabitEthernet0/0/0/0
 !
 interface GigabitEthernet0/0/0/2
 !
!
```

**Protocol Stack Generated:**
- **Physical Layer**: Nodes, interfaces, and connections
- **IS-IS Layer**: Level 2 adjacencies, auto-generated NETs from loopbacks
- **MPLS Layer**: LDP sessions on all IS-IS adjacencies, router-id from loopback
- **iBGP Layer**: Route reflector topology (PEs → RRs)

### L3VPN Configuration

**Input:** Add customer sites to PE routers:

```yaml
# Add customer edge routers to topology
- nodes:
    - CE1:
        role: ce
        data:
          organisation: NetCorp
          asn: 65100
          loopback: 192.168.1.1/32
        endpoints:
          - Gi0/0

    - CE2:
        role: ce
        data:
          organisation: NetCorp
          asn: 65100
          loopback: 192.168.2.1/32
        endpoints:
          - Gi0/0

- links:
    - [PE1, Gi0/0/0/1, CE1, Gi0/0]  # PE-CE link
    - [PE3, Gi0/0/0/1, CE2, Gi0/0]  # PE-CE link
```

**Build L3VPN Layer:**

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
```

**Generated VRF Configuration** (PE1):

```cisco
vrf NETCORP
 address-family ipv4 unicast
  import route-target
   65000:100
  !
  export route-target
   65000:100
  !
 !
!
interface GigabitEthernet0/0/0/1
 description to CE1 (NetCorp)
 vrf NETCORP
 ipv4 address 10.100.1.1 255.255.255.252
!
router bgp 65000
 vrf NETCORP
  rd 65000:100
  address-family ipv4 unicast
   redistribute connected
  !
  neighbor 10.100.1.2
   remote-as 65100
   description CE1
   address-family ipv4 unicast
    route-policy NETCORP-IN in
    route-policy NETCORP-OUT out
   !
  !
 !
!
```

**Result:**
- **VRF Name**: `NETCORP`
- **Route Distinguisher**: `65000:100`
- **Route Targets**: `65000:100` (import/export)
- **PE-CE Sessions**: eBGP between PE1↔CE1, PE3↔CE2

### Containerlab Deployment

**Export to Containerlab:**

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

**Generated Containerlab File** (transitnet.clab.yml):

```yaml
name: transitnet
mgmt:
  network: mgmt
  ipv4-subnet: 172.20.20.0/24

topology:
  nodes:
    P1:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.11
      binds:
        - ./configs/P1.cfg:/config/startup-config.cfg

    P3:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.13
      binds:
        - ./configs/P3.cfg:/config/startup-config.cfg

    PE1:
      kind: cisco_xrv9k
      image: vrnetlab/vr-xrv9k:7.3.2
      mgmt-ipv4: 172.20.20.21
      binds:
        - ./configs/PE1.cfg:/config/startup-config.cfg

  links:
    - endpoints: ["P1:Gi0/0/0/0", "P3:Gi0/0/0/0"]
    - endpoints: ["P1:Gi0/0/0/2", "PE1:Gi0/0/0/0"]
```

**Deploy and Verify:**

```bash
# Deploy topology
sudo containerlab deploy -t transitnet.clab.yml

# Verify deployment
sudo containerlab inspect -t transitnet.clab.yml

# Output:
# +---+---------------------+--------------+-------------------+-------+---------+
# | # |        Name         | Container ID |       Image       | Kind  |  State  |
# +---+---------------------+--------------+-------------------+-------+---------+
# | 1 | clab-transitnet-P1  | abc123...    | vr-xrv9k:7.3.2   | xrv9k | running |
# | 2 | clab-transitnet-P3  | def456...    | vr-xrv9k:7.3.2   | xrv9k | running |
# | 3 | clab-transitnet-PE1 | ghi789...    | vr-xrv9k:7.3.2   | xrv9k | running |

# Test IS-IS neighbors on P1
docker exec -it clab-transitnet-P1 show isis neighbors

# Expected output:
# IS-IS CORE neighbors:
# System Id       Interface       SNPA           State  Holdtime Type IETF-NSF
# P3              Gi0/0/0/0       *PtoP*         Up     28       L2   Capable
# PE1             Gi0/0/0/2       *PtoP*         Up     29       L2   Capable

# Verify LDP sessions
docker exec -it clab-transitnet-P1 show mpls ldp neighbor

# Expected output:
# Peer LDP Ident: 10.0.0.3:0; Local LDP Ident 10.0.0.1:0
#   TCP connection: 10.0.0.3:646 - 10.0.0.1:28577
#   State: Oper; Msgs sent/rcvd: 12/11; Downstream
# Peer LDP Ident: 10.0.0.11:0; Local LDP Ident 10.0.0.1:0
#   TCP connection: 10.0.0.11:646 - 10.0.0.1:12389
#   State: Oper; Msgs sent/rcvd: 10/9; Downstream
```

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

---
layout: default
---

# AutoNetkit

<span class="status-badge status-complete">PhD 2017</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Complete (PhD research project) |
| **Language** | Python |
| **Key Library** | NetworkX · GraphML |
| **Platforms** | Multi-vendor (Cisco, Juniper, Quagga) |
| **Year** | 2012-2017 |
| **License** | Open Source |

---

## Overview

AutoNetkit is a network configuration automation tool developed during PhD research. It transforms high-level topology designs into vendor-specific device configurations through abstract network models and Python-based design logic.

## Problem It Solves

Network configuration automation before AutoNetkit faced challenges:

**Manual Configuration:**
- Error-prone CLI commands
- Inconsistent naming and addressing
- Difficult to maintain large topologies
- Time-consuming to make changes

**Existing Tools:**
- Limited to single vendor
- No abstraction layer
- Hard-coded logic difficult to extend
- No formal model for network design

**AutoNetkit provided:**
- Visual topology design with automatic configuration
- Abstract network model separating topology from implementation
- Python-based extensible design logic
- Multi-vendor configuration generation
- Formal approach to network representation

## Architecture

### Visual Topology Capture

Draw networks in visual tools like yEd:

**GraphML Input:**
- Standard XML-based graph format
- Node properties (device type, AS number, loopback)
- Edge properties (link type, capacity)
- Visual layout preserved for documentation

**Topology Definition:**
```graphml
<node id="r1">
  <data key="device_type">router</data>
  <data key="asn">65000</data>
  <data key="loopback">10.0.0.1</data>
</node>
```

### Abstract Network Model

Multi-layer graph representation:

**Physical Layer (G_phy):**
- Devices, interfaces, cables
- Hardware specifications
- Physical connectivity

**Logical Layer:**
- VLANs, VRFs, routing domains
- IP addressing and subnetting
- Logical segmentation

**Protocol Layer (G_bgp, G_ospf, etc.):**
- BGP sessions and ASNs
- OSPF areas and costs
- ISIS levels
- Protocol-specific attributes

### Python Design Logic

Express network design in Python:

```python
# Configure iBGP full mesh within each AS
for asn, devices in G_phy.groupby("asn").items():
    routers = [d for d in devices if d.is_router]
    ibgp_edges = [(s, t) for s in routers for t in routers if s != t]
    G_bgp.add_edges_from(ibgp_edges, type='ibgp')

# Configure OSPF on all router interfaces
for router in G_phy.routers():
    for interface in router.interfaces():
        if interface.is_physical:
            interface.ospf_area = 0
            interface.ospf_cost = calculate_cost(interface.bandwidth)
```

### Configuration Compilation

Transform abstract model to vendor configs:

**Compiler Pipeline:**
1. Parse GraphML topology
2. Build multi-layer graph representation
3. Execute design logic (addressing, protocols)
4. Validate design consistency
5. Generate vendor-specific configurations

**Vendor Support:**
- Cisco IOS / IOS-XE
- Juniper JunOS
- Quagga (Linux routing)
- Extensible compiler framework

## Features

### Automatic IP Addressing

Intelligent address allocation:

**Algorithms:**
- Loopback addresses per router
- Point-to-point link addressing
- Subnet allocation by AS or area
- IPv4 and IPv6 support

**Collision Detection:**
- Validates no overlapping subnets
- Checks for duplicate addresses
- Enforces addressing policies

### Protocol Configuration

Automated routing protocol setup:

**OSPF:**
- Area assignment
- Interface cost calculation
- Network type configuration
- Authentication setup

**BGP:**
- iBGP full mesh or route reflectors
- eBGP peer configuration
- AS-path prepending
- Community tagging

**ISIS:**
- Level assignment (L1, L2, L1/L2)
- Metric calculation
- Area configuration

### Multi-Vendor Output

Single topology generates configs for all vendors:

**Cisco IOS Example:**
```
interface GigabitEthernet0/0
 ip address 10.0.1.1 255.255.255.252
 ip ospf cost 10
 ip ospf network point-to-point
```

**Juniper JunOS Example:**
```
interfaces {
    ge-0/0/0 {
        unit 0 {
            family inet {
                address 10.0.1.1/30;
            }
        }
    }
}
protocols {
    ospf {
        area 0.0.0.0 {
            interface ge-0/0/0.0 {
                metric 10;
                interface-type p2p;
            }
        }
    }
}
```

### Visualization

Network diagram generation:

**Output Formats:**
- GraphML (visual editors)
- PDF diagrams
- PNG/SVG images
- JSON for web visualization

**Layouts:**
- Physical topology view
- Logical routing domain view
- BGP AS topology
- Per-protocol views

## Research Contributions

### Abstract Network Model

Formal separation of concerns:

**Physical/Logical/Protocol Layers:**
- Independent modification without cascading changes
- Protocol-agnostic topology definition
- Reusable design patterns across vendors

**Published Research:**
Multiple academic papers on network abstraction and automation.

### Design Logic as Code

Python-based network design:

**Benefits:**
- Version control for network designs
- Unit tests for design logic
- Reusable design patterns
- Programmatic validation

**Limitations Addressed:**
- Traditional CLI configuration is imperative
- AutoNetkit design logic is declarative
- Easier to reason about network behavior

## Use Cases

### Lab Topology Generation

Network lab integration:

**Workflow:**
1. Draw topology in yEd
2. AutoNetkit generates configurations
3. Load configs into virtual routers
4. Lab environment ready for testing

**Applications:**
- Training and certification prep
- Protocol behavior testing
- Configuration validation

### Research Networks

Academic network research:

**Reproducibility:**
- Topology definitions in version control
- Automated configuration ensures consistency
- Easy to share and replicate experiments

**Scale:**
- Generate large topologies automatically
- Test at scale without manual configuration

### Network Design Prototyping

Pre-production validation:

**Design Iteration:**
- Rapid topology changes
- Instant configuration regeneration
- Catch design errors before deployment

## Technical Details

### Technology Stack

**Core:**
- Python 2.7 (legacy codebase)
- NetworkX for graph operations
- Mako templates for config generation
- GraphML parsing

**Architecture:**
- Plugin system for compilers
- Template-based config generation
- Multi-graph representation
- Modular design logic

### Limitations

**Legacy Status:**
- Python 2.7 codebase (pre-Python 3)
- Limited to routing protocols (no SDN)
- No real-time configuration push
- Research prototype, not production-hardened

### Successor Projects

Modern descendants:

**ank-pydantic:**
- Type-safe Pydantic models
- Rust-backed graph engine
- Modern Python 3.12+
- Enhanced vendor support

**TopoGen:**
- Rust implementation
- Focus on topology generation only
- Python bindings via PyO3

## Development Status

**PhD Complete (2017):**
- Research contributions published
- Used in Cisco VIRL project
- Open source release
- Legacy codebase maintained for historical reference

**Not Under Active Development:**
- Superseded by ank-pydantic and TopoGen
- Available for reference and historical interest
- Demonstrates research foundations for current projects

## Academic Impact

**Publications:**
- PhD thesis on network automation
- Conference papers on abstract models
- Workshop presentations

**Industry Adoption:**
- Used for network research and teaching
- Influenced modern network automation tools

## Links

- **Legacy Website:** autonetkit.org (archived)
- **Documentation:** Publications and thesis
- **Related:** [ank-pydantic](ank-pydantic) is the modern successor
- **Related:** [TopoGen](topogen) handles topology generation

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- yEd topology design interface
- GraphML input example
- Multi-layer graph visualization
- Python design logic example
- Generated Cisco IOS configuration
- Generated Juniper JunOS configuration
- Network diagram output
- Abstract model flowchart
-->

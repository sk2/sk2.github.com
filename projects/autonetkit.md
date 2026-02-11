---
layout: default
---

# AutoNetkit

<span class="status-badge status-active">PhD 2017</span>

[← Back to Projects](../projects)

---


## The Insight

Configuration automation often lacks a formal model, leading to vendor-specific hard-coded logic. **AutoNetkit** solves this by transforming high-level topologies into vendor-neutral abstract models. It then compiles these models into device-specific configurations (Cisco, Juniper, Quagga) using Python-based design logic.

## Quick Facts

| | |
|---|---|
| **Status** | PhD 2017 |
| **Language** | Python |
| **Started** | 2025 |

---

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

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

## Architecture

AutoNetkit uses a multi-layer graph representation:
- **Physical Layer**: Hardware, interfaces, and cabling.
- **Logical Layer**: IP addressing, VLANs, and VRFs.
- **Protocol Layer**: BGP sessions, OSPF areas, and ISIS levels.

A compiler pipeline parses GraphML topologies, executes design logic for addressing and protocols, and generates validated configurations.

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

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

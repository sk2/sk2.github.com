---
layout: default
---

# ank-pydantic

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active development |
| **Language** | Python + Rust (PyO3) |
| **Key Library** | Pydantic, petgraph |
| **Platforms** | 11+ vendor platforms supported |
| **Started** | 2024 |
| **License** | TBD |

---

## Overview

ank-pydantic models network topologies with Pydantic and queries them with a fast Rust-backed graph engine. It provides type-safe topology definition with validation at definition time, combined with high-performance graph operations through Rust.

## Problem It Solves

Building network topologies requires balancing three competing concerns:

**Graph Libraries (NetworkX, rustworkx):**
- ✓ Fast graph operations
- ✗ Untyped - easy to create invalid structures
- ✗ No validation until runtime errors occur

**Source-of-Truth Tools (NetBox, Nautobot):**
- ✓ Great for inventory management
- ✗ Not designed for topology analysis
- ✗ Limited query capabilities for network-specific questions

**Custom Solutions:**
- ✓ Full control over design
- ✗ Must build validation layer from scratch
- ✗ Must build storage and query systems
- ✗ Must implement graph algorithms

**ank-pydantic solves all three:**
- Type safety through Pydantic models
- Performance through Rust-backed graph operations
- Rich query API without manual graph walking

## Architecture

### Type-Safe Models

```python
from ank_pydantic.core.topology import Topology
from ank_pydantic.core.models import BaseTopologyNode, BaseTopologyEndpoint

class Router(BaseTopologyNode):
    vendor: str = "Cisco"
    model: str
    ios_version: str

class Interface(BaseTopologyEndpoint):
    speed: str = "1G"
    duplex: str = "full"
```

Pydantic validates at definition time. Invalid structures are impossible to create.

### Multi-Layer Modeling

Separate physical, logical, and protocol views of the same network:
- **Physical layer:** Devices, cables, interfaces
- **Logical layer:** VLANs, VRFs, routing domains
- **Protocol layer:** OSPF areas, BGP ASNs, MPLS LSPs

Each layer can be queried and analyzed independently.

### Rust-Backed Graph Engine

Graph operations (traversals, shortest paths, connectivity checks) run in Rust via PyO3. Python ergonomics with Rust performance.

### Rich Query API

```python
# Find all routers in datacenter with 10G uplinks
routers = topology.query.nodes() \
    .filter_by_type(Router) \
    .filter_by_location("datacenter") \
    .with_interface_speed("10G") \
    .count()

# Traverse from edge router to all connected hosts
paths = topology.query.paths() \
    .from_node("edge-router-01") \
    .to_type(Host) \
    .shortest()
```

Chainable filters without manual graph walking.

## Features

### Configuration Generation

Multi-vendor configuration compilers for 11+ platforms:
- Cisco IOS/IOS-XE
- Cisco NX-OS
- Juniper JunOS
- Arista EOS
- And more

From single topology definition, generate configs for entire network.

### Validation

**Structural validation:**
- Check for loops in spanning tree
- Verify BGP peer connectivity
- Validate OSPF area assignments

**Policy compliance:**
- Enforce naming conventions
- Check security policies (ACLs, firewall rules)
- Verify redundancy requirements

### Optional Extras

**API Server (FastAPI):**
- REST API for topology CRUD operations
- WebSocket support for real-time updates
- OpenAPI documentation

**CLI:**
- Import topologies from YAML/JSON
- Export configurations
- Run validation checks

**Visualization:**
- Integration with netvis for topology visualization
- Auto-generate diagrams from topology

## Use Cases

**Design Validation Before Deployment:**
Catch errors before pushing to production. Verify routing, check reachability, validate policies.

**Multi-Vendor Config Generation:**
Define once, deploy everywhere. Single topology generates configs for Cisco, Juniper, Arista from one source.

**Architecture Compliance:**
Enforce standards across network. Check naming, validate redundancy, verify security policies.

**SDN Controller Prototyping:**
Build network intent engine. Transform high-level policies into low-level configs.

**Documentation:**
Auto-generate network diagrams and documentation from topology definitions.

## When NOT to Use

**Real-Time Monitoring:**
Use time-series databases (Prometheus, InfluxDB) instead. ank-pydantic is for design and config generation, not operational monitoring.

**Replacing NetBox/Nautobot:**
Use alongside, not instead of. NetBox is your source of truth. ank-pydantic adds topology analysis and config generation.

**Simple Graph Algorithms:**
If you just need Dijkstra or BFS, use NetworkX directly. ank-pydantic adds value when you need type safety + multi-vendor config generation.

## Development Status

Active development with regular feature additions.

**Core Features Complete:**
- Type-safe models ✅
- Rust graph engine ✅
- Multi-layer modeling ✅
- Query API ✅
- Configuration compilers ✅

**In Progress:**
- Additional vendor platform support
- Enhanced validation rules
- Performance optimizations
- API server improvements

## Links

- **GitHub:** Coming soon (currently private)
- **Documentation:** See repository docs/ directory
- **Related:** [ANK Workbench](ank-workbench) integrates ank-pydantic for unified workflow

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

<!-- TODO: Add screenshots:
- Code example showing topology definition
- Query API usage with results
- Generated configuration output
- Validation error examples
- Multi-layer topology visualization
-->

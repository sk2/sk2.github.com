---
layout: default
section: network-automation
description: "Rust-based network topology layout and visualization engine."
---

# Network Visualization Engine

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-03-30</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Usage](#usage)
- [Features](#features)
- [Current Status](#current-status)

![Hero Image](/images/hero-diagram.svg)


---

## Concept

Rust-based network topology layout and visualization engine. Takes multi-layer network topologies (via petgraph) and renders them using layout algorithms that minimize edge crossings, bundle related connections, and respect hierarchical or geographic structure. Outputs SVG, PDF, and PNG with interactive browser embedding via WASM.

Design follows Tufte's principles: maximize information density, minimize chartjunk. An automated WCAG 3:1 contrast system ensures accessibility without manual tuning.

<div class="mermaid">
flowchart LR
    T[Topology<br/>Sources] --> L[Layout<br/>Algorithms]
    L --> R[Renderer]
    R --> SVG[SVG]
    R --> PDF[PDF]
    R --> PNG[PNG]
    R --> WASM[WASM<br/>Browser]
</div>

<div class="mermaid">
block-beta
    columns 1
    eBGP["eBGP"]
    iBGP["iBGP"]
    OSPF["OSPF"]
    IP["IP Layer"]
    L2["Layer 2"]
    Physical["Physical"]
</div>

---

## Code Samples

### README.md

```markdown
# Adapter Examples

This directory contains runnable scripts that demonstrate the end-to-end workflow:

external data -> `netvis import` -> topology YAML -> `netvis --input` -> SVG

All outputs are written to `target/` (gitignored by default).

## LLDP/CDP discovery JSON

Script: `examples/adapters/lldp-import.sh`

Runs an LLDP import from a JSON file and renders an SVG.

Run (from repo root):

```bash
bash examples/adapters/lldp-import.sh
```

Optional: pass a custom discovery JSON path:

```bash
bash examples/adapters/lldp-import.sh /path/to/discovery.json
```

Expected outputs:

- `target/lldp-imported.yaml`
- `target/lldp-imported.svg`

Sample input: `examples/adapters/sample-lldp.json`

## NetBox

Script: `examples/adapters/netbox-import.sh`

Requires a NetBox API token via env var (the script never prints it).

Environment variables:

- `NETBOX_TOKEN` (required)
- `NETBOX_URL` (recommended)

Run:

```bash
export NETBOX_URL=https://netbox.example.com
export NETBOX_TOKEN=...   # read-only token
bash examples/adapters/netbox-import.sh
```

You can also pass the NetBox URL as the first argument to override `NETBOX_URL`:

```bash
bash examples/adapters/netbox-import.sh https://netbox.example.com
```

Expected outputs:

- `target/netbox-imported.yaml`
- `target/netbox-imported.svg`

## Notes

- These scripts run `cargo run --features cli --bin netvis ...`. The first run may take a while to compile.
- If you have a `netvis` binary on your PATH already, you can run the equivalent `netvis import ...` commands directly.

```

### pdf-export.yaml

```yaml
# PDF Export Configuration for Documents and Presentations
#
# This YAML shows recommended PDF export settings for different use cases.
# Use with the Rust API: PdfOptions::default().page_size(...).title(...)
#
# For CLI usage, the output file extension (.pdf) triggers PDF export:
#   netvis --input topology.yaml --output diagram.pdf
#
# The settings below document PdfOptions API fields.

# Document Metadata (embedded in PDF properties)
metadata:
  title: "Network Topology Diagram"
  author: "NetVis"
  subject: "Infrastructure Documentation"
  keywords: "network, topology, diagram"

# Page Settings
page_size: content_size   # Options: content_size (default), a4, letter, custom
# For custom size:
# page_size:
#   custom:
#     width_mm: 297
#     height_mm: 210

# Margins (in millimeters)
margins_mm: 5.0

# DPI for coordinate mapping (default: 72.0)
dpi: 72.0

# Recommended render settings for PDF output
render:
  theme: print            # Print theme has high contrast for paper
  width: 1200
  height: 900

# Use Cases:
#
# 1. Technical Documentation:
#    - page_size: a4 or letter
#    - margins_mm: 10-15 for binding
#    - theme: print (black lines on white)
#
# 2. Presentations:
#    - page_size: content_size (fits slide exactly)
#    - theme: light or network
#    - Larger width (1600+) for detail
#
# 3. Posters/Large Format:
#    - page_size: custom (A1, A0, etc.)
#    - margins_mm: 20+
#    - High DPI (150-300) for quality

```

### png-print.yaml

```yaml
# PNG Export Configuration for High-Quality Printing
#
# This YAML shows recommended PNG settings for print output.
# Optimized for physical documents, posters, and professional printing.
#
# Use with the Rust API: PngOptions::default().dpi(300).scale(2.0)...
#
# CLI export example:
#   netvis --input topology.yaml --output diagram.png --width 2550 --height 3300
#
# The settings below document PngOptions API fields.

# High Resolution for Print
dpi: 300                  # Print standard (300 DPI minimum)
scale: 2.0                # 2x rasterization for crisp edges

# Dimensions (pixels at 300 DPI)
# Letter size: 8.5" x 11" at 300 DPI = 2550 x 3300 pixels
# A4 size: 210mm x 297mm at 300 DPI = 2480 x 3508 pixels
width: 2550
height: 3300

# Quality Settings
compression: high         # Best compression for archival quality
                          # Larger file but maximum quality

# Background for Paper
background: white         # White for standard paper printing
                          # Use theme background color for specialty paper

# Antialiasing
antialias: true           # Smooth edges are critical for print

# Recommended render settings for print
render:
  theme: print            # High contrast, optimized for paper
  width: 1200             # Scene width (scaled to print dimensions)
  height: 900
  labels: label

# Common Print Sizes at 300 DPI:
#
# Letter (8.5" x 11"):
#   width: 2550, height: 3300 (portrait)
#   width: 3300, height: 2550 (landscape)
#
# A4 (210mm x 297mm):
#   width: 2480, height: 3508 (portrait)
#   width: 3508, height: 2480 (landscape)
#
# Tabloid (11" x 17"):
#   width: 3300, height: 5100
#
# A3 (297mm x 420mm):
#   width: 3508, height: 4961
#
# Use Cases:
#
# 1. Technical Document Insert:
#    - width: 2550, height: 1800 (half page)
#    - dpi: 300
#    - theme: print
#
# 2. Wall Poster (A1/A0):
#    - width: 7016+ (A1 at 300 DPI)
#    - dpi: 150-200 (can reduce for very large)
#    - scale: 3.0 or higher
#
# 3. Presentation Handout:
#    - dpi: 150 (sufficient for handouts)
#    - compression: balanced

```

### png-web.yaml

```yaml
# PNG Export Configuration for Web Display
#
# This YAML shows recommended PNG settings for web/screen use.
# Optimized for dashboards, documentation sites, and embedding.
#
# Use with the Rust API: PngOptions::default().dpi(72).compression(...)
#
# CLI export is automatic when output ends in .png:
#   netvis --input topology.yaml --output diagram.png --width 1200 --height 800
#
# The settings below document PngOptions API fields.

# Resolution
dpi: 72                   # Web standard (72 or 96 DPI)
scale: 1.0                # 1x for web, 2x for retina

# Dimensions (in pixels)
width: 1200
height: 800

# Compression
compression: fast         # Options: fast, balanced (default), high
                          # 'fast' is fine for web - smaller file, quick load

# Background
background: white         # Options: white, transparent, or hex color (#rrggbb)
                          # Use 'transparent' for overlays on colored backgrounds

# Antialiasing
antialias: true           # Always true for smooth edges on screen

# Recommended render settings for web PNG
render:
  theme: dark             # Dark theme common for dashboards/NOC displays
  width: 1200
  height: 800
  labels: label

# Use Cases:
#
# 1. Dashboard/NOC Display:
#    - theme: dark
#    - width: 1920, height: 1080 (full HD)
#    - scale: 1.0
#
# 2. Documentation Site:
#    - theme: light
#    - width: 800-1200
#    - compression: fast
#    - background: white
#
# 3. Retina/HiDPI Display:
#    - scale: 2.0 (doubles pixel count)
#    - Keeps file sizes reasonable with good quality
#
# 4. Email Attachment:
#    - width: 800 (smaller for email clients)
#    - compression: high
#    - background: white

```

### README.md

```markdown
# NetVis Example Gallery

This directory contains checked-in example outputs for NetVis.

- Top-level `*.svg` files are reproducible example renders. Refresh them with `python3 scripts/regenerate_example_outputs.py`.
- `examples/gallery.html` uses a curated subset of those top-level SVGs for browsing.
- `examples/visual-system-v2-manifest.json` defines the active hero set and recovery/reference examples.
- `verification/` contains separate QA artifacts generated by ignored tests; those are not the curated gallery.

## Hero vs Recovery Curation

The default public gallery view is intentionally narrower than the full regression corpus. Only `hero_gallery_outputs` in `examples/visual-system-v2-manifest.json` should anchor README, homepage, or product proof until they pass full-size and preview-scale review.

Current recovery/reference outputs remain checked in and browsable, but should not be promoted as public proof until their listed recovery gates pass:

- `04-kubernetes-cluster.svg` - recovery reference for cloud/application grouping, labels, and routing.
- `gallery-campus-realworld-light.svg` - recovery reference for campus palette, icon, and route hierarchy work.
- `template-hub-spoke-large.svg` - stress/regression fixture for density clustering or aggregation.

## v1.2 Effects Showcase

The gallery demonstrates visual effects (drop shadows, glow) across different topology types and real-world scenarios.

### Topology Types

| Topology | File | Description |
|----------|------|-------------|
| Mesh | `gallery-mesh-effects.yaml` | Dense mesh with emphasis on critical paths |
| Ring | `gallery-ring-effects.yaml` | Ring topology with root node highlight |
| Tree | `gallery-tree-effects.yaml` | Hierarchical layout with tiered shadows |
| Geographic | `gallery-geo-effects.yaml` | WAN with geographic positioning |

### Effect Comparison

| File | Purpose |
|------|---------|
| `gallery-effects-comparison.yaml` | Side-by-side comparison of no effects, subtle, and emphasis |

### Real-World Scenarios

| Scenario | File | Key Effects |
|----------|------|-------------|
| Datacenter | `gallery-datacenter-realworld.yaml` | Spine emphasis, firewall glow |
| Campus | `gallery-campus-realworld.yaml` | Core emphasis, wireless controller glow |
| WAN | `gallery-wan-realworld.yaml` | HQ selection glow, regional hierarchy |

### Rendering Gallery Examples

The checked-in top-level SVGs are regenerated from current source topologies via:

```bash
python3 scripts/regenerate_example_outputs.py
```

The refresh workflow renders standard CLI outputs with `--icon-dialect obsidian`,
`--quality-target 80`, and `--max-iterations 8`, and then runs
`netvis check-quality examples/outputs --strict`. The very largest synthetic gallery fixtures
cap the iteration loop earlier so the full checked-in corpus stays refreshable. A successful
run is now the acceptance path for checked-in gallery/output refreshes.

To audit the inventory and freshness without re-rendering:

```bash
python3 scripts/regenerate_example_outputs.py --check
```

To inspect freshness only and temporarily skip the strict quality gate:

```bash
python3 scripts/regenerate_example_outputs.py --check --skip-quality-gate
```

### Preview-Scale Review Pack

Generate full-size PNGs, 480px gallery-preview PNGs, copied SVGs, a flat upload
folder, and a Gemini/vision-model prompt for the active hero set with:

```bash
python3 scripts/generate_showcase_review_pack.py --scope hero
```

Use `--scope all` when recovery/reference outputs should be reviewed alongside
the hero set, or `--scope extended` when the review should focus on radial,
starburst, geographic, ring, and large-density layouts. Use `--scope advanced`
when the pack should demonstrate advanced algorithms, including subway routing,
edge bundling, force-directed layouts, hierarchical layouts, orthogonal routing,
isometric/multilayer views, clustering, inferred geographic seeding,
radial/starburst, geographic, ring, and large-density outputs. Use
`--scope conformance` for the small required pack that preserves geographic,
inferred-location, starburst/radial, and large-density cases in every review
[cycle](../cycle). The generated pack lands under
`.artifacts/netvis-review-pack/` by default and includes `manifest.json`,
`README.md`, `review-prompt.md`, and `upload/` files with non-clashing `full-`,
`preview-480-`, and `svg-` prefixes.

The manual promotion gate is: inspect both the full PNG and preview PNG before
using any output as README, homepage, or public gallery proof. Fail the output if
labels, icons, hierarchy, routing, density, or whitespace become unreadable at
preview scale. Use the PNGs for full-size/thumbnail visual judgment and the SVGs
as source-fidelity attachments when the review tool supports them.

### Available Effects

- `drop-shadow-subtle`: Subtle depth for secondary elements
- `drop-shadow-emphasis`: Strong depth for primary elements
- `glow-selection`: Highlight selected/active elements

---

## Template Example Outputs

The top-level SVG corpus includes template outputs, tutorial outputs, themed renders, diff renders, and the curated gallery subset.

## Files

### Spine-Leaf Template

- `template-spine-leaf-small.svg` (12 nodes) - 2-tier datacenter fabric
- `template-spine-leaf-medium.svg` (30 nodes) - 3-tier fabric with pods
- `template-spine-leaf-large.svg` (556 nodes) - 5-tier mega datacenter

### Hub-Spoke Template

- `template-hub-spoke-small.svg` (9 nodes) - Enterprise WAN
- `template-hub-spoke-medium.svg` (25 nodes) - Global regional hierarchy
- `template-hub-spoke-large.svg` (620 nodes) - Global enterprise WAN

### Ring Template

- `template-ring-small.svg` (8 nodes) - Campus backbone ring
- `template-ring-medium.svg` (20 nodes) - Metro dual ring
- `template-ring-large.svg` (500 nodes) - 5 metro transport rings

### Multi-Tier Template

- `template-multi-tier-small.svg` (10 nodes) - 3-tier web app
- `template-multi-tier-medium.svg` (35 nodes) - Production microservices
- `template-multi-tier-large.svg` (550 nodes) - Large Kubernetes cluster

## How to Regenerate

Regenerate every top-level checked-in SVG output with:

```bash
python3 scripts/regenerate_example_outputs.py
```

## Notes

- Ring examples use `layout: force_directed` instead of the ring template because the radial layout algorithm requires tree-like graphs, and rings have cycles.
- Large examples (500+ nodes) are programmatically generated and may take 1-2 seconds to render.
- All SVG files can be viewed in any modern web browser.

```

### README.md

```markdown
# Rendering Verification Artifacts

These files are generated by ignored verification tests to visually check NetVis rendering quality (anti-aliasing, stroke crispness, transparency, and scale behavior).

They are separate from the curated example gallery in the parent directory.

## How To Regenerate

Run:

```bash
cargo test verification::rendering_quality::generate_visual_reference -- --ignored --nocapture
```

## Visual Inspection Checklist

- Curves: no stair-stepping on Bezier curves at 1x/2x/3x (zoom in and pan along long edges)
- Strokes: 1px strokes look crisp (no gray blur) at typical viewer zoom levels
- Text: labels remain readable; glyph edges look smooth (not jagged)

## Expected Passing Characteristics

- Smooth edges on curves and node outlines (anti-aliasing active)
- 2x and 3x PNGs are exact pixel-scale multiples of 1x
- SVG `viewBox` + `preserveAspectRatio` preserve layout when viewport size changes

## Source

- Topology: `examples/topologies/basic.yaml`
- Renderer: `src/render/svg.rs` via `SvgRenderer::render`

```

### basic_topology.py

```python
#!/usr/bin/env python3
"""Basic topology example using NetVis Python bindings.

This example demonstrates:
- Creating a topology with nodes and edges
- Using the attrs parameter for custom metadata
- Using different layout algorithms
- Rendering to SVG, PNG, and PDF
"""

import netvis


def main():
    # Create a simple spine-leaf datacenter topology
    topo = netvis.Topology()

    # Add spine switches with custom attrs for inventory tracking
    topo.add_node(
        "spine-1",
        node_type="switch",
        label="Spine 1",
        attrs={
            "vendor": "arista",
            "model": "7050X3",
            "rack": "R01",
            "serial": "SPN001ABC",
            "mgmt_ip": "10.0.0.1",
        },
    )
    topo.add_node(
        "spine-2",
        node_type="switch",
        label="Spine 2",
        attrs={
            "vendor": "arista",
            "model": "7050X3",
            "rack": "R01",
            "serial": "SPN002DEF",
            "mgmt_ip": "10.0.0.2",
        },
    )

    # Add leaf switches
    for i in range(1, 5):
        topo.add_node(
            f"leaf-{i}",
            node_type="switch",
            label=f"Leaf {i}",
            attrs={
                "vendor": "arista",
                "model": "7280R3",
                "rack": f"R0{((i - 1) // 2) + 2}",
                "serial": f"LEF{i:03d}XYZ",
            },
        )

    # Add servers with custom attributes
    for i in range(1, 9):
        leaf_num = ((i - 1) // 2) + 1
        topo.add_node(
            f"server-{i}",
            node_type="server",
            label=f"Server {i}",
            attrs={
                "os": "ubuntu-22.04",
                "cpu_cores": 64,
                "memory_gb": 256,
                "role": "compute" if i % 2 == 0 else "storage",
            },
        )
        # Add edge with cable/connection metadata
        topo.add_edge(
            f"server-{i}",
            f"leaf-{leaf_num}",
            from_interface="eno1",
            to_interface=f"Eth1/{i % 48}",
            attrs={"speed": "25G", "cable_type": "DAC", "length_m": 3},
        )

    # Connect leaves to spines (full mesh) with fabric links
    for leaf in range(1, 5):
        topo.add_edge(
            f"leaf-{leaf}",
            "spine-1",
            from_interface="Eth1/49",
            to_interface=f"Eth1/{leaf}",
            attrs={
                "speed": "100G",
                "cable_type": "single-mode-fiber",
                "length_m": 15,
                "circuit_id": f"FAB-L{leaf}-S1",
            },
        )
        topo.add_edge(
            f"leaf-{leaf}",
            "spine-2",
            from_interface="Eth1/50",
            to_interface=f"Eth1/{leaf}",
            attrs={
                "speed": "100G",
                "cable_type": "single-mode-fiber",
                "length_m": 15,
                "circuit_id": f"FAB-L{leaf}-S2",
            },
        )

    print(f"Topology: {topo.node_count()} nodes, {topo.edge_count()} edges")

    # Render with different layouts
    print("Rendering with hierarchical layout...")
    topo.render_to_file("spine-leaf-hierarchical.svg", layout="hierarchical")

    print("Rendering with force-directed layout...")
    topo.render_to_file("spine-leaf-force.svg", layout="force-directed")

    print("Rendering to PNG...")
    topo.render_to_file("spine-leaf.png", layout="hierarchical", scale=2.0)

    print("Done! Check output files.")


if __name__ == "__main__":
    main()

```

### netbox_integration.py

```python
#!/usr/bin/env python3
"""Example: Structuring NetBox-style data for NetVis visualization.

This example demonstrates the PATTERN for using NetVis with data from
Network Management Systems (NMS) like NetBox, Infrahub, or Nautobot.

NOTE: Direct API integration is intentionally not included in NetVis.
You should:
1. Query your NMS using its Python client (pynetbox, infrahub-sdk, etc.)
2. Transform the data into the format shown below
3. Pass it to NetVis for visualization

This separation of concerns keeps NetVis focused and avoids dependencies
on specific NMS versions, authentication schemes, and API changes.

Example workflow in your script:
    # 1. Query your NMS yourself
    # (e.g., get devices and connections for a site)
    devices = query_devices_from_nms(...)
    links = query_links_from_nms(...)

    # 2. Transform to NetVis format (as shown in mock_topology below)
    topo = transform_nms_to_netvis(devices, links)

    # 3. Render
    topo.render_to_file('topology.svg')
"""

import netvis


def mock_topology() -> netvis.Topology:
    """Create a mock topology demonstrating NMS data patterns.

    This simulates data you would get from an NMS query, showing:
    - How to preserve NMS metadata in attrs
    - Common device attributes (status, serial, platform, rack, IP)
    - Cable/connection attributes (type, status, length)

    In your real script, replace this with data from your NMS query.
    """
    return netvis.Topology.from_dict(
        {
            "nodes": [
                {
                    "id": "dc1-spine-01",
                    "type": "switch",
                    "label": "DC1 Spine 01",
                    # Preserve NMS metadata in attrs for downstream use
                    # (e.g., click handlers, tooltips, reports)
                    "attrs": {
                        "netbox_id": 101,
                        "status": "active",
                        "serial": "ABC123",
                        "platform": "arista-eos",
                        "rack": "R01",
                        "primary_ip": "10.0.0.1/32",
                    },
                },
                {
                    "id": "dc1-spine-02",
                    "type": "switch",
                    "label": "DC1 Spine 02",
                    "attrs": {
                        "netbox_id": 102,
                        "status": "active",
                        "serial": "ABC124",
                        "platform": "arista-eos",
                        "rack": "R01",
                        "primary_ip": "10.0.0.2/32",
                    },
                },
                {
                    "id": "dc1-leaf-01",
                    "type": "switch",
                    "label": "DC1 Leaf 01",
                    "attrs": {
                        "netbox_id": 201,
                        "status": "active",
                        "serial": "DEF456",
                        "platform": "arista-eos",
                        "rack": "R02",
                    },
                },
                {
                    "id": "dc1-leaf-02",
                    "type": "switch",
                    "label": "DC1 Leaf 02",
                    "attrs": {
                        "netbox_id": 202,
                        "status": "active",
                        "serial": "DEF457",
                        "platform": "arista-eos",
                        "rack": "R02",
                    },
                },
                {
                    "id": "dc1-srv-01",
                    "type": "server",
                    "label": "Web Server 01",
                    "attrs": {
                        "netbox_id": 301,
                        "status": "active",
                        "tenant": "web-team",
                        "platform": "linux",
                    },
                },
                {
                    "id": "dc1-srv-02",
                    "type": "server",
                    "label": "Web Server 02",
                    "attrs": {
                        "netbox_id": 302,
                        "status": "active",
                        "tenant": "web-team",
                        "platform": "linux",
                    },
                },
                {
                    "id": "dc1-fw-01",
                    "type": "firewall",
                    "label": "Firewall",
                    "attrs": {
                        "netbox_id": 401,
                        "status": "active",
                        "platform": "panos",
                    },
                },
            ],
            "edges": [
                {
                    "source": "dc1-leaf-01",
                    "target": "dc1-spine-01",
                    "from_interface": "Eth1/49",
                    "to_interface": "Eth1/1",
                    # Preserve cable metadata from NetBox
                    "attrs": {
                        "netbox_cable_id": 1001,
                        "cable_type": "smf",
                        "cable_status": "connected",
                        "cable_length": 10,
                        "cable_length_unit": "m",
                    },
                },
                {
                    "source": "dc1-leaf-01",
                    "target": "dc1-spine-02",
                    "from_interface": "Eth1/50",
                    "to_interface": "Eth1/1",
                    "attrs": {
                        "netbox_cable_id": 1002,
                        "cable_type": "smf",
                        "cable_status": "connected",
                    },
                },
                {
                    "source": "dc1-leaf-02",
                    "target": "dc1-spine-01",
                    "from_interface": "Eth1/49",
                    "to_interface": "Eth1/2",
                    "attrs": {
                        "netbox_cable_id": 1003,
                        "cable_type": "smf",
                        "cable_status": "connected",
                    },
                },
                {
                    "source": "dc1-leaf-02",
                    "target": "dc1-spine-02",
                    "from_interface": "Eth1/50",
                    "to_interface": "Eth1/2",
                    "attrs": {
                        "netbox_cable_id": 1004,
                        "cable_type": "smf",
                        "cable_status": "connected",
                    },
                },
                {
                    "source": "dc1-srv-01",
                    "target": "dc1-leaf-01",
                    "from_interface": "eno1",
                    "to_interface": "Eth1/1",
                    "attrs": {
                        "netbox_cable_id": 2001,
                        "cable_type": "cat6a",
                        "cable_status": "connected",
                    },
                },
                {
                    "source": "dc1-srv-02",
                    "target": "dc1-leaf-02",
                    "from_interface": "eno1",
                    "to_interface": "Eth1/1",
                    "attrs": {
                        "netbox_cable_id": 2002,
                        "cable_type": "cat6a",
                        "cable_status": "connected",
                    },
                },
                {
                    "source": "dc1-fw-01",
                    "target": "dc1-spine-01",
                    "from_interface": "eth0",
                    "to_interface": "Eth1/48",
                    "attrs": {
                        "netbox_cable_id": 3001,
                        "cable_type": "smf",
                        "cable_status": "connected",
                    },
                },
            ],
        }
    )


def main():
    """Demonstrate the pattern for NMS integration."""
    print("NetVis + NMS Integration Pattern")
    print("=" * 40)
    print()
    print("This example shows how to structure data from NetBox/Infrahub/Nautobot")
    print("for visualization with NetVis.")
    print()
    print("In your script, you would:")
    print("  1. Query your NMS using its Python client")
    print("  2. Transform results to the format shown in mock_topology()")
    print("  3. Pass to NetVis for rendering")
    print()

    # Create topology from mock data (simulating NMS query results)
    topo = mock_topology()

    print(f"Topology: {topo.node_count()} nodes, {topo.edge_count()} edges")

    # Render with hierarchical layout (good for datacenter topologies)
    topo.render_to_file(
        "netbox-topology.svg", layout="hierarchical", width=1400, height=900
    )
    print("Saved: netbox-topology.svg")

    # Also render as PNG for documentation
    topo.render_to_file("netbox-topology.png", layout="hierarchical", scale=2.0)
    print("Saved: netbox-topology.png")


if __name__ == "__main__":
    main()

```

### adversarial-almost-junctions.yaml

```yaml
name: Adversarial Almost Junctions

# Near-misses around a central crossing to stress false_junction_ambiguity checks.
render:
  layout: orthogonal
  seed: 42
  width: 1300
  height: 900
  padding: 70
  labels: label
  theme: network

nodes:
  - { id: north, label: North, node_type: router, position_hint: [0, -300] }
  - { id: south, label: South, node_type: router, position_hint: [0, 300] }
  - { id: west, label: West, node_type: router, position_hint: [-320, 0] }
  - { id: east, label: East, node_type: router, position_hint: [320, 0] }

  - { id: near-nw, label: Near-NW, node_type: switch, position_hint: [-25, -20] }
  - { id: near-ne, label: Near-NE, node_type: switch, position_hint: [25, -10] }
  - { id: near-sw, label: Near-SW, node_type: switch, position_hint: [-20, 20] }
  - { id: near-se, label: Near-SE, node_type: switch, position_hint: [20, 25] }

edges:
  - { from: north, to: south, label: trunk-ns }
  - { from: west, to: east, label: trunk-we }

  - { from: north, to: near-ne }
  - { from: near-ne, to: east }

  - { from: west, to: near-sw }
  - { from: near-sw, to: south }

  - { from: near-nw, to: east }
  - { from: west, to: near-se }

```

### adversarial-dense-hub-spoke-fan.yaml

```yaml
name: Adversarial Dense Hub-Spoke Fan

# Leaf-heavy spoke sectors intended to stress large fan label density around a single hub.
render:
  layout: force_directed
  preset: wan
  seed: 42
  width: 1700
  height: 1100
  padding: 80
  labels: label
  theme: network

nodes:
  - { id: hub, label: Regional-Hub, node_type: router, position_hint: [0, 0] }

  - { id: fan-01, label: Fan-01, node_type: host, position_hint: [320, -220] }
  - { id: fan-02, label: Fan-02, node_type: host, position_hint: [360, -180] }
  - { id: fan-03, label: Fan-03, node_type: host, position_hint: [390, -140] }
  - { id: fan-04, label: Fan-04, node_type: host, position_hint: [420, -100] }
  - { id: fan-05, label: Fan-05, node_type: host, position_hint: [445, -60] }
  - { id: fan-06, label: Fan-06, node_type: host, position_hint: [460, -20] }
  - { id: fan-07, label: Fan-07, node_type: host, position_hint: [465, 20] }
  - { id: fan-08, label: Fan-08, node_type: host, position_hint: [455, 60] }
  - { id: fan-09, label: Fan-09, node_type: host, position_hint: [430, 100] }
  - { id: fan-10, label: Fan-10, node_type: host, position_hint: [400, 140] }
  - { id: fan-11, label: Fan-11, node_type: host, position_hint: [365, 180] }
  - { id: fan-12, label: Fan-12, node_type: host, position_hint: [325, 220] }

  - { id: west-1, label: West-1, node_type: host, position_hint: [-300, -100] }
  - { id: west-2, label: West-2, node_type: host, position_hint: [-320, 0] }
  - { id: west-3, label: West-3, node_type: host, position_hint: [-300, 100] }
  - { id: north-1, label: North-1, node_type: host, position_hint: [-30, -320] }
  - { id: south-1, label: South-1, node_type: host, position_hint: [30, 320] }

edges:
  - { from: hub, to: fan-01 }
  - { from: hub, to: fan-02 }
  - { from: hub, to: fan-03 }
  - { from: hub, to: fan-04 }
  - { from: hub, to: fan-05 }
  - { from: hub, to: fan-06 }
  - { from: hub, to: fan-07 }
  - { from: hub, to: fan-08 }
  - { from: hub, to: fan-09 }
  - { from: hub, to: fan-10 }
  - { from: hub, to: fan-11 }
  - { from: hub, to: fan-12 }

  - { from: hub, to: west-1 }
  - { from: hub, to: west-2 }
  - { from: hub, to: west-3 }
  - { from: hub, to: north-1 }
  - { from: hub, to: south-1 }

  - { from: fan-03, to: fan-06 }
  - { from: fan-04, to: fan-07 }
  - { from: fan-05, to: fan-08 }
  - { from: fan-06, to: fan-09 }
  - { from: fan-07, to: fan-10 }
  - { from: fan-08, to: fan-11 }

```

---

## Visuals

### Network Visualisation Examples

![Geographic WAN](/images/geographic_wan.png)

![Bundled Mesh](/images/bundled_mesh.png)

![Hierarchical Datacenter](/images/hierarchical_datacenter.png)

![Labels Dense](/images/labels_dense.png)

![Force Directed Basic](/images/force_directed_basic.png)

---

## Usage

```bash
# Render a topology to SVG
netvis --input topology.yaml --output network.svg

# Geographic layout
netvis --input backbone.yaml --layout geographic --output map.svg

# Multi-layer isometric view
netvis --input datacenter.yaml --layout isometric --layers physical,l2,ospf --output layers.svg

# Import from LLDP discovery
netvis import --format lldp --input discovery.json --output topology.yaml

# Timeline across snapshots
netvis timeline --input snapshots/ --output timeline.svg
```

---

## Features

**Rendering:**
- SVG, PDF, PNG output
- WASM target for browser embedding
- SVG filter effects (drop shadows, glow) with Tufte-inspired guardrails
- Effect budget system prevents performance cliffs on large topologies
- Signature-based filter deduplication reduces SVG file size

**Analysis:**
- Path highlighting via BFS
- Traffic utilization overlays with NOC color mapping
- Timeline mode for multi-snapshot SVG export with incremental diffs
- Temporal entity queries (when did a node appear/change/disappear)
- Filter by type, tag, group, or layer without re-running layout

**Integration:**
- Python bindings via PyO3
- YAML/JSON topology input
- Adapters for LLDP/CDP discovery JSON and NetBox import
- Contract-versioned API for stable embedding

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust, Python, TypeScript |

---

## What This Is

A Rust-based network topology layout and visualization engine with 10+ layout algorithms, publication-quality rendering, WebGPU compute backend, and 3D/AR export. Takes complex multi-layer network topologies (via petgraph) and renders them using advanced algorithms that reduce visual complexity while preserving structural clarity. Outputs SVG, PDF, PNG, STL, GLB formats with interactive browser embedding via WASM.

---

## Core Value

Transform network topologies into clear, information-dense visualizations using algorithms that minimize edge crossings, bundle related connections, and respect hierarchical/geographic structure — enabling understanding of networks that would otherwise be visual noise.

---

## Requirements



---

## # Validated

v1.9 Layout Algorithm Expansion (shipped 2026-03-22):
- ✓ Circular arc layout with chord/arc edges and group-aware sectors — v1.9
- ✓ Curve elegance (Catmull-Rom, B-spline, rounded corners, Laplacian smoothing) — v1.9
- ✓ Node micro-visualizations (sparklines, pie/donut charts, bar charts) — v1.9
- ✓ Publication composition (legends, scale bars, figure presets, inset maps, QR codes) — v1.9
- ✓ Network domain semantics (interfaces, spanning tree, VRF/VLAN, LAG, port maps) — v1.9
- ✓ Motif simplification (subgraph detection, collapse to annotated glyphs) — v1.9
- ✓ WebGPU compute backend (GPU force-directed, Barnes-Hut tree walk) — v1.9
- ✓ 3D export (STL/GLB generation, WebXR AR session integration) — v1.9
- ✓ Orthogonal A* edge routing — v1.9
- ✓ WASM neighborhood reheating for interactive performance — v1.9

All  features from original roadmap:
- ✓ petgraph-based input API for topology definition
- ✓ Isometric multi-layer layout (Physical → L2 → IP → OSPF → iBGP → eBGP stacking)
- ✓ Edge bundling (hierarchical and force-directed bundling algorithms)
- ✓ Bezier edge routing with crossing/collision reduction
- ✓ Starburst/radial layout for containment groups (ASes, data centers, VLANs)
- ✓ Force-directed positioning with weighted edges (peering-aware, using fjadra)
- ✓ Radial tree layout for hierarchical structures
- ✓ Multiple node type support (routers, switches, servers, broadcast domains)
- ✓ Edge weight visualization (line thickness, style differentiation)
- ✓ SVG output
- ✓ PDF output
- ✓ PNG output
- ✓ Configuration API for layout selection and parameters
- ✓ CLI tool with JSON/YAML topology loading

v1.2 Visual Polish & Production Hardening (shipped 2026-02-09):
- ✓ SVG filter infrastructure with signature-based deduplication — v1.2
- ✓ Visual effects (drop shadows, glow, gradients, inner shadows) with semantic guardrails — v1.2
- ✓ WCAG 3:1 non-text contrast enforcement via automated parameter tuning — v1.2
- ✓ High-Contrast theme with AAA (21:1) contrast and redundant emphasis channels — v1.2
- ✓ Label collision avoidance with perpendicular-FIRST edge placement strategy — v1.2
- ✓ Export quality diagnostics for SVG/PNG/PDF material diffs — v1.2

v1.3 Embed Readiness & API Stability (shipped 2026-02-16):
- ✓ Deterministic rendering with golden fixture suite (55 SVG + 8 PNG + 8 PDF baselines) — v1.3
- ✓ Structured diagnostics envelope (v1.0 schema) with JSON/YAML/NDJSON CLI output — v1.3
- ✓ Multi-surface embedding API: contracts::v1 boundary, Rust facade, WASM envelope — v1.3
- ✓ R*-tree spatial label placement with scored candidates and viewport-aware sizing — v1.3
- ✓ CI governance: overlap gate, API drift detection, SemVer checks, versioned JSON Schemas — v1.3
- ✓ Rust SVG quality analyzer with label distance metrics (zero Python dependency) — v1.3

---

## # Active

v1.0.0 Release preparation:
- [ ] CLI user guide documentation
- [ ] Topology file format reference (JSON/YAML schema)
- [ ] Configuration file reference (NetVisConfig schema)
- [ ] Basic rustdoc on public APIs (module-level + core types)
- [ ] GitHub Actions CI pipeline (test, clippy, fmt, docs)
- [ ] Criterion benchmarks for layouts and rendering
- [ ] Package metadata for crates.io
- [ ] CHANGELOG.md for v1.0.0
- [ ] Security audit and preparation

---

## # Out of Scope

v1.0 feature development (complete):
- Python bindings — deferred to v1.1+ after release
- Browser/WASM embedding — deferred to v1.1+
- Interactive features (click events, zoom, show/hide) — deferred to v1.1+
- Topology discovery/parsing — users provide topology files
- Real-time animation — static output only

v1.0.0 release scope exclusions:
- Comprehensive library API documentation — CLI-first, defer detailed rustdoc to v1.1
- Examples for Rust library usage — have CLI examples, defer programmatic examples
- Advanced benchmarking (GPU, parallelization) — basic criterion benchmarks only
- Multi-platform CI testing — Linux/macOS only initially

---

## Planning Workflow

**Inbox Processing:**
Before starting milestone planning, review `inbox.md` in the project root for captured feature ideas and tasks. Categorize items as:
- **Current milestone:** Add to active requirements if critical
- **Future milestone:** Reference in out-of-scope or defer to next version
- **Research needed:** Flag for investigation before commitment

This ensures no ideas are lost and provides a backlog for future planning cycles.

---

## Context

**Background:**
This project builds on visualization concepts from academic work on Abstract Network Models, which represent networks across multiple protocol layers (Physical, Layer 2, IP Address, OSPF, iBGP, eBGP) with cross-layer associations. The goal is to make these visualizations programmatically accessible.

**Related project:**
Will eventually integrate with a "Topology Visualisation and Querying" tool (React-based) as an embedded visualization component with bidirectional communication (click events out, highlight commands in). This informs the need to design for browser embedding even though it's not v1 scope.

**Inspiration sources:**
- D3.js radial tree and hierarchical edge bundling
- Datashader/edgebundle hammer bundling algorithm
- Topology Zoo geographic network maps
- Edward Tufte's principles on information density and visual clarity
- fjadra (Rust port of d3-force) for force simulation

**Architecture vision:**
```
[Topology Sources] → [Input/petgraph] → [Core Layout Engine] → [Output/Render]
                                               ↓
                                    Multiple layout algorithms
                                    composable and configurable
```

---

## Constraints

- **Language**: Rust — required for performance of iterative layout algorithms (force-directed convergence, edge bundling optimization)
- **Graph library**: petgraph — well-maintained, performant, good API for network topology representation
- **Force simulation**: fjadra — Rust port of d3-force, WebAssembly-friendly, designed for interactive performance
- **Design philosophy**: Tufte-inspired — maximize information density, minimize chartjunk, clarity over decoration

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Rust for implementation | Iterative algorithms (force-directed, bundling) need performance; future WASM target | ✓ Good (v1.2: 51K LOC, WASM working) |
| petgraph for graph structure | Mature, performant, good Rust ecosystem fit | ✓ Good |
| fjadra for force simulation | d3-force semantics in Rust, WASM-ready, active development | ✓ Good |
| Library-first architecture | Primary use case is programmatic generation, not GUI tool | ✓ Good |
| Static output for v1 | Reduce scope; interactive features layered on later | ✓ Good |
| Defer Python bindings | Get core right first; bindings are mechanical once API is stable | ✓ Good (shipped v1.1) |
| SVG filters over raster post-processing (v1.2) | Maintain vector fidelity, theme-aware, resolution-independent | ✓ Good |
| Tufte-first design philosophy (v1.2) | Effects must enhance information, not decorate | ✓ Good (semantic guardrails prevent chartjunk) |
| Effect budget system >50 elements (v1.2) | Prevent performance cliff from excessive SVG filters | ✓ Good (auto-disable with warnings) |
| Signature-based filter deduplication (v1.2) | Reduce SVG bloat, share identical filter definitions | ✓ Good (O(1) reuse lookup) |
| Quantized EffectParams buckets (v1.2) | Enable WCAG tuning while preserving filter dedup | ✓ Good (0..=10 buckets) |
| WCAG 3:1 automated enforcement (v1.2) | Accessibility compliance without manual tuning | ✓ Good (auto-adjust + numeric warnings) |
| Text-anchor alignment for labels (v1.2) | Break geometric constraint (close + side + no truncation) | ✓ Good (10px spacing vs 150-233px) |
| Perpendicular-FIRST offset strategy (v1.2) | Keep edge labels visually connected while avoiding strokes | ✓ Good (zero overlap warnings) |

---

## Ecosystem Context

This project is part of a seven-tool network automation ecosystem. netvis provides topology visualization and rendering — the "visualize" stage of the pipeline.

**Role:** Render network topologies as high-quality static output (SVG/PNG/PDF) or interactive visualizations (WASM). Consume topology data from any upstream tool.

**Key integration points:**
- Renders topologies from [topogen](../topogen) (YAML), [ank-pydantic](../ank-pydantic) (JSON), or [netflowsim](../netflowsim) (GeoJSON with stats)
- WASM target enables embedding directly in the workbench browser UI
- Python bindings (PyO3) for programmatic rendering in Python workflows
- Geographic layout mode consumes lat/lon coordinates from [topogen](../topogen)'s geo module
- Contract-first versioned API (`contracts::v1`) for stable embedding

**Architecture documents:**
- [Ecosystem Architecture Overview](../../automationarch/README.md) — full ecosystem design, data flow, workflows
- [Ecosystem Critical Review](../../automationarch/REVIEW.md) — maturity assessment, integration gaps, strategic priorities

*Last updated: 2026-03-23 after v2.0 milestone initialization*

---

## Current Status

2026-03-30 -- Completed 182-03 U-slot annotation SVG rendering (gap closure)

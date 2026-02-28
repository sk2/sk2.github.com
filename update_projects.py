#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Clean Room Generation: Every page is rebuilt from scratch from Source of Truth metadata.
Includes Hardcoded Overrides to prevent loss of high-value technical content.
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime, timedelta


@dataclass
class ProjectInfo:
    name: str
    slug: str
    original_slug: str
    path: Path
    category: str
    status: str
    status_detail: Optional[str] = None
    stack: list[str] = field(default_factory=list)
    sections: Dict[str, str] = field(default_factory=dict)
    current_status: str = ""
    roadmap_summary: list[str] = field(default_factory=list)
    line_count: int = 0
    last_activity_date: Optional[datetime] = None


# SOURCE OF TRUTH: Explicit mapping of projects to ecosystems
ECOSYSTEM_MAP = {
    "network-simulator": "network-automation",
    "netsim": "network-automation",
    "ank_pydantic": "network-automation",
    "ank-pydantic": "network-automation",
    "compilation": "network-automation",
    "ank_nte": "network-automation",
    "ank-nte": "network-automation",
    "ank_workbench": "network-automation",
    "ank-workbench": "network-automation",
    "topogen": "network-automation",
    "cliscrape": "network-automation",
    "configparsing": "network-automation",
    "deviceinteraction": "network-automation",
    "automationarch": "network-automation",
    "autonetkit": "network-automation",
    "autonetkit-foundation": "network-automation",
    "netflowsim": "network-automation",
    "netvis": "network-automation",
    "ank_netcfg": "network-automation",
    "ank-netcfg": "network-automation",
    "netassure": "network-automation",
    "signals": "signal-processing",
    "spectra": "signal-processing",
    "rtltcp": "signal-processing",
    "passive": "signal-processing",
    "rf-signal-analysis": "signal-processing",
    "wifi-radar": "signal-processing",
    "wifi-signal-analysis": "signal-processing",
    "healthypi": "agentic-systems",
    "multi-agent": "agentic-systems",
    "multi-agent-assistant": "agentic-systems",
    "cycle": "agentic-systems",
    "hrv": "agentic-systems",
}

PROJECT_ALIASES = {
    "ank_pydantic": "Network Modeling & Configuration Library",
    "ank-pydantic": "Network Modeling & Configuration Library",
    "cliscrape": "CLI Parser",
    "rtltcp": "Radio Streaming Server",
    "auroradata": "Aurora Advisor",
    "netflowsim": "Performance Simulator",
    "ank_netcfg": "Network Configuration Framework",
    "ank-netcfg": "Network Configuration Framework",
    "netassure": "Network Analysis Engine",
    "netsim": "Network Simulator",
    "network-simulator": "Network Simulator",
    "compilation": "Network Compilation Engine",
    "topogen": "Topology Generator",
    "ank-nte": "Topology Engine Core",
    "ank-workbench": "Automation Workbench",
    "autonetkit-foundation": "Network Modeling Foundations",
    "autonetkit": "Configuration Generation (AutoNetkit)",
    "netvis": "Visualization Engine",
    "passive": "Signal Reflection Analysis",
    "signals": "Spectrum Analysis",
    "configparsing": "Brownfield Ingestion & Analysis",
    "soundarray": "Sound Array",
}

# Canonical URL mapping: consolidate alternate slugs into a single published page.
# This ensures the rich simulator page remains the primary destination, even if other
# sources refer to the pretty slug.
CANONICAL_SLUG = {
    "network-simulator": "netsim",
    "ank-netcfg": "ank-netcfg",  # Consolidate ank_netcfg variants to hyphenated form
}

# GOLDEN MASTER CONTENT: Used to ensure high-value technical detail is never lost.
PROJECT_CONTENT_OVERRIDES = {
    "netsim": {
        "Concept": "Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.\n\nUnlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.",
        "Protocols Implemented": "- **Routing**: OSPF (point-to-point, Area 0, LSA Types 1/2, Dijkstra SPF), IS-IS (L1/L2 hierarchical, LSP flooding), BGP (iBGP/eBGP, communities, route propagation).\n- **MPLS**: LDP label distribution, label push/swap/pop operations, MPLS OAM.\n- **Resilience**: BFD (bidirectional forwarding detection, async mode).\n- **Tunneling**: GRE encapsulation, VRF isolation (L3VPN foundations).\n- **Layer 2/3**: ARP request/reply, ICMP echo (ping), Time Exceeded (traceroute).",
        "Architecture": "- **Tick-based execution**: Deterministic, reproducible simulations (~1ms per tick).\n- **RIB/FIB separation**: Mirrors real router behavior for high-fidelity state validation.\n- **Convergence detection**: Automatically detects network stabilization to minimize simulation time.\n- **Scripted commands**: Diagnostics can be executed at specific ticks or immediately after convergence.",
        "Performance": "Simulates 100+ device topologies in seconds. Generates structured JSON output for seamless integration into CI/CD pipelines.",
    },
    "ank-workbench": {
        "Concept": "**An orchestration platform** that integrates the ANK ecosystem tools (TopoGen, ank_pydantic, Network Simulator, NetVis) into one seamless workflow. It serves as the **glue layer** that coordinates the entire network automation pipeline, allowing engineers to generate topologies, model networks declaratively, run lightweight simulations, and visualize results from a unified interface.\n\n```\n┌──────────────────────────────────────────────────────────────────┐\n│                        ANK Workbench                             │\n│         (Orchestration · Web UI · Workflow Management)           │\n│   ┌──────────────┬──────────────┬──────────────┬──────────────┐ │\n│   │   TopoGen    │ ank-pydantic │   Simulator  │    NetVis    │ │\n└───┴──────────────┴──────────────┴──────────────┴──────────────┴─┘\n```",
        "Key Capabilities": "- **Design-First Workflow**: Declarative Pydantic models → lightweight simulation → integrated topology/config/behavior visualization.\n- **Persistent Help System**: Non-modal drawer with contextual tips and route-aware visibility.\n- **Sample Gallery**: Curated offline topologies ranging from 2-node starters to 12-node spine-leaf data centers.\n- **Intelligent Empty States**: Cause-specific UI patterns with outcome previews to guide new users.\n- **Guided Tour**: 8-step workflow coverage with CSS-only spotlight for rapid onboarding.",
        "Visuals": "The Workbench provides real-time feedback through integrated NetVis overlays, allowing for the inspection of physical, logical, and protocol layers alongside routing table state and simulation diagnostics.",
    },
    "ank-pydantic": {
        "Concept": "A Python-native configuration engine for defining a network model and compiling it into a consistent, reviewable plan. It solves the 'type safety vs performance' problem by combining the ergonomics of Pydantic models with a fast Rust graph core (NTE).\n\nAs one of the two primary modeling tools in the ecosystem, it offers a high-level, developer-friendly interface for building complex network designs. It uses an explicit intermediate representation and transformation passes (design -> plan -> protocol layers) to ensure architectural consistency across the entire topology.",
        "Features": "- **Type-Safe Modeling**: Device, interface, and relationship models with strict Pydantic validation.\n- **Rust-Backed Operations**: High-performance graph traversals and queries via PyO3 and petgraph.\n- **Rich Query API**: Chainable filters and traversals that replace manual graph walking with declarative intent.\n- **Multi-Layer Support**: Native modeling of physical, logical, and protocol views within a single graph structure.\n- **Multi-Vendor Generation**: Compiles intent into validated configurations for 11+ major networking platforms.",
    },
    "compilation": {
        "Concept": "A native Rust-based configuration compiler that serves as a high-performance alternative to the Python-based modeling engine. While sharing the same underlying data models and 'Whiteboard -> Build' philosophy, this tool is built for maximum execution speed and formal verification during the compilation process.\n\nIt treats network design as 'source code' that is parsed, validated, and transformed through multiple intermediate representations (IR). By modeling the network as a set of interconnected state machines, the engine can verify that the generated configuration is not only syntactically correct but also logically sound across massive multi-vendor estates.",
        "Technical Depth": "- **High-Performance Pipeline**: Native Rust implementation optimized for sub-second compilation of 10,000+ node graphs.\n- **Static Analysis**: Detects reachability issues, protocol mismatches, and configuration drifts during the build phase.\n- **Deterministic Output**: Ensures that the same input design always produces identical, bit-compatible configuration output.\n- **Architectural Invariants**: Formally enforces design rules (e.g., 'no single point of failure in the core') as part of the compilation logic.",
    },
    "autonetkit": {
        "Concept": "A compiler-based framework for automated network provisioning. AutoNetkit transforms high-level network designs into validated device configurations across heterogeneous hardware and protocol environments.\n\nTraditional network configuration is often manual and vendor-specific. AutoNetkit introduces a declarative approach where engineers define the network design, and the engine handles the transformations required to generate the underlying protocol parameters and CLI commands.\n\nThe current work is focused on a modern compiler pipeline: a stable intermediate representation, explicit transformation passes, and predictable code generation for multiple targets.",
        "Roadmap Direction": "- **Intermediate Representations (IR):** A canonical, network-wide model that separates design requirements from device-specific implementation details.\n- **Compiler Passes:** Validation and rewrite passes that make changes explainable (and reversible) rather than implicit side effects.\n- **Deterministic Output:** Stable ordering and repeatable generation to support diffs, review, and CI gating.\n- **Multi-Target Backends:** Separate backends for vendor CLIs and structured formats (e.g., JSON/YAML) to support tooling and audit workflows.",
        "Features": "- **Automated IP Addressing**: Intelligent allocation of loopbacks and link subnets across multiple protocol layers.\n- **Protocol Orchestration**: Automatic generation of consistent OSPF areas, IS-IS levels, and BGP peering relationships (iBGP/eBGP).\n- **Multi-Vendor Support**: Compiles intent into native configuration formats for Cisco (IOS, XR, NX-OS), Juniper (JunOS), and Arista (EOS).\n- **Visual Feedback**: Generates real-time topological diagrams to verify the physical and logical structure of the design.",
        "Architecture": "AutoNetkit employs a multi-stage transformation pipeline:\n1. **Specification Abstraction**: Captures the high-level design intent.\n2. **Intermediate Representation**: A network-wide graph model that maintains cross-vendor consistency.\n3. **Device Specialization**: Transforms the abstract model into device-specific protocol state.\n4. **Template Assembly**: Generates the final CLI commands using verified vendor templates.",
        "Impact": "Earlier iterations of AutoNetkit were integrated into industry tooling for automated lab provisioning. That integration reflects the lineage of the approach, not the current in-progress implementation.\n\nTo avoid confusion with the current configuration engine, this page focuses on the ideas and the compiler-style approach rather than tying claims to any specific modern implementation.",
    },
    "configparsing": {
        "Concept": "A specialized framework for **Brownfield Ingestion and Analysis**. It extracts high-level architectural intent and topology relationships from legacy network state—including vendor-specific CLI configurations and unstructured PDF documentation—normalizing them into a vendor-neutral model.\n\nThis system bridges the gap between existing deployments and the modern, declarative ANK toolchain. By leveraging LLM-powered RAG pipelines, it identifies complex protocol relationships and link roles that are often hidden in thousands of lines of manual configuration.",
        "Use Cases": '- **Automated Network Audit**: Identify inconsistencies and compliance drifts across legacy multi-vendor estates.\n- **Migration Planning**: Automatically generate "As-Is" topology models and protocol relationships for hardware refresh or greenfield migrations.\n- **Intent Extraction**: Transform manual device configurations into structured, declarative models.',
        "Technical Depth": "The system acts as the 'External Discovery' input for the Workbench, bridging the gap between existing brownfield deployments and the modern, declarative design toolchain.",
    },
    # Prefer the rich long-form simulator page as the canonical one.
    # The pretty slug (network-simulator) is retained, but its content is sourced from netsim.
    "autonetkit-foundation": {
        "Concept": "The original research that established the principles of automated network configuration. This work introduced the **Whiteboard → Plan → Build** transformation model, which allows engineers to work with high-level design abstractions while the system handles the technical implementation details.",
        "Research Contribution": "- **Abstractions**: Identified the fundamental primitives needed to represent network intent independently of vendor syntax.\n- **Transformations**: Developed graph-based algorithms to automatically calculate IP addresses, OSPF areas, and BGP peerings.\n- **Scalability**: Verified that automated generation can handle core-network topologies with hundreds of devices in seconds.\n- **Industry Impact (Legacy)**: Earlier iterations were integrated into industry tooling for automated lab provisioning.",
    },
    "topogen": {
        "Concept": "A Rust-based topology generation engine that consolidates complex network graph algorithms into a unified, high-performance library. It enables the creation of realistic, validated network structures ranging from small lab setups to massive data center and backbone environments.",
        "Features": "- **Data Center Patterns**: Generate leaf-spine and fat-tree topologies with realistic tier ratios and oversubscription parameters.\n- **WAN & Backbone Models**: Create ring, mesh, POP-based, and hierarchical structures based on real-world ISP patterns.\n- **Random Graph Models**: Support for Barabási-Albert (scale-free) and Watts-Strogatz (small-world) algorithms for research and scale testing.\n- **Traffic Matrix Generation**: Automatically produce demand matrices using gravity models and distance-based weighting.",
        "Technical Depth": "The engine is implemented in Rust for maximum performance, allowing for the sub-second generation of 10,000+ node graphs. It exports a standardized YAML format that is consumed across the entire ANK ecosystem, ensuring structural consistency from design to simulation.",
    },
    "ank-nte": {
        "Concept": "The high-performance graph core that powers the ANK ecosystem. NTE (Network Topology Engine) provides a native Rust implementation of multi-layer network graphs, optimized for low-latency queries and complex topological transformations.",
        "Architecture": "Built as a 14-crate Cargo workspace, the engine utilizes `petgraph`'s StableDiGraph for structural persistence. It features a pluggable datastore architecture supporting Polars, DuckDB, and Lite backends, allowing for efficient attribute storage and bulk data analysis.",
        "Technical Depth": "The engine implements a 'Write-Through' model with Python bindings via PyO3. Mutations in the Python layer are automatically persisted to the Rust core, ensuring that topological queries always execute against high-performance compiled graph algorithms rather than slower interpreted structures.",
    },
    "netflowsim": {
        "Concept": "A performance analysis engine that utilizes analytic queuing models and Monte Carlo simulations to validate network capacity at scale. Unlike packet-level simulators, netflowsim focuses on probabilistic outcomes across billions of traffic flows.",
        "Use Cases": "- **Capacity Planning**: Identify bottleneck links and compute-bound nodes before traffic growth impacts production.\n- **Resilience Testing**: Probabilistically analyze the impact of link or node failures on overall network throughput and latency.\n- **Routing Strategy Validation**: Compare the performance of different traffic engineering strategies (e.g., ECMP vs RSVP-TE) against realistic demand matrices.",
        "Technical Depth": "The engine uses M/M/1 and M/D/1 queuing models implemented in a highly parallelized Rust execution environment. It leverages the Rayon crate to distribute Monte Carlo iterations across all available CPU cores, enabling the analysis of massive traffic scenarios in seconds.",
    },
    "ank-netcfg": {
        "Concept": "A modern, type-safe configuration engine that serves as a successor and sibling to the original AutoNetkit research. It implements the same 'Whiteboard -> Plan -> Build' transformation model but utilizes a modern, schema-enforced pipeline to ensure configuration correctness across heterogeneous network fleets.",
        "Technical Depth": "Sitting alongside the core ANK toolchain, ank_netcfg focuses on the high-fidelity transformation of network intent into vendor-specific device states. It provides the protocol-level intelligence needed to generate consistent OSPF, BGP, and MPLS configurations while maintaining strict type safety via a Pydantic-based model layer.",
    },
    "netassure": {
        "Concept": "A multi-paradigm computational analysis tool for network topology verification, prediction, and optimization. It provides five complementary analysis approaches: formal verification (header space analysis, reachability), graph algorithms (centrality, community detection), failure cascade modeling (percolation theory, Monte Carlo), machine learning (GNN-based failure prediction), and optimization (topology tuning, design suggestions).\n\nUnlike single-purpose tools, netassure operates on three data sources simultaneously—static topology from autonetkit, simulation results from netsim/netflowsim, and runtime telemetry from production systems—providing comprehensive analysis across the entire network lifecycle.",
        "Architecture": "**Hybrid Rust + Python design** optimized for performance and flexibility:\n- **Rust core** handles deterministic, performance-critical algorithms (formal verification via Z3, graph operations via petgraph, cascade modeling)\n- **Python layer** provides ML capabilities (PyTorch Geometric for GNN models), telemetry integration (Prometheus, BMP, NetFlow), and statistical optimization\n- **PyO3 bindings** enable seamless integration, allowing Python code to invoke high-performance Rust algorithms without serialization overhead",
        "Key Capabilities": "- **Formal Verification**: Header Space Analysis, reachability checking, loop detection, equivalence verification using Z3\n- **Graph Analysis**: Centrality metrics, community detection, path diversity, network robustness quantification\n- **Failure Cascade Modeling**: Percolation theory simulations, Monte Carlo analysis (1000+ iterations), load redistribution scenarios\n- **Machine Learning**: GNN-based failure prediction, traffic forecasting, anomaly detection trained on simulation data\n- **Optimization**: Topology optimization suggestions, protocol parameter tuning, design constraint solving",
        "Tech Stack": "Rust (petgraph, rustworkx, z3-rs, rayon, PyO3), Python (PyTorch, PyTorch Geometric, MLflow, Prometheus client, Polars)",
    },
    # NOTE: Keep each project key unique; later entries overwrite earlier ones.
}

CATEGORY_MAP = {
    "network": (
        "🌐 Network Engineering",
        "Tools for network design, simulation, and analysis.",
        "/network-automation",
    ),
    "sdr": (
        "📡 Radio Systems",
        "Radio signal analysis and spectrum monitoring.",
        "/signal-processing",
    ),
    "health": (
        "🏥 Health & Biometrics",
        "Real-time biometric signal processing.",
        "/agentic-systems",
    ),
    "astrophotography": (
        "🔭 Astrophotography",
        "Autonomous imaging and celestial monitoring.",
        None,
    ),
    "photography": ("📷 Photography", "Automated camera control and monitoring.", None),
    "agents": (
        "🤖 Autonomous Systems",
        "Secure systems for agents and infrastructure automation.",
        "/agentic-systems",
    ),
    "data": (
        "📊 Data & Utilities",
        "Geospatial analytics and time-series discovery.",
        "/data-analytics",
    ),
    "wellness": (
        "🧘 Wellness & Sound",
        "Sound analysis and wellness monitoring.",
        None,
    ),
    "experimental": (
        "🧪 Experimental",
        "Exploratory projects and technical experiments.",
        None,
    ),
}


# Stable ordering for public browsing.
# Only applies within a category; anything not listed falls through to the default sort.
CATEGORY_ORDER = {
    "network": [
        "netsim",
        "autonetkit",
        "compilation",
        "ank-netcfg",
        "netassure",
        "configparsing",
        "netvis",
        "ank-nte",
        "topogen",
        "ank-workbench",
        "cliscrape",
        "netflowsim",
        "autonetkit-foundation",
        "ank-pydantic",
    ]
}

FM_SECTIONS = {
    "network": "network-automation",
    "sdr": "signal-processing",
    "agents": "agentic-systems",
    "health": "agentic-systems",
    "data": "data-analytics",
}

# Professional Narrative Sequence
DETAILED_SECTIONS = [
    "Concept",
    "The Insight",
    "Overview",
    "What This Is",
    "Problem It Solves",
    "Core Value",
    "Features",
    "Key Capabilities",
    "Use Cases",
    "Screenshots",
    "Visuals",
    "Architecture",
    "Technical Depth",
    "Security Model",
    "Implementation Details",
    "Protocols Implemented",
    "Performance",
    "Metrics",
    "Integration",
    "Hardware",
    "Agents",
    "Components",
    "Tech Stack",
    "Research Contribution",
    "Impact",
    "Automation",
    "Usage",
    "Available Commands",
    "Output Formats",
    "Quick Facts",
]

# Sections that, if manually polished in the website repo, should be preserved.
# These will NOT be overwritten by raw metadata from .planning/PROJECT.md.
STABLE_SECTIONS = {
    "Concept",
    "The Insight",
    "Overview",
    "What This Is",
    "Problem It Solves",
    "Core Value",
    "Architecture",
    "Technical Depth",
    "Features",
    "Key Capabilities",
    "Use Cases",
    "Screenshots",
    "Visuals",
    "Implementation Details",
    "Tech Stack",
    "Research Contribution",
    "Impact",
    "Quick Facts",
}


def extract_sections(content: str) -> Dict[str, str]:
    # Parse level-2 headings ("## ...") into a section map.
    sections: Dict[str, str] = {}

    in_code_fence = False
    current_header: Optional[str] = None
    current_lines: list[str] = []

    for line in content.splitlines():
        if re.match(r"^\s*```", line):
            in_code_fence = not in_code_fence

        if not in_code_fence:
            # Skip auto-generated footers and table of contents
            if line.strip().startswith("[← Back to"):
                continue
            if line.strip() == "---":
                continue

            # Look for level-2 headings as section boundaries
            m = re.match(r"^##\s*(.+?)\s*$", line)
            if m:
                header = m.group(1).strip()
                if header in ["Contents"]:
                    current_header = None
                    continue
                
                if current_header is not None:
                    body = "\n".join(current_lines).strip()
                    if body:
                        sections[current_header] = body
                current_header = header
                current_lines = []
                continue

        if current_header is not None:
            current_lines.append(line)

    if current_header is not None:
        body = "\n".join(current_lines).strip()
        body = re.sub(r"\n+---+\s*$", "", body)
        if body:
            sections[current_header] = body

    return sections


def clean_text(text: str) -> str:
    """Aggressively strip phases, progress, and project management clutter."""
    text = re.sub(r"\(Phase.*?\)", "", text)
    text = re.sub(r"Phase \d+.*?\d+", "", text)
    text = re.sub(r"\*\*Phase \d+.*?\*\*", "", text)
    text = re.sub(r"\d+%", "", text)
    text = re.sub(r"^\s*·\s*\*\*.*?\*\*\s*$", "", text, flags=re.MULTILINE)
    # Strip trailing horizontal rules and whitespace
    text = text.strip()
    text = re.sub(r"\n+---+\s*$", "", text)
    return text.strip()


def generate_toc(content: str) -> str:
    """Generate a table of contents from ## headers."""
    headers = re.findall(r"^##\s+([^#\n]+)\s*$", content, re.MULTILINE)
    headers = [
        h.strip() for h in headers if h.strip() not in ["Contents", "Quick Facts"]
    ]
    if len(headers) < 4:
        return ""
    links = []
    for h in headers:
        slug = h.lower().replace(" ", "-")
        slug = re.sub(r"[^a-z0-9-]", "", slug)
        slug = re.sub(r"-+", "-", slug)
        links.append(f"- [{h}](#{slug})")
    return "## Contents\n\n" + "\n".join(links) + "\n\n"


def get_back_links(category: str) -> str:
    links = []
    if category in FM_SECTIONS:
        slug = FM_SECTIONS[category]
        title = slug.replace("-", " ").title()
        if slug == "network-automation":
            title = "Network Automation"
        if slug == "agentic-systems":
            title = "Autonomous Systems"
        if slug == "signal-processing":
            title = "Signal Processing"
        links.append(f"[← Back to {title}](../{slug})")
    links.append("[← Back to Projects](../projects)")
    return "\n\n".join(links)


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists():
        return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists():
        return None
    content = project_md.read_text()

    name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    project_name = re.sub(
        r"^(Project|PROJECT):\s*", "", project_name, flags=re.IGNORECASE
    )

    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {
        "multi-agent-assistant": "multi-agent",
        "passive": "rf-signal-analysis",
        "wifi-radar": "wifi-signal-analysis",
        "ank_pydantic": "ank-pydantic",
    }
    slug = slug_mappings.get(slug, slug)

    # Canonical slug mapping: consolidate alternate slugs to a single published page.
    # Keep old slugs in ECOSYSTEM_MAP for categorization, but generate content under the canonical slug.
    canonical_from = slug
    slug = CANONICAL_SLUG.get(slug, slug)

    # Apply display-name alias based on original slug first, then canonical slug.
    if canonical_from in PROJECT_ALIASES:
        project_name = PROJECT_ALIASES[canonical_from]
    elif slug in PROJECT_ALIASES:
        project_name = PROJECT_ALIASES[slug]

    sections = extract_sections(content)

    # Preserve rich long-form content if upstream docs provide it. Some projects
    # historically used headings like "The Insight" and "Technical Depth" with
    # code examples; these should not be dropped during regeneration.
    # Check both the canonical slug and the original source slug for overrides.
    for s_key in [slug, canonical_from]:
        if s_key in PROJECT_CONTENT_OVERRIDES:
            for sec, body in PROJECT_CONTENT_OVERRIDES[s_key].items():
                sections[sec] = body

    cat = "experimental"
    s = slug.lower()
    if any(x in s for x in ["photo-tour"]):
        cat = "photography"
    elif any(x in s for x in ["watchnoise", "psytrance"]):
        cat = "wellness"
    elif any(x in s for x in ["healthypi", "hrv"]):
        cat = "health"
    elif any(
        x in s
        for x in [
            "spectra",
            "rtltcp",
            "wifi-signal-analysis",
            "signals",
            "rf-signal-analysis",
        ]
    ):
        cat = "sdr"
    elif any(x in s for x in ["astro", "aurora", "eclipse", "satellites"]):
        cat = "astrophotography"
    elif any(x in s for x in ["agent", "multi-agent", "cycle"]):
        cat = "agents"
    elif any(
        x in s
        for x in [
            "netflow",
            "polars",
            "tileserver",
            "matrix-time-series",
            "matrix-profile",
            "weather",
            "omnifocus-db",
            "cliscrape",
            "nascleanup",
            "devmon",
        ]
    ):
        cat = "data"
    elif any(
        x in s
        for x in [
            "netvis",
            "ank",
            "topogen",
            "netsim",
            "autonetkit",
            "network",
            "configparsing",
            "nte",
            "orchestrator",
            "automationarch",
            "netflowsim",
        ]
    ):
        cat = "network"

    stack = []
    constraints = sections.get("Constraints", "")
    tech_patterns = [
        r"\*\*Tech Stack[:\-]?\*\*:?\s*(.+)",
        r"\*\*Language\*\*:?\s*(.+?)(?:\s+—|$)",
    ]
    for pattern in tech_patterns:
        match = re.search(pattern, constraints)
        if match:
            s_str = match.group(1).split("\n")[0]
            stack.extend([s.strip() for s in re.split(r"[,;·]", s_str) if s.strip()])
            break

    current_status, last_activity_date = "", None
    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text()
        la_match = re.search(r"Last activity:\s*(.+)", state_content)
        if la_match:
            activity_text = la_match.group(1).strip()
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", activity_text)
            if date_match:
                try:
                    last_activity_date = datetime.strptime(
                        date_match.group(1), "%Y-%m-%d"
                    )
                except ValueError:
                    pass
            current_status = activity_text

    status_detail = "Active"
    if last_activity_date:
        today = datetime(2026, 2, 24)
        if today - last_activity_date <= timedelta(days=7):
            status_detail = "Recently Updated"
        else:
            status_detail = f"Last Active: {last_activity_date.strftime('%Y-%m-%d')}"

    roadmap_summary = []
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text()
        ms_matches = re.finditer(
            r"^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$", roadmap_content, re.MULTILINE
        )
        for match in ms_matches:
            ms_name = clean_text(match.group(1))
            ms_detail = clean_text(match.group(2))
            roadmap_summary.append(f"**{ms_name}** {ms_detail}")
            if len(roadmap_summary) >= 5:
                break

    return ProjectInfo(
        name=project_name,
        slug=slug,
        original_slug=canonical_from,
        path=project_path,
        category=cat,
        status="active",
        status_detail=status_detail,
        stack=stack,
        sections=sections,
        current_status=current_status,
        roadmap_summary=roadmap_summary,
        last_activity_date=last_activity_date,
    )


def generate_detailed_page(project: ProjectInfo) -> str:
    # Auto-generate Quick Facts if not present
    if "Quick Facts" not in project.sections:
        facts = []
        if project.status_detail:
            facts.append(f"| **Status** | {project.status_detail} |")
        if project.stack:
            facts.append(f"| **Stack** | {', '.join(project.stack)} |")
        if facts:
            project.sections["Quick Facts"] = "| | |\n|---|---|\n" + "\n".join(facts)

    eco_slug = ECOSYSTEM_MAP.get(project.slug, "projects")
    fm = f"---\nlayout: default\nsection: {eco_slug}\n---\n\n"
    status_badge = (
        f'<span class="status-badge status-active">{project.status_detail}</span>'
    )
    back_links = get_back_links(project.category)
    header = f"# {project.name}\n\n{status_badge}\n\n{back_links}\n\n---\n\n"
    intro_parts = []
    processed_sections = set()
    for s in [
        "Concept",
        "The Insight",
        "Overview",
        "What This Is",
        "Problem It Solves",
        "Core Value",
    ]:
        if s in project.sections:
            intro_parts.append(clean_text(project.sections[s]))
            processed_sections.add(s)
            
    body_list = []
    if intro_parts:
        body_list.append(f"## Concept\n\n" + "\n\n".join(intro_parts))
    
    # First, append standard sections in the preferred narrative order
    for s in DETAILED_SECTIONS:
        if s in project.sections and s not in processed_sections:
            body_list.append(f"## {s}\n\n{clean_text(project.sections[s])}")
            processed_sections.add(s)
            
    # Then, append any other remaining sections that weren't in the standard list
    # to ensure NO content is lost during the merge/cleanup.
    for s, content in project.sections.items():
        if s not in processed_sections and s not in ["Current Status", "Roadmap", "Contents"]:
            body_list.append(f"## {s}\n\n{clean_text(content)}")

    if project.current_status:
        body_list.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary:
        body_list.append(
            "## Roadmap\n\n"
            + "\n".join([f"- {item}" for item in project.roadmap_summary])
        )
    
    final_body = "\n\n---\n\n".join(body_list)
    toc = generate_toc(final_body)
    
    # Ensure only one separator between header and body, and before back-links
    return fm + header + toc + final_body + f"\n\n---\n\n{back_links}\n"


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = [
        "---",
        "layout: default",
        "---",
        "",
        "# Projects",
        "",
        "Focused on network engineering, autonomous systems, and signal processing.",
        "",
        "---",
        "",
    ]
    # Exclude internal/planning artifacts and pages we don't want listed publicly.
    hidden_slugs = set()

    visible_projects = [p for p in projects if p.slug not in hidden_slugs]

    def sort_key(p: ProjectInfo):
        # Primary: stable ordering within category
        order = CATEGORY_ORDER.get(p.category, [])
        try:
            idx = order.index(p.slug)
        except ValueError:
            idx = 10_000

        # Secondary: keep large flagship pages first
        return (idx, -p.line_count, p.name)

    sorted_projects = sorted(visible_projects, key=sort_key)
    categorized = {k: [] for k in CATEGORY_MAP.keys()}
    for p in sorted_projects:
        categorized[p.category].append(p)
    for cat_key, (title, desc, link) in CATEGORY_MAP.items():
        projs = categorized[cat_key]
        if not projs:
            continue
        lines.append(f"## {title}\n")
        for p in projs:
            summary = ""
            for k in [
                "Concept",
                "The Insight",
                "Overview",
                "What This Is",
                "Core Value",
            ]:
                if k in p.sections:
                    summary = p.sections[k].strip().split("\n\n")[0]
                    summary = clean_text(re.sub(r"!\[.*?\]\(.*?\)", "", summary))
                    if summary:
                        break
            summary = (
                summary.replace("high-performance", "fast")
                .replace("blazing-fast", "fast")
                .replace("cutting-edge", "modern")
            )
            sents = re.split(r"(?<=[.!?])\s+", summary)
            summary = " ".join(sents[:3])
            lines.append(f"### [{p.name}](projects/{p.slug})\n")
            lines.append(
                f'<span class="status-badge status-active">{p.status_detail}</span>'
            )
            lines.append(f"\n\n{summary}\n\n")
    lines.append(
        "<style>\n.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }\n.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }\nsection { margin-bottom: 2em; }\n</style>"
    )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scan-dirs",
        nargs="+",
        default=["~/dev"],
    )
    args = parser.parse_args()

    # If a regen run happens without the real project folders present, the output
    # collapses into short stubs. Prefer failing loudly over silently clobbering
    # long-form pages.
    scan_paths = [Path(d).expanduser() for d in args.scan_dirs]
    existing = [p for p in scan_paths if p.exists()]
    if not existing:
        raise SystemExit(
            "No --scan-dirs paths exist. Refusing to regenerate project pages. "
            "Pass valid project roots (e.g. --scan-dirs ~/dev)."
        )
    projects = []
    for p in existing:
        if p.exists():
            for pd in sorted(p.iterdir()):
                if (
                    not pd.is_dir()
                    or "-clean-" in pd.name
                    or "backup" in pd.name.lower()
                ):
                    continue
                info = parse_project_metadata(pd)
                if info:
                    projects.append(info)
    projects_dir = Path("projects")
    scanned_slugs = {p.slug for p in projects}
    for slug in PROJECT_CONTENT_OVERRIDES:
        if slug not in scanned_slugs:
            canonical = CANONICAL_SLUG.get(slug, slug)
            if canonical in scanned_slugs:
                continue
            name = PROJECT_ALIASES.get(slug, slug.title())
            projects.append(
                ProjectInfo(
                    name=name,
                    slug=canonical,
                    original_slug=slug,
                    path=projects_dir / f"{slug}.md",
                    category="network",
                    status="active",
                    status_detail="Active",
                    sections=PROJECT_CONTENT_OVERRIDES[slug],
                )
            )

    # Maintenance: Identify existing project pages in the projects/ directory that 
    # were not scanned or explicitly overridden. This ensures they still get 
    # formatting fixes, Quick Facts, and footer cleanup.
    processed_slugs = {p.slug for p in projects}
    for pp in sorted(projects_dir.glob("*.md")):
        slug = pp.stem
        if slug in processed_slugs or slug == "todo":
            continue
        
        # Load metadata from existing page
        content = pp.read_text()
        name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        name = name_match.group(1).strip() if name_match else slug.title()
        
        # Extract ALL existing sections to preserve them
        existing_sections = extract_sections(content)
        
        # Simple category detection from frontmatter or slug
        cat = "experimental"
        if 'section: network-automation' in content: cat = "network"
        elif 'section: signal-processing' in content: cat = "sdr"
        elif 'section: agentic-systems' in content: cat = "agents"
        elif 'section: data-analytics' in content: cat = "data"
        
        projects.append(
            ProjectInfo(
                name=name,
                slug=slug,
                original_slug=slug,
                path=pp,
                category=cat,
                status="active",
                status_detail="Active",
                sections=existing_sections,
            )
        )

    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        
        # Merge logic: if the page already exists, preserve stable sections that have 
        # been manually polished.
        if pp.exists():
            existing_content = pp.read_text()
            existing_sections = extract_sections(existing_content)
            for sec in STABLE_SECTIONS:
                if sec in existing_sections:
                    # Check if it was an explicit golden master override in the script.
                    # Overrides take precedence over manual edits for high-value content.
                    is_override = False
                    for s_key in [p.slug, p.original_slug]:
                        if s_key in PROJECT_CONTENT_OVERRIDES and sec in PROJECT_CONTENT_OVERRIDES[s_key]:
                            is_override = True
                            break
                    
                    if not is_override:
                        # Prefer the locally polished version
                        p.sections[sec] = existing_sections[sec]
        
        p.line_count = len(generate_detailed_page(p).splitlines())
        pp.write_text(generate_detailed_page(p))
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()

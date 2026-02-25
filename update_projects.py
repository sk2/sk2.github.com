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
    "ank_pydantic": "Configuration Engine",
    "ank-pydantic": "Configuration Engine",
    "cliscrape": "CLI Parser",
    "rtltcp": "Radio Streaming Server",
    "auroradata": "Aurora Advisor",
    "netflowsim": "Performance Simulator",
    "netsim": "Network Simulator",
    "network-simulator": "Network Simulator",
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
}

# GOLDEN MASTER CONTENT: Used to ensure high-value technical detail is never lost.
PROJECT_CONTENT_OVERRIDES = {
    "network-simulator": {
        # This key should not normally be used because network-simulator is canonicalized to netsim.
        # Kept defensively in case a future source bypasses canonicalization.
        "Concept": "This page is kept for backward-compatible linking. The canonical, detailed documentation lives on the main Network Simulator page.",
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
    "ank-pydantic": {
        "Concept": "A modern configuration engine for defining a network model and compiling it into a consistent, reviewable plan for downstream tooling. Built with type-safe Pydantic models and a fast Rust core (NTE), it provides a predictable, programmable way to manage large-scale topology data and derived configuration state.\n\nA Python library for modeling and querying network topologies, backed by a high-performance Rust core (`ank_nte`). Uses an explicit intermediate representation and transformation passes (design -> plan -> protocol layers), with type-safe models for nodes/edges/layers and a composable query API.",
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
        "network-simulator",
        "autonetkit",
        "configparsing",
        "netvis",
        "ank-nte",
        "topogen",
        "ank-workbench",
        "cliscrape",
        "netflowsim",
        "autonetkit-foundation",
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
    "Features",
    "Key Capabilities",
    "Use Cases",
    "Screenshots",
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
    "Development Status",
    "Roadmap",
    "Quick Facts",
]


def extract_sections(content: str) -> Dict[str, str]:
    # Parse level-2 headings ("## ...") into a section map.
    # Important: do not treat headings inside fenced code blocks as section
    # boundaries.
    sections: Dict[str, str] = {}

    in_code_fence = False
    current_header: Optional[str] = None
    current_lines: list[str] = []

    for line in content.splitlines():
        if re.match(r"^\s*```", line):
            in_code_fence = not in_code_fence

        if not in_code_fence:
            m = re.match(r"^##\s+(.+?)\s*$", line)
            if m:
                if current_header is not None:
                    body = "\n".join(current_lines).strip()
                    if body:
                        sections[current_header] = body
                current_header = m.group(1).strip()
                current_lines = []
                continue

        if current_header is not None:
            current_lines.append(line)

    if current_header is not None:
        body = "\n".join(current_lines).strip()
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
    # (No-op here other than ensuring we don't later filter these out.)
    if slug in PROJECT_CONTENT_OVERRIDES:
        for sec, body in PROJECT_CONTENT_OVERRIDES[slug].items():
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
    eco_slug = ECOSYSTEM_MAP.get(project.slug, "projects")
    fm = f"---\nlayout: default\nsection: {eco_slug}\n---\n\n"
    status_badge = (
        f'<span class="status-badge status-active">{project.status_detail}</span>'
    )
    back_links = get_back_links(project.category)
    header = f"# {project.name}\n\n{status_badge}\n\n{back_links}\n\n---\n\n"
    intro_parts = []
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
    body_list = []
    if intro_parts:
        body_list.append(f"## Concept\n\n" + "\n\n".join(intro_parts))
    for s in DETAILED_SECTIONS:
        if s in project.sections and s not in [
            "Concept",
            "The Insight",
            "Overview",
            "What This Is",
            "Problem It Solves",
            "Core Value",
        ]:
            body_list.append(f"## {s}\n\n{clean_text(project.sections[s])}")
    if project.current_status:
        body_list.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary:
        body_list.append(
            "## Roadmap\n\n"
            + "\n".join([f"- {item}" for item in project.roadmap_summary])
        )
    final_body = "\n\n---\n\n".join(body_list)
    toc = generate_toc(final_body)
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
                    path=projects_dir / f"{slug}.md",
                    category="network",
                    status="active",
                    status_detail="Active",
                    sections=PROJECT_CONTENT_OVERRIDES[slug],
                )
            )
    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        p.line_count = len(generate_detailed_page(p).splitlines())
        pp.write_text(generate_detailed_page(p))
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()

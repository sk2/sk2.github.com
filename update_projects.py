#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Clean Room Generation: Every page is rebuilt from scratch from Source of Truth metadata.
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
    "network_simulator": "network-automation",
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
    "ank_pydantic": "Network Modeling Library",
    "ank-pydantic": "Network Modeling Library",
    "cliscrape": "CLI Parser",
    "rtltcp": "Radio Streaming Server",
    "auroradata": "Aurora Advisor",
    "netflowsim": "Performance Simulator",
    "netsim": "Network Simulator",
    "topogen": "Topology Generator",
    "ank-nte": "Topology Engine Core",
    "ank-workbench": "Automation Workbench",
    "autonetkit-foundation": "Network Modeling Foundations",
    "autonetkit": "AutoNetkit",
    "netvis": "Visualization Engine",
    "passive": "Signal Reflection Analysis",
    "signals": "Spectrum Analysis",
}

# GOLDEN MASTER CONTENT: Used when metadata is missing or for legacy projects
PROJECT_CONTENT_OVERRIDES = {
    "autonetkit": {
        "Concept": "Network topology modeling typically forces a choice between the speed of untyped graph libraries (NetworkX) and the rigidity of database-backed sources of truth. **AutoNetkit** eliminates this trade-off by using Pydantic for schema validation and a Rust core (`petgraph`) for graph traversals.\n\nIt is a modern reimagining of the original AutoNetkit research, reclaiming the name for a production-ready automation library.",
        "Core Value": "Expressive Python API backed by compiled graph algorithms (petgraph), with automatic configuration generation for multi-vendor network deployments.",
        "Features": "- **Type-safe modeling**: Every device, link, and protocol attribute is validated using Pydantic.\n- **High-performance core**: Graph traversals and topological queries are executed in Rust.\n- **Multi-vendor support**: Generates configurations for Cisco, Juniper, Arista, and more.\n- **Intent-based workflow**: Define the target state and let the engine handle the addressing and protocol logic.",
        "Architecture": "Specification abstraction → intermediate network-wide state representation → low-level device configuration → template assembly."
    },
    "autonetkit-foundation": {
        "Concept": "The original research that established the principles of automated network configuration. This work introduced the **Whiteboard → Plan → Build** transformation model, which allows engineers to work with high-level design abstractions while the system handles the technical implementation details.",
        "Core Value": "Demonstrated that a compiler-based approach can successfully automate the configuration of complex, multi-vendor data networks at scale.",
        "Research Contribution": "- **Abstractions**: Identified the fundamental primitives needed to represent network intent independently of vendor syntax.\n- **Transformations**: Developed graph-based algorithms to automatically calculate IP addresses, OSPF areas, and BGP peerings.\n- **Scalability**: Verified that automated generation can handle core-network topologies with hundreds of devices in seconds.\n- **Industry Impact**: Integrated into Cisco's Virtual Internet Routing Lab (VIRL) for automated lab provisioning."
    }
}

CATEGORY_MAP = {
    "network": ("🌐 Network Engineering", "Tools for network design, simulation, and analysis.", "/network-automation"),
    "sdr": ("📡 Radio Systems", "Radio signal analysis and spectrum monitoring.", "/signal-processing"),
    "health": ("🏥 Health & Biometrics", "Real-time biometric signal processing.", "/agentic-systems"),
    "astrophotography": ("🔭 Astrophotography", "Autonomous imaging and celestial monitoring.", None),
    "photography": ("📷 Photography", "Automated camera control and monitoring.", None),
    "agents": ("🤖 Autonomous Systems", "Secure systems for agents and infrastructure automation.", "/agentic-systems"),
    "data": ("📊 Data & Utilities", "Geospatial analytics and time-series discovery.", "/data-analytics"),
    "wellness": ("🧘 Wellness & Sound", "Sound analysis and wellness monitoring.", None),
    "experimental": ("🧪 Experimental", "Exploratory projects and technical experiments.", None)
}

# Professional Narrative Sequence
DETAILED_SECTIONS = [
    "Concept", "The Insight", "Overview", "What This Is", "Problem It Solves", 
    "Features", "Key Capabilities", "Use Cases", "Screenshots", "Architecture", 
    "Technical Depth", "Security Model", "Implementation Details", 
    "Protocols Implemented", "Performance", "Metrics", "Integration", 
    "Hardware", "Agents", "Components", "Tech Stack", "Research Contribution"
]

def extract_sections(content: str) -> Dict[str, str]:
    sections = {}
    matches = re.finditer(r'^##\s+(.*?)\s*$(.*?)(?=^##\s|\Z)', content, re.MULTILINE | re.DOTALL)
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        if body: sections[header] = body
    return sections


def clean_text(text: str) -> str:
    """Aggressively strip phases, progress, and project management clutter."""
    text = re.sub(r'\(Phase.*?\)', '', text)
    text = re.sub(r'Phase \d+.*?\d+', '', text)
    text = re.sub(r'\*\*Phase \d+.*?\*\*', '', text)
    text = re.sub(r'\d+%', '', text)
    text = re.sub(r'^\s*·\s*\*\*.*?\*\*\s*$', '', text, flags=re.MULTILINE)
    return text.strip()


def generate_toc(content: str) -> str:
    """Generate a table of contents from ## headers."""
    headers = re.findall(r'^##\s+([^#\n]+)\s*$', content, re.MULTILINE)
    headers = [h.strip() for h in headers if h.strip() not in ["Contents", "Quick Facts"]]
    if len(headers) < 4: return ""
    links = []
    for h in headers:
        slug = h.lower().replace(" ", "-")
        slug = re.sub(r'[^a-z0-9-]', '', slug)
        slug = re.sub(r'-+', '-', slug)
        links.append(f"- [{h}](#{slug})")
    return "## Contents\n\n" + "\n".join(links) + "\n\n"


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists(): return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists(): return None
    content = project_md.read_text()
    
    name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    project_name = re.sub(r'^(Project|PROJECT):\s*', '', project_name, flags=re.IGNORECASE)
    
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {"multi-agent-assistant": "multi-agent", "passive": "rf-signal-analysis", "wifi-radar": "wifi-signal-analysis", "ank_pydantic": "ank-pydantic"}
    slug = slug_mappings.get(slug, slug)
    
    if slug in PROJECT_ALIASES: project_name = PROJECT_ALIASES[slug]
    
    sections = extract_sections(content)
    if slug in PROJECT_CONTENT_OVERRIDES:
        for sec, body in PROJECT_CONTENT_OVERRIDES[slug].items():
            sections[sec] = body

    cat = "experimental"
    s = slug.lower()
    if any(x in s for x in ["photo-tour"]): cat = "photography"
    elif any(x in s for x in ["watchnoise", "psytrance"]): cat = "wellness"
    elif any(x in s for x in ["healthypi", "hrv"]): cat = "health"
    elif any(x in s for x in ["spectra", "rtltcp", "wifi-signal-analysis", "signals", "rf-signal-analysis"]): cat = "sdr"
    elif any(x in s for x in ["astro", "aurora", "eclipse", "satellites"]): cat = "astrophotography"
    elif any(x in s for x in ["agent", "multi-agent", "cycle"]): cat = "agents"
    elif any(x in s for x in ["netflow", "polars", "tileserver", "matrix-time-series", "matrix-profile", "weather", "omnifocus-db", "cliscrape", "nascleanup", "devmon"]): cat = "data"
    elif any(x in s for x in ["netvis", "ank", "topogen", "netsim", "autonetkit", "network", "configparsing", "nte", "orchestrator", "automationarch", "netflowsim"]): cat = "network"
    
    stack = []
    constraints = sections.get("Constraints", "")
    tech_patterns = [r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', r'\*\*Language\*\*:?\s*(.+?)(?:\s+—|$)']
    for pattern in tech_patterns:
        match = re.search(pattern, constraints)
        if match:
            s_str = match.group(1).split('\n')[0]
            stack.extend([s.strip() for s in re.split(r'[,;·]', s_str) if s.strip()])
            break
            
    current_status, last_activity_date = "", None
    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text(); la_match = re.search(r'Last activity:\s*(.+)', state_content)
        if la_match:
            activity_text = la_match.group(1).strip()
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', activity_text)
            if date_match:
                try: last_activity_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
                except ValueError: pass
            current_status = activity_text
            
    status_detail = "Active"
    if last_activity_date:
        today = datetime(2026, 2, 24)
        if today - last_activity_date <= timedelta(days=7): status_detail = "Recently Updated"
        else: status_detail = f"Last Active: {last_activity_date.strftime('%Y-%m-%d')}"

    roadmap_summary = []
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text(); ms_matches = re.finditer(r'^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$', roadmap_content, re.MULTILINE)
        for match in ms_matches:
            ms_name = clean_text(match.group(1))
            ms_detail = clean_text(match.group(2))
            roadmap_summary.append(f"**{ms_name}** {ms_detail}")
            if len(roadmap_summary) >= 5: break

    return ProjectInfo(name=project_name, slug=slug, path=project_path, category=cat, status="active", status_detail=status_detail, stack=stack, sections=sections, current_status=current_status, roadmap_summary=roadmap_summary, last_activity_date=last_activity_date)


def generate_detailed_page(project: ProjectInfo) -> str:
    # 1. Frontmatter
    eco_slug = ECOSYSTEM_MAP.get(project.slug, "projects")
    fm = f"---\nlayout: default\nsection: {eco_slug}\n---\n\n"
    
    # 2. Header
    status_badge = f'<span class="status-badge status-active">{project.status_detail}</span>'
    back_eco_link = ""
    if eco_slug != "projects":
        eco_title = eco_slug.replace('-', ' ').title()
        if eco_slug == "network-automation": eco_title = "Network Automation"
        if eco_slug == "agentic-systems": eco_title = "Autonomous Systems"
        if eco_slug == "signal-processing": eco_title = "Signal Processing"
        back_eco_link = f"[← Back to {eco_title}](../{eco_slug})\n\n"
        
    header = f"# {project.name}\n\n{status_badge}\n\n{back_eco_link}[← Back to Projects](../projects)\n\n---\n\n"
    
    # 3. Product Narrative
    # Merge intro sections into Concept
    intro_parts = []
    for s in ["Concept", "The Insight", "Overview", "What This Is", "Problem It Solves", "Core Value"]:
        if s in project.sections:
            intro_parts.append(clean_text(project.sections[s]))
    
    body_list = [f"## Concept\n\n" + "\n\n".join(intro_parts)]
    
    # Standard sections
    for s in ["Features", "Key Capabilities", "Use Cases", "Screenshots", "Architecture", "Technical Depth", "Security Model", "Implementation Details", "Protocols Implemented", "Performance", "Metrics", "Integration", "Hardware", "Agents", "Components", "Tech Stack", "Research Contribution"]:
        if s in project.sections and s not in ["Concept", "The Insight", "Overview", "What This Is", "Problem It Solves", "Core Value"]:
            body_list.append(f"## {s}\n\n{clean_text(project.sections[s])}")
            
    # 4. Status and Roadmap
    if project.current_status:
        body_list.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary:
        body_list.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
        
    assembled_body = "\n\n---\n\n".join(body_list)
    toc = generate_toc(assembled_body)
    
    footer = f"\n\n---\n\n{back_eco_link}[← Back to Projects](../projects)\n"
    
    return fm + header + toc + assembled_body + footer


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = ["---", "layout: default", "---", "", "# Projects", "", "Focused on network engineering, autonomous systems, and signal processing.", "", "---", ""]
    sorted_projects = sorted(projects, key=lambda x: x.line_count, reverse=True)
    categorized = {k: [] for k in CATEGORY_MAP.keys()}
    for p in sorted_projects: categorized[p.category].append(p)
    for cat_key, (title, desc, link) in CATEGORY_MAP.items():
        projs = categorized[cat_key]
        if not projs: continue
        lines.append(f"## {title}\n")
        for p in projs:
            summary = ""
            for k in ["Concept", "The Insight", "Overview", "What This Is", "Core Value"]:
                if k in p.sections:
                    summary = p.sections[k].strip().split('\n\n')[0]
                    summary = clean_text(re.sub(r'!\[.*?\]\(.*?\)', '', summary))
                    if summary: break
            summary = summary.replace("high-performance", "fast").replace("blazing-fast", "fast").replace("cutting-edge", "modern")
            sents = re.split(r'(?<=[.!?])\s+', summary); summary = ' '.join(sents[:3])
            lines.append(f"### [{p.name}](projects/{p.slug})\n")
            lines.append(f'<span class="status-badge status-active">{p.status_detail}</span>')
            lines.append(f"\n\n{summary}\n\n")
    lines.append('<style>\n.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }\n.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }\nsection { margin-bottom: 2em; }\n</style>')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--scan-dirs", nargs="+", default=["~/dev", "~/PycharmProjects", "~/RustroverProjects"]); args = parser.parse_args()
    projects = []
    for d in args.scan_dirs:
        p = Path(d).expanduser()
        if p.exists():
            for pd in sorted(p.iterdir()):
                if not pd.is_dir() or "-clean-" in pd.name or "backup" in pd.name.lower(): continue
                info = parse_project_metadata(pd)
                if info: projects.append(info)
    
    projects_dir = Path("projects")
    scanned_slugs = {p.slug for p in projects}
    # Add manual/legacy overrides
    for slug in PROJECT_CONTENT_OVERRIDES:
        if slug not in scanned_slugs:
            name = PROJECT_ALIASES.get(slug, slug.title())
            projects.append(ProjectInfo(name=name, slug=slug, path=projects_dir / f"{slug}.md", category="network", status="active", status_detail="Active", sections=PROJECT_CONTENT_OVERRIDES[slug]))

    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        # CLEAN ROOM GENERATION: Every page is rebuilt from scratch
        p.line_count = len(generate_detailed_page(p).splitlines())
        pp.write_text(generate_detailed_page(p))
        
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()

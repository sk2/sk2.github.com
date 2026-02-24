#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Safe content preservation mode.
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict
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


PROJECT_ALIASES = {
    "NTE: Engine Hardening & LadybugDB Evaluation": "Topology Core (NTE)",
    "Network Automation Ecosystem - Overall Architecture Definition": "Network Automation Ecosystem",
    "ank_pydantic": "Network Modeling Library",
    "ank-pydantic": "Network Modeling Library",
    "Project Spectra": "Spectrum Analysis",
    "Passive Radar - KrakenSDR Multi-Beam System": "Signal Reflection Analysis",
    "Wi-Fi Radar (KrakenSDR)": "Wi-Fi Signal Analysis",
    "cliscrape": "CLI Parser",
    "Project Context: rtltcp-rust": "Radio Streaming Server",
    "AuroraData - Aurora Planning & Substorm Advisor": "Aurora Advisor",
    "Network Configuration Parsing & Analysis Framework": "Configuration Analysis",
    "netflowsim": "Performance Simulator",
    "netsim": "Network Simulator",
    "topogen": "Topology Generator",
    "ank-nte": "Topology Core (NTE)",
    "ank-workbench": "Automation Workbench",
    "autonetkit-foundation": "Network Modeling Foundations",
    "autonetkit": "AutoNetkit",
    "configparsing": "Configuration Analysis",
    "netvis": "Visualization Engine",
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

FM_SECTIONS = {
    "network": "network-automation",
    "sdr": "signal-processing",
    "agents": "agentic-systems",
    "health": "agentic-systems",
    "data": "data-analytics"
}

CONCEPT_MERGE = ["The Insight", "Overview", "What This Is", "Problem It Solves", "Core Value"]
FEATURE_MERGE = ["Key Capabilities"]
PRODUCT_SECTIONS = ["Problem It Solves", "Features", "Key Capabilities", "Use Cases", "Screenshots"]
TECHNICAL_SECTIONS = [
    "Architecture", "Technical Depth", "Security Model", "Implementation Details", 
    "Protocols Implemented", "Performance", "Metrics", "Integration", 
    "Hardware", "Agents", "Components", "Tech Stack"
]

def extract_sections(content: str) -> Dict[str, str]:
    sections = {}
    matches = re.finditer(r'^##\s+(.*?)\s*$(.*?)(?=^##\s|\Z)', content, re.MULTILINE | re.DOTALL)
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        if body: sections[header] = body
    return sections


def generate_toc(content: str) -> str:
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


def get_back_links(category: str) -> str:
    links = []
    if category in FM_SECTIONS:
        slug = FM_SECTIONS[category]
        title = slug.replace('-', ' ').title()
        if slug == "network-automation": title = "Network Automation"
        if slug == "agentic-systems": title = "Autonomous Systems"
        if slug == "signal-processing": title = "Signal Processing"
        links.append(f"[← Back to {title}](../{slug})")
    links.append("[← Back to Projects](../projects)")
    return "\n\n".join(links)


def clean_text(text: str) -> str:
    text = re.sub(r'\(Phase.*?\)', '', text)
    text = re.sub(r'Phase \d+.*?\d+', '', text)
    text = re.sub(r'\*\*Phase \d+.*?\*\*', '', text)
    text = re.sub(r'\d+%', '', text)
    return text.strip()


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists(): return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists(): return None
    content = project_md.read_text()
    all_sections = extract_sections(content)
    name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    project_name = re.sub(r'^(Project|PROJECT):\s*', '', project_name, flags=re.IGNORECASE)
    project_name = re.sub(r'\s*\(KrakenSDR\)$', '', project_name)
    if project_name in PROJECT_ALIASES: project_name = PROJECT_ALIASES[project_name]
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {"multi-agent-assistant": "multi-agent", "watch-noise": "watchnoise", "passive": "rf-signal-analysis", "wifi-radar": "wifi-signal-analysis", "ank_pydantic": "ank-pydantic"}
    slug = slug_mappings.get(slug, slug)
    if slug in PROJECT_ALIASES: project_name = PROJECT_ALIASES[slug]
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
    constraints = all_sections.get("Constraints", "")
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
            activity_text = la_match.group(1).strip(); date_match = re.search(r'(\d{4}-\d{2}-\d{2})', activity_text)
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
    return ProjectInfo(name=project_name, slug=slug, path=project_path, category=cat, status="active", status_detail=status_detail, stack=stack, sections=all_sections, current_status=current_status, roadmap_summary=roadmap_summary, last_activity_date=last_activity_date)


def generate_status_badge(project: ProjectInfo) -> str:
    detail = project.status_detail or "Active"
    cls = "status-updated" if detail == "Recently Updated" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def update_existing_file(content: str, project: ProjectInfo) -> str:
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm_block = content[fm_match.start():fm_match.end()] if fm_match else "---\nlayout: default\n---"
    body = content[fm_match.end():].strip() if fm_match else content.strip()
    
    # Aggressively remove generated top/bottom wrappers ONLY
    body = re.sub(r'^# .*?\n', '', body, flags=re.MULTILINE)
    body = re.sub(r'<span class="status-badge.*?>.*?</span>', '', body)
    body = re.sub(r'\[← Back to .*?\]\(.*?\)', '', body)
    body = re.sub(r'## Contents\n\n(.*?)(?=\n\n##|\n\n---|\Z)', '', body, flags=re.DOTALL)
    body = body.replace("## Contents\n", "")
    
    # Strip existing Roadmap and Current Status if they're lists
    body = re.sub(r'## Current Status\n\n(.*?)(?=\n\n##|\n\n---|\Z)', '', body, flags=re.DOTALL)
    body = re.sub(r'## Roadmap\n\n(.*?)(?=\n\n##|\n\n---|\Z)', '', body, flags=re.DOTALL)
    body = body.replace("## Current Status\n", "").replace("## Roadmap\n", "")
    body = re.sub(r'^---\s*$', '', body, flags=re.MULTILINE)
    
    body = body.strip()
    
    # REASSEMBLE
    back_links = get_back_links(project.category)
    header_block = f"# {project.name}\n\n{generate_status_badge(project)}\n\n{back_links}"
    
    footer_sections = []
    if project.current_status: footer_sections.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary: footer_sections.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
    
    footer_block = "\n\n---\n\n".join(footer_sections)
    
    # Calculate new TOC
    full_temp_body = body + "\n\n" + footer_block
    toc = generate_toc(full_temp_body)
    
    return fm_block + "\n\n" + header_block + "\n\n---\n\n" + toc + body + "\n\n---\n\n" + footer_block + "\n\n---\n\n" + back_links + "\n"


def generate_detailed_page(project: ProjectInfo) -> str:
    fm = f"---\nlayout: default"
    if project.category in FM_SECTIONS: fm += f"\nsection: {FM_SECTIONS[project.category]}"
    fm += "\n---"
    back_links = get_back_links(project.category); header = f"# {project.name}\n\n{generate_status_badge(project)}\n\n{back_links}"
    concept_parts = ["## Concept"]
    if "Concept" in project.sections: concept_parts[0] = f"## Concept\n\n{clean_text(project.sections['Concept'])}"
    for h in CONCEPT_MERGE:
        if h in project.sections and h != "Concept": concept_parts.append(f"### {h}\n\n{clean_text(project.sections[h])}")
    body_list = ["\n\n".join(concept_parts)]
    features_body = ""
    if "Features" in project.sections: features_body = f"## Features\n\n{clean_text(project.sections['Features'])}"
    for h in FEATURE_MERGE:
        if h in project.sections:
            f_text = f"### {h}\n\n{clean_text(project.sections[h])}"
            if features_body: features_body += f"\n\n{f_text}"
            else: features_body = f"## Features\n\n{f_text}"
    if features_body: body_list.append(features_body)
    for sec in PRODUCT_SECTIONS:
        if sec in project.sections and sec != "Features": body_list.append(f"## {sec}\n\n{clean_text(project.sections[sec])}")
    for sec in TECHNICAL_SECTIONS:
        if sec in project.sections: body_list.append(f"## {sec}\n\n{clean_text(project.sections[sec])}")
    
    footer_sections = []
    if project.current_status: footer_sections.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary: footer_sections.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
    
    assembled_content = "\n\n---\n\n".join(body_list)
    toc = generate_toc(assembled_content + "\n\n" + "\n\n".join(footer_sections))
    return fm + "\n\n" + header + "\n\n---\n\n" + toc + assembled_content + "\n\n---\n\n" + "\n\n---\n\n".join(footer_sections) + "\n\n---\n\n" + back_links + "\n"


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
            lines.append(f"{generate_status_badge(p)}")
            lines.append(f"\n\n{summary}\n\n")
    lines.append('<style>\n.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }\n.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }\n.status-updated { background-color: #e3f2fd; color: #0d47a1; border: 1px solid #bbdefb; }\n.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }\nh3 { margin-bottom: 0.1em; }\nh3 + .status-badge { margin-top: 0; }\nsection { margin-bottom: 2em; }\n</style>')
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
    scanned_slugs = {p.slug for p in projects}; scanned_names = {p.name for p in projects}
    for legacy_md in sorted(projects_dir.glob("*.md")):
        if legacy_md.stem not in scanned_slugs:
            content = legacy_md.read_text(); name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if name_match:
                name = name_match.group(1).strip()
                if name in scanned_names: continue
                projects.append(ProjectInfo(name=name, slug=legacy_md.stem, path=legacy_md, category="experimental", status="active", sections=extract_sections(content)))
    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        if pp.exists(): p.line_count = len(pp.read_text().splitlines())
        else: p.line_count = 0
    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        if pp.exists():
            content = pp.read_text()
            metadata_headers = [h for h in CONCEPT_MERGE + FEATURE_MERGE + PRODUCT_SECTIONS + TECHNICAL_SECTIONS if h in p.sections]
            file_headers = re.findall(r'^##\s+(.*?)$', content, re.MULTILINE)
            missing_some = any(h not in file_headers and h != "Concept" for h in metadata_headers)
            # FORCE RE-SYNC if it looks like we've lost content
            if len(content.split('\n')) < 30 or missing_some or "## Contents" not in content:
                pp.write_text(generate_detailed_page(project=p))
                continue
            pp.write_text(update_existing_file(content, p))
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()

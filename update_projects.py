#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Enforces a clean, understated, and powerful style with navigation for long pages.
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict


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


PROJECT_ALIASES = {
    "NTE: Engine Hardening & LadybugDB Evaluation": "Network Topology Engine",
    "Network Automation Ecosystem - Overall Architecture Definition": "Network Automation Ecosystem",
    "ank_pydantic": "Network Modeling Library",
    "Project Spectra": "Spectrum Analysis",
    "Passive Radar - KrakenSDR Multi-Beam System": "Signal Reflection Analysis",
    "Wi-Fi Radar (KrakenSDR)": "Wi-Fi Signal Analysis",
    "cliscrape": "CLI Parser",
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

def extract_sections(content: str) -> Dict[str, str]:
    sections = {}
    matches = re.finditer(r'^##\s+(.*?)\s*$(.*?)(?=^##\s|\Z)', content, re.MULTILINE | re.DOTALL)
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        if body: sections[header] = body
    return sections


def generate_toc(content: str) -> str:
    """Generate a table of contents from ## headers."""
    headers = re.findall(r'^##\s+(.*?)\s*$', content, re.MULTILINE)
    if len(headers) < 4:
        return ""
    
    links = []
    for h in headers:
        slug = h.lower().replace(" ", "-").replace("&", "").replace("?", "").replace("(", "").replace(")", "").replace(":", "")
        slug = re.sub(r'-+', '-', slug)
        links.append(f"- [{h}](#{slug})")
    
    return "## Contents\n\n" + "\n".join(links) + "\n\n---\n"


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
    
    if project_name in PROJECT_ALIASES:
        project_name = PROJECT_ALIASES[project_name]

    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {
        "multi-agent-assistant": "multi-agent", 
        "watch-noise": "watchnoise", 
        "passive": "rf-signal-analysis", 
        "wifi-radar": "wifi-signal-analysis",
        "ank_pydantic": "ank-pydantic"
    }
    slug = slug_mappings.get(slug, slug)

    cat = "experimental"
    s = slug.lower()
    if any(x in s for x in ["photo-tour"]): cat = "photography"
    elif any(x in s for x in ["watchnoise", "psytrance"]): cat = "wellness"
    elif any(x in s for x in ["healthypi", "hrv"]): cat = "health"
    elif any(x in s for x in ["spectra", "rtltcp", "wifi-signal-analysis", "signals", "rf-signal-analysis"]): cat = "sdr"
    elif any(x in s for x in ["astro", "aurora", "eclipse", "satellites"]): cat = "astrophotography"
    elif any(x in s for x in ["agent", "multi-agent", "cycle"]): cat = "agents"
    elif any(x in s for x in ["netflow", "polars", "tileserver", "matrix-time-series", "matrix-profile", "weather", "omnifocus-db", "cliscrape", "nascleanup", "devmon"]): cat = "data"
    elif any(x in s for x in ["netvis", "ank", "topogen", "netsim", "autonetkit", "network", "configparsing", "nte", "orchestrator", "automationarch"]): cat = "network"

    stack = []
    constraints = all_sections.get("Constraints", "")
    tech_patterns = [r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', r'\*\*Language\*\*:?\s*(.+?)(?:\s+—|$)']
    for pattern in tech_patterns:
        match = re.search(pattern, constraints)
        if match:
            s_str = match.group(1).split('\n')[0]
            stack.extend([s.strip() for s in re.split(r'[,;·]', s_str) if s.strip()])
            break

    status, status_detail, current_status = "active", None, ""
    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text()
        state_sections = extract_sections(state_content)
        pos = state_sections.get("Current Position", "")
        if pos:
            ph_match = re.search(r'Phase:\s*(.*)', pos)
            if ph_match:
                status_detail = ph_match.group(1).strip()
                m_xy = re.search(r'(\d+)\s*of\s*(\d+)', status_detail)
                pr_match = re.search(r'Progress:.*?(\d+)%', pos)
                if m_xy and pr_match: status_detail = f"Phase {m_xy.group(1)}/{m_xy.group(2)} ({pr_match.group(1)}%)"
                elif m_xy: status_detail = f"Phase {m_xy.group(1)}/{m_xy.group(2)}"
        la_match = re.search(r'\*\*Last activity:\*\*\s*(.+)', state_content)
        if la_match: current_status = la_match.group(1).strip()

    roadmap_summary = []
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text()
        ms_matches = re.finditer(r'^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$', roadmap_content, re.MULTILINE)
        for match in ms_matches:
            ms_name, ms_detail = match.group(1).strip(), match.group(2).strip()
            roadmap_summary.append(f"{ms_name} {ms_detail}")
            if len(roadmap_summary) >= 3: break

    return ProjectInfo(name=project_name, slug=slug, path=project_path, category=cat, status=status, status_detail=status_detail, stack=stack, sections=all_sections, current_status=current_status, roadmap_summary=roadmap_summary)


def generate_status_badge(project: ProjectInfo) -> str:
    detail = project.status_detail or "Active"
    cls = "status-planning" if project.status == "planning" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def generate_quick_facts(project: ProjectInfo) -> str:
    return f"## Quick Facts\n\n| | |\n|---|---|\n| **Status** | {project.status_detail or project.status.capitalize()} |\n| **Language** | {', '.join(project.stack) if project.stack else 'N/A'} |\n"


def update_existing_file(content: str, project: ProjectInfo) -> str:
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm_lines = fm_match.group(1).split('\n') if fm_match else ["layout: default"]
    
    new_fm_lines = []
    for line in fm_lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-") or line.startswith("|") or line.startswith("##"): continue
        if ":" in line: new_fm_lines.append(line)
    
    if not any(l.startswith("section:") for l in new_fm_lines) and project.category in FM_SECTIONS:
        new_fm_lines.append(f"section: {FM_SECTIONS[project.category]}")
        
    body = content[fm_match.end():].strip() if fm_match else content.strip()
    sections = re.split(r'^(?=##\s|---)', body, flags=re.MULTILINE)
    clean_sections = []
    for sec in sections:
        sec = sec.strip()
        if not sec or sec == "---" or sec == "|" or sec.startswith("## Contents"): continue
        if sec.startswith("# ") or sec.startswith("<span class=\"status-badge") or sec.startswith("[← Back to"): continue
        if any(sec.startswith(f"## {h}") for h in ["Roadmap", "Current Status", "Quick Facts"]): continue
        if sec.startswith("- v") or sec.startswith("- Phase") or sec.startswith("- Milestone"): continue
        if sec.startswith("|") and "**Status**" in sec: continue
        clean_sections.append(sec)
    
    header_block = f"# {project.name}\n\n{generate_status_badge(project)}\n\n[← Back to Projects](../projects)\n\n---"
    gen_sections = [generate_quick_facts(project).strip()]
    if project.roadmap_summary:
        gen_sections.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
    
    fm_block = f"---\n" + "\n".join(new_fm_lines) + f"\n---"
    
    # Body assembly
    body_content = []
    concept_sec = next((s for s in clean_sections if s.startswith("## Concept")), None)
    if concept_sec:
        body_content.append(concept_sec)
        clean_sections.remove(concept_sec)
    
    body_content.extend(gen_sections)
    body_content.extend(clean_sections)
    
    assembled_body = "\n\n---\n\n".join(body_content)
    toc = generate_toc(assembled_body)
    
    if toc:
        assembled_body = toc + "\n" + assembled_body

    return fm_block + "\n\n" + header_block + "\n\n" + assembled_body + "\n\n---\n\n[← Back to Projects](../projects)\n"


def generate_detailed_page(project: ProjectInfo) -> str:
    fm = f"---\nlayout: default"
    if project.category in FM_SECTIONS: fm += f"\nsection: {FM_SECTIONS[project.category]}"
    fm += "\n---"
    
    lines = [fm, "", f"# {project.name}", "", generate_status_badge(project), "", "[← Back to Projects](../projects)", "", "---", ""]
    
    content_lines = []
    found_first = False
    for sec in ["Concept", "The Insight", "Overview", "What This Is", "Problem It Solves", "Features"]:
        body = project.sections.get(sec)
        if body:
            heading = "Concept" if not found_first else sec
            found_first = True
            content_lines.append(f"## {heading}\n"); content_lines.append(body + "\n")
    
    content_lines.append(generate_quick_facts(project))
    if project.roadmap_summary:
        content_lines.append("## Roadmap\n")
        for item in project.roadmap_summary: content_lines.append(f"- {item}")
        content_lines.append("")
    
    assembled_content = "\n".join(content_lines)
    toc = generate_toc(assembled_content)
    if toc:
        lines.append(toc)
    
    lines.append(assembled_content)
    lines.append("---\n"); lines.append("[← Back to Projects](../projects)\n")
    return "\n".join(lines)


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = ["---", "layout: default", "---", "", "# Projects", "", "Focused on network engineering, autonomous systems, and signal processing.", "", "---", ""]
    
    categorized = {k: [] for k in CATEGORY_MAP.keys()}
    for p in sorted(projects, key=lambda x: x.name): categorized[p.category].append(p)

    for cat_key, (title, desc, link) in CATEGORY_MAP.items():
        projs = categorized[cat_key]
        if not projs: continue
        
        lines.append(f"## {title}\n")
        for p in projs:
            summary = ""
            for k in ["Concept", "The Insight", "Overview", "What This Is", "Core Value"]:
                if k in p.sections:
                    summary = p.sections[k].strip().split('\n\n')[0]
                    summary = re.sub(r'!\[.*?\]\(.*?\)', '', summary).strip()
                    if summary: break
            
            summary = summary.replace("high-performance", "fast").replace("blazing-fast", "fast").replace("cutting-edge", "modern")
            sents = re.split(r'(?<=[.!?])\s+', summary)
            summary = ' '.join(sents[:3])

            lines.append(f"### [{p.name}](projects/{p.slug})\n")
            lines.append(f"{generate_status_badge(p)}")
            lines.append(f"\n\n{summary}\n\n")
    
    lines.append('<style>\n.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }\n.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }\n.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }\nh3 { margin-bottom: 0.1em; }\nh3 + .status-badge { margin-top: 0; }\nsection { margin-bottom: 2em; }\n</style>')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-dirs", nargs="+", default=["~/dev", "~/PycharmProjects", "~/RustroverProjects"])
    args = parser.parse_args()
    
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
    scanned_names = {p.name for p in projects}
    for legacy_md in sorted(projects_dir.glob("*.md")):
        if legacy_md.stem not in scanned_slugs:
            content = legacy_md.read_text()
            name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if name_match:
                name = name_match.group(1).strip()
                if name in scanned_names: continue
                projects.append(ProjectInfo(name=name, slug=legacy_md.stem, path=legacy_md, category="experimental", status="active", sections=extract_sections(content)))

    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        if pp.exists():
            content = pp.read_text()
            if len(content.split('\n')) > 30:
                pp.write_text(update_existing_file(content, p))
                continue
        pp.write_text(generate_detailed_page(p))
        
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()

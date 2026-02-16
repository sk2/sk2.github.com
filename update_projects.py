#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Enforces "Understated Expert" style and keeps roadmaps/status in sync.
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
    milestone: Optional[str] = None
    next_milestone: Optional[str] = None
    roadmap_summary: list[str] = field(default_factory=list)


def extract_sections(content: str) -> Dict[str, str]:
    sections = {}
    matches = re.finditer(r'^##\s+(.*?)\s*$(.*?)(?=^##\s|\Z)', content, re.MULTILINE | re.DOTALL)
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        if body: sections[header] = body
    return sections


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists(): return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists(): return None
    content = project_md.read_text()
    all_sections = extract_sections(content)
    name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    project_name = re.sub(r'^Project:\s*', '', re.sub(r'^PROJECT:\s*', '', project_name, flags=re.IGNORECASE), flags=re.IGNORECASE)
    
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {"multi-agent-assistant": "multi-agent", "watch-noise": "watchnoise"}
    slug = slug_mappings.get(slug, slug)

    stack = []
    constraints = all_sections.get("Constraints", "")
    tech_patterns = [r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', r'\*\*Language\*\*:?\s*(.+?)(?:\s+—|$)']
    for pattern in tech_patterns:
        match = re.search(pattern, constraints)
        if match:
            s_str = match.group(1).split('\n')[0]
            stack.extend([s.strip() for s in re.split(r'[,;]', s_str) if s.strip()])
            break

    status, status_detail, current_status, milestone = "active", None, "", None
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
            ms_match = re.search(r'Milestone:\s*(.*)', pos)
            if ms_match: milestone = ms_match.group(1).strip()
        la_match = re.search(r'\*\*Last activity:\*\*\s*(.+)', state_content)
        if la_match: current_status = la_match.group(1).strip()

    roadmap_summary, next_milestone = [], None
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text()
        ms_matches = re.finditer(r'^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$', roadmap_content, re.MULTILINE)
        for match in ms_matches:
            ms_name, ms_detail = match.group(1).strip(), match.group(2).strip()
            if not next_milestone: next_milestone = ms_name
            roadmap_summary.append(f"{ms_name} {ms_detail}")
            if len(roadmap_summary) >= 3: break

    return ProjectInfo(name=project_name, slug=slug, path=project_path, category="network", status=status, status_detail=status_detail, stack=stack, sections=all_sections, current_status=current_status, milestone=milestone, next_milestone=next_milestone, roadmap_summary=roadmap_summary)


def generate_status_badge(project: ProjectInfo) -> str:
    detail = project.status_detail or "Active Development"
    cls = "status-planning" if project.status == "planning" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def generate_quick_facts(project: ProjectInfo) -> str:
    return f"## Quick Facts\n\n| | |\n|---|---|\n| **Status** | {project.status_detail or project.status.capitalize()} |\n| **Language** | {', '.join(project.stack) if project.stack else 'N/A'} |\n| **Started** | 2026 |\n"


def update_existing_file(content: str, project: ProjectInfo) -> str:
    content = re.sub(r'^#\s+.*$', f"# {project.name}", content, flags=re.MULTILINE)
    content = re.sub(r'<span class="status-badge.*?>.*?</span>', generate_status_badge(project), content)
    content = re.sub(r'## Quick Facts\n\n\|.*?\|(?=\n\n##|\n\n---)', generate_quick_facts(project).strip(), content, flags=re.DOTALL)
    if project.roadmap_summary:
        roadmap_text = "## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]) + "\n"
        if "## Roadmap" in content: content = re.sub(r'## Roadmap\n\n(.*?)(?=\n\n##|\n\n---)', roadmap_text.strip(), content, flags=re.DOTALL)
        else:
            if "## Current Status" in content: content = content.replace("## Current Status", roadmap_text + "\n## Current Status")
            else: content = re.sub(r'(?=\n---)', "\n" + roadmap_text, content)
    if project.current_status:
        status_text = f"## Current Status\n\n{project.current_status}\n"
        if "## Current Status" in content: content = re.sub(r'## Current Status\n\n(.*?)(?=\n\n##|\n\n---)', status_text.strip(), content, flags=re.DOTALL)
        else: content = re.sub(r'(?=\n---)', "\n" + status_text, content)
    return content


def generate_detailed_page(project: ProjectInfo) -> str:
    lines = ["---", "layout: default", "---", "", f"# {project.name}", "", generate_status_badge(project), "", "[← Back to Projects](../projects)", "", "---", "", "## The Insight", "", project.sections.get("Core Value", project.sections.get("Overview", "Developing...")), "", generate_quick_facts(project), "---"]
    for sec in ["Overview", "What This Is", "Problem It Solves", "Features", "Key Capabilities", "Architecture", "Technical Depth", "Security Model", "Implementation Details", "Protocols Implemented", "Performance", "Metrics", "Use Cases", "Hardware", "Agents"]:
        if sec == "Core Value": continue
        body = project.sections.get(sec)
        if body: lines.append(f"## {sec}\n"); lines.append(body + "\n")
    if project.roadmap_summary:
        lines.append("## Roadmap\n")
        for item in project.roadmap_summary: lines.append(f"- {item}")
        lines.append("")
    if project.current_status: lines.append(f"## Current Status\n\n{project.current_status}\n")
    lines.append("---\n"); lines.append("[← Back to Projects](../projects) | [Development Philosophy](../development)\n")
    return "\n".join(lines)


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = ["---", "layout: default", "---", "", "# Projects", "", "Focusing on network automation, high-performance signal processing, and secure multi-agent architectures.", "", "---", ""]
    
    # Categories from README
    categories = {
        "network": ("🌐 Network Engineering", "High-performance tools for topology modeling, deterministic protocol simulation, and visualization.", "/network-automation", []),
        "sdr": ("📡 Software Defined Radio", "Autonomous spectrum monitoring, distributed SIGINT systems, and RF signal processing.", "/signal-processing", []),
        "health": ("🏥 Health & Biometrics", "Modular health monitoring ecosystems and real-time biometric signal processing.", "/agentic-systems", []), # Link to agentic since it's agent-driven
        "astrophotography": ("🔭 Astrophotography", "Autonomous imaging systems, solar wind monitoring, and celestial event automation.", None, []),
        "photography": ("📷 Photography", "Automated camera control, HFR monitoring, and night sky photography systems.", None, []),
        "agents": ("🤖 AI & Agents", "Security-first architectures for multi-agent coordination and isolated automation.", "/agentic-systems", []),
        "data": ("📊 Data & Utilities", "High-performance tools for large-scale geospatial analytics and time-series pattern discovery.", "/data-analytics", []),
        "wellness": ("🧘 Wellness & Sound", "Algorithmic music engines and biometric wellness monitoring.", None, []),
        "experimental": ("🧪 Experimental", "Projects in exploratory phases or related to technical hobbies.", None, [])
    }

    for p in sorted(projects, key=lambda x: x.name):
        cat = "experimental"
        nl = p.name.lower()
        slug = p.slug.lower()
        
        # Mapping logic from README
        if any(x in slug for x in ["photo-tour"]): cat = "photography"
        elif any(x in slug for x in ["watchnoise", "watch-noise", "psytrance"]): cat = "wellness"
        elif any(x in slug for x in ["healthypi", "hrv"]): cat = "health"
        elif any(x in slug for x in ["spectra", "rtltcp", "wifi-radar", "signals", "passive", "radar"]): cat = "sdr"
        elif any(x in slug for x in ["astro", "aurora", "eclipse", "satellites"]): cat = "astrophotography"
        elif any(x in slug for x in ["agent", "multi-agent", "cycle"]): cat = "agents"
        elif any(x in slug for x in ["netflow", "polars", "tileserver", "matrix-time-series", "matrix-profile", "weather", "omnifocus-db", "cliscrape", "nascleanup", "devmon"]): cat = "data"
        elif any(x in slug for x in ["netvis", "ank", "topogen", "netsim", "autonetkit", "network", "configparsing", "nte"]): cat = "network"
        
        if cat in categories:
            categories[cat][3].append(p)
        else:
            categories["experimental"][3].append(p)

    for cat_key, (title, desc, link, projs) in categories.items():
        if not projs: continue
        lines.append(f"## {title}\n")
        if link: lines.append(f"> **[View Ecosystem →]({link})**\n> {desc}\n")
        for p in projs:
            parts = []
            # Improved summary extraction: Concept, Overview, What This Is, Core Value, Problem It Solves
            for k in ["Concept", "The Insight", "Overview", "What This Is", "Core Value", "Problem It Solves"]:
                if k in p.sections:
                    # Take the first paragraph
                    first_para = p.sections[k].strip().split('\n\n')[0]
                    # Remove markdown images
                    first_para = re.sub(r'!\[.*?\]\(.*?\)', '', first_para).strip()
                    if first_para:
                        parts.append(first_para)
            
            summary = ' '.join(parts)
            if summary:
                sents = re.split(r'(?<=[.!?])\s+', summary)
                # Ensure 4-5 sentences and add paragraph breaks every 2 sentences as per README
                summary_sents = sents[:5]
                formatted_summary = ""
                for i in range(0, len(summary_sents), 2):
                    chunk = ' '.join(summary_sents[i:i+2])
                    formatted_summary += chunk + "\n\n"
                summary = formatted_summary.strip()

            lines.append(f"### [{p.name}](projects/{p.slug})\n")
            lines.append(f"{generate_status_badge(p)}")
            if p.stack: lines.append(f" · **{' · '.join(p.stack[:3])}**")
            lines.append(f"\n\n{summary}\n\n")
    
    lines.append('<style>\n.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }\n.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }\n.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }\nh3 { margin-bottom: 0.1em; }\nh3 + .status-badge { margin-top: 0; }\nsection { margin-bottom: 2em; }\nblockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 2px solid #495057; background: #f8f9fa; font-style: normal; font-size: 0.9em; }\n</style>')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--scan-dirs", nargs="+", default=["~/dev"]); args = parser.parse_args()
    projects = []
    for d in args.scan_dirs:
        p = Path(d).expanduser()
        if p.exists():
            for pd in p.iterdir():
                if pd.is_dir():
                    info = parse_project_metadata(pd)
                    if info: projects.append(info)
    
    # Legacy projects logic restored
    projects_dir = Path("projects")
    if projects_dir.exists():
        scanned_slugs = {p.slug for p in projects}
        scanned_names = {p.name for p in projects}
        for legacy_md in projects_dir.glob("*.md"):
            if legacy_md.stem not in scanned_slugs:
                content = legacy_md.read_text()
                name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if name_match:
                    name = name_match.group(1).strip()
                    if name in scanned_names: continue
                    status, status_detail, stack = "active", "Active Development", []
                    badge_match = re.search(r'<span class="status-badge.*?>(.*?)</span>', content)
                    if badge_match: status_detail = badge_match.group(1).strip()
                    stack_match = re.search(r'\|\s*\*\*Language\*\*\s*\|\s*(.*?)\s*\|', content)
                    if stack_match: stack = [s.strip() for s in re.split(r'[,·]', stack_match.group(1).strip()) if s.strip() and s.strip() != "N/A"]
                    projects.append(ProjectInfo(name=name, slug=legacy_md.stem, path=legacy_md, category="experimental", status=status, status_detail=status_detail, stack=stack, sections=extract_sections(content)))

    for p in projects:
        pp = projects_dir / f"{p.slug}.md"
        if pp.exists():
            content = pp.read_text()
            if len(content.split('\n')) > len(generate_detailed_page(p).split('\n')) * 2:
                pp.write_text(update_existing_file(content, p))
                continue
        pp.write_text(generate_detailed_page(p))
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")


if __name__ == "__main__":
    main()
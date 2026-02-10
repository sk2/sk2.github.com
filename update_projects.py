#!/usr/bin/env python3
"""
Update website projects page from project metadata.

Scans project directories for .planning/PROJECT.md, STATE.md, ROADMAP.md
and generates the projects.md page with current status and details.

Enforces "Strunk and White" style: omit needless words, use active voice.

Usage:
    python update_projects.py
    python update_projects.py --dry-run
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict


@dataclass
class ProjectInfo:
    """Metadata extracted from project planning documents."""
    name: str
    path: Path
    category: str
    status: str
    status_detail: Optional[str] = None
    stack: list[str] = field(default_factory=list)
    sections: Dict[str, str] = field(default_factory=dict)
    current_status: str = ""
    github_url: Optional[str] = None


def extract_sections(content: str) -> Dict[str, str]:
    """Extract all ## sections from markdown."""
    sections = {}
    # Find all ## headers and their content until the next header or end of file
    matches = re.finditer(r'^##\s+(.*?)\s*$(.*?)(?=^##\s|\Z)', content, re.MULTILINE | re.DOTALL)
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        if body:
            sections[header] = body
    return sections


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    """Parse project metadata from .planning directory."""
    planning_dir = project_path / ".planning"
    if not planning_dir.exists():
        return None

    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists():
        return None

    content = project_md.read_text()
    all_sections = extract_sections(content)

    # Extract tech stack from "Constraints" or "Context"
    stack = []
    constraints = all_sections.get("Constraints", "")
    if "Tech Stack" in constraints:
        tech_match = re.search(r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', constraints)
        if tech_match:
            stack_str = tech_match.group(1).split('\n')[0]
            stack = [s.strip() for s in re.split(r'[,;]', stack_str) if s.strip()]

    # Determine status from STATE.md
    status = "active"
    status_detail = None
    current_status = ""

    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text()
        state_sections = extract_sections(state_content)
        
        position = state_sections.get("Current Position", "")
        if position:
            phase_match = re.search(r'Phase:\s*(\d+)\s*of\s*(\d+)', position)
            if phase_match:
                current_phase, total_phases = phase_match.groups()
                progress_match = re.search(r'Progress:.*?(\d+)%', position)
                if progress_match:
                    status_detail = f"Phase {current_phase}/{total_phases} ({progress_match.group(1)}%)"
                else:
                    status_detail = f"Phase {current_phase}/{total_phases}"

        last_activity = re.search(r'\*\*Last activity:\*\*\s*(.+)', state_content)
        if last_activity:
            current_status = last_activity.group(1).strip()

    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text()
        if "All phases complete" in roadmap_content or "100%" in roadmap_content:
            status = "complete"
            status_detail = "Production Ready"

    return ProjectInfo(
        name=project_path.name,
        path=project_path,
        category="network",  # Default, categorized later
        status=status,
        status_detail=status_detail,
        stack=stack,
        sections=all_sections,
        current_status=current_status
    )


def categorize_project(project: ProjectInfo) -> str:
    """Categorize project based on name and content."""
    name_lower = project.name.lower()
    overview = str(project.sections).lower()

    if any(x in name_lower for x in ['netvis', 'ank', 'topogen', 'netsim', 'autonetkit']):
        return "network"
    if any(x in name_lower for x in ['astro', 'healthypi', 'spectra']):
        return "signal"
    if any(x in name_lower for x in ['agent', 'cycle']):
        return "agents"
    
    if 'network' in overview or 'topology' in overview:
        return "network"
    if any(x in overview for x in ['signal', 'biometric', 'spectrum']):
        return "signal"
    if 'agent' in overview:
        return "agents"

    return "network"


def generate_status_badge(project: ProjectInfo) -> str:
    """Generate status badge HTML."""
    if project.status == "complete":
        return '<span class="status-badge status-complete">Production Ready</span>'
    detail = project.status_detail or ("Planning" if project.status == "planning" else "Active Development")
    cls = "status-planning" if project.status == "planning" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def generate_project_section(project: ProjectInfo) -> str:
    """Generate markdown for a single project, preserving detail and structure."""
    lines = [f"### {project.name}", "", generate_status_badge(project), ""]

    # Interesting sections to include if they exist
    priority_sections = [
        "Core Value", "Overview", "What This Is", "Problem It Solves",
        "Architecture", "Technical Depth", "Security Model", "Features",
        "Protocols Implemented", "Performance", "Metrics"
    ]

    included_count = 0
    for sec_name in priority_sections:
        content = project.sections.get(sec_name)
        if content:
            # For "Overview" type sections, just include the text
            if sec_name in ["Core Value", "Overview", "What This Is"]:
                lines.append(content)
            else:
                # For others, include the header as bold
                lines.append(f"**{sec_name}:**")
                lines.append(content)
            lines.append("")
            included_count += 1

    if project.stack:
        lines.append(f"**Stack:** {' · '.join(project.stack)}")
        lines.append("")

    if project.current_status:
        lines.append(f"**Current Status:** {project.current_status}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_projects_page(projects: list[ProjectInfo]) -> str:
    """Generate complete projects.md content."""
    lines = [
        "---", "layout: default", "---", "",
        "# Projects", "",
        "My work focuses on network automation tools, signal processing systems, and multi-agent architectures.",
        "", "---", ""
    ]

    categories = {
        "network": ("Network Engineering", []),
        "signal": ("Signal Processing & Hardware", []),
        "agents": ("AI & Agents", []),
        "legacy": ("Legacy", [])
    }

    for project in projects:
        project.category = categorize_project(project)
        categories[project.category][1].append(project)

    for cat_id, (title, cat_projects) in categories.items():
        if not cat_projects: continue
        lines.append(f"## {title}\n")
        for project in sorted(cat_projects, key=lambda p: p.name):
            lines.append(generate_project_section(project))

    lines.append("## Development Approach\n")
    lines.append("I plan work in `.planning/` directories with phase-based execution. I verify completeness with formal documents. I use NATS for message coordination. I write comprehensive tests. I document architecture decisions in PROJECT.md and STATE.md.\n")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("projects.md"))
    args = parser.parse_args()

    base_dirs = [Path.home() / "dev", Path.home() / "PycharmProjects", Path.home() / "RustroverProjects"]
    projects = []
    for d in base_dirs:
        if not d.exists(): continue
        for p_dir in d.iterdir():
            if p_dir.is_dir() and not p_dir.name.startswith('.'):
                info = parse_project_metadata(p_dir)
                if info: projects.append(info)

    content = generate_projects_page(projects)
    if args.dry_run:
        print(content)
    else:
        args.output.write_text(content)
        print(f"✓ Updated {args.output}")


if __name__ == "__main__":
    main()
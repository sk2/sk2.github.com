#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.

Scans project directories for .planning/PROJECT.md, STATE.md, ROADMAP.md
and generates:
1. projects.md (Summary index)
2. projects/*.md (Detailed project pages)

Enforces "Strunk and White" style.
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
    slug: str
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

    # Slug for filenames
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")

    # Extract tech stack
    stack = []
    constraints = all_sections.get("Constraints", "")
    if "Tech Stack" in constraints:
        tech_match = re.search(r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', constraints)
        if tech_match:
            stack_str = tech_match.group(1).split('\n')[0]
            stack = [s.strip() for s in re.split(r'[,;]', stack_str) if s.strip()]

    # Status from STATE.md
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
        slug=slug,
        path=project_path,
        category="network",  # categorized later
        status=status,
        status_detail=status_detail,
        stack=stack,
        sections=all_sections,
        current_status=current_status
    )


def categorize_project(project: ProjectInfo) -> str:
    name_lower = project.name.lower()
    overview = str(project.sections).lower()
    if any(x in name_lower for x in ['netvis', 'ank', 'topogen', 'netsim', 'autonetkit']): return "network"
    if any(x in name_lower for x in ['astro', 'healthypi', 'spectra']): return "signal"
    if any(x in name_lower for x in ['agent', 'cycle']): return "agents"
    if 'network' in overview or 'topology' in overview: return "network"
    if any(x in overview for x in ['signal', 'biometric', 'spectrum']): return "signal"
    return "network"


def generate_status_badge(project: ProjectInfo) -> str:
    if project.status == "complete":
        return '<span class="status-badge status-complete">Production Ready</span>'
    detail = project.status_detail or "Active Development"
    cls = "status-planning" if project.status == "planning" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def generate_detailed_page(project: ProjectInfo) -> str:
    """Generate the full markdown for an individual project page."""
    lines = [
        "---", "layout: default", "---", "",
        f"# {project.name}", "",
        generate_status_badge(project), "",
        "[← Back to Projects](../projects)", "", "---", "",
        "## Quick Facts", "",
        "| | |", "|---|---|",
        f"| **Status** | {project.status_detail or project.status.capitalize()} |",
        f"| **Language** | {', '.join(project.stack) if project.stack else 'N/A'} |",
        "| **Started** | 2025 |", "", "---", ""
    ]

    # Include all relevant sections from PROJECT.md
    priority_sections = [
        "Core Value", "Overview", "What This Is", "Problem It Solves",
        "Architecture", "Technical Depth", "Security Model", "Features",
        "Protocols Implemented", "Performance", "Metrics", "Usage Examples"
    ]

    for sec_name in priority_sections:
        content = project.sections.get(sec_name)
        if content:
            lines.append(f"## {sec_name}\n")
            lines.append(content + "\n")

    if project.current_status:
        lines.append("## Current Status\n")
        lines.append(f"{project.current_status}\n")

    lines.append("---\n")
    lines.append("[← Back to Projects](../projects) | [Development Philosophy](../development)\n")
    
    return "\n".join(lines)


def generate_summary_section(project: ProjectInfo) -> str:
    """Generate a brief summary for the main projects.md index."""
    # Try to get the first paragraph of Overview or Core Value
    overview = project.sections.get("Overview") or project.sections.get("Core Value") or project.sections.get("What This Is") or ""
    summary = overview.split('\n\n')[0]
    
    return f"### [{project.name}](projects/{project.slug})\n\n{generate_status_badge(project)}\n\n{summary}\n\n---\n"


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = [
        "---", "layout: default", "---", "",
        "# Projects", "",
        "My work focuses on network automation tools, signal processing systems, and multi-agent architectures.",
        "", "---", ""
    ]

    categories = {"network": ("Network Engineering", []), "signal": ("Signal Processing & Hardware", []), "agents": ("AI & Agents", [])}
    for p in projects:
        p.category = categorize_project(p)
        if p.category in categories: categories[p.category][1].append(p)

    for cat_id, (title, cat_projects) in categories.items():
        if not cat_projects: continue
        lines.append(f"## {title}\n")
        for p in sorted(cat_projects, key=lambda x: x.name):
            lines.append(generate_summary_section(p))

    lines.append("## Development Approach\n\nI plan work in `.planning/` directories with phase-based execution. I document architecture decisions in PROJECT.md and STATE.md.\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    base_dirs = [Path.home() / "dev", Path.home() / "PycharmProjects", Path.home() / "RustroverProjects"]
    projects = []
    for d in base_dirs:
        if not d.exists(): continue
        for p_dir in d.iterdir():
            if p_dir.is_dir() and not p_dir.name.startswith('.'):
                info = parse_project_metadata(p_dir)
                if info: projects.append(info)

    if args.dry_run:
        print("Summary Index Preview:")
        print(generate_projects_index(projects)[:500] + "...")
    else:
        # 1. Update projects.md
        Path("projects.md").write_text(generate_projects_index(projects))
        
        # 2. Update projects/*.md
        projects_dir = Path("projects")
        projects_dir.mkdir(exist_ok=True)
        for p in projects:
            file_path = projects_dir / f"{p.slug}.md"
            file_path.write_text(generate_detailed_page(p))
            
        print(f"✓ Updated projects.md and {len(projects)} detailed pages in projects/")


if __name__ == "__main__":
    main()

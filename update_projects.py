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

    # Extract project name from # header
    name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name

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
        name=project_name,
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
    sections_lower = str(project.sections).lower()

    # Explicit assignments based on user feedback
    if "watchnoise" in name_lower: return "personal-apps"
    if "nascleanup" in name_lower: return "data-utilities"
    if "photo-tour" in name_lower: return "personal-apps"
    if "open-astro-core" in name_lower or "open-astro-node" in name_lower: return "astrophotography"

    # Keyword-based assignments
    if any(x in name_lower for x in ['netvis', 'ank', 'topogen', 'netsim', 'autonetkit']): return "network"
    if any(x in name_lower for x in ['healthypi', 'spectra']): return "signal"
    if any(x in name_lower for x in ['agent', 'cycle', 'multi-agent-assistant']): return "agents"

    # Fallback to content-based (less specific, ordered by preference)
    if 'network' in sections_lower or 'topology' in sections_lower: return "network"
    if any(x in sections_lower for x in ['signal', 'biometric', 'spectrum', 'radio']): return "signal"
    if any(x in sections_lower for x in ['astro', 'telescope', 'astrophotography']): return "astrophotography"
    if 'data' in sections_lower or 'geospatial' in sections_lower or 'utilities' in sections_lower: return "data-utilities"
    if 'agent' in sections_lower or 'ai' in sections_lower: return "agents"
    if 'personal' in sections_lower or 'app' in sections_lower or 'watch' in sections_lower: return "personal-apps"
    
    return "other" # New default category for anything uncategorized


def generate_status_badge(project: ProjectInfo) -> str:
    if project.status == "complete":
        return '<span class="status-badge status-complete">Production Ready</span>'
    detail = project.status_detail or "Active Development"
    cls = "status-planning" if project.status == "planning" else "status-active"
    return f'<span class="status-badge {cls}">{detail}</span>'


def generate_detailed_page(project: ProjectInfo) -> str:
    """Generate the full markdown for an individual project page."""
    # Try to extract "The Insight" from existing file to preserve it
    existing_insight = ""
    file_path = Path("projects") / f"{project.slug}.md"
    if file_path.exists():
        content = file_path.read_text()
        insight_match = re.search(r'## The Insight\n\n(.*?)(?=\n\n##|\n\n---)', content, re.DOTALL)
        if insight_match:
            existing_insight = insight_match.group(1).strip()

    lines = [
        "---", "layout: default", "---", "",
        f"# {project.name}", "",
        generate_status_badge(project), "",
        "[← Back to Projects](../projects)", "", "---", ""
    ]

    if existing_insight:
        lines.extend(["", "## The Insight", "", existing_insight, ""])
    elif "Core Value" in project.sections:
        lines.extend(["", "## The Insight", "", project.sections["Core Value"], ""])

    lines.extend([
        "## Quick Facts", "",
        "| | |", "|---|---|",
        f"| **Status** | {project.status_detail or project.status.capitalize()} |",
        f"| **Language** | {', '.join(project.stack) if project.stack else 'N/A'} |",
        "| **Started** | 2025 |", "", "---", ""
    ])

    # Include all relevant sections from PROJECT.md
    priority_sections = [
        "Overview", "What This Is", "Problem It Solves",
        "Architecture", "Technical Depth", "Security Model", "Features",
        "Protocols Implemented", "Performance", "Metrics"
    ]

    for sec_name in priority_sections:
        if sec_name == "Core Value" and (existing_insight or "Core Value" in project.sections): 
            # Skip Core Value if we already used it or have an insight
            if sec_name in project.sections and not existing_insight and project.sections[sec_name] == existing_insight:
                 continue
        
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


def main():
    parser = argparse.ArgumentParser(description="Update projects pages.")
    parser.add_argument("--scan-dirs", nargs="+",
                        default=["~/dev", "~/PycharmProjects", "~/RustroverProjects"],
                        help="Directories to scan for projects with .planning/PROJECT.md")
    args = parser.parse_args()

    # Scan for projects with .planning/PROJECT.md
    projects = []
    for scan_dir in args.scan_dirs:
        scan_path = Path(scan_dir).expanduser()
        if not scan_path.exists():
            continue

        for project_dir in scan_path.iterdir():
            if not project_dir.is_dir():
                continue
            project_info = parse_project_metadata(project_dir)
            if project_info:
                projects.append(project_info)

    # Also include legacy projects (existing .md files without .planning dirs)
    projects_dir = Path("projects")
    if projects_dir.exists():
        scanned_slugs = {p.slug for p in projects}
        scanned_names = {p.name for p in projects}
        for legacy_md in projects_dir.glob("*.md"):
            if legacy_md.stem not in scanned_slugs:
                # Read existing file to preserve it
                content = legacy_md.read_text()
                name_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                if name_match:
                    name = name_match.group(1).strip()

                    # Skip if a project with this name already exists (from new scan)
                    if name in scanned_names:
                        print(f"  Skipping duplicate: {name} (using newly scanned version)")
                        continue

                    print(f"  Preserving legacy project: {name}")

                    # Extract basic metadata for index generation
                    status = "active"
                    status_detail = "Active Development"
                    badge_match = re.search(r'<span class="status-badge.*?>(.*?)</span>', content)
                    if badge_match:
                        status_detail = badge_match.group(1).strip()
                        if "Complete" in status_detail or "Ready" in status_detail:
                            status = "complete"

                    stack = []
                    stack_match = re.search(r'\|\s*\*\*Language\*\*\s*\|\s*(.*?)\s*\|', content)
                    if stack_match:
                        stack_str = stack_match.group(1).strip()
                        stack = [s.strip() for s in re.split(r'[,·]', stack_str) if s.strip() and s.strip() != "N/A"]

                    sections = extract_sections(content)

                    legacy_project = ProjectInfo(
                        name=name,
                        slug=legacy_md.stem,
                        path=legacy_md,
                        category="other",
                        status=status,
                        status_detail=status_detail,
                        stack=stack,
                        sections=sections
                    )
                    projects.append(legacy_project)

    if not projects:
        print("No projects found with .planning/PROJECT.md")
        return

    # Sort projects by name
    projects.sort(key=lambda x: x.name)
    print(f"Found {len(projects)} projects: {[p.name for p in projects]}")

    # Generate individual project pages
    projects_dir = Path("projects")
    projects_dir.mkdir(exist_ok=True)

    for project in projects:
        page_content = generate_detailed_page(project)
        page_path = projects_dir / f"{project.slug}.md"
        page_path.write_text(page_content)
        print(f"  Generated {page_path}")

    # Generate index
    index_content = generate_projects_index(projects)
    Path("projects.md").write_text(index_content)
    print("Updated projects.md")


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = [
        "---", "layout: default", "---", "",
        "# Projects", "",
        "My work focuses on network automation tools, signal processing systems, and multi-agent architectures.",
        "", "---", ""
    ]

    categories = {
        "network": ("Network Engineering", []),
        "signal": ("Signal Processing & Hardware", []),
        "astrophotography": ("Astrophotography", []),
        "agents": ("AI & Agents", []),
        "data-utilities": ("Data & Utilities", []),
        "personal-apps": ("Personal Apps", []),
        "other": ("Other Projects", []) # For any uncategorized
    }
    for p in projects:
        p.category = categorize_project(p)
        if p.category in categories: categories[p.category][1].append(p)
        else: categories["other"][1].append(p) # Assign to 'other' if category not defined

    for cat_id, (title, cat_projects) in categories.items():
        if not cat_projects:
            continue
        lines.append(f"## {title}\n")
        lines.append('<div class="projects-grid">\n') # Start grid for category
        for p in sorted(cat_projects, key=lambda x: x.name):
            overview = p.sections.get("Overview") or p.sections.get("Core Value") or p.sections.get("What This Is") or ""
            summary = overview.split('\n\n')[0]
            if len(summary) > 200:
                summary = summary[:197] + "..."

            lines.append(f'  <div class="project-card">')
            lines.append(f'    <div class="project-header">')
            lines.append(f'      {generate_status_badge(p)}')
            lines.append(f'      <h2>{p.name}</h2>')
            lines.append(f'    </div>')
            lines.append(f'    <div class="project-meta">')
            for tech in p.stack[:3]: # Show top 3 techs
                lines.append(f'      <span class="project-badge">{tech}</span>')
            lines.append(f'    </div>')
            lines.append(f'    <p>{summary}</p>')
            lines.append(f'    <a href="projects/{p.slug}" class="btn">View Details →</a>')
            lines.append(f'  </div>\n')
        lines.append('</div>\n') # End grid for category


    # Extract principles from development.md if it exists
    principles = []
    dev_md_path = Path("development.md")
    if dev_md_path.exists():
        dev_content = dev_md_path.read_text()
        principles_match = re.search(r'## Principles\s*\n(.*?)(?=\n##|\Z)', dev_content, re.DOTALL | re.MULTILINE)
        if principles_match:
            for line in principles_match.group(1).strip().split('\n'):
                if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                    # Clean up the numbered list item, convert to bullet point
                    # Ensure each principle starts with a dash and is properly formatted
                    principle = re.sub(r'^\d+\.\s*\*\*(.*?)\*\*[:\-]?\s*(.*)', r'- **\1**: \2', line.strip())
                    principles.append(principle)

    lines.append("## Development Approach\n")
    lines.append("I build tools with a **planning-first** approach. Every project lives in a `.planning/` directory, where I define core values in `PROJECT.md`, track execution in `STATE.md`, and verify progress through rigorous phase-based goals.\n")
    
    if principles:
        lines.append("### Core Principles\n")
        lines.extend(principles)
        lines.append("")

    lines.append("[Detailed Development Philosophy](development)\n")
    lines.append('<style>')
    lines.append('.projects-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: var(--space-lg); margin-top: var(--space-xl); }')
    lines.append('.project-card { display: flex; flex-direction: column; justify-content: space-between; padding: var(--space-xl); border: 1px solid var(--border-color); border-radius: 8px; background-color: var(--bg-secondary); }')
    lines.append('.project-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: var(--space-sm); }')
    lines.append('.project-header h2 { margin: 0; font-size: 1.5rem; }')
    lines.append('.project-meta { margin-bottom: var(--space-sm); }')
    lines.append('.project-badge { display: inline-block; padding: 0.25rem 0.6rem; margin-right: 0.5rem; border-radius: 4px; background-color: var(--code-bg); color: var(--text-secondary); font-size: 0.75rem; }')
    lines.append('.btn { display: inline-block; margin-top: var(--space-md); padding: 0.5rem 1rem; background-color: var(--bg-tertiary); color: var(--text-primary); border-radius: 6px; font-weight: 600; font-size: 0.875rem; transition: all var(--transition-fast); text-decoration: none; }')
    lines.append('.btn:hover { background-color: var(--accent); color: white; }')
    lines.append('.status-badge { display: inline-block; padding: 0.2em 0.6em; border-radius: 4px; font-size: 0.75em; font-weight: 600; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; }')
    lines.append('.status-complete { background-color: #28a745; color: white; }')
    lines.append('.status-active { background-color: #007bff; color: white; }')
    lines.append('.status-planning { background-color: #ffc107; color: #343a40; }')
    lines.append('</style>')

    return "\n".join(lines)


if __name__ == "__main__":
    main()
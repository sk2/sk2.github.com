#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.

Scans project directories for .planning/PROJECT.md, STATE.md, ROADMAP.md
and generates:
1. projects.md (Summary index)
2. projects/*.md (Detailed project pages)

Enforces "Understated Expert" style.
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

    # Clean up project names (remove verbose prefixes)
    project_name = re.sub(r'^PROJECT:\s*', '', project_name, flags=re.IGNORECASE)
    project_name = re.sub(r'^Project:\s*', '', project_name, flags=re.IGNORECASE)
    project_name = re.sub(r'\s*\([^)]+\)$', '', project_name)  # Remove trailing parentheticals

    # Slug for filenames with special mappings
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")

    # Special slug mappings to consolidate duplicates
    slug_mappings = {
        "multi-agent-assistant": "multi-agent",
        "watch-noise": "watchnoise", # Corrected to match existing watchnoise.md
    }
    slug = slug_mappings.get(slug, slug)

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
    """Categorize projects for grouping in index."""
    name_lower = project.name.lower()
    sections_lower = str(project.sections).lower()

    # Network projects
    if any(x in name_lower for x in ['netvis', 'ank', 'topogen', 'netsim', 'autonetkit', 'network']):
        return "network"

    # Data & Simulation
    if any(x in name_lower for x in ['netflow', 'polars', 'tileserver', 'matrix-time-series', 'matrix-profile', 'matrix_profile', 'weather', 'simulation']):
        return "data"

    # AI & Agents
    if any(x in name_lower for x in ['agent', 'multi-agent', 'cycle']):
        return "agents"

    # Signal processing / SDR
    if any(x in name_lower for x in ['healthypi', 'spectra', 'passive', 'radar', 'kraken', 'rtltcp', 'wifi-radar']):
        return "signal"

    return "experimental"


def generate_status_badge(project: ProjectInfo) -> str:
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
        "| **Started** | 2026 |", "", "---", ""
    ])

    # Include priority sections from PROJECT.md
    priority_sections = [
        "Overview", "What This Is", "Problem It Solves", "Core Value",
        "Features", "Key Capabilities", "Technical Features",
        "Architecture", "Technical Depth", "Security Model",
        "Implementation Details", "Design Decisions",
        "Protocols Implemented", "Performance", "Metrics",
        "Use Cases", "Integration", "Hardware", "Agents", "Components"
    ]

    for sec_name in priority_sections:
        if sec_name == "Core Value" and existing_insight:
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


def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = [
        "---", "layout: default", "---", "",
        "# Projects", "",
        "Focusing on network automation, high-performance signal processing, and secure multi-agent architectures.",
        "", "---", ""
    ]

    # Group by category matching the established order
    categories = {
        "network": ("🌐 Network Engineering", "High-performance tools for topology modeling, deterministic protocol simulation, and visualization.", "/network-automation", []),
        "data": ("📊 Data Science & Simulation", "High-performance tools for large-scale geospatial analytics and time-series pattern discovery.", "/data-analytics", []),
        "agents": ("🤖 AI & Agents", "Security-first architectures for multi-agent coordination and isolated automation.", "/agentic-systems", []),
        "signal": ("📡 Signal Processing & RF", "SDR spectrum monitoring and biometric signal processing using modular acquisition pipelines.", "/signal-processing", []),
        "experimental": ("🔭 Experimental & Hobbies", "Projects in exploratory phases or related to technical hobbies.", None, [])
    }

    for p in projects:
        p.category = categorize_project(p)
        if p.category in categories:
            categories[p.category][3].append(p)
        else:
            categories["experimental"][3].append(p)

    # Generate sections
    for cat_key, (cat_title, cat_desc, cat_link, cat_projects) in categories.items():
        if not cat_projects:
            continue

        lines.append(f"## {cat_title}\n")
        if cat_link:
            lines.append(f"> **[View Ecosystem →]({cat_link})**")
            lines.append(f"> {cat_desc}\n")

        for p in sorted(cat_projects, key=lambda x: x.name):
            # Build summary from multiple sections
            summary_parts = []
            for section_key in ["Overview", "What This Is", "Core Value", "Problem It Solves"]:
                content = p.sections.get(section_key)
                if content:
                    first_para = content.split('\n\n')[0]
                    summary_parts.append(first_para)

            summary = ' '.join(summary_parts) if summary_parts else ""

            if summary:
                sentences = re.split(r'(?<=[.!?])\s+', summary)
                num_sentences = min(5, len(sentences))
                selected_sentences = sentences[:num_sentences]
                paragraphs = []
                for i in range(0, len(selected_sentences), 2):
                    para = ' '.join(selected_sentences[i:i+2])
                    paragraphs.append(para)
                summary = '\n\n'.join(paragraphs)

            lines.append(f"### [{p.name}](projects/{p.slug})\n")
            lines.append(f"{generate_status_badge(p)}")

            if p.stack:
                tech_str = " · ".join(p.stack[:3])
                lines.append(f" · **{tech_str}**")

            lines.append("\n")
            if summary:
                lines.append(f"{summary}\n")
            lines.append("")

    lines.append('<style>')
    lines.append('.status-badge { display: inline-block; padding: 0.2em 0.6em; margin: 0.3em 0; border-radius: 4px; font-size: 0.8em; font-weight: 600; }')
    lines.append('.status-active { background-color: #f8f9fa; color: #495057; border: 1px solid #dee2e6; }')
    lines.append('.status-planning { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }')
    lines.append('h3 { margin-bottom: 0.1em; }')
    lines.append('h3 + .status-badge { margin-top: 0; }')
    lines.append('section { margin-bottom: 2em; }')
    lines.append('blockquote { margin: 1em 0; padding: 0.5em 1em; border-left: 2px solid #495057; background: #f8f9fa; font-style: normal; font-size: 0.9em; }')
    lines.append('</style>')

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Update projects pages.")
    parser.add_argument("--scan-dirs", nargs="+",
                        default=["~/dev", "~/PycharmProjects", "~/RustroverProjects"],
                        help="Directories to scan for projects with .planning/PROJECT.md")
    args = parser.parse_args()

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

    # Legacy projects
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
                    if name in scanned_names:
                        continue
                    
                    status = "active"
                    status_detail = "Active Development"
                    badge_match = re.search(r'<span class="status-badge.*?>(.*?)</span>', content)
                    if badge_match:
                        status_detail = badge_match.group(1).strip()

                    stack = []
                    stack_match = re.search(r'\|\s*\*\*Language\*\*\s*\|\s*(.*?)\s*\|', content)
                    if stack_match:
                        stack_str = stack_match.group(1).strip()
                        stack = [s.strip() for s in re.split(r'[,·]', stack_str) if s.strip() and s.strip() != "N/A"]

                    sections = extract_sections(content)
                    projects.append(ProjectInfo(
                        name=name, slug=legacy_md.stem, path=legacy_md,
                        category="experimental", status=status,
                        status_detail=status_detail, stack=stack, sections=sections
                    ))

    projects.sort(key=lambda x: x.name)
    print(f"Found {len(projects)} projects")

    for project in projects:
        page_path = Path("projects") / f"{project.slug}.md"
        page_content = generate_detailed_page(project)

        if page_path.exists():
            existing_content = page_path.read_text()
            if len(existing_content.split('\n')) > len(page_content.split('\n')) * 3:
                name_match = re.search(r'^#\s+(.+)$', existing_content, re.MULTILINE)
                if name_match:
                    project.name = name_match.group(1).strip()
                continue

        page_path.write_text(page_content)

    index_content = generate_projects_index(projects)
    Path("projects.md").write_text(index_content)
    print("Updated projects.md and individual pages")


if __name__ == "__main__":
    main()
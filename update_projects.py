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

    # Clean up project names (remove verbose prefixes)
    project_name = re.sub(r'^PROJECT:\s*', '', project_name, flags=re.IGNORECASE)
    project_name = re.sub(r'^Project:\s*', '', project_name, flags=re.IGNORECASE)
    project_name = re.sub(r'\s*\([^)]+\)$', '', project_name)  # Remove trailing parentheticals like (KrakenSDR)

    # Slug for filenames with special mappings
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")

    # Special slug mappings to consolidate duplicates
    slug_mappings = {
        "multi-agent-assistant": "multi-agent",
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

    # Note: Don't assume production readiness based on phase completion
    # Just use the phase progress as the status detail

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

    # Signal processing / SDR / Hardware
    if any(x in name_lower for x in ['healthypi', 'spectra', 'passive', 'radar', 'kraken']):
        return "signal"

    # Astrophotography
    if any(x in name_lower for x in ['astro', 'asiair']) or 'astro' in sections_lower:
        return "astrophotography"

    # Photography
    if any(x in name_lower for x in ['photo-tour', 'photo tour']):
        return "photography"

    # AI & Agents
    if any(x in name_lower for x in ['agent', 'multi-agent', 'cycle']):
        return "agents"

    # Data & Utilities
    if any(x in name_lower for x in ['cleanup', 'tileserver', 'tile']):
        return "data"

    # Wellness & Sound
    if any(x in name_lower for x in ['watch', 'noise', 'wave', 'sleep', 'health']):
        # Exclude healthypi (that's signal processing hardware)
        if 'healthypi' not in name_lower:
            return "wellness"

    return "other"


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

    # Include all relevant sections from PROJECT.md (expanded for more detail)
    priority_sections = [
        "Overview", "What This Is", "Problem It Solves", "Core Value",
        "Features", "Key Capabilities", "Technical Features",
        "Architecture", "Technical Depth", "Security Model",
        "Implementation Details", "Design Decisions",
        "Protocols Implemented", "Performance", "Metrics",
        "Use Cases", "Integration", "Hardware", "Agents", "Components"
    ]

    for sec_name in priority_sections:
        # Skip Core Value if we already used it in The Insight section
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
        page_path = projects_dir / f"{project.slug}.md"
        page_content = generate_detailed_page(project)

        # Preserve existing detailed content if it's substantially longer
        # (indicates manual enrichment that shouldn't be lost)
        if page_path.exists():
            existing_content = page_path.read_text()
            existing_lines = len(existing_content.split('\n'))
            new_lines = len(page_content.split('\n'))

            # If existing file has 3x more content, it's likely manually enriched
            # Also extract the existing name for use in the index
            if existing_lines > new_lines * 3:
                # Extract name from existing file and update project info
                name_match = re.search(r'^#\s+(.+)$', existing_content, re.MULTILINE)
                if name_match:
                    project.name = name_match.group(1).strip()
                print(f"  Preserving detailed content: {page_path} ({existing_lines} vs {new_lines} lines)")
                continue

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

    # Group by category
    categories = {
        "network": ("Network Engineering", []),
        "signal": ("Signal Processing & SDR", []),
        "astrophotography": ("Astrophotography", []),
        "photography": ("Photography", []),
        "agents": ("AI & Agents", []),
        "data": ("Data & Utilities", []),
        "wellness": ("Wellness & Sound", []),
        "other": ("Other", [])
    }

    for p in projects:
        p.category = categorize_project(p)
        if p.category in categories:
            categories[p.category][1].append(p)
        else:
            categories["other"][1].append(p)

    # Generate sections
    for cat_key, (cat_title, cat_projects) in categories.items():
        if not cat_projects:
            continue

        lines.append(f"## {cat_title}\n")

        for p in sorted(cat_projects, key=lambda x: x.name):
            # Build summary from multiple sections to get 4-5 sentences
            summary_parts = []
            for section_key in ["Overview", "What This Is", "Core Value", "Problem It Solves"]:
                content = p.sections.get(section_key)
                if content:
                    # Get first paragraph
                    first_para = content.split('\n\n')[0]
                    summary_parts.append(first_para)

            summary = ' '.join(summary_parts) if summary_parts else ""

            # Extract first 4-5 sentences with paragraph breaks for readability
            if summary:
                sentences = re.split(r'(?<=[.!?])\s+', summary)
                # Take 4-5 sentences depending on length
                if len(sentences) <= 3:
                    num_sentences = len(sentences)
                elif len(sentences[0]) > 100:
                    num_sentences = min(4, len(sentences))
                else:
                    num_sentences = min(5, len(sentences))

                # Add paragraph breaks every 2-3 sentences
                selected_sentences = sentences[:num_sentences]
                paragraphs = []
                for i in range(0, len(selected_sentences), 2):
                    # Group 2 sentences per paragraph
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


    # Note: Development philosophy section removed per user preference
    # Simple list layout - minimal CSS needed
    lines.append('<style>')
    lines.append('.status-badge { display: inline-block; padding: 0.3em 0.8em; margin: 0.5em 0; border-radius: 4px; font-size: 0.85em; font-weight: 600; }')
    lines.append('.status-active { background-color: #007bff; color: white; }')
    lines.append('.status-planning { background-color: #ffc107; color: #343a40; }')
    lines.append('</style>')

    return "\n".join(lines)


if __name__ == "__main__":
    main()
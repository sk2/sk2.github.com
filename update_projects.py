#!/usr/bin/env python3
"""
Update website projects page from project metadata.

Scans project directories for .planning/PROJECT.md, STATE.md, ROADMAP.md
and generates the projects.md page with current status and details.

Usage:
    python update_projects.py
    python update_projects.py --dry-run  # Preview without writing
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ProjectInfo:
    """Metadata extracted from project planning documents."""
    name: str
    path: Path
    category: str  # "network", "signal", "agents", "legacy"
    status: str  # "active", "planning", "complete", "legacy"
    status_detail: Optional[str] = None  # e.g., "Phase 4/6 (88%)"
    stack: list[str] = field(default_factory=list)
    overview: str = ""
    features: list[str] = field(default_factory=list)
    current_status: str = ""
    github_url: Optional[str] = None


def extract_yaml_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    result = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()
    return result


def extract_section(content: str, header: str) -> str:
    """Extract content under a markdown header."""
    pattern = rf'^##\s+{re.escape(header)}\s*$\n(.*?)(?=^##\s|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_bullet_points(content: str) -> list[str]:
    """Extract bullet points from markdown content."""
    points = []
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('- ') or line.startswith('* '):
            # Remove markdown formatting
            point = re.sub(r'\*\*(.*?)\*\*', r'\1', line[2:])
            point = re.sub(r'`(.*?)`', r'\1', point)
            points.append(point.strip())
    return points


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    """Parse project metadata from .planning directory."""
    planning_dir = project_path / ".planning"
    if not planning_dir.exists():
        return None

    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists():
        return None

    content = project_md.read_text()

    # Extract core value/overview
    core_value = extract_section(content, "Core Value")
    overview_section = extract_section(content, "Overview") or extract_section(content, "What This Is")
    overview = overview_section or core_value or ""

    # Clean up overview - keep more detail but strip excessive whitespace
    overview = overview.strip()

    # Extract tech stack from constraints or context
    stack = []
    constraints = extract_section(content, "Constraints")
    if "Tech Stack" in constraints:
        tech_match = re.search(r'\*\*Tech Stack[:\-]?\*\*:?\s*(.+)', constraints)
        if tech_match:
            stack_str = tech_match.group(1).split('\n')[0]
            stack = [s.strip() for s in re.split(r'[,;]', stack_str) if s.strip()]

    # Try to extract from requirements
    if not stack:
        requirements = extract_section(content, "Requirements")
        if requirements:
            # Look for technology mentions
            tech_patterns = ['Python', 'Rust', 'Swift', 'TypeScript', 'React', 'FastAPI', 'NATS', 'Docker']
            stack = [tech for tech in tech_patterns if tech.lower() in requirements.lower()]

    # Determine status from STATE.md if exists
    status = "active"
    status_detail = None
    current_status = ""

    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text()

        # Extract current position
        position = extract_section(state_content, "Current Position")
        if position:
            # Look for phase info
            phase_match = re.search(r'Phase:\s*(\d+)\s*of\s*(\d+)', position)
            if phase_match:
                current_phase = int(phase_match.group(1))
                total_phases = int(phase_match.group(2))

                # Look for progress percentage
                progress_match = re.search(r'Progress:.*?(\d+)%', position)
                if progress_match:
                    progress = int(progress_match.group(1))
                    status_detail = f"Phase {current_phase}/{total_phases} ({progress}%)"
                else:
                    status_detail = f"Phase {current_phase}/{total_phases}"

        # Extract last activity
        last_activity = re.search(r'\*\*Last activity:\*\*\s*(.+)', state_content)
        if last_activity:
            current_status = last_activity.group(1).strip()

    # Check ROADMAP.md for completion status
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        roadmap_content = roadmap_md.read_text()
        if "All phases complete" in roadmap_content or "100%" in roadmap_content:
            status = "complete"
            status_detail = "Production Ready"

    project_info = ProjectInfo(
        name=project_path.name,
        path=project_path,
        category="network",  # Will be categorized later
        status=status,
        status_detail=status_detail,
        stack=stack,
        overview=overview,
        current_status=current_status
    )

    return project_info


def categorize_project(project: ProjectInfo) -> str:
    """Categorize project based on name and content."""
    name_lower = project.name.lower()
    overview_lower = project.overview.lower()

    if any(x in name_lower for x in ['netvis', 'ank', 'topogen', 'netsim', 'autonetkit']):
        return "network"

    if any(x in name_lower for x in ['astro', 'healthypi', 'spectra']):
        return "signal"

    if any(x in name_lower for x in ['agent', 'cycle']):
        return "agents"

    if 'network' in overview_lower or 'topology' in overview_lower:
        return "network"

    if any(x in overview_lower for x in ['signal', 'biometric', 'spectrum', 'telescope']):
        return "signal"

    if 'agent' in overview_lower:
        return "agents"

    return "network"  # Default


def scan_projects(base_dirs: list[Path]) -> list[ProjectInfo]:
    """Scan multiple base directories for projects."""
    projects = []

    for base_dir in base_dirs:
        if not base_dir.exists():
            continue

        for project_dir in base_dir.iterdir():
            if not project_dir.is_dir():
                continue

            # Skip hidden directories and common non-project dirs
            if project_dir.name.startswith('.'):
                continue

            project_info = parse_project_metadata(project_dir)
            if project_info:
                project_info.category = categorize_project(project_info)
                projects.append(project_info)

    return projects


def generate_status_badge(project: ProjectInfo) -> str:
    """Generate status badge HTML."""
    if project.status == "complete":
        return '<span class="status-badge status-complete">Production Ready</span>'
    elif project.status == "planning":
        detail = project.status_detail or "Planning"
        return f'<span class="status-badge status-planning">{detail}</span>'
    else:  # active
        detail = project.status_detail or "Active Development"
        return f'<span class="status-badge status-active">{detail}</span>'


def generate_project_section(project: ProjectInfo) -> str:
    """Generate markdown for a single project."""
    lines = []

    # Title
    lines.append(f"### {project.name}")
    lines.append("")
    lines.append(generate_status_badge(project))
    lines.append("")

    # Overview
    if project.overview:
        lines.append(project.overview)
        lines.append("")

    # Tech stack
    if project.stack:
        stack_str = " · ".join(project.stack)
        lines.append(f"**Stack:** {stack_str}")
        lines.append("")

    # Current status (from STATE.md)
    if project.current_status:
        lines.append(f"**Current Status:** {project.current_status}")
        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def generate_projects_page(projects: list[ProjectInfo]) -> str:
    """Generate complete projects.md content."""
    lines = [
        "---",
        "layout: default",
        "---",
        "",
        "# Projects",
        "",
        "My work focuses on network automation tools, signal processing systems, and multi-agent architectures.",
        "",
        "---",
        ""
    ]

    # Group by category
    categories = {
        "network": ("Network Engineering", []),
        "signal": ("Signal Processing & Hardware", []),
        "agents": ("AI & Agents", []),
        "legacy": ("Legacy", [])
    }

    for project in projects:
        categories[project.category][1].append(project)

    # Generate sections
    for category, (title, category_projects) in categories.items():
        if not category_projects:
            continue

        lines.append(f"## {title}")
        lines.append("")

        for project in sorted(category_projects, key=lambda p: p.name):
            lines.append(generate_project_section(project))

    # Add development approach footer
    lines.extend([
        "## Development Approach",
        "",
        "I plan work in `.planning/` directories with phase-based execution. I verify completeness with formal documents. I use NATS for message coordination. I write comprehensive tests. I document architecture decisions in PROJECT.md and STATE.md.",
        ""
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Update website from project metadata")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--output", type=Path, default=Path("projects.md"), help="Output file")
    args = parser.parse_args()

    # Scan project directories
    base_dirs = [
        Path.home() / "dev",
        Path.home() / "PycharmProjects",
        Path.home() / "RustroverProjects"
    ]

    print("Scanning projects...")
    projects = scan_projects(base_dirs)
    print(f"Found {len(projects)} projects with metadata")

    for project in projects:
        print(f"  - {project.name} ({project.category}, {project.status})")

    # Generate content
    content = generate_projects_page(projects)

    if args.dry_run:
        print("\n" + "="*60)
        print("DRY RUN - Generated content:")
        print("="*60)
        print(content)
    else:
        args.output.write_text(content)
        print(f"\n✓ Updated {args.output}")


if __name__ == "__main__":
    main()

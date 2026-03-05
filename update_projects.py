#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Automated collection of PDFs, images, and code snippets.
"""

import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime, timedelta


@dataclass
class ProjectInfo:
    name: str
    slug: str
    original_slug: str
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
    assets: List[Path] = field(default_factory=list)
    docs: List[Path] = field(default_factory=list)


# SOURCE OF TRUTH: Explicit mapping of projects to ecosystems
ECOSYSTEM_MAP = {
    "network-simulator": "network-automation",
    "netsim": "network-automation",
    "ank_pydantic": "network-automation",
    "ank-pydantic": "network-automation",
    "compilation": "network-automation",
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
    "ank_netcfg": "network-automation",
    "ank-netcfg": "network-automation",
    "netassure": "network-automation",
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
    "ank_pydantic": "Network Modeling & Configuration Library",
    "ank-pydantic": "Network Modeling & Configuration Library",
    "cliscrape": "CLI Parser",
    "rtltcp": "Radio Streaming Server",
    "auroradata": "Aurora Advisor",
    "netflowsim": "Performance Simulator",
    "ank_netcfg": "Network Configuration Framework",
    "ank-netcfg": "Network Configuration Framework",
    "netassure": "Network Analysis Engine",
    "netsim": "Network Simulator",
    "network-simulator": "Network Simulator",
    "compilation": "Network Compilation Engine",
    "topogen": "Topology Generator",
    "ank-nte": "Topology Engine Core",
    "ank-workbench": "Automation Workbench",
    "autonetkit-foundation": "Network Modeling Foundations",
    "autonetkit": "Configuration Generation (AutoNetkit)",
    "netvis": "Visualization Engine",
    "passive": "Signal Reflection Analysis",
    "signals": "Spectrum Analysis",
    "configparsing": "Brownfield Ingestion & Analysis",
    "soundarray": "Sound Array",
}

CANONICAL_SLUG = {
    "network-simulator": "netsim",
    "ank-netcfg": "ank-netcfg",
}

PROJECT_CONTENT_OVERRIDES = {
    "netsim": {
        "Concept": "Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.\n\nUnlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.",
    },
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
    "experimental": ("🧪 Experimental", "Exploratory projects and technical experiments.", None),
}

DETAILED_SECTIONS = [
    "Concept", "Technical Reports", "Code Samples", "Usage", "Visuals",
    "Architecture", "Features", "Current Status", "Roadmap", "Quick Facts",
]

# Sections that should be updated if new assets/metadata are found, even if polished
ALWAYS_UPDATE_SECTIONS = {"Technical Reports", "Code Samples", "Visuals", "Current Status", "Roadmap"}
# Sections that are preserved from the website repo if they exist
STABLE_SECTIONS = {"Concept", "Architecture", "Features", "Quick Facts", "Usage"}

def extract_sections(content: str) -> Dict[str, str]:
    sections: Dict[str, str] = {}
    in_code_fence = False
    current_header: Optional[str] = None
    current_lines: list[str] = []
    for line in content.splitlines():
        if re.match(r"^\s*```", line): in_code_fence = not in_code_fence
        if not in_code_fence:
            if line.strip().startswith("[← Back to") or line.strip() == "---": continue
            m = re.match(r"^##\s*(.+?)\s*$", line)
            if m:
                header = m.group(1).strip()
                if header == "Contents":
                    current_header = None
                    continue
                if current_header: sections[current_header] = "\n".join(current_lines).strip()
                current_header, current_lines = header, []
                continue
        if current_header: current_lines.append(line)
    if current_header: sections[current_header] = "\n".join(current_lines).strip()
    return sections

def clean_text(text: str) -> str:
    text = re.sub(r"\(Phase.*?\)", "", text)
    text = re.sub(r"Phase \d+.*?\d+", "", text)
    text = re.sub(r"\*\*Phase \d+.*?\*\*", "", text)
    text = re.sub(r"\d+%", "", text)
    text = re.sub(r"^\s*·\s*\*\*.*?\*\*\s*$", "", text, flags=re.MULTILINE)
    return text.strip()

def generate_toc(content: str) -> str:
    headers = re.findall(r"^##\s+([^#\n]+)\s*$", content, re.MULTILINE)
    headers = [h.strip() for h in headers if h.strip() not in ["Contents", "Quick Facts"]]
    if len(headers) < 4: return ""
    links = [f"- [{h}](#{re.sub(r'-+', '-', re.sub(r'[^a-z0-9-]', '', h.lower().replace(' ', '-')))})" for h in headers]
    return "## Contents\n\n" + "\n".join(links) + "\n\n"

def get_back_links(category: str) -> str:
    links = []
    if category in FM_SECTIONS:
        slug = FM_SECTIONS[category]
        title = slug.replace("-", " ").title().replace("Agentic Systems", "Autonomous Systems")
        links.append(f"[← Back to {title}](../{slug})")
    links.append("[← Back to Projects](../projects)")
    return "\n\n".join(links)

FM_SECTIONS = {"network": "network-automation", "sdr": "signal-processing", "agents": "agentic-systems", "health": "agentic-systems", "data": "data-analytics"}

def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists(): return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists(): return None
    content = project_md.read_text()
    name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {"multi-agent-assistant": "multi-agent", "passive": "rf-signal-analysis", "wifi-radar": "wifi-signal-analysis", "ank_pydantic": "ank-pydantic", "ank_nte": "ank-nte", "ank_workbench": "ank-workbench", "network-simulator": "netsim"}
    slug = slug_mappings.get(slug, slug)
    slug = CANONICAL_SLUG.get(slug, slug)
    if slug in PROJECT_ALIASES: project_name = PROJECT_ALIASES[slug]
    sections = extract_sections(content)
    for s_key in [slug]:
        if s_key in PROJECT_CONTENT_OVERRIDES:
            for sec, body in PROJECT_CONTENT_OVERRIDES[s_key].items(): sections[sec] = body
    cat = "experimental"
    s = slug.lower()
    if "photo-tour" in s: cat = "photography"
    elif any(x in s for x in ["watchnoise", "watch-noise", "psytrance"]): cat = "wellness"
    elif any(x in s for x in ["healthypi", "hrv"]): cat = "health"
    elif any(x in s for x in ["spectra", "rtltcp", "wifi-signal-analysis", "signals", "rf-signal-analysis"]): cat = "sdr"
    elif any(x in s for x in ["astro", "aurora", "eclipse", "satellites"]): cat = "astrophotography"
    elif any(x in s for x in ["agent", "multi-agent", "cycle"]): cat = "agents"
    elif any(x in s for x in ["netflow", "polars", "tileserver", "matrix-time-series", "weather", "omnifocus-db", "cliscrape", "nascleanup", "devmon"]): cat = "data"
    elif any(x in s for x in ["netvis", "ank", "topogen", "netsim", "autonetkit", "network", "configparsing", "nte", "orchestrator", "automationarch", "netflowsim"]): cat = "network"
    assets, docs = [], []
    docs_dir = project_path / "docs"
    if docs_dir.exists():
        for pdf in docs_dir.rglob("*.pdf"):
            if any(x in pdf.name for x in ["paper.pdf", "techreport.pdf"]): docs.append(pdf)
    for ext in ["*.png", "*.svg"]:
        for img in project_path.rglob(ext):
            if any(x in str(img) for x in ["node_modules", ".venv", ".pytest_cache"]): continue
            if img.parent.name in ["figures", "images", "visuals"] or any(x in img.name for x in ["diagram", "example", "hero"]): assets.append(img)
    code_samples = []
    # Search in examples/ and tests/python/ (for Query API)
    for search_dir in [project_path / "examples", project_path / "tests" / "python"]:
        if search_dir.exists():
            for f in sorted(search_dir.glob("*")):
                if f.is_file() and f.suffix in [".yaml", ".py", ".rs", ".md"] and f.stat().st_size < 10000:
                    lang = f.suffix[1:] if f.suffix != ".md" else "markdown"
                    code_samples.append(f"### {f.name}\n\n```{lang}\n{f.read_text()}\n```")
    if code_samples: sections["Code Samples"] = "\n\n".join(code_samples[:8])
    current_status, last_activity_date = "", None
    state_md = planning_dir / "STATE.md"
    if state_md.exists():
        state_content = state_md.read_text()
        la_match = re.search(r"Last activity:\s*(.+)", state_content)
        if la_match:
            activity_text = la_match.group(1).strip()
            date_match = re.search(r"(\d{4}-\d{2}-\d{2})", activity_text)
            if date_match:
                try: last_activity_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
                except ValueError: pass
            current_status = activity_text
    status_detail = "Active"
    if last_activity_date:
        today = datetime.now()
        if today - last_activity_date <= timedelta(days=7): status_detail = "Recently Updated"
        else: status_detail = f"Last Active: {last_activity_date.strftime('%Y-%m-%d')}"
    roadmap_summary = []
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        ms_matches = re.finditer(r"^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$", roadmap_md.read_text(), re.MULTILINE)
        for match in ms_matches:
            roadmap_summary.append(f"**{clean_text(match.group(1))}** {clean_text(match.group(2))}")
            if len(roadmap_summary) >= 5: break
    return ProjectInfo(project_name, slug, project_path.name, project_path, cat, "active", status_detail, sections=sections, current_status=current_status, roadmap_summary=roadmap_summary, last_activity_date=last_activity_date, assets=assets, docs=docs)

def generate_detailed_page(project: ProjectInfo) -> str:
    if "Quick Facts" not in project.sections:
        project.sections["Quick Facts"] = f"| | |\n|---|---|\n| **Status** | {project.status_detail} |"
    eco_slug = ECOSYSTEM_MAP.get(project.slug, "projects")
    fm = f"---\nlayout: default\nsection: {eco_slug}\n---\n\n"
    header = f"# {project.name}\n\n<span class=\"status-badge status-active\">{project.status_detail}</span>\n\n{get_back_links(project.category)}\n\n---\n\n"
    
    # Process assets fresh
    if project.assets:
        img_lines = []
        for asset in project.assets:
            dest = Path("images") / asset.name
            try: shutil.copy2(asset, dest)
            except: pass
            img_lines.append(f"![{asset.stem}](/images/{asset.name})")
        project.sections["Visuals"] = "\n\n".join(img_lines[:5])
    
    if project.docs:
        doc_lines = []
        doc_dir = Path("assets/docs")
        doc_dir.mkdir(parents=True, exist_ok=True)
        for doc in project.docs:
            dest_name = f"{project.slug}-{doc.name}"
            try: shutil.copy2(doc, doc_dir / dest_name)
            except: pass
            doc_lines.append(f"- [Download Technical Report: {doc.name}](/assets/docs/{dest_name})")
        project.sections["Technical Reports"] = "\n".join(doc_lines)
    
    # Load existing page to preserve stable sections
    dest_path = Path("projects") / f"{project.slug}.md"
    if dest_path.exists():
        existing_sections = extract_sections(dest_path.read_text())
        for sec in STABLE_SECTIONS:
            if sec in existing_sections and sec not in ALWAYS_UPDATE_SECTIONS:
                project.sections[sec] = existing_sections[sec]

    body_list, processed_sections = [], set()
    for s in ["Concept", "The Insight", "Overview"]:
        if s in project.sections:
            body_list.append(f"## Concept\n\n{clean_text(project.sections[s])}")
            processed_sections.add(s)
            break
    for s in DETAILED_SECTIONS:
        if s in project.sections and s not in processed_sections:
            body_list.append(f"## {s}\n\n{clean_text(project.sections[s])}")
            processed_sections.add(s)
    for s, content in project.sections.items():
        if s not in processed_sections and s not in ["Current Status", "Roadmap", "Contents"]:
            body_list.append(f"## {s}\n\n{clean_text(content)}")
    if project.current_status: body_list.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary: body_list.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
    final_body = "\n\n---\n\n".join(body_list)
    return fm + header + generate_toc(final_body) + final_body + f"\n\n---\n\n{get_back_links(project.category)}\n"

def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = ["---", "layout: default", "---", "", "# Projects", "", "Focused on network engineering, autonomous systems, and signal processing.", "", "---", ""]
    sorted_projs = sorted(projects, key=lambda p: (list(CATEGORY_MAP.keys()).index(p.category), p.name))
    categorized = {k: [] for k in CATEGORY_MAP.keys()}
    for p in sorted_projs: categorized[p.category].append(p)
    for cat_key, (title, desc, link) in CATEGORY_MAP.items():
        projs = categorized[cat_key]
        if not projs: continue
        lines.append(f"## {title}\n")
        for p in projs:
            summary = ""
            for k in ["Concept", "The Insight", "Overview", "What This Is"]:
                if k in p.sections:
                    summary = " ".join(re.split(r"(?<=[.!?])\s+", clean_text(re.sub(r"!\[.*?\]\(.*?\)", "", p.sections[k])))[:3])
                    if summary: break
            lines.append(f"### [{p.name}](projects/{p.slug})\n\n{summary}\n\n")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-dirs", nargs="+", default=["~/dev"])
    args = parser.parse_args()
    scan_paths = [Path(d).expanduser() for d in args.scan_dirs]
    existing = [p for p in scan_paths if p.exists()]
    if not existing: raise SystemExit("No --scan-dirs paths exist.")
    projects = []
    for p in existing:
        for pd in sorted(p.iterdir()):
            if pd.is_dir() and not pd.name.startswith("."):
                info = parse_project_metadata(pd)
                if info: projects.append(info)
    projects_dir = Path("projects")
    projects_dir.mkdir(exist_ok=True)
    for p in projects: (projects_dir / f"{p.slug}.md").write_text(generate_detailed_page(p))
    Path("projects.md").write_text(generate_projects_index(projects))
    print("Sync complete.")

if __name__ == "__main__": main()

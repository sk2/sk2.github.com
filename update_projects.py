#!/usr/bin/env python3
"""
Update website projects page and individual project pages from project metadata.
Automated collection of PDFs, images, and code snippets.
Includes richer cards, hero image extraction, global recent activity, and cross-linking.
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
    hero_asset: Optional[Path] = None

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
    "ank-nte": "Network Topology Engine",
    "ank-workbench": "Network Automation Workbench",
    "autonetkit-foundation": "Network Modeling Foundations",
    "autonetkit": "Configuration Generation (AutoNetkit)",
    "netvis": "Network Visualization Engine",
    "passive": "Signal Reflection Analysis",
    "signals": "Spectrum Analysis",
    "configparsing": "Brownfield Ingestion",
    "soundarray": "Sound Array",
}

CANONICAL_SLUG = {
    "network-simulator": "netsim",
    "ank-netcfg": "ank-netcfg",
}

PROJECT_CONTENT_OVERRIDES = {
    "netsim": {
        "Concept": "Deterministic tick-based network protocol simulator validating configurations before production deployment. It provides protocol-level fidelity with same-topology-same-results guarantees, allowing engineers to verify control-plane behavior without the overhead of full VM emulation.\n\nUnlike packet-level simulators that focus on bit-level accuracy, this engine focuses on **protocol convergence and state validation**. It mirrors the behavior of real router operating systems, including the separation of RIB and FIB, allowing for the empirical testing of complex routing policies and failure scenarios.",
        "Visuals": "### Basic Validation\n![Simulator Demo](/images/netsim-basic-demo.gif)\n\n### Interactive Daemon Mode\n![Daemon Demo](/images/netsim-daemon-demo.gif)\n\n### Enterprise Case Study\n![Enterprise Case Study](/images/netsim-case-study-enterprise.gif)\n",
    },
    "netvis": {
        "Visuals": "### Network Visualisation Examples\n\n![Geographic WAN](/images/geographic_wan.png)\n\n![Bundled Mesh](/images/bundled_mesh.png)\n\n![Hierarchical Datacenter](/images/hierarchical_datacenter.png)\n\n![Labels Dense](/images/labels_dense.png)\n\n![Force Directed Basic](/images/force_directed_basic.png)\n"
    },
    "ank-netcfg": {
        "Usage": "### DSL Transformation Example\n\n```yaml\n# DSL Transformation Rule\n# Applied when device_os matches 'nxos'\ntransformations:\n  - name: nxos_lowering\n    when: \"device_os == 'nxos'\"\n    rules:\n      - match: \"kind == 'interface' && name.startsWith('Ethernet')\"\n        apply:\n          name: \"name + '/1'\"\n          mtu: 9216  # Force jumbo frames\n```"
    },
    "topogen": {
        "Usage": "### Topology DSL Example\n\n```yaml\n# Example: Multi-layer POP underlay with mesh overlay\nname: multi-layer-pop-backbone\ntype: multi-layer\n\nlayers:\n  - name: physical\n    type: pop\n    count: 5\n    redundancy: n+1\n\n  - name: backbone\n    type: mesh\n    node_count: 4\n    underlay: physical\n    strategy: shortest-path\n```"
    },
    "signals": {
        "Visuals": "### Waterfall & TUI Interface\n\n![Spectra Waterfall](/images/spectra-waterfall-screenshot.png)\n\n### RF Fingerprinting Results\n\n![RF Fingerprinting](/images/rf_fingerprinting_results.png)\n\n### Vector Search (Top-K Matches)\n\n![Vector Search](/images/search_topk_example.png)\n"
    },
    "datavis": {
        "Visuals": "![GBIF global biodiversity density rendered by DataRaster](/images/datavis-gbif-3b.png)\n*The full GBIF release — 3.62 billion species-occurrence records — rendered as a single density layer with an equalized-histogram transfer and the inferno colormap. The Parquet release is read directly from S3, with no intermediate aggregation step.*\n\n![Global earthquake density rendered by DataRaster](/images/datavis-earthquakes.png)\n*Every recorded earthquake epicentre as a density map. Plate boundaries emerge from the raw point cloud with no point-by-point drawing.*\n\n![Flight-path density rendered by DataRaster](/images/datavis-flights.jpg)\n*Line rendering: hundreds of thousands of great-circle flight paths aggregated into a single density layer.*\n\n![Urban trip density rendered by DataRaster](/images/datavis-citibike.png)\n*Point density at city scale — bike-share trip endpoints across a metro area.*\n"
    },
    "matrix-time-series": {
        "Visuals": "![Electricity-demand signal with matrix-profile annotations](/images/matrix-annotated-profile.png)\n*Top: an electricity-demand signal with the discovered discord and matching motifs boxed. Bottom: the matrix profile — its lowest point locates the strongest motif, its highest point the clearest anomaly.*\n\n![Steam-generator signal with motif arcs](/images/matrix-motif-arc-fanout.png)\n*Motif arc fan-out: arcs connect each occurrence of a recurring shape across a steam-generator sensor trace, with the matrix profile below.*\n"
    },
}

CATEGORY_MAP = {
    "network": ("Network Engineering", "Tools for network design, simulation, and analysis.", "/network-automation"),
    "sdr": ("Radio Systems", "Radio signal analysis and spectrum monitoring.", "/signal-processing"),
    "health": ("Health & Biometrics", "Real-time biometric signal processing.", "/agentic-systems"),
    "astrophotography": ("Astrophotography", "Autonomous imaging and celestial monitoring.", None),
    "photography": ("Photography", "Automated camera control and monitoring.", None),
    "agents": ("Autonomous Systems", "Secure systems for agents and infrastructure automation.", "/agentic-systems"),
    "data": ("Data & Utilities", "Dense spatial rendering and time-series pattern discovery.", "/data-analytics"),
    "wellness": ("Wellness & Sound", "Sound analysis and wellness monitoring.", None),
    "experimental": ("Experimental", "Exploratory projects and technical experiments.", None),
}

DETAILED_SECTIONS = [
    "Concept", "Interactive Playground (WASM Mock Demo)", "Code Samples", "Visuals", "Usage",
    "Architecture", "Features", "Current Status", "Roadmap", "Quick Facts",
]

ALWAYS_UPDATE_SECTIONS = {"Code Samples", "Visuals", "Current Status", "Roadmap"}
STABLE_SECTIONS = {"Concept", "Interactive Playground (WASM Mock Demo)", "Architecture", "Features", "Quick Facts", "Usage"}

FM_SECTIONS = {"network": "network-automation", "sdr": "signal-processing", "agents": "agentic-systems", "health": "agentic-systems", "data": "data-analytics", "astrophotography": "photography", "photography": "photography", "wellness": "signal-processing", "experimental": "data-analytics"}

# Generate global slug list for cross-linking
ALL_SLUGS = set(list(CANONICAL_SLUG.values()) + list(CANONICAL_SLUG.keys()) + list(ECOSYSTEM_MAP.keys()))
SLUG_REGEX = re.compile(r'\b(' + '|'.join(re.escape(s) for s in ALL_SLUGS if len(s) > 3) + r')\b')

def linkify_text(text: str, current_slug: str) -> str:
    """Automatically convert mentions of other projects into internal links."""
    def replace_func(match):
        matched_slug = match.group(1)
        if matched_slug == current_slug or matched_slug == CANONICAL_SLUG.get(current_slug, current_slug):
            return matched_slug
        canonical = CANONICAL_SLUG.get(matched_slug, matched_slug)
        return f"[{matched_slug}](../{canonical})"
    
    parts = re.split(r'(\[[^\]]+\]\([^)]+\))', text)
    for i in range(0, len(parts), 2):
        parts[i] = SLUG_REGEX.sub(replace_func, parts[i])
    return "".join(parts)


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

def extract_description(sections: Dict[str, str], max_len: int = 160) -> str:
    """Extract a short meta description from the Concept/Overview section."""
    for key in ["Concept", "The Insight", "Overview"]:
        if key in sections:
            text = clean_text(sections[key])
            text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # strip images
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links to text
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # bold to plain
            text = re.sub(r"\*([^*]+)\*", r"\1", text)  # italic to plain
            text = re.sub(r"\s+", " ", text).strip()
            sentences = re.split(r"(?<=[.!?])\s+", text)
            desc = sentences[0] if sentences else ""
            if len(desc) < 60 and len(sentences) > 1:
                desc = " ".join(sentences[:2])
            if len(desc) > max_len:
                desc = desc[:max_len - 1].rsplit(" ", 1)[0] + "\u2026"
            # Escape characters that break YAML
            desc = desc.replace('"', "'")
            return desc
    return ""

TOC_SECTIONS = {
    "Concept", "Simulation Output", "Interactive Playground (WASM Mock Demo)",
    "Technical Reports", "Code Samples", "Visuals", "Usage",
    "Architecture", "Features", "Current Status", "Roadmap",
}

def generate_toc(content: str) -> str:
    headers = re.findall(r"^##\s+([^#\n]+)\s*$", content, re.MULTILINE)
    seen, unique = set(), []
    for h in headers:
        h = h.strip()
        if h in TOC_SECTIONS and h not in seen:
            unique.append(h)
            seen.add(h)
    headers = unique
    if len(headers) < 3: return ""
    links = [f"- [{h}](#{re.sub(r'-+', '-', re.sub(r'[^a-z0-9-]', '', h.lower().replace(' ', '-')))})" for h in headers]
    return "## Contents\n\n" + "\n".join(links) + "\n\n"

_papers_manifest_cache: Optional[Dict[str, str]] = None

def _get_papers_manifest_ids(papers_dir: Path) -> Dict[str, str]:
    """Return {manifest_id: resolved_project_path} from papers manifest."""
    global _papers_manifest_cache
    if _papers_manifest_cache is not None:
        return _papers_manifest_cache
    _papers_manifest_cache = {}
    manifest = papers_dir / "scripts" / "papers_manifest.yaml"
    if not manifest.exists():
        return _papers_manifest_cache
    import yaml
    with open(manifest) as f:
        data = yaml.safe_load(f)
    for proj in data.get("projects", []):
        mid = proj["id"]
        # Resolve the path relative to papers_dir
        doc_path = (papers_dir / proj["path"]).resolve()
        # Walk up to find the project root (first dir under ~/dev)
        project_root = doc_path
        while project_root.parent != papers_dir.parent and project_root.parent != project_root:
            project_root = project_root.parent
        _papers_manifest_cache[mid] = str(project_root)
    return _papers_manifest_cache


def parse_project_metadata(project_path: Path) -> Optional[ProjectInfo]:
    planning_dir = project_path / ".planning"
    if not planning_dir.exists(): return None
    project_md = planning_dir / "PROJECT.md"
    if not project_md.exists(): return None
    content = project_md.read_text()
    name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    project_name = name_match.group(1).strip() if name_match else project_path.name
    project_name = re.sub(r"^(?:PROJECT:\s*|Project:\s*)", "", project_name)
    slug = project_path.name.lower().replace("_", "-").replace(" ", "-")
    slug_mappings = {"multi-agent-assistant": "multi-agent", "passive": "rf-signal-analysis", "wifi-radar": "wifi-signal-analysis", "ank_pydantic": "ank-pydantic", "ank_nte": "ank-nte", "ank_workbench": "ank-workbench", "network-simulator": "netsim", "ank_netcfg": "ank-netcfg"}
    slug = slug_mappings.get(slug, slug)
    slug = CANONICAL_SLUG.get(slug, slug)
    if slug in PROJECT_ALIASES: project_name = PROJECT_ALIASES[slug]
    sections = extract_sections(content)
    for s_key in [slug]:
        if s_key in PROJECT_CONTENT_OVERRIDES:
            for sec, body in PROJECT_CONTENT_OVERRIDES[s_key].items(): sections[sec] = body
    cat = "experimental"
    s = slug.lower()
    if any(x in s for x in ["photo-tour", "import-asiair"]): cat = "photography"
    elif any(x in s for x in ["watchnoise", "watch-noise", "psytrance"]): cat = "wellness"
    elif any(x in s for x in ["healthypi", "hrv"]): cat = "health"
    elif any(x in s for x in ["spectra", "rtltcp", "wifi-signal-analysis", "signals", "rf-signal-analysis", "soundarray"]): cat = "sdr"
    elif any(x in s for x in ["astro", "aurora", "eclipse", "satellites"]): cat = "astrophotography"
    elif any(x in s for x in ["agent", "multi-agent", "cycle"]): cat = "agents"
    elif any(x in s for x in ["netvis", "ank", "topogen", "netsim", "autonetkit", "network", "configparsing", "nte", "orchestrator", "automationarch", "netflowsim", "netassure", "cliscrape", "deviceinteraction"]): cat = "network"
    elif any(x in s for x in ["polars", "tileserver", "matrix-time-series", "datavis", "data-raster", "weather", "omnifocus-db", "nascleanup", "devmon"]): cat = "data"
    
    stack = []
    if (project_path / "Cargo.toml").exists(): stack.append("Rust")
    if (project_path / "pyproject.toml").exists() or (project_path / "requirements.txt").exists(): stack.append("Python")
    if "React" in content or "TypeScript" in content: stack.append("TypeScript")
    if "Polars" in content: stack.append("Polars")
    
    assets, docs = [], []
    hero_asset = None
    docs_dir = project_path / "docs"
    if docs_dir.exists():
        for pdf in docs_dir.rglob("*.pdf"):
            if any(x in pdf.name for x in ["techreport.pdf", "paper.pdf", "usermanual.pdf"]) or pdf.parent.name in ["techreport", "paper", "usermanual"]: docs.append(pdf)
    # Also check centralised papers/out/ directory for pre-built PDFs.
    # Only pick up files whose name exactly matches "{manifest_id}-{doctype}.pdf".
    papers_out = project_path.parent / "papers" / "out"
    if papers_out.exists() and not docs:
        manifest_ids = _get_papers_manifest_ids(papers_out.parent)
        project_ids = {mid for mid, mpath in manifest_ids.items()
                       if Path(mpath).resolve().is_relative_to(project_path.resolve())}
        for mid in project_ids:
            for pdf in papers_out.glob(f"{mid}-*.pdf"):
                if "-docs-" in pdf.name or "-doc-" in pdf.name: continue
                if pdf not in docs:
                    docs.append(pdf)
    for ext in ["*.png", "*.svg", "*.gif"]:
        for img in project_path.rglob(ext):
            if any(x in str(img) for x in ["node_modules", ".venv", ".pytest_cache", "target", "implementations"]): continue
            if re.match(r"^\d+[_\d]*\.", img.name): continue  # Skip numbered thesis figures
            if img.parent.name in ["figures", "images", "visuals"] or any(x in img.name for x in ["diagram", "example", "hero", "demo"]): 
                assets.append(img)
                if not hero_asset and ("hero" in img.name or "architecture" in img.name):
                    hero_asset = img
    
    if not hero_asset and assets:
        for a in assets:
            if "diagram" in a.name or "example" in a.name:
                hero_asset = a
                break
                
    code_samples = []
    # Search in examples/ and tests/python/ (for Query API)
    search_dirs = [project_path / "examples", project_path / "tests" / "python", project_path / "netcfg-core" / "tests"]
    for search_dir in search_dirs:
        if search_dir.exists():
            for f in sorted(search_dir.rglob("*")):
                if f.is_file() and f.suffix in [".yaml", ".py", ".md"] and f.stat().st_size < 15000:
                    lang = f.suffix[1:] if f.suffix != ".md" else "markdown"
                    if lang == "rs": lang = "rust"
                    if lang == "py": lang = "python"
                    code_samples.append(f"### {f.name}\n\n```{lang}\n{f.read_text()}\n```")
    if code_samples: sections["Code Samples"] = "\n\n".join(code_samples[:10])
    
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
        if today - last_activity_date <= timedelta(days=14): status_detail = "Recently Updated"
        else: status_detail = f"Last Active: {last_activity_date.strftime('%Y-%m-%d')}"
    roadmap_summary = []
    roadmap_md = planning_dir / "ROADMAP.md"
    if roadmap_md.exists():
        ms_matches = re.finditer(r"^- (?:◆|❍|[\w\s]+)\s+\*\*(.*?)\*\*(.*?)$", roadmap_md.read_text(), re.MULTILINE)
        for match in ms_matches:
            roadmap_summary.append(f"**{clean_text(match.group(1))}** {clean_text(match.group(2))}")
            if len(roadmap_summary) >= 5: break
            
    return ProjectInfo(project_name, slug, project_path.name, project_path, cat, "active", status_detail, stack=stack, sections=sections, current_status=current_status, roadmap_summary=roadmap_summary, last_activity_date=last_activity_date, assets=assets, docs=docs, hero_asset=hero_asset)

def generate_detailed_page(project: ProjectInfo) -> str:
    if "Quick Facts" not in project.sections:
        facts = [f"| **Status** | {project.status_detail} |"]
        if project.stack: facts.append(f"| **Stack** | {', '.join(project.stack)} |")
        project.sections["Quick Facts"] = "| | |\n|---|---|\n" + "\n".join(facts)
        
    section = FM_SECTIONS.get(project.category)
    fm_section = f"\nsection: {section}" if section else ""
    stack_html = " ".join([f'<span class="stack-badge">{s}</span>' for s in project.stack])
    header = f"# {project.name}\n\n<div class=\"badges-row\">\n  <span class=\"status-badge status-active\">{project.status_detail}</span>\n  {stack_html}\n</div>\n\n---\n\n"
    
    if project.assets:
        img_lines = []
        for asset in project.assets:
            dest = Path("images") / asset.name
            try: shutil.copy2(asset, dest)
            except: pass
            # Create prefixed copy for netsim gifs (project page references netsim-*.gif)
            if project.slug in ("netsim", "network-simulator") and asset.suffix == ".gif":
                prefixed = Path("images") / f"netsim-{asset.name}"
                try: shutil.copy2(asset, prefixed)
                except: pass
            if project.hero_asset and asset.name == project.hero_asset.name:
                continue
            img_lines.append(f"![{asset.stem}](/images/{asset.name})")
        
        if "Visuals" not in PROJECT_CONTENT_OVERRIDES.get(project.slug, {}):
            if img_lines: project.sections["Visuals"] = "\n\n".join(img_lines[:8])
            elif "Visuals" in project.sections: del project.sections["Visuals"]
    
    dest_path = Path("projects") / f"{project.slug}.md"
    existing_sections: Dict[str, str] = {}
    existing_extra_fm = ""
    if dest_path.exists():
        existing_text = dest_path.read_text()
        existing_sections = extract_sections(existing_text)
        for sec in STABLE_SECTIONS:
            if sec in existing_sections and sec not in ALWAYS_UPDATE_SECTIONS and sec not in PROJECT_CONTENT_OVERRIDES.get(project.slug, {}):
                project.sections[sec] = existing_sections[sec]
        fm_match = re.match(r"^---\n(.*?)\n---", existing_text, re.DOTALL)
        if fm_match:
            for line in fm_match.group(1).splitlines():
                if line.startswith(("sitemap:", "permalink:")):
                    existing_extra_fm += f"\n{line}"

    # Generate frontmatter after stable sections are merged so description
    # can draw from the preserved Concept text.
    desc = extract_description(project.sections)
    fm_desc = f"\ndescription: \"{desc}\"" if desc else ""
    fm = f"---\nlayout: default{fm_section}{fm_desc}{existing_extra_fm}\n---\n\n"

    # When a page already exists, only allow known sections or sections already
    # present on the page.  This prevents PROJECT.md extras from re-bloating
    # pages that were manually trimmed.
    allowed_sections = set(DETAILED_SECTIONS) | {"Current Status", "Roadmap", "Contents"}
    if existing_sections:
        allowed_sections |= set(existing_sections.keys())

    body_list, processed_sections = [], set()
    if project.hero_asset:
        body_list.append(f"![Hero Image](/images/{project.hero_asset.name})\n")

    for s in ["Concept", "The Insight", "Overview"]:
        if s in project.sections:
            body_list.append(f"## Concept\n\n{linkify_text(clean_text(project.sections[s]), project.slug)}")
            processed_sections.add(s)
            break

    for s in DETAILED_SECTIONS:
        if s in project.sections and s not in processed_sections:
            body_list.append(f"## {s}\n\n{linkify_text(clean_text(project.sections[s]), project.slug)}")
            processed_sections.add(s)

    for s, content in project.sections.items():
        if s not in processed_sections and s not in ["Current Status", "Roadmap", "Contents"] and s in allowed_sections:
            body_list.append(f"## {s}\n\n{linkify_text(clean_text(content), project.slug)}")
            
    if project.current_status: body_list.append(f"## Current Status\n\n{clean_text(project.current_status)}")
    if project.roadmap_summary: body_list.append("## Roadmap\n\n" + "\n".join([f"- {item}" for item in project.roadmap_summary]))
    
    final_body = "\n\n---\n\n".join(body_list)
    return fm + header + generate_toc(final_body) + final_body + "\n"

def generate_projects_index(projects: list[ProjectInfo]) -> str:
    lines = ["---", "layout: default", "title: Projects", "---", "", "# Projects", "", "Focused on network engineering, autonomous systems, and signal processing.", "", "---", ""]
    lines.append('<div class="search-container"><input type="text" id="projectSearch" placeholder="Search projects, stack, or descriptions..." onkeyup="filterProjects()"></div>\n')
    valid_dates = [p for p in projects if p.last_activity_date is not None]
    recent = sorted(valid_dates, key=lambda x: x.last_activity_date or datetime.min, reverse=True)[:5]
    if recent:
        lines.append("## Recent Activity\n")
        lines.append('<ul class="recent-activity-list">')
        for p in recent:
            status_text = clean_text(p.current_status).split("—")[-1].strip()
            date_str = p.last_activity_date.strftime("%Y-%m-%d") if p.last_activity_date else ""
            lines.append(f'<li><strong>{date_str}</strong>: <a href="projects/{p.slug}">{p.name}</a> — <em>{status_text}</em></li>')
        lines.append('</ul>\n\n---\n')
    sorted_projs = sorted(projects, key=lambda p: (list(CATEGORY_MAP.keys()).index(p.category), p.name))
    categorized = {k: [] for k in CATEGORY_MAP.keys()}
    for p in sorted_projs: categorized[p.category].append(p)
    for cat_key, (title, _desc, _link) in CATEGORY_MAP.items():
        projs = categorized[cat_key]
        if not projs: continue
        lines.append(f"## {title}\n")
        lines.append('<div class="project-grid">')
        for p in projs:
            summary = ""
            for k in ["Concept", "The Insight", "Overview", "What This Is"]:
                if k in p.sections:
                    summary = " ".join(re.split(r"(?<=[.!?])\s+", clean_text(re.sub(r"!\[.*?\]\(.*?\)", "", p.sections[k])))[:3])
                    if summary: break
            stack_html = "".join([f'<span class="stack-badge">{s}</span>' for s in p.stack])
            lines.append(f'<div class="project-card" data-search="{p.name.lower()} {summary.lower()} {" ".join(p.stack).lower()} {p.slug.lower()}">')
            lines.append(f'  <h3 class="card-title"><a href="projects/{p.slug}">{p.name}</a></h3>')
            lines.append(f'  <div class="badges-row card-badges"><span class="status-badge status-active">{p.status_detail}</span> {stack_html}</div>')
            if p.hero_asset: lines.append(f'  <img src="../images/{p.hero_asset.name}" class="project-thumbnail" alt="{p.name} diagram" />')
            lines.append(f'  <p class="card-description">{summary}</p>')
            lines.append('</div>\n')
        lines.append('</div>\n')
    lines.append("""
<!-- Styles in assets/css/main.css -->
<script>
function filterProjects() {
    var input, filter, cards, card, i, txtValue;
    input = document.getElementById('projectSearch');
    filter = input.value.toLowerCase();
    cards = document.getElementsByClassName('project-card');
    for (i = 0; i < cards.length; i++) {
        card = cards[i];
        txtValue = card.getAttribute('data-search');
        if (txtValue.indexOf(filter) > -1) { card.style.display = ""; } else { card.style.display = "none"; }
    }
}
</script>
    """)
    return "\n".join(lines)

REPORTS_CATEGORY_MAP = {
    "network": "Network Engineering",
    "sdr": "Radio Systems",
    "wellness": "Sound & Music",
    "astrophotography": "Astrophotography",
    "data": "Data & Utilities",
}

def generate_reports_page(projects: list[ProjectInfo]) -> str:
    """Generate reports.md from projects that have docs (excluding SKIP_DOCS)."""
    lines = [
        "---", "layout: default", "title: Technical Reports",
        'description: Downloadable technical reports, research papers, and user manuals for network automation, signal processing, and music generation projects.',
        "---", "",
        "# Technical Reports", "",
        "Detailed technical documentation for selected projects. Each report covers architecture, design decisions, and implementation details.",
        "", "---",
    ]

    SKIP_DOCS = {"automationarch"}
    categorized: Dict[str, list] = {}
    for p in projects:
        if p.slug in SKIP_DOCS or not p.docs:
            continue
        cat_label = REPORTS_CATEGORY_MAP.get(p.category)
        if not cat_label:
            continue
        categorized.setdefault(cat_label, []).append(p)

    # Scan assets/docs/ for all existing PDFs per project slug
    doc_dir = Path("assets/docs")
    for section_order in ["Network Engineering", "Radio Systems", "Sound & Music", "Astrophotography", "Data & Utilities"]:
        projs = categorized.get(section_order, [])
        if not projs:
            continue
        lines.append(f"\n## {section_order}\n")
        lines.append('<div class="project-grid">')
        for p in sorted(projs, key=lambda x: x.name):
            stack_html = "".join(f'<span class="stack-badge">{s}</span>' for s in p.stack)
            desc = extract_description(p.sections, 120)
            # Find all PDFs for this project in assets/docs/
            doc_links = []
            if doc_dir.exists():
                for pdf in sorted(doc_dir.glob(f"{p.slug}*")):
                    if "techreport" in pdf.name:
                        doc_links.append(f'      <a href="/assets/docs/{pdf.name}" class="doc-link">Tech Report</a>')
                    elif "paper" in pdf.name:
                        doc_links.append(f'      <a href="/assets/docs/{pdf.name}" class="doc-link">Paper</a>')
                    elif "usermanual" in pdf.name:
                        doc_links.append(f'      <a href="/assets/docs/{pdf.name}" class="doc-link">Manual</a>')
                    elif pdf.suffix == ".pdf":
                        doc_links.append(f'      <a href="/assets/docs/{pdf.name}" class="doc-link">Tech Report</a>')
            if not doc_links:
                continue
            lines.append(f'  <div class="project-card">')
            lines.append(f'    <h3 class="card-title"><a href="/projects/{p.slug}">{p.name}</a></h3>')
            lines.append(f'    <div class="badges-row card-badges">{stack_html}</div>')
            lines.append(f'    <p class="card-description">{desc}</p>')
            lines.append(f'    <div class="doc-links">')
            lines.extend(doc_links)
            lines.append(f'    </div>')
            lines.append(f'  </div>\n')
        lines.append('</div>\n')
        lines.append('---')

    # Master index: flat list of all reports with direct download links
    all_reports: list[tuple[str, str, str]] = []  # (project_name, label, pdf_path)
    for cat_label in ["Network Engineering", "Radio Systems", "Sound & Music", "Astrophotography", "Data & Utilities"]:
        for p in sorted(categorized.get(cat_label, []), key=lambda x: x.name):
            if doc_dir.exists():
                for pdf in sorted(doc_dir.glob(f"{p.slug}*")):
                    if "techreport" in pdf.name:
                        all_reports.append((p.name, "Tech Report", pdf.name))
                    elif "paper" in pdf.name:
                        all_reports.append((p.name, "Paper", pdf.name))
                    elif "usermanual" in pdf.name:
                        all_reports.append((p.name, "Manual", pdf.name))
                    elif pdf.suffix == ".pdf":
                        all_reports.append((p.name, "Tech Report", pdf.name))

    if all_reports:
        lines.append("\n## All Reports\n")
        lines.append("| Project | Document | Download |")
        lines.append("|---------|----------|----------|")
        for name, label, pdf_name in all_reports:
            lines.append(f"| {name} | {label} | [PDF](/assets/docs/{pdf_name}) |")
        lines.append("")

    lines.append("\n[← Back to Projects](projects)")
    return "\n".join(lines)

IGNORE_DIR_PATTERNS = ("_corrupted", "-corrupted", "_nmb1", "-nmb1", ".broken", ".bak", ".old")
HIDDEN_FROM_LISTINGS = {"multi-agent"}

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
            if not pd.is_dir() or pd.name.startswith("."):
                continue
            if any(pat in pd.name for pat in IGNORE_DIR_PATTERNS):
                continue
            info = parse_project_metadata(pd)
            if info: projects.append(info)
    projects_dir = Path("projects")
    projects_dir.mkdir(exist_ok=True)
    for p in projects: (projects_dir / f"{p.slug}.md").write_text(generate_detailed_page(p))
    listed = [p for p in projects if p.slug not in HIDDEN_FROM_LISTINGS]
    Path("projects.md").write_text(generate_projects_index(listed))
    print(f"Sync complete. {len(projects)} pages generated, {len(listed)} listed.")

if __name__ == "__main__": main()

# Website

This repository is the source for `sk2.github.com` / `sk2.id.au`, built with Jekyll.

## Build & Deploy

1. **Local Build:**
   - Ensure Ruby 3.0+ is installed.
   - Install dependencies: `./script/bootstrap`
   - Build the site: `./script/cibuild`
2. **Deploy:** Push changes to the `master` branch to deploy to GitHub Pages.

## Maintenance Protocol

The project pages are synchronized from local development directories using `update_projects.py`. To maintain professional quality and prevent content regression, follow this "Source of Truth" protocol:

1.  **Metadata is Master:** Primary project descriptions are pulled from `.planning/PROJECT.md` in each project's folder.
2.  **Golden Master Overrides:** High-value technical content (Architecture, Impact, Research Foundations) for key projects is hardcoded in the `PROJECT_CONTENT_OVERRIDES` dictionary within `update_projects.py`. This ensures critical detail is never lost during a sync.
3.  **Clean Room Generation:** The sync script completely rebuilds project pages from scratch. **Never manually edit files in the `projects/` directory**, as they are overwritten on every sync.
4.  **Activity-Based Status:** Project statuses are automatically derived from the `Last activity` date in each project's `STATE.md`.
    - `Recently Updated`: Work within the last 7 days.
    - `Last Active: [Date]`: For older work.
    - No internal metrics (Phases, Percentages) are shown on the public site.

### Workflow Gap (Important)

The current workflow has a known failure mode: rich, manually written project pages in `projects/` can be clobbered by a regeneration run.

What we want instead is two-track content management:

- **Stable content (canonical narrative):** Concept, architecture, technical depth, screenshots/diagrams.
- **Fresh content (incremental updates):** recent milestone notes, phase/plan references, notable changes since the last release.

This repo does not yet have a reliable, well-documented source-of-truth location for the stable content. Before running bulk regeneration, confirm where the authoritative project documents live (e.g., per-project `.planning/PROJECT.md`) and ensure the sync script is sourcing from them.

Action item (not tonight): define and document a workflow that preserves stable content while appending incremental updates, without rewrites or large-scale content loss.

### Current Working Convention (Temporary)

Until a better workflow exists, treat `/Users/simonknight/dev` as the canonical project root on this machine:

- Stable content lives in each project at `.planning/PROJECT.md`
- Recency/status lives in `.planning/STATE.md` ("Last activity")
- The website is regenerated from those sources via `python3 update_projects.py --scan-dirs /Users/simonknight/dev`

If the scan dirs are missing, do not run regeneration: it will collapse long-form pages into stubs.

### Simulator Page Notes

The Network Simulator page is generated from `/Users/simonknight/dev/network-simulator/.planning/PROJECT.md`.

If you want the public page to demonstrate real usage, put runnable examples directly into the upstream doc using fenced code blocks (```yaml, ```bash, ```python). The site layout will collapse/expand long blocks automatically.

Important: do not edit `sk2.github.com/projects/netsim.md` by hand. It is generated.

### Common Failure Modes

- Running `update_projects.py` without the correct `--scan-dirs` available regenerates stubs and overwrites rich pages.
- Editing files under `projects/` works briefly and then gets wiped on the next regen.
- If a project section isn't showing up, ensure the upstream doc uses a level-2 heading (`## Section Name`) and that the generator includes it in `DETAILED_SECTIONS`.

## Design & Writing Philosophy

### Tone: Understated, Confident, Technical
- **Engineer-to-Peer:** Write as an engineer explaining work to a peer. Avoid superlatives, marketing filler ("cutting-edge", "blazing-fast"), and exclamation marks.
- **Show, Don't Tell:** Use specific outcomes and architectural details instead of adjectives.
- **Product First:** Focus on the utility and problem-solving aspect of the project before diving into technical implementation.

### Content Structure
- **Concept-Led:** Every project leads with a **Concept** section that merges the vision, problem, and core value into a single narrative.
- **Progressive Disclosure:**
  - Main Index: Concise 2-3 sentence summaries.
  - Ecosystem Pages: Narrative flow showing how the tools work together as a toolchain.
  - Project Pages: Deep technical detail, screenshots, and architecture.
- **Automated Navigation:**
  - **Contents Index:** Automatically generated for pages with 4+ sections.
  - **Contextual Back-links:** Projects automatically link back to their specific ecosystem (e.g., "Back to Network Automation").

### Layout Features
- **Integrated Code Expansion:** The layout automatically manages long code blocks (>15 lines) with a "Show More" toggle.
- **Diagram Detection:** ASCII diagrams (using `┌`, `│`, `─`) are automatically detected and shown in full, bypassing the expansion logic.
- **Standardized Titles:** Project names are automatically standardized across the site (e.g., `netsim` → **Network Simulator**).

## Writing Style

All prose follows **The Elements of Style** (Strunk and White).
- Omit needless words.
- Use the active voice.
- Prefer the specific to the general.
- Avoid loose sentences.

## Analytics

The site uses **Plausible Analytics** for privacy-friendly, GDPR-compliant tracking.
- Domain: `sk2.id.au`
- Configured in `_layouts/default.html`

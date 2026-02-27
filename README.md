# Website

This repository is the source for `sk2.github.com` / `sk2.id.au`, built with Jekyll.

## Build & Deploy

1. **Local Build:**
   - Ensure Ruby 3.0+ is installed.
   - Install dependencies: `./script/bootstrap`
   - Build the site: `./script/cibuild`
2. **Deploy:** Push changes to the `master` branch to deploy to GitHub Pages.

## Maintenance Protocol

The project pages are synchronized from local development directories using `update_projects.py`. To maintain professional quality and prevent content regression, the site uses a **Two-Track** content management model:

1.  **Stable Content (Polished Narrative):** Canonical technical detail—Concept, Architecture, Tech Stack, Visuals—lives directly in the `projects/*.md` files within this repo. Once you polish these sections, `update_projects.py` will preserve them during subsequent syncs.
2.  **Fresh Content (Automated Sync):** Current activity, milestones, and status are automatically pulled from external `.planning/STATE.md` and `ROADMAP.md` in each project's folder (using the `--scan-dirs` flag).
3.  **Golden Master Overrides:** Critical technical content can also be hardcoded in the `PROJECT_CONTENT_OVERRIDES` dictionary within `update_projects.py` for absolute persistence across all environments.

### Maintenance Workflow

- **To Improve Content:** Edit the markdown files directly in `projects/*.md`. Use the "Stable" section headers (e.g., `## Concept`, `## Architecture`) to ensure your changes are preserved.
- **To Update Status:** Run `python3 update_projects.py --scan-dirs ~/dev`. This will sync the "Fresh" sections (Roadmap, Current Status) and the status badge while leaving your polished "Stable" sections intact.
- **Cleanup:** Running the sync script automatically fixes common formatting issues, duplicates, and ensures consistent navigation links across the site.

### Workflow Improvements

The previous "Clean Room Generation" model (which clobbered manual edits) has been replaced with a **Synchronization & Merge** model. 

- **Protected Sections:** If a section header is in the `STABLE_SECTIONS` list (see `update_projects.py`), the script will prioritize the local `projects/*.md` version over the external `.planning/PROJECT.md`.
- **Duplicate Prevention:** The script now automatically detects and strips duplicate footers and horizontal rules that were previously a source of "page churn".
- **Auto-Quick Facts:** If a `## Quick Facts` section is missing, the script will generate a basic one from metadata, which you can then manually polish.

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

# Website

This repository is the source for `sk2.github.com` / `sk2.id.au`, built with Jekyll.

## Build & Deploy

1. **Local Build:**
   - Ensure Ruby 3.0+ is installed.
   - Install dependencies: `./script/bootstrap`
   - Build the site: `./script/cibuild`
2. **Deploy:** Push changes to the `master` branch to deploy to GitHub Pages.

## Maintenance Protocol

The project pages are synchronized from local development directories using `update_projects.py`. To maintain professional quality and prevent content regression, the site uses a **Synchronization & Merge** content management model.

### Automated Asset Collection

The script automatically scans the project directories (provided via `--scan-dirs`) for high-value assets:

1.  **Technical Reports:** Scans `docs/` for `paper.pdf` or `techreport.pdf`. These are copied to `assets/docs/` and linked in a `## Technical Reports` section.
2.  **Visuals:** Scans for images (`.png`, `.svg`) in `figures/`, `images/`, or `visuals/` folders, or files with `diagram`, `example`, or `hero` in the name. These are copied to `images/` and included in a `## Visuals` section.
3.  **Code Samples:** Scans `examples/` and `tests/python/` for `.yaml`, `.py`, `.rs`, and `.md` files. High-signal snippets are included in a `## Code Samples` section.

### Two-Track Content Model

1.  **Stable Content (Polished Narrative):** Canonical technical detail—Concept, Architecture, Tech Stack—lives directly in the `projects/*.md` files within this repo. Once you polish these sections, `update_projects.py` will preserve them during subsequent syncs.
2.  **Fresh Content (Automated Sync):** Current activity, milestones, status, and assets (Reports, Code, Visuals) are automatically pulled from external project folders.

### Maintenance Workflow

- **To Improve Content:** Edit the markdown files directly in `projects/*.md`. Use the "Stable" section headers (e.g., `## Concept`, `## Architecture`) to ensure your changes are preserved.
- **To Update Status & Assets:** Run `python3 update_projects.py --scan-dirs ~/dev`. This will sync the "Fresh" sections (Roadmap, Current Status, Technical Reports, Code Samples, Visuals) and the status badge while leaving your polished "Stable" sections intact.
- **Cleanup:** Running the sync script automatically fixes common formatting issues, duplicates, and ensures consistent navigation links across the site.

### Workflow Improvements

- **Protected Sections:** Sections in `STABLE_SECTIONS` are prioritized from the local repo.
- **Always Updated:** Sections in `ALWAYS_UPDATE_SECTIONS` (Reports, Code, Visuals) are always pulled fresh from the source projects.
- **Duplicate Prevention:** The script automatically detects and strips duplicate content.
- **Auto-Quick Facts:** Generates a basic `## Quick Facts` section if missing.

## Design & Writing Philosophy

### Tone: Understated, Confident, Technical
- **Engineer-to-Peer:** Write as an engineer explaining work to a peer. Avoid superlatives, marketing filler ("cutting-edge", "blazing-fast"), and exclamation marks.
- **Show, Don't Tell:** Use specific outcomes and architectural details instead of adjectives.
- **Product First:** Focus on the utility and problem-solving aspect of the project before diving into technical implementation.

### Content Structure
- **Concept-Led:** Every project leads with a **Concept** section that merges the vision, problem, and core value into a single narrative.
- **Progressive Disclosure:**
  - Main Index: Concise 2-3 sentence summaries.
  - Project Pages: Deep technical detail, code samples, and technical reports.
- **Automated Navigation:**
  - **Contents Index:** Automatically generated for pages with 4+ sections.
  - **Contextual Back-links:** Projects automatically link back to their specific ecosystem.

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

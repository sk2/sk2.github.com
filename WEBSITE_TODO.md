# Website TODO

Tracked improvements for flow, readability, navigation, and polish. Items marked [DONE] have been completed.

---

## Navigation & Structure

### 1. Nav/category alignment [DONE]
Nav dropdown now has 5 categories matching sections in projects.md.

### 2. Category landing page consistency [DONE]
All 5 category pages now have consistent structure: pipeline diagrams, per-tool descriptions with badges, and cross-category footer links.
- `network-automation.md`: Core Platform cards + Supporting Tools list
- `data-analytics.md`: Pipeline diagram + tool descriptions with code examples
- `photography.md`: Pipeline diagram + per-tool descriptions
- `signal-processing.md`: Pipeline diagram + per-tool descriptions with badges
- `agentic-systems.md`: Architecture diagram + system descriptions

### 3. ecosystem.md vs. network-automation.md redundancy [DONE]
Redirected ecosystem.md to network-automation.md.

---

## Content & Readability

### 4. Homepage "Featured Work" visual hierarchy [DONE]
Project cards showing the four core Rust engines (NTE, Netsim, netcfg, NetVis) with descriptions matching network-automation.md.

### 5. Empty project cards [DONE]
Populated all blank card descriptions in projects.md.

### 6. Category landing pages: Rust code and hardcoded styles [DONE]
Removed hardcoded `<style>` blocks from data-analytics.md and photography.md. Replaced Rust code block in data-analytics.md with Python example and link to project page.

### 9. Project page bloat [DONE]
All project pages trimmed to ~100-250 lines. Removed concatenated internal docs (README dumps, decision tables, constraint lists, phase checklists, full YAML topology dumps, Requirements/Constraints/Key Decisions sections, duplicate "What This Is"/"Core Value" sections).

Pages trimmed:
- `netsim.md`: 1332 → ~250 lines
- `ank-pydantic.md`: 2044 → ~150 lines
- `ank-nte.md`: 1404 → ~130 lines
- `ank-netcfg.md`: 1509 → ~140 lines
- `topogen.md`: 626 → ~110 lines
- `ank-workbench.md`: 521 → ~120 lines (wired up 4 screenshots)
- `deviceinteraction.md`: 297 → ~120 lines
- `configparsing.md`: 165 → ~65 lines
- `netvis.md`: 803 → ~160 lines (done earlier)

---

## UX & Interaction

### 7. No "back to top" on long project pages
**Action:** Add a floating "back to top" button (CSS + minimal JS in default.html) that appears after scrolling past the first screen.

### 8. Breadcrumb navigation duplication
Project pages have hardcoded `[← Back to ...]` links AND the layout-based breadcrumb system.

**Action:** Standardize on the layout breadcrumb. Set `section:` in each project page's front matter, then remove inline `← Back to` links from content.

---

## Visual Content

### Network Engineering
- [x] Network Simulator: 11 GIF demos
- [x] Visualization Engine: 9 PNG/SVG gallery images
- [x] Network Automation Workbench: 4 web UI screenshots (projects, editor, workflow, visualize)
- [ ] Topology Generator: CLI usage examples, generated topology visualizations

### Signal Processing
- [x] Spectrum Analysis: waterfall visualization (spectra-waterfall.png referenced in signal-processing.md)
- [ ] HealthyPi: signal plots (ECG, PPG), HRV analysis output

### Astrophotography
- [ ] OpenAstro Node: TUI screenshot, web UI mockup
- [ ] EclipseStack: alignment visualization

### Autonomous Systems
- [ ] Multi-Agent Assistant: architecture diagram, NATS message flow
- [ ] Cycle Agent: UI mockup, KICKR Core integration diagram

---

## Update Script

- [ ] Update `update_projects.py` to set `section:` front matter based on category
- [ ] Remove inline back-link generation from script (breadcrumbs handled by layout)
- [ ] Ensure `update_projects.py` category taxonomy matches new 5-category structure
- [ ] Prevent script from re-bloating trimmed pages (preserve stable sections)

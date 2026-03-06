# Website TODO

Tracked improvements for flow, readability, navigation, and polish. Items marked [DONE] have been completed.

---

## Navigation & Structure

### 1. Nav/category alignment [DONE]
Nav dropdown now has 5 categories (Network Automation, Signal Processing, Photography, Data & Analytics, Autonomous Systems) matching the sections in projects.md. Removed the separate "Architecture" nav item.

### 2. Category landing page consistency
Category landing pages vary in depth:
- `network-automation.md`: thorough (pipeline diagram, categorized tools) [DONE - rewritten]
- `data-analytics.md`: thorough (pipeline diagram, code examples) — still has hardcoded `<style>` and Rust code
- `photography.md`: thorough (pipeline diagram, per-tool descriptions) — still has hardcoded `<style>`
- `signal-processing.md`: thin (one-line descriptions, no pipeline or code)
- `agentic-systems.md`: thin (three short paragraphs, two links)

**Action:** Flesh out thin pages or fold into projects page. Remove hardcoded `<style>` blocks from data-analytics.md and photography.md.

### 3. ecosystem.md vs. network-automation.md redundancy [DONE]
Redirected ecosystem.md to network-automation.md. Updated homepage link. Removed "Architecture" nav item.

---

## Content & Readability

### 4. Homepage "Featured Work" visual hierarchy [DONE]
Replaced bullet list with project cards using the card grid system.

### 5. Empty project cards [DONE]
Populated all blank card descriptions in projects.md.

### 6. Category landing pages: Rust code and hardcoded styles
Remaining work:
- `data-analytics.md`: Rust code block (matrix-profile-rs example) and hardcoded `<style>` with `#007bff`, `#28a745`, `#ffc107`
- `photography.md`: hardcoded `<style>` with non-theme-aware badge colors

**Action:** Replace Rust code with YAML/CLI examples or project page links. Replace `<style>` blocks with theme-aware CSS classes.

### 9. Project page bloat [DONE for netsim, netvis]
Several project pages were 800-1800 lines of concatenated internal docs (decision tables, constraint lists, phase checklists, full YAML topology dumps). Rewrote:
- `netsim.md`: 1849 lines → ~200 lines. Clean TOC (8 items), 11 GIF demos, protocol list, simulation output, concise status.
- `netvis.md`: 803 lines → ~160 lines. Gallery with 9 visualization PNGs/SVGs, layout algorithm list, feature summary.

**Remaining project pages to audit for similar bloat:**
- [ ] `ank-pydantic.md`
- [ ] `ank-workbench.md`
- [ ] `ank-nte.md`
- [ ] `ank-netcfg.md`
- [ ] `topogen.md`
- [ ] `deviceinteraction.md`
- [ ] `configparsing.md`

---

## UX & Interaction

### 7. No "back to top" on long project pages
**Action:** Add a floating "back to top" button (CSS + minimal JS in default.html) that appears after scrolling past the first screen.

### 8. Breadcrumb navigation duplication
Project pages have hardcoded `[← Back to ...]` links AND the layout-based breadcrumb system. Some pages use both (double navigation), others use neither.

**Action:** Standardize on the layout breadcrumb. Set `section:` in each project page's front matter, then remove inline `← Back to` links from content.

---

## Visual Content

### Network Engineering
- [x] Network Simulator: 11 GIF demos (basic, daemon, TUI, enterprise, chaos, self-healing, L3VPN, SR, trace, scale, assertion)
- [x] Visualization Engine: 9 PNG/SVG gallery images (enterprise, datacenter, ISP, geographic, isometric, radial, theme, NOC, traffic)
- [ ] Network Automation Workbench: web UI screenshots (workbench-projects.png, workbench-editor.png etc. exist but not referenced)
- [ ] Topology Generator: CLI usage examples, generated topology visualizations

### Signal Processing
- [ ] Spectrum Analysis: waterfall visualization (spectra-waterfall.png exists but not referenced in signals.md)
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

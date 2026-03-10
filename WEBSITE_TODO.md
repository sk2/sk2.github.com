# Website TODO

Tracked improvements for flow, readability, navigation, and polish.

---

## Completed

- **Nav/category alignment**: 5-category dropdown matching projects.md sections
- **Category landing pages**: Consistent structure across all 5 pages (pipeline diagrams, badges, cross-category footers)
- **ecosystem.md redirect**: Meta-refresh redirect to /network-automation
- **Homepage featured work**: Four core Rust engine cards with descriptions
- **Project card descriptions**: All blank cards populated
- **Hardcoded styles removed**: No inline `<style>` blocks in content pages (moved to main.css)
- **Project page bloat**: All pages trimmed to ~100-250 lines
- **Breadcrumb duplication fixed**: Removed inline back-links from all 47 project pages; layout breadcrumb (via `section` front matter) is the single source
- **SEO foundations**: OG tags, favicon, canonical URLs, sitemap.xml, robots.txt, meta description priority fix
- **Template variable fix**: Corrected Eleventy data access (`title`/`section` instead of `page.title`/`page.section`)
- **404 page**: Custom page with site nav and links
- **Reports page**: Card-based listing of all tech reports, papers, and manuals
- **Photography voice**: Removed templated "What It Is:" headers

---

## Open

### UX

- [x] **Back to top button**: Floating button appears after scrolling past first viewport height

### Visual Content

**Network Engineering:**
- [ ] Topology Generator: CLI usage examples, generated topology visualizations

**Signal Processing:**
- [ ] HealthyPi: signal plots (ECG, PPG), HRV analysis output

**Astrophotography:**
- [ ] OpenAstro Node: TUI screenshot, web UI mockup
- [ ] EclipseStack: alignment visualization

**Autonomous Systems:**
- [ ] Multi-Agent Assistant: architecture diagram, NATS message flow
- [ ] Cycle Agent: UI mockup, KICKR Core integration diagram

### Update Script

- [x] Set `section:` front matter based on `FM_SECTIONS` category mapping
- [x] Remove `get_back_links()` function and all back-link generation
- [x] Add photography/astrophotography to `FM_SECTIONS` mapping
- [x] Prevent script from re-bloating trimmed pages (preserve stable sections)

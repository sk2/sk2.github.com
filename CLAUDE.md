# Claude Instructions for Website

## Voice & Tone

**Understated, confident, technical.** Write as an engineer explaining work to a peer. No marketing language, no superlatives, no hype. The work speaks for itself.

- Prefer specifics to adjectives. Instead of "high-performance", state the mechanism ("Rust-native graph engine") or the outcome ("126,000 lines of Rust, 1,350 tests"). Let the reader infer quality.
- Avoid these words/phrases: "high-performance", "cutting-edge", "state-of-the-art", "blazing-fast", "game-changing", "revolutionary", "radar", "passive radar". If something is fast, say why or show numbers.
- For RF reflection projects, use "signal reflection", "illumination reflection", or "bistatic geometry" — never "radar". The work is signal processing research, not surveillance.
- No exclamation marks in prose.
- Follow Strunk & White: omit needless words, use active voice, prefer the specific to the general.

## Project Naming

Use full product names in all prose text:

| Code Name | Full Product Name |
|-----------|------------------|
| `NetVis` | Network Visualization Engine |
| `ank_pydantic` | Network Modeling & Configuration Library |
| `netsim` | Network Simulator |
| `TopoGen` | Topology Generator |
| `NTE` | Network Topology Engine |
| `ANK Workbench` | Network Automation Workbench |
| `rtltcp-rust` | Multi-SDR Streaming Server |
| `psytrance` | Algorithmic Music Engine |
| `satellites` | Satellite Tracker |

Keep code names only in: Python imports, CLI commands, repository URLs, file paths, and code examples.

## Page Structure

- Use "Concept" as the opening section heading on project pages (not "The Insight", "The Idea", or "Overview").
- Avoid templated section headers like "What It Is", "Problem It Solves", "Why This Tool?". Use natural, specific headings or fold content into the introduction.
- Each project page has one footer: `[<- Back to Network Automation](../network-automation)` or equivalent.

## Upcoming Projects

None currently — all active projects have pages.

## Technical

- Jekyll site using the minimal theme with custom layout in `_layouts/default.html`
- CSS in `assets/css/main.css` with CSS custom properties for light/dark themes
- Navigation uses a dropdown for project categories under "Projects"
- Build: `./script/bootstrap && ./script/cibuild`
- Deploy: push to `master` branch (GitHub Pages)

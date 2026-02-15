# The Minimal theme

[![Build Status](https://travis-ci.org/pages-themes/minimal.svg?branch=master)](https://travis-ci.org/pages-themes/minimal) [![Gem Version](https://badge.fury.io/rb/jekyll-theme-minimal.svg)](https://badge.fury.io/rb/jekyll-theme-minimal)

*Minimal is a Jekyll theme for GitHub Pages. You can [preview the theme to see what it looks like](http://pages-themes.github.io/minimal), or even [use it today](#usage).*

![Thumbnail of minimal](thumbnail.png)

## Usage

To use the Minimal theme:

1. Add the following to your site's `_config.yml`:

    ```yml
    theme: jekyll-theme-minimal
    ```

2. Optionally, if you'd like to preview your site on your computer, add the following to your site's `Gemfile`:

    ```ruby
    gem "github-pages", group: :jekyll_plugins
    ```



## Customizing

### Configuration variables

Minimal will respect the following variables, if set in your site's `_config.yml`:

```yml
title: [The title of your site]
description: [A short description of your site's purpose]
```

Additionally, you may choose to set the following optional variables:

```yml
show_downloads: ["true" or "false" to indicate whether to provide a download URL]
google_analytics: [Your Google Analytics tracking ID]
```

### Stylesheet

If you'd like to add your own custom styles:

1. Create a file called `/assets/css/style.scss` in your site
2. Add the following content to the top of the file, exactly as shown:
    ```scss
    ---
    ---

    @import "{{ site.theme }}";
    ```
3. Add any custom CSS (or Sass, including imports) like immediately after the `@import` line

### Layouts

If you'd like to change the theme's HTML layout:

1. [Copy the original template](https://github.com/pages-themes/minimal/blob/master/_layouts/default.html) from the theme's repository<br />(*Pro-tip: click "raw" to make copying easier*)
2. Create a file called `/_layouts/default.html` in your site
3. Paste the default layout content copied in the first step
4. Customize the layout as you'd like

## Roadmap

See the [open issues](https://github.com/pages-themes/minimal/issues) for a list of proposed features (and known issues).

## Project philosophy

The Minimal theme is intended to make it quick and easy for GitHub Pages users to create their first (or 100th) website. The theme should meet the vast majority of users' needs out of the box, erring on the side of simplicity rather than flexibility, and provide users the opportunity to opt-in to additional complexity if they have specific needs or wish to further customize their experience (such as adding custom CSS or modifying the default layout). It should also look great, but that goes without saying.

## Contributing

Interested in contributing to Minimal? We'd love your help. Minimal is an open source project, built one contribution at a time by users like you. See [the CONTRIBUTING file](docs/CONTRIBUTING.md) for instructions on how to contribute.

### Previewing the theme locally

If you'd like to preview the theme locally (for example, in the process of proposing a change):

1. Clone down the theme's repository (`git clone https://github.com/pages-themes/minimal`)
2. `cd` into the theme's directory
3. Run `script/bootstrap` to install the necessary dependencies
4. Run `bundle exec jekyll serve` to start the preview server
5. Visit [`localhost:4000`](http://localhost:4000) in your browser to preview the theme

### Running tests

The theme contains a minimal test suite, to ensure a site with the theme would build successfully. To run the tests, simply run `script/cibuild`. You'll need to run `script/bootstrap` once before the test script will work.

## Maintenance & Updates

### Updating Projects
The list of projects in `projects.md` can be generated from project metadata in your development directories.

```bash
python3 update_projects.py
```

This script scans `~/dev`, `~/PycharmProjects`, and `~/RustroverProjects` for projects containing `.planning/PROJECT.md`.

**Important Configuration & Preferences:**

**Status & Labeling:**
- **No "Production Ready" assumptions**: NEVER mark projects as "Production Ready" based on phase completion. Show actual phase progress (e.g., "Phase 17/20 (79%)").
- **No fabricated completion status**: Projects are not production ready just because all phases are complete.

**Layout & Organization:**
- **Categorized sections**: Group projects into categories (Network Engineering, Software Defined Radio, Health & Biometrics, Astrophotography, Photography, AI & Agents, Data & Utilities, Wellness & Sound).
- **Simple list format**: Use section headers (`##` for category, `###` for project) NOT grid/card layouts.
- **No Development Philosophy section**: The projects.md index should NOT include a "Development Approach" section at the bottom.
- **Category assignments**: Photo Tour → Photography; WatchNoise/Wave → Wellness & Sound; HealthyPi → Health & Biometrics; SDR projects → Software Defined Radio.

**Project Summaries:**
- **Complete sentences**: Show 4-5 full sentences, NOT truncated at character limits.
- **Paragraph breaks**: Add paragraph breaks every 2 sentences for readability (NOT single long blocks).
- **Sentence-aware splitting**: Split on punctuation boundaries (`.`, `!`, `?`) to avoid mid-word cutoffs.
- **Length-adaptive**: 4 sentences for long first sentences, 5 sentences for shorter ones.
- **Extract from multiple sections**: Combine content from Overview, What This Is, Core Value, and Problem It Solves to build comprehensive summaries.

**Project Names & Slugs:**
- **Clean project names**: Remove verbose prefixes like "PROJECT:", "Project:", and trailing parentheticals like "(KrakenSDR)".
- **Extract from headers**: Use the project name from the `# Header` in PROJECT.md, not the directory name.
- **Slug mappings**: Consolidate duplicates (e.g., `multi-agent-assistant` → `multi-agent`).

**Content Preservation:**
- **Preserve detailed content**: If existing .md file has 3x more lines than generated version, keep the existing file (indicates manual enrichment).
- **Extract names from preserved files**: When preserving detailed content, use the project name from the existing file, not PROJECT.md.
- **Legacy projects**: Keep existing project .md files that don't have .planning directories (e.g., autonetkit, nascleanup).
  - **AutoNetkit (PycharmProjects/autonetkit_legacy)**: This is the legacy PhD project. The active development is the **Network Modeling & Configuration Library** in `~/dev/ank_pydantic`.

**Special Cases:**
- **Multi-Agent Assistant**: The project page includes a comprehensive "Individual Agents" section listing all 13+ agents with their languages, purposes, and security tiers. This is a key feature and should be preserved.
- **Network Simulator**: Should be substantially detailed (250+ lines) with complete protocol lists, features, requirements validated, architecture decisions, and tech stack. Not a brief overview.
- **Network Automation Workbench**: Position as "complements existing network tools" NOT "commercial product" or "modern alternative to GNS3". It's a complementary tool with declarative, intent-based workflow.

**Page Sections to Include:**
Expand project pages with these sections when available: Overview, What This Is, Problem It Solves, Features, Key Capabilities, Architecture, Technical Depth, Security Model, Implementation Details, Protocols Implemented, Performance, Use Cases, Integration, Hardware, Agents, Components.

**Footer:**
- Each project page should have ONE footer link: `[← Back to Projects](../projects)` at the end
- NO duplicate footers (bug previously caused 9 duplicates)

## Homepage & Ecosystem Pages

### Homepage (index.md) Content Guidelines

**Research & Background:**
- Remove presentation mentions (e.g., "presented at PyCon AU") - not substantive
- Focus on outcomes and impact (e.g., "integrated into Cisco's VIRL platform")
- Emphasize ongoing work evolution rather than past conference talks

**Areas of Interest (NOT "Technical Competencies"):**
- Keep honest - list actual experience, not aspirational skills
- Languages: Only include languages with real experience
- Technical Domains: Broad areas (distributed computing, simulation, data processing)
- Product & Innovation: Team structures, product design, problem-solving focus
- Background: Include educational background (electrical engineering, economics)
- NO embellished claims (SIMD optimization, zero-copy structures) unless actually implemented

### Ecosystem Pages

**Created Pages:**
- `/network-automation` - Network Automation Ecosystem
- `/data-analytics` - Data Analytics & Visualization Ecosystem
- `/agentic-systems` - Agentic Systems Ecosystem
- `/signal-processing` - Signal Processing & RF Ecosystem

**Content Structure:**
Each ecosystem page follows this format:
1. Vision & Philosophy (why these tools exist)
2. Architecture diagram showing integration
3. Detailed tool sections (What It Is, Key Features, Examples, Use Cases, Current Status, Tech Stack)
4. Philosophy section (Why This Approach?)
5. Open Source & Contributions links

**Messaging Guidelines:**
- **Network Simulator**: Emphasize "rapid prototyping" NOT "protocol-level fidelity"
  - Goal is quick testing and iteration, catching obvious errors
  - NOT a replacement for full emulation or production testing
- **Examples**: Use CLI examples (user-friendly) over Rust API examples where possible
- **AutoNetkit**: Use `deploy_to_containerlab()` not `deploy_to_virl()`
- **Images**: Use absolute paths (`/images/...`) not relative paths
- **Getting Started**: Remove "For Researchers" section (not substantive)

**Navigation:**
All 4 ecosystem pages are linked in the main navigation header for easy discovery.

**Callout Boxes:**
Each project category in projects.md has a callout box linking to its ecosystem page:
```markdown
> **[View X Ecosystem →](ecosystem-page)**
> Brief description of what the ecosystem covers.
```

## CV Maintenance

The CV page (`cv.md`) is manually maintained with these guidelines:

**Professional Work Section:**
- Include ONLY professional/academic collaborations (e.g., AutoNetkit/Cisco VIRL)
- Do NOT duplicate personal projects already on /projects page
- Focus on work done for companies, institutions, or significant external collaborations

**PhD Section:**
- Summary of research focus and outcomes
- NO supervisors/examiners lists (unnecessary detail)
- Emphasize contributions and results (e.g., "Created AutoNetkit, integrated into Cisco VIRL")

**Technical Skills:**
- Organize Tools & Frameworks into categories (Infrastructure, Web, Data/ML, Rust Ecosystem, Network)
- Base on actual technology used across all work, not just current projects

## Guidelines for Future Maintenance

When maintaining or expanding this website, strictly adhere to these architectural and stylistic principles:

### Voice: Understated, Confident, Technical
- **Calm authority, not marketing.** Write as an engineer explaining work to a peer. No superlatives, no hype, no exclamation marks. The work speaks for itself.
- **Lead with the core idea.** Every project page begins with a short section explaining the technical problem and architectural approach — not a sales pitch. Use the heading "Concept" (not "The Insight", "The Idea", or "Overview").
- **Prefer specifics to adjectives.** Instead of "high-performance", state what it does: "processes 10k-node topologies in under a second", "126,000 lines of Rust", "1,350 tests". When numbers aren't available, describe the mechanism: "Rust-native graph engine", "compiled layout algorithms". Let the reader infer performance.
- **Avoid "high-performance".** This phrase appears generic and marketing-adjacent. Prefer: "fast", "native-speed", "Rust-native", or just describe the architecture and let it speak.
- **No templated section headers.** Avoid formulaic headings like "What It Is", "Problem It Solves", "Why This Tool?". Use natural, specific headings or fold the content into the introduction.
- **Show, don't overwhelm.** Use raw code blocks and CLI outputs for technical substance. Do NOT use collapsible `<details>` blocks — the technical evidence should be visible.
- **Tight prose.** Follow Strunk & White. Remove loose sentences. Let technical outcomes and realistic examples carry the weight.
- **Use full product names in prose.** Refer to projects by their full names (Network Visualization Engine, Network Simulator, etc.) in all prose text. Keep code names (netvis, netsim, ank_pydantic) only in code examples, CLI commands, imports, and repository URLs.

### Structural Consistency
- **Status Badges**: Use standardized status badges. Do not embellish "Production Ready" status; show actual phase completion (e.g., "Phase 18/20").
- **Dual Breadcrumbs**: Maintain `[← Back to Ecosystem]` and `[← Back to Projects]` navigation on all sub-pages.
- **Footer**: Every project page must have exactly one footer link: `[← Back to Projects](../projects)`.
- **Ecosystem Callouts**: Use blockquote callouts in `projects.md` to link to the respective ecosystem visions immediately under the category header.

### Content Architecture
- **Progressive Disclosure**: Ecosystem pages focus on Vision, Philosophy, and Architecture. Move deep technical details, protocol examples, and API usage to individual project pages.
- **No Zero-Value Content**: Remove trivial scripts or 0%-complete placeholders that dilute the professional brand. Focus on systems with significant architectural depth.

### ITAR and Export Control Compliance
**CRITICAL: Avoid content that may fall under International Traffic in Arms Regulations (ITAR) or export control.**

When describing RF signal processing, radar, or related projects:
- **DO NOT** use terms like "passive radar", "target detection", "surveillance", "tracking", or "covert operation"
- **DO NOT** describe military/defense applications, capabilities, or use cases
- **DO NOT** mention specific detection ranges, accuracies, or performance metrics that suggest military utility
- **DO** frame projects as academic experiments, signal processing research, or educational explorations
- **DO** use neutral technical language: "signal reflections", "bistatic geometry", "Doppler analysis"
- **DO** emphasize cost-effectiveness and educational value over operational capabilities

**Examples:**
- ❌ "Passive radar system for covert aircraft tracking"
- ✅ "RF signal reflection experiments exploring bistatic geometry"
- ❌ "Multi-target surveillance with 50km range"
- ✅ "Signal processing experiments with ambient RF sources"

This is not just about compliance — it protects the site, the projects, and the ability to share technical work publicly.

## Writing Style

All prose on this site follows **The Elements of Style** (Strunk and White).

- **Omit needless words.**
- **Use the active voice.**
- **Prefer the specific to the general.**
- **Avoid a succession of loose sentences.**

**Tone:** Understated, confident, technical. Write as an engineer explaining work to a peer — never as a marketer. The power is in the specifics and the architecture, not in adjectives. Avoid "high-performance", "cutting-edge", "state-of-the-art", "blazing-fast", and similar filler. If something is fast, say why (Rust, compiled, native graph algorithms) or show numbers.

**Project names:** Use full product names in prose (Network Visualization Engine, not NetVis). Keep code names only in code examples, CLI commands, and imports.

**Section headings:** Use "Concept" as the opening section for project pages. Avoid templated headers like "What It Is" or "Problem It Solves".

### Building and Deploying
The site is built using Jekyll. To build locally:

1. Ensure you have Ruby 3.0+ installed (required for modern Jekyll dependencies).
2. Install dependencies: `./script/bootstrap` (or `bundle install`).
3. Build the site: `./script/cibuild`.

Push changes to the `master` branch to deploy to GitHub Pages.

## Analytics

The site uses **Plausible Analytics** for privacy-friendly, cookieless tracking.

**Setup:**
1. Sign up at https://plausible.io (30-day free trial, then $9/month)
2. Add domain: `sk2.id.au`
3. Script is already configured in `_layouts/default.html` line 20
4. Deploy and verify tracking in Plausible dashboard

**Why Plausible:**
- Privacy-friendly, GDPR compliant, no cookies
- Lightweight (< 1KB script, no performance impact)
- No cookie consent banner needed
- Simple, beautiful dashboard
- Open source

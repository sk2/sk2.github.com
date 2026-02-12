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
3. Add any custom CSS (or Sass, including imports) you'd like immediately after the `@import` line

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
  - **AutoNetkit (PycharmProjects/autonetkit_legacy)**: This is the legacy PhD project. The active development is **ank_pydantic** in `~/dev/ank_pydantic`.

**Special Cases:**
- **Multi-Agent Assistant**: The project page includes a comprehensive "Individual Agents" section listing all 13+ agents with their languages, purposes, and security tiers. This is a key feature and should be preserved.
- **NetSim**: Should be substantially detailed (250+ lines) with complete protocol lists, features, requirements validated, architecture decisions, and tech stack. Not a brief overview.
- **ANK Workbench**: Position as "complements existing network tools" NOT "commercial product" or "modern alternative to GNS3". It's a complementary tool with declarative, intent-based workflow.

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

**Active Projects:**
- Keep concise (4 bullet points max)
- Link to /projects for full list
- Biometric tools: "Building agent-based analysis systems on top of the HealthyPi hardware platform" (not "part of HealthyPi")

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

## Recent Session Summary (2026-02-12)

Major website overhaul focused on creating ecosystem pages, adding examples, and toning down embellishments:

### Ecosystem Pages Created
- `/network-automation` - Network automation toolchain with examples
- `/data-analytics` - Data analytics and visualization tools
- `/agentic-systems` - Multi-agent architectures with security details
- `/signal-processing` - RF and biometric signal processing

All four pages added to main navigation and linked via callout boxes in projects.md.

### Content Improvements
- **Network Simulator**: Added larger 25-router example with realistic CLI output showing convergence metrics, LSA counts, timing
- **NetVis**: Added mesh and ring topology visualizations, switched from Rust API to CLI examples
- **Spectra**: Added screenshot of signal census interface
- **Topology Zoo**: Added 2000+ citation count with Google Scholar link and GÉANT visualization

### Honest Positioning
- Removed embellished claims (SIMD optimization, zero-copy structures, etc.)
- Changed from "Technical Competencies" to "Areas of Interest"
- Toned down HealthyPi claims - clarified it's experimental work on existing hardware by Protocentral
- Added "Limitations" section to network simulator
- Removed PyCon AU presentation mentions
- Removed "For Researchers" sections

### Architecture Updates
- Updated network automation diagram showing Analysis Module and workflow
- Changed to Containerlab deployment (not VIRL)
- Fixed image paths for proper loading

### Content Removed
- Philosophy sections with marketing language
- Overly promotional descriptions
- Claims about capabilities not yet implemented

### Principle Established
Keep website understated and honest. Show what tools actually do, not what they aspire to be.

## Recent Session Summary (2026-02-12 Evening)

Major refactoring of ecosystem pages and project content distribution:

### Content Architecture Fix
- **Problem**: Ecosystem overview page (network-automation.md) had 814 lines with detailed examples, while individual project pages were stubs (38 lines)
- **Solution**: Moved 574 lines of detailed content to individual project pages where it belongs
  - Network Simulator: Added 300+ lines of OSPF examples, database dumps, convergence metrics
  - NetVis: Added layout examples, integration code, visualization samples
  - ank_pydantic: Added Python API examples and integration details
  - TopoGen: Added data center generation examples
- **Result**: Ecosystem page now 240 lines (70% reduction), proper progressive disclosure

### Navigation Improvements
- Added dual breadcrumb navigation to all network project pages
  - "Back to Network Automation" + "Back to Projects"
  - Users can return to their entry point instead of losing context
- Fixed missing section headers (TopoGen, AutoNetkit) on ecosystem page
- Added complete table of contents with anchor links

### Protocol Examples
- **Added NetFlow Sim project** with flow-based performance analysis details
- **Replaced OSPF-heavy examples** with multi-protocol showcase:
  - Example 1: OSPF Triangle (basic validation)
  - Example 2: IS-IS L1/L2 Hierarchy (service provider routing) - NEW
  - Example 3: Protocol State Inspection (OSPF database dumps)
  - Example 4: BGP Multi-AS Route Propagation (eBGP peering) - NEW
- **Updated protocol status**: BGP from "In Development" to fully implemented
  - Route Reflection (RFC 4456)
  - Communities & Extended Communities (RFC 1997, RFC 4360)
  - Graceful Restart (RFC 4724)
  - VPNv4 Multi-Protocol BGP (RFC 4760)

### Bug Fixes
- Fixed all projects showing "Started: 2025" → "2026" (25 files updated)
- Removed Martin/tileserver references from NetFlowSim (not relevant)
- Cleaned up duplicate footer links (nascleanup.md, watchnoise.md)

### Commits Made
- `2648149` Refactor ecosystem pages: move detailed content to project pages
- `e44a093` Add NetFlow Sim to network automation ecosystem page
- `63c491b` Fix network automation page: add TOC and missing section headers
- `6ed60aa` Add IS-IS example to Network Simulator page
- `f6631c0` Fix project start year from 2025 to 2026
- `3a3ea07` Add BGP example and update protocol status

### Next Steps (Pending)

**BGP Example Enhancement** (User creating)
- Current BGP example is only 3 nodes (boring)
- User will create larger, more impressive BGP example showing:
  - Route reflection hierarchy, or
  - Multi-AS transit scenario, or
  - Data center BGP deployment
- Once created, add to website to replace current Example 4

**Feature Lists Enhancement** (Suggested but interrupted)
- Add more complete feature lists for each project
- Currently feature lists are brief; could be expanded with:
  - Detailed capabilities
  - Supported protocols/formats
  - Integration points
  - Performance characteristics

## Guidelines for Future Agents

When maintaining or expanding this website, strictly adhere to these architectural and stylistic principles:

### Core Philosophy: "Show, Don't Tell"
- **Lead with Insight**: Every project page must begin with a "The Insight" section that explains the *why* and the *problem* before the *how*.
- **Use Real Examples**: Prefer actual CLI outputs, YAML configurations, and code snippets over abstract descriptions.
- **Visual Evidence**: If a project involves visualization (NetVis, Spectra, Tileserver), include actual rendered output or screenshots.

### Quality & Honesty
- **No Embellishment**: Never claim "Production Ready" based on phase completion. Use factual status markers (e.g., "Phase 18/20").
- **Acknowledge Limitations**: Projects should include a "Limitations" section to maintain professional credibility.
- **Actual Experience**: Only list languages and tools with demonstrated usage in the project files.

### Structural Consistency
- **Status Badges**: Use standardized status badges in both `projects.md` and individual project pages.
- **Ecosystem Callouts**: Every category in `projects.md` must have a blockquote callout linking to its respective ecosystem page.
- **Navigation**: Maintain dual breadcrumbs ("Back to Ecosystem" + "Back to Projects") on all project sub-pages to preserve user context.
- **Footer**: Ensure every project page has exactly one footer link: `[← Back to Projects](../projects)`.

### Content Architecture
- **Progressive Disclosure**: Keep ecosystem pages high-level (vision/architecture) and move deep technical details/examples to individual project pages.
- **Writing Style**: Strictly follow Strunk & White. Omit needless words. Use active voice. Prefer specific over general.

### Maintenance Workflow
1.  **Update Metadata**: Ensure "Started" year and "Status" are accurate and consistent.
2.  **Verify Links**: Check that all ecosystem and project links are functional.
3.  **Sync CV**: If a major project reaches a significant milestone, update the "Professional Work" section in `cv.md`.
4.  **Run Build**: Always verify the site builds without errors using `./script/cibuild` before finalizing changes.

## Writing Style

All prose on this site follows **The Elements of Style** (Strunk and White).

- **Omit needless words.**
- **Use the active voice.**
- **Prefer the specific to the general.**
- **Avoid a succession of loose sentences.**

When adding or updating project descriptions, ensure they remain information-dense and strictly adhere to these principles.

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

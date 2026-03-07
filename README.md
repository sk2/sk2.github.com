# Website

Source for [sk2.id.au](https://sk2.id.au), built with [Eleventy](https://www.11ty.dev/) and deployed via GitHub Pages.

## Structure

```
├── index.md                  # Homepage
├── projects.md               # All projects listing with search
├── reports.md                # Technical reports and papers
├── cv.md                     # Curriculum vitae
├── thesis.md                 # PhD thesis
├── network-automation.md     # Category: Network Automation
├── signal-processing.md      # Category: Signal Processing
├── photography.md            # Category: Photography & Astrophotography
├── data-analytics.md         # Category: Data & Analytics
├── agentic-systems.md        # Category: Autonomous Systems
├── projects/                 # 47 individual project pages
├── insights/                 # Technical articles
├── _layouts/default.html     # Site layout (nav, breadcrumbs, footer)
├── assets/css/main.css       # Styles (light/dark themes via CSS custom properties)
├── assets/docs/              # PDFs (tech reports, papers, manuals)
├── images/                   # Project screenshots, diagrams, demos
├── _data/site.json           # Site metadata (title, description, url)
├── sitemap.njk               # Auto-generated sitemap (Nunjucks template)
├── robots.txt                # Search engine directives
└── .eleventy.js              # Eleventy configuration
```

## Build & Deploy

```sh
npm install                       # Install dependencies
npx @11ty/eleventy --serve        # Local dev server at localhost:8080
npx @11ty/eleventy                # Build to _site/
```

Deploy: push to `master` (GitHub Pages).

## Navigation

The layout uses `section` front matter for breadcrumb navigation. Set it on project pages to get automatic back-links:

```yaml
---
layout: default
section: network-automation
---
```

Valid sections: `network-automation`, `signal-processing`, `photography`, `data-analytics`, `agentic-systems`, `insights`.

## Project Sync

Project pages are synchronized from local development directories using `update_projects.py`:

```sh
python3 update_projects.py --scan-dirs ~/dev
```

This scans for metadata, technical reports, images, and code samples, then updates `projects/*.md` while preserving hand-written stable sections (Concept, Architecture, Tech Stack).

## Writing Style

All prose follows the voice guidelines in `CLAUDE.md`: understated, technical, no marketing language. See the naming table there for canonical project names.

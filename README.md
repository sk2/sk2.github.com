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
- **Categorized sections**: Group projects into categories (Network Engineering, Signal Processing & SDR, Astrophotography, AI & Agents, Data & Utilities, Personal Apps).
- **Simple list format**: Use section headers (`##` for category, `###` for project) NOT grid/card layouts.
- **No Development Philosophy section**: The projects.md index should NOT include a "Development Approach" section at the bottom.

**Project Summaries:**
- **Complete sentences**: Show 4-5 full sentences, NOT truncated at character limits.
- **Sentence-aware splitting**: Split on punctuation boundaries (`.`, `!`, `?`) to avoid mid-word cutoffs.
- **Length-adaptive**: 4 sentences for long first sentences, 5 sentences for shorter ones.
- **Extract from sections**: Use Overview, Core Value, or "What This Is" sections for summaries.

**Project Names & Slugs:**
- **Clean project names**: Remove verbose prefixes like "PROJECT:", "Project:", and trailing parentheticals like "(KrakenSDR)".
- **Extract from headers**: Use the project name from the `# Header` in PROJECT.md, not the directory name.
- **Slug mappings**: Consolidate duplicates (e.g., `multi-agent-assistant` → `multi-agent`).

**Content Preservation:**
- **Preserve detailed content**: If existing .md file has 3x more lines than generated version, keep the existing file (indicates manual enrichment).
- **Extract names from preserved files**: When preserving detailed content, use the project name from the existing file, not PROJECT.md.
- **Legacy projects**: Keep existing project .md files that don't have .planning directories (e.g., autonetkit, nascleanup).

**Special Cases:**
- **Multi-Agent Assistant**: The project page includes a comprehensive "Individual Agents" section listing all 13+ agents with their languages, purposes, and security tiers. This is a key feature and should be preserved.

**Page Sections to Include:**
Expand project pages with these sections when available: Overview, What This Is, Problem It Solves, Features, Key Capabilities, Architecture, Technical Depth, Security Model, Implementation Details, Protocols Implemented, Performance, Use Cases, Integration, Hardware, Agents, Components.

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
2. Add your domain (e.g., `sk2.github.io` or your custom domain)
3. Update `_layouts/default.html` line 20:
   - Change `data-domain="yourdomain.com"` to your actual domain
4. Deploy and verify tracking in Plausible dashboard

**Why Plausible:**
- Privacy-friendly, GDPR compliant, no cookies
- Lightweight (< 1KB script, no performance impact)
- No cookie consent banner needed
- Simple, beautiful dashboard
- Open source

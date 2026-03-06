# Website

This repository is the source for `sk2.github.com` / `sk2.id.au`, built with [Eleventy](https://www.11ty.dev/).

## Build & Deploy

1. **Install dependencies:** `./script/bootstrap` (runs `npm install`)
2. **Build the site:** `./script/cibuild` (runs `npx @11ty/eleventy`)
3. **Local dev server:** `npx @11ty/eleventy --serve`
4. **Deploy:** Push changes to the `master` branch (GitHub Pages).

## Project Sync

The project pages are synchronized from local development directories using `update_projects.py`.

```sh
python3 update_projects.py --scan-dirs ~/dev
```

This scans project directories for metadata, technical reports, images, and code samples, then updates `projects/*.md` pages while preserving hand-written "stable" sections (Concept, Architecture, Tech Stack).

### Netsim Demo Gifs

The Network Simulator has demo gifs that live in `network-simulator/docs/images/` and are copied to `images/` with a `netsim-` prefix. To sync them:

```sh
python3 update_projects.py --scan-dirs ~/dev
```

The script copies gifs from the source repo and creates both prefixed (`netsim-basic-demo.gif`) and unprefixed (`basic-demo.gif`) copies. The netsim project page references the prefixed versions.

### Two-Track Content Model

1. **Stable Content (Polished Narrative):** Canonical technical detail — Concept, Architecture, Tech Stack — lives directly in `projects/*.md`. The sync script preserves these sections.
2. **Fresh Content (Automated Sync):** Status, milestones, assets (Reports, Code, Visuals) are pulled from external project folders.

### Maintenance Workflow

- **To improve content:** Edit `projects/*.md` directly using stable section headers (`## Concept`, `## Architecture`).
- **To update status & assets:** Run `python3 update_projects.py --scan-dirs ~/dev`.

## Writing Style

All prose follows **The Elements of Style** (Strunk and White) and the project's `CLAUDE.md` voice guidelines. See `CLAUDE.md` for the full naming table and tone rules.

## Analytics

The site uses **Plausible Analytics** for privacy-friendly tracking. Configured in `_layouts/default.html`.

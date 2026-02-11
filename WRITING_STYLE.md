# Writing Style & Project Guidelines

This document outlines the ground rules for writing and updating project descriptions on this website. The goal is to ensure consistency, technical precision, and adherence to the "Show, Don't Tell" philosophy.

## 1. The Strunk & White Mandate

All prose must follow the principles of **The Elements of Style** (Strunk and White).

- **Omit needless words.** If a word doesn't add information, delete it.
- **Use the active voice.** "The system processes data" is better than "Data is processed by the system."
- **Prefer the specific to the general.** Avoid vague adjectives like "powerful," "innovative," or "flexible." Describe *what* makes it so.
- **Avoid a succession of loose sentences.** Vary sentence structure but prioritize clarity.

## 2. Technical Precision over Marketing

Avoid "markety" language and sales pitches. Focus on the engineering reality.

- **Instead of:** "Our revolutionary AI-powered assistant streamlines your workflow like never before."
- **Use:** "A containerized multi-agent system that uses NATS for low-latency coordination and Pydantic for schema enforcement."

### Ground Rules for Project Content:
1. **Focus on "The Insight":** Every project starts with a problem and a non-obvious solution. Describe the "why" technically.
2. **Architecture First:** Describe the system components and how they interact.
3. **Quantify:** Use metrics where possible (e.g., "582 tests," "Phase 4/6," "supports 11+ platforms").
4. **No Fluff:** Remove "I'm proud to present," "This project aims to," and similar filler.

## 3. "Show, Don't Tell"

Don't tell the reader the tool is "easy to use." Show them a 4-line code snippet or a 1-line CLI command that demonstrates it.

- Each detailed project page should include a **Quick Facts** table.
- Each page should have a clear **Architecture** or **Technical Depth** section.
- Use **The Insight** header to capture the core technical value proposition.

## 4. Maintenance Workflow

When using `update_projects.py`:
- The script pulls data from `.planning/PROJECT.md` and `STATE.md`.
- **Manual Polish is Mandatory:** The script provides the data; the human (or agent) provides the Strunk & White polish.
- **Preserve "The Insight":** The script is configured to try and preserve manually written "The Insight" sections. Do not overwrite these with raw summaries.

## 5. Visual Standards
- Use card-based summaries on the index page.
- Decouple technical deep-dives from the main landing area.
- Ensure all images have descriptive alt-text and clear captions.

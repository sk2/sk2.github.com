---
layout: default
section: network-automation
---

# Network Output Parser

<span class="status-badge status-active">Active</span>

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Use Cases](#use-cases)
- [Architecture](#architecture)
- [Performance](#performance)
- [Tech Stack](#tech-stack)

## Concept

### What This Is

`cliscrape` is a high-performance CLI scraping and parsing tool for network devices, written in Rust. It provides a modern, ergonomic, and blazingly fast alternative to legacy tools like `TextFSM`, while maintaining first-class compatibility with existing templates.

### Core Value

The one thing that must work perfectly: **Extremely fast, reliable parsing of semi-structured CLI output into structured data, regardless of whether the template is legacy TextFSM or the new ergonomic format.**

---

## Use Cases

- **Automation Pipelines**: Parse device output in CI/CD workflows (10-50x faster)
- **Template Development**: Interactive TUI for debugging template regex patterns
- **Migration Path**: Drop-in replacement for Python TextFSM with existing templates
- **Multi-Device Scraping**: Parallel processing of hundreds of device outputs

---

## Architecture

**Core Components:**
- **FSM Engine**: State-machine parser with value definitions, transitions, and actions
- **TextFSM Parser**: Compatibility layer for legacy `.textfsm` files
- **Template IR**: Intermediate representation supporting both TextFSM and modern formats
- **TUI**: ratatui-based debugger with input stream, state visualization, and match trace

**Memory Management:**
- Pre-allocated record buffers to avoid heap churn
- Zero-copy values using `Cow<'a, str>` where possible
- Compiled regex set for fast rule dispatching

---

## Performance

Rust's zero-cost abstractions and compiled regex engine deliver 10-50x faster parsing compared to Python TextFSM. Fully parallelizable across multiple files without GIL contention. Instant startup (compiled binary) vs. interpreted Python overhead.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Rust |
| Regex | `regex` crate |
| TUI | `ratatui` + `crossterm` |
| Parsing | Custom lexer/parser |
| Templates | TextFSM + YAML/TOML |

<style>
.status-badge {
  display: inline-block;
  padding: 0.3em 0.8em;
  margin: 0.5em 0;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
}
.status-active {
  background-color: #007bff;
  color: white;
}
</style>

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

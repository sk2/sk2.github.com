---
layout: default
section: network-automation
---

# Network Output Parser

<span class="status-badge status-active">Phase 7/11 (50%)</span>



[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

---

## Contents

- [Concept](#concept)
- [Key Features](#key-features)
- [Performance](#performance)
- [Architecture](#architecture)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [What This Is](#what-this-is)
- [Core Value](#core-value)

## Concept

Network automation relies on parsing unstructured CLI output from devices. TextFSM handles this but suffers from Python's GIL limitations and slow regex execution. This Rust-based parser replicates TextFSM's state-machine semantics with native performance — parse massive `show tech-support` outputs in milliseconds, not seconds.

---

## Key Features

### TextFSM Compatibility
Full support for the TextFSM grammar. Use existing community templates (ntc-templates library) without modification. The parser translates `.textfsm` files into the internal FSM representation, enabling seamless migration from Python-based workflows.

### State Machine Engine
Finite state machine processes text line-by-line with typed variables, state transitions, and actions (Next, Continue, Record, Clear). Pre-compiled regex patterns with fast dispatching via RegexSet.

### TUI Debugger
Interactive template development environment showing real-time FSM state transitions, variable captures, and match visualization. See which line matched which rule and why — eliminates "regex soup" debugging.

### Modern Template Format
Structured YAML/TOML templates as an alternative to TextFSM's positional DSL:

```yaml
values:
  interface: \S+
  ip_address: \d+\.\d+\.\d+\.\d+|unassigned
  status: up|down|administratively down
  protocol: up|down

states:
  Start:
    - match: ^${interface}\s+${ip_address}\s+\S+\s+\S+\s+${status}\s+${protocol}
      action: Record
```

---

## Performance

Rust's zero-cost abstractions and compiled regex engine deliver 10-50x faster parsing compared to Python TextFSM. Fully parallelizable across multiple files without GIL contention. Instant startup (compiled binary) vs. interpreted Python overhead.

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

## Use Cases

- **Automation Pipelines**: Parse device output in CI/CD workflows (10-50x faster)
- **Template Development**: Interactive TUI for debugging template regex patterns
- **Migration Path**: Drop-in replacement for Python TextFSM with existing templates
- **Multi-Device Scraping**: Parallel processing of hundreds of device outputs

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

## What This Is

`cliscrape` is a high-performance CLI scraping and parsing tool for network devices, written in Rust. It provides a modern, ergonomic, and blazingly fast alternative to legacy tools like `TextFSM`, while maintaining first-class compatibility with existing templates.

---

## Core Value

The one thing that must work perfectly: **Extremely fast, reliable parsing of semi-structured CLI output into structured data, regardless of whether the template is legacy TextFSM or the new ergonomic format.**

---

[← Back to Data Analytics](../data-analytics)

[← Back to Projects](../projects)

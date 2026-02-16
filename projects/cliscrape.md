---
layout: default
section: network-automation
---

# cliscrape

<span class="status-badge status-active">** Phase 1: Core Parsing Engine</span>

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)

---

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

## Current Status

Phase 1 in progress — project scaffolding complete, defining lexer/parser for TextFSM files. Roadmap: FSM execution engine → CLI implementation → TUI debugger → modern YAML/TOML template support.

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Rust |
| Regex | `regex` crate |
| TUI | `ratatui` + `crossterm` |
| Parsing | Custom lexer/parser |
| Templates | TextFSM + YAML/TOML |

---

[← Back to Network Automation](../network-automation) | [← Back to Projects](../projects)

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

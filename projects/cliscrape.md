---
layout: default
section: network-automation
description: "Parsing engine for network device CLI output. Transforms semi-structured text (show commands, routing tables, BGP summaries) into structured data (JSON/YAML)…"
---

# CLI Parser

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-05-02</span>
  <span class="stack-badge">Rust</span>
</div>

---

## Contents

- [Concept](#concept)
- [Features](#features)
- [Current Status](#current-status)

## Concept

Parsing engine for network device CLI output. Transforms semi-structured text (show commands, routing tables, BGP summaries) into structured data (JSON/YAML) using an optimized Rust state machine. Provides full compatibility with the industry-standard ntc-templates library while offering 10–50x faster execution than Python-based alternatives like TextFSM.

---

## Features

- Rust parsing engine with pre-compiled regex patterns and non-backtracking execution
- First-class ntc-templates compatibility plus a clean YAML/TOML template format
- Interactive TUI debugger (ratatui) for real-time template testing against device output
- Zero-copy parsing for minimal overhead during large-scale processing
- Thread-safe design for concurrent parsing across multiple device outputs

---

## Quick Facts

| | |
|---|---|
| **Status** | Active |
| **Stack** | Rust |

---

## # Core Value

Enable rapid, reliable extraction of network state. The engine is built for predictable parsing, structured diagnostics, and policy-aware validation; release performance claims should be tied to current benchmark output.

---

## Use Cases

- **High-Frequency Monitoring**: Parse `show` commands in polling cycles for telemetry and health checks.
- **Inventory Discovery**: Automatically extract device details, interface states, and hardware versions for asset management.
- **Pre-deployment Validation**: Verify the current state of a network before pushing configuration changes to ensure safety.
- **Automated Troubleshooting**: Rapidly analyze complex outputs like routing tables or BGP summaries during incident response.

---

## Technical Depth

The engine is built on a custom regex-based state machine implemented in Rust. It utilizes pre-compiled patterns and a non-backtracking execution model to ensure deterministic performance even with complex multi-state templates.

- **Stack**: Rust, `regex` crate for optimized matching, `ratatui` for the TUI debugger.
- **Parallelism**: Thread-safe design allowing for concurrent parsing of multiple device outputs across all available CPU cores.
- **Validation**: Required fields, coverage thresholds, and field constraints can warn or fail depending on parse options.

---

## Current Status

2026-05-02 — closed Universal Ledger epic. 189 tests across 18 binaries enforce the schema contract end-to-end.

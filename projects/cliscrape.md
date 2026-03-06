---
layout: default
section: network-automation
---

# CLI Parser

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span>
</div>

[← Back to Network Automation](../network-automation)

[← Back to Projects](../projects)

---

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

## Use Cases

- Telemetry polling: parse `show` commands in high-frequency monitoring cycles
- Inventory discovery: extract device details, interface states, and hardware versions
- Pre-deployment validation: verify network state before pushing configuration changes
- Incident response: rapidly analyze routing tables and BGP summaries during troubleshooting

---

[← Back to Network Automation](../network-automation)

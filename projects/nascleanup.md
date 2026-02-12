---
layout: default
---

# nascleanup

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---


## The Insight

Manual deduplication of large NAS shares is error-prone and slow. **nascleanup** uses Rust for rapid content-based hashing and traversal, automating the organization and deduplication of distributed file systems.

## Quick Facts

| | |
|---|---|
| **Status** | Active Development |
| **Language** | Rust |
| **Started** | 2026 |

---

## What This Is

A Rust-based CLI tool for deduplicating and organizing large file shares. Optimized for Docker execution on DSM, it uses an indexing layer for fast file comparison and metadata management.

## Architecture

- **Language:** Rust (for performance and safety).
- **Core Engine:** A CLI tool capable of rapid traversal and content-based hashing.
- **Execution:** Optimized for Docker/Native execution on DSM to minimize network latency.
- **Data Model:** Indexing layer to store file hashes and metadata for fast comparison.
- **Intelligence:** Future integration of ML for content-based classification.

---

[← Back to Projects](../projects)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

---

[← Back to Projects](../projects) | [Development Philosophy](../development)

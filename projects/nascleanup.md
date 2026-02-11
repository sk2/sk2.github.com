---
layout: default
---

# nascleanup

<span class="status-badge status-active">Active Development</span>

[← Back to Projects](../projects)

---

## Quick Facts

| | |
|---|---|
| **Status** | Active Development |
| **Language** | Rust |
| **Started** | 2025 |

---

## Overview

A Rust-based tool designed to deduplicate and organize large file shares, particularly on NAS devices. It identifies redundant data, optimizes storage, and helps maintain data integrity across distributed file systems.

## Problem It Solves

NAS devices often accumulate duplicate files and disorganized data over time, leading to wasted storage space and difficulty in managing backups. Manual cleanup is tedious and error-prone. `nascleanup` automates this process.

## Architecture

- **Language:** Rust (for performance and safety).
- **Core Engine:** A CLI tool capable of rapid traversal and content-based hashing.
- **Execution:** Optimized for Docker/Native execution on DSM to minimize network latency.
- **Data Model:** Indexing layer to store file hashes and metadata for fast comparison.
- **Intelligence:** Future integration of ML for content-based classification.

---

[← Back to Projects](../projects) | [Development Philosophy](../development)
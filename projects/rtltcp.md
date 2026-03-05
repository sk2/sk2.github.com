---
layout: default
section: signal-processing
---

# Radio Streaming Server

<span class="status-badge status-active">Last Active: 2026-02-22</span>

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

---

## Contents

- [Code Samples](#code-samples)
- [What This Is](#what-this-is)
- [Why It Exists](#why-it-exists)
- [Core Value](#core-value)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Key Decisions](#key-decisions)
- [Current Status](#current-status)

## Code Samples

### rte1_probe.rs

```rs
//! Minimal RTE1 extended protocol probe.
//!
//! Connects to an rtltcp-rust server, negotiates the extended protocol,
//! prints the handshake, reads a few frames, and reports sample statistics.
//!
//! Usage:
//!   cargo run --example rte1_probe -- [host:port]
//!
//! Default: localhost:1234

use std::io::{Read, Write};
use std::net::TcpStream;
use std::time::Duration;

fn main() {
    let addr = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "localhost:1234".into());

    println!("Connecting to {}...", addr);
    let mut stream = TcpStream::connect(&addr).expect("failed to connect");
    stream.set_read_timeout(Some(Duration::from_secs(5))).ok();

    // Send extended protocol magic
    stream.write_all(b"RTE1").expect("failed to send magic");
    println!("Sent RTE1 magic");

    // Read 24-byte extended handshake
    let mut hs = [0u8; 24];
    stream
        .read_exact(&mut hs)
        .expect("failed to read handshake");

    if &hs[0..4] != b"RTE1" {
        eprintln!("Server did not respond with RTE1 (got {:?})", &hs[0..4]);
        std::process::exit(1);
    }

    let format_id = hs[4];
    let bits = hs[5];
    let capability_flags = hs[6];
    let sample_rate = u32::from_be_bytes([hs[8], hs[9], hs[10], hs[11]]);
    let frequency = u32::from_be_bytes([hs[12], hs[13], hs[14], hs[15]]);
    let serial = u32::from_be_bytes([hs[16], hs[17], hs[18], hs[19]]);

    let format_name = match format_id {
        0 => "u8",
        1 => "i16le",
        2 => "f32le",
        _ => "unknown",
    };

    let has_stats = capability_flags & 0x01 != 0;

    println!();
    println!("Extended handshake received:");
    println!("  Sample format:  {} (id={})", format_name, format_id);
    println!("  Bits/sample:    {}", bits);
    println!(
        "  Capabilities:   0x{:02X}{}",
        capability_flags,
        if has_stats { " [stats]" } else { "" }
    );
    println!(
        "  Sample rate:    {} Hz ({:.3} MHz)",
        sample_rate,
        sample_rate as f64 / 1e6
    );
    println!(
        "  Frequency:      {} Hz ({:.3} MHz)",
        frequency,
        frequency as f64 / 1e6
    );
    println!("  Device serial:  0x{:08X}", serial);
    println!();

    let bytes_per_component = match format_id {
        0 => 1usize,
        1 => 2,
        2 => 4,
        _ => {
            eprintln!("Unknown format, cannot read frames");
            std::process::exit(1);
        }
    };

    // Read frames (data + stats interleaved)
    let max_frames = 10;
    let mut data_count = 0;
    let mut stats_count = 0;
    println!("Reading up to {} frames...", max_frames);
    println!();

    for _ in 0..max_frames {
        // Read 5-byte typed frame header: [type, len0, len1, len2, len3]
        let mut hdr = [0u8; 5];
        if stream.read_exact(&mut hdr).is_err() {
            eprintln!(
                "Connection closed after {} data + {} stats frames",
                data_count, stats_count
            );
            break;
        }
        let frame_type = hdr[0];
        let payload_len = u32::from_le_bytes([hdr[1], hdr[2], hdr[3], hdr[4]]) as usize;

        // Read payload
        let mut payload = vec![0u8; payload_len];
        if stream.read_exact(&mut payload).is_err() {
            eprintln!("Failed to read frame payload");
            break;
        }

        match frame_type {
            0x00 => {
                // Data frame
                data_count += 1;
                let iq_pairs = payload_len / (bytes_per_component * 2);

                let preview = match format_id {
                    0 => {
                        let vals: Vec<String> =
                            payload.iter().take(8).map(|v| format!("{}", v)).collect();
                        vals.join(", ")
                    }
                    1 => {
                        let vals: Vec<String> = payload
                            .chunks_exact(2)
                            .take(4)
                            .map(|c| format!("{}", i16::from_le_bytes([c[0], c[1]])))
                            .collect();
                        vals.join(", ")
                    }
                    2 => {
                        let vals: Vec<String> = payload
                            .chunks_exact(4)
                            .take(4)
                            .map(|c| format!("{:.6}", f32::from_le_bytes([c[0], c[1], c[2], c[3]])))
                            .collect();
                        vals.join(", ")
                    }
                    _ => String::from("?"),
                };

                println!(
                    "  [DATA  {}] {} bytes, {} IQ pairs  [{}...]",
                    data_count, payload_len, iq_pairs, preview
                );
            }
            0x01 => {
                // Stats frame
                stats_count += 1;
                let json_str = String::from_utf8_lossy(&payload);
                println!("  [STATS {}] {}", stats_count, json_str);
            }
            _ => {
                println!(
                    "  [UNKNOWN type=0x{:02X}] {} bytes",
                    frame_type, payload_len
                );
            }
        }
    }

    println!();
    println!(
        "Done. Received {} data frames, {} stats frames.",
        data_count, stats_count
    );
}

```

---

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-02-22 |

---

## What This Is

A cross-platform (targeted at Raspberry Pi) server that interfaces with multiple SDR devices (RTL-SDR, AirSpy HF+) and streams raw IQ samples over the network using the industry-standard `rtl_tcp` protocol. It features a built-in TUI for live configuration and device management.

---

## Why It Exists

Existing C-based implementations (like `rtl_tcp` and `hfp_tcp`) are often single-threaded, difficult to manage when running multiple devices, and lack modern observability/control features. This project aims to:
- Leverage Rust for safety and high-performance concurrency.
- Simplify multi-SDR management through a single binary.
- Provide a responsive TUI for real-time adjustments (frequency, gain, etc.).
- Enable future network optimizations (compression, error correction).

---

## Core Value

The ability to reliably and efficiently stream high-fidelity IQ data from multiple SDRs over a network with a modern management interface.

---

## Tech Stack

- **Language:** Rust
- **Hardware Interface:** `libusb` (via FFI wrapping of `librtlsdr` and `libairspyhf`)
- **Networking:** TCP (implementing the `rtl_tcp` protocol)
- **UI:** Terminal User Interface (TUI) via `ratatui` or similar
- **Config:** TOML file-backed persistence
- **Target:** Raspberry Pi (cross-compiled from macOS/Linux)

---

## Requirements



---

## # Validated

(None yet — ship to validate)

---

## # Active

- [ ] Support for RTL-SDR hardware via `librtlsdr` wrapping.
- [ ] Support for AirSpy HF+ hardware via `libairspyhf` wrapping.
- [ ] Implementation of the `rtl_tcp` network protocol.
- [ ] Multi-threaded architecture to handle multiple SDR streams concurrently.
- [ ] TUI for viewing status and updating configuration live.
- [ ] Persistent configuration stored in a TOML file.
- [ ] Cross-compilation pipeline for Raspberry Pi (ARM).

---

## # Out of Scope

- **Pure Rust Drivers:** (Initial phase) Using C-library wrapping instead for faster time-to-market.
- **Advanced Network Coding:** (Initial phase) Delta compression and Raptor codes are deferred to later optimizations.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Wrapping C Libs | Faster implementation of hardware logic while focusing on the Rust networking/UI layer. | Pending |
| Monolithic Binary | Easier to manage and deploy initially via SSH. | Pending |
| TOML Config | Human-readable and easy to edit or programmatically update. | Pending |

*Last updated: 2026-02-12 after initialization*

---

## Current Status

2026-02-22 - Completed 05-04-PLAN.md

---

[← Back to Signal Processing](../signal-processing)

[← Back to Projects](../projects)

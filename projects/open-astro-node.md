---
layout: default
section: photography
description: "OpenAstro Node — a headless astrophotography controller that runs unattended overnight sessions on low-power hardware: guiding, meridian flips, safety, and a 'Goodnight' shutdown protocol."
hand_written: true
---

# OpenAstro Node

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Concept

A headless astrophotography controller built to run all night without supervision. Each node drives one camera and one mount, executes the imaging plan, guides through PHD2, handles meridian flips on schedule, and walks the rig through a defined "Goodnight" protocol when the session ends or the weather turns. If two nodes share a mount, they coordinate so only one of them is driving at a time.

OpenAstro Core does the imaging math and the device drivers. The Node sits on top and is responsible for the session: what happens between dark and dawn, including the parts the photographer doesn't want to wake up for.

---

## Architecture

<div class="mermaid">
flowchart TD
    PLAN["Imaging Plan<br/><small>target · framing · sequence</small>"]
    SESS["Session Controller<br/><small>tonight's run</small>"]
    GUIDE["PHD2 Guiding<br/><small>tracking corrections</small>"]
    FLIP["Meridian Flip Manager<br/><small>scheduled · safe</small>"]
    SAFE["Safety Monitor<br/><small>weather · cloud · dawn</small>"]
    GN["Goodnight Protocol<br/><small>park · cap · power-down</small>"]
    UI1["Web UI<br/><small>responsive remote control</small>"]
    UI2["Terminal UI<br/><small>local SSH operator view</small>"]
    PLAN --> SESS
    SESS --> GUIDE
    SESS --> FLIP
    SAFE --> SESS
    SESS --> GN
    SESS --> UI1
    SESS --> UI2
</div>

The two UIs serve different operators on the same controller: the web UI for a phone on the couch, the terminal UI over SSH when the network is the only thing left and you need to know what the rig is currently doing.

---

[← Back to Photography & Astrophotography](../photography)

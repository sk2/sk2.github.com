---
layout: default
title: Simon Knight — Engineer
description: Telecommunications and software engineer working at the boundary between network engineering and signal processing — protocol simulators, graph topology engines, spatial rendering, and bistatic signal reflection.
---

# Simon Knight

Telecommunications and software engineer in Adelaide, South Australia. I build tools at the boundary between network engineering and signal processing: deterministic protocol simulators, graph topology engines, large-scale spatial rendering, and bistatic signal reflection.

PhD in computer science (University of South Australia, 2017) on the automated configuration of large networks. The same compiler-and-graph approach shows up across most of the projects here.

[![Global flight network rendered as a ridge structure by DataRaster](/images/home-hero-flights.png)](/projects/datavis)
*The global airline network — **67,000 great-circle routes** — processed into a corridor ridge structure. Major hubs and the transoceanic corridors between them surface as bright spines instead of overlapping lines. One pass through DataRaster over the raw OpenFlights point cloud. [DataRaster →](/projects/datavis)*

**[Browse all projects](projects)**

## Featured Work

<div class="project-grid">
<div class="project-card">
  <h3 class="card-title"><a href="/projects/datavis">DataRaster</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">Python</span></div>
  <p class="card-description">Rust-native engine for rendering massive spatial datasets into density maps and raster tiles. A ten-crate workspace with a CLI, tile server, and Python and WASM front ends — a deployment-friendly Datashader backend.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/matrix-time-series">matrix-profile-rs</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">Polars</span></div>
  <p class="card-description">Matrix Profile algorithms (STOMP, SCAMP, SCRIMP++) in native Rust. Parameter-free motif and anomaly discovery in time series, with SIMD kernels and a Polars dataframe plugin.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/signals">Spectra</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Python</span></div>
  <p class="card-description">SDR-based spectrum monitoring that classifies and indexes everything it sees. Multi-radio capture feeds an ML pipeline that identifies modulations and writes a searchable signal census, with a TUI waterfall for live inspection.</p>
</div>

<div class="project-card">
  <h3 class="card-title"><a href="/projects/psytrance">Overtone</a></h3>
  <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
  <p class="card-description">Generative psytrance synthesis from first principles. A multi-scale energy model drives procedural pattern generation; an effects chain and humanisation layer turn the result into a produced-sounding track. Tala-style additive rhythm biases the underlying grid.</p>
</div>

</div>

## Background

Bachelor of Engineering (Telecommunications, First Class Honours) and Bachelor of Economics from the University of Adelaide. PhD in Computer Science (2017) from the University of South Australia, where I developed the AutoNetKit modeling framework for automated network configuration.

- [Read my PhD thesis](thesis)
- [View CV](cv)

[View all projects](projects)

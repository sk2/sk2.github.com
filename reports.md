---
layout: default
title: Technical Reports
---

# Technical Reports

Detailed technical documentation for selected projects. Each report covers architecture, design decisions, and implementation details.

---

## Network Engineering

<div class="project-grid">
  <div class="project-card">
    <h3 class="card-title"><a href="/projects/ank-netcfg">Network Configuration Framework</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
    <p class="card-description">Compiles vendor-neutral graph models into device-specific configurations.</p>
    <div class="doc-links">
      <a href="/assets/docs/ank-netcfg-netcfg-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/ank-netcfg-netcfg-paper.pdf" class="doc-link">Paper</a>
      <a href="/assets/docs/ank-netcfg-netcfg-usermanual.pdf" class="doc-link">Manual</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/ank-nte">Network Topology Engine</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
    <p class="card-description">14-crate graph engine ensuring every topological mutation is structurally sound.</p>
    <div class="doc-links">
      <a href="/assets/docs/ank-nte-nte-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/ank-nte-nte-paper.pdf" class="doc-link">Paper</a>
      <a href="/assets/docs/ank-nte-nte-usermanual.pdf" class="doc-link">Manual</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/netsim">Network Simulator</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
    <p class="card-description">Deterministic protocol simulator for OSPF, IS-IS, and BGP validation.</p>
    <div class="doc-links">
      <a href="/assets/docs/netsim-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/netsim-paper.pdf" class="doc-link">Paper</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/netvis">Visualization Engine</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span><span class="stack-badge">TypeScript</span></div>
    <p class="card-description">Layout engine for dense, multi-layer network topologies with edge bundling.</p>
    <div class="doc-links">
      <a href="/assets/docs/netvis-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/netvis-paper.pdf" class="doc-link">Paper</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/ank-pydantic">Network Modeling & Configuration Library</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Python</span></div>
    <p class="card-description">Pydantic models for declarative network topology and configuration generation.</p>
    <div class="doc-links">
      <a href="/assets/docs/ank-pydantic-ank-techreport.pdf" class="doc-link">Tech Report</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/automationarch">Network Automation Ecosystem</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Python</span><span class="stack-badge">Rust</span></div>
    <p class="card-description">A multi-layered ecosystem for automated network infrastructure management.</p>
    <div class="doc-links">
      <a href="/assets/docs/automationarch-ecosystem-techreport.pdf" class="doc-link">Tech Report</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/ank-workbench">Network Automation Workbench</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
    <p class="card-description">Interactive TUI for visualizing and planning network transformations.</p>
    <div class="doc-links">
      <a href="/assets/docs/ank-workbench-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/ank-workbench-paper.pdf" class="doc-link">Paper</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/topogen">Topology Generator</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Rust</span></div>
    <p class="card-description">High-performance DSL-based engine for synthesizing massive topologies.</p>
    <div class="doc-links">
      <a href="/assets/docs/topogen-topogen-techreport.pdf" class="doc-link">Tech Report</a>
      <a href="/assets/docs/topogen-topogen-paper.pdf" class="doc-link">Paper</a>
    </div>
  </div>
</div>

---

## Radio Systems

<div class="project-grid">
  <div class="project-card">
    <h3 class="card-title"><a href="/projects/rf-signal-analysis">Signal Reflection Analysis</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Python</span></div>
    <p class="card-description">Passive radar systems using commercial signal reflection for position tracking.</p>
    <div class="doc-links">
      <a href="/assets/docs/rf-signal-analysis-passive-radar-techreport.pdf" class="doc-link">Tech Report</a>
    </div>
  </div>

  <div class="project-card">
    <h3 class="card-title"><a href="/projects/signals">Spectrum Analysis</a></h3>
    <div class="badges-row card-badges"><span class="stack-badge">Python</span></div>
    <p class="card-description">SDR-based signal monitoring and waterfall analysis with vector indexing.</p>
    <div class="doc-links">
      <a href="/assets/docs/signals-spectra-techreport.pdf" class="doc-link">Tech Report</a>
    </div>
  </div>
</div>

<style>
.doc-links {
  margin-top: 1rem;
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}
.doc-link {
  display: inline-block;
  padding: 0.25rem 0.6rem;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 500;
  text-decoration: none !important;
  color: var(--text-secondary) !important;
  transition: all 0.2s ease;
}
.doc-link:hover {
  background: var(--bg-tertiary);
  border-color: var(--link);
  color: var(--link) !important;
}
</style>

---

[← Back to Projects](projects)

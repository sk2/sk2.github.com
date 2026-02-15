# Website TODO

## Screenshots and Visual Content

Add visual content to project pages to provide substance and demonstrate functionality:

### Network Engineering Projects

**Network Visualization Engine:**
- [ ] Example topology visualizations (force-directed, hierarchical, radial)
- [ ] CLI usage example with output
- [ ] Side-by-side comparison of different layout algorithms
- [ ] Edge bundling demonstration

**Network Modeling & Configuration Library:**
- [ ] Code example showing type-safe topology definition
- [ ] Query API usage examples
- [ ] Generated configuration output samples

**Network Automation Workbench:**
- [ ] Screenshot of web UI (topology editor, visualization)
- [ ] Guided tour screenshots
- [ ] Sample gallery view
- [ ] Workflow demonstration (design → simulate → visualize)

**Topology Generator:**
- [ ] CLI usage examples (generate data center, WAN, random topologies)
- [ ] Generated YAML topology example
- [ ] Visualization of generated topologies

**Network Simulator:**
- [ ] CLI output showing simulation run
- [ ] Routing table output (`show ip route`)
- [ ] Ping/traceroute output examples
- [ ] JSON output sample

### Signal Processing Projects

**Astro:**
- [ ] TUI screenshot (terminal interface)
- [ ] Web UI mockup/screenshot (when available)
- [ ] Example capture/imaging session

**HealthyPi:**
- [ ] Signal plots (ECG, PPG, EDA waveforms)
- [ ] HRV analysis output
- [ ] Virtual Patient simulator output

**Spectra:**
- [ ] Waterfall visualization concept/screenshot
- [ ] SDR hardware photos
- [ ] Antenna setup photos

### Agent Projects

**Multi-Agent Assistant:**
- [ ] Architecture diagram
- [ ] NATS message flow visualization
- [ ] Security dashboard screenshot
- [ ] Agent log output samples

**Cycle Agent:**
- [ ] UI mockup (terrain visualization)
- [ ] KICKR Core integration diagram

## Content Improvements

- [ ] Create individual project pages (projects/netvis.md, projects/ank-pydantic.md, etc.) using full product names
- [ ] Convert projects.md to summary page with links to individual pages
- [ ] Add "Quick Facts" boxes to each project page (year started, language, test count, status)
- [ ] Include relevant links (GitHub, docs, papers) on each project page
- [ ] Add "Getting Started" sections with installation/usage for active projects

## Structure

```
projects.md              # Summary page with all projects
projects/
  netvis.md             # Detailed page with screenshots
  ank-pydantic.md
  ank-workbench.md
  topogen.md
  netsim.md
  astro.md
  healthypi.md
  spectra.md
  multi-agent.md
  cycle-agent.md
  autonetkit.md
```

## Update Script Enhancements

- [ ] Modify update_projects.py to generate individual project pages
- [ ] Add screenshot/image detection and inclusion
- [ ] Generate summary page with links to detailed pages
- [ ] Include quick stats boxes in generated pages

---
layout: default
title: "Tick-Based Determinism vs. Full Emulation"
section: insights
---

# Tick-Based Determinism vs. Full Emulation
*Why we chose a custom Rust protocol simulator over Containerlab.*

<div class="badges-row" style="margin-bottom: 2rem;">
  <span class="status-badge">Architecture Insight</span>
  <span class="stack-badge">Rust</span>
  <span class="stack-badge">Network Simulator</span>
</div>

When building the **[Network Simulator](../projects/netsim)**, the first question was: *Why not just use Containerlab?*

Containerlab, GNS3, and EVE-NG are the industry standards. They work by booting real vendor operating systems (cEOS, vQFX, XRv) in containers or VMs and wiring them together using Linux network namespaces.

For many tasks—like learning vendor CLI syntax or testing a specific Ansible playbook—full emulation is the correct choice. But for **automated, at-scale architectural validation**, full emulation has three fatal flaws:

1. **Weight:** Booting 100 virtual routers requires a massive server. It takes minutes to start, and gigabytes of RAM.
2. **Non-Determinism:** Virtual machines share CPU time. If you run an OSPF convergence test twice, the exact timing of LSA flooding will differ. A race condition that causes a routing loop might happen 1 time out of 10.
3. **Opacity:** You cannot easily pause a real routing daemon, inspect its internal queues, and step it forward millisecond by millisecond.

### The Tick-Based Approach

To achieve CI/CD-style rigor for physical networks, we needed tests that run in seconds and produce identical results 100% of the time. 

We abandoned full OS emulation and instead built a custom, deterministic protocol engine in Rust.

```rust
// A simplified view of the Simulator tick loop
pub fn run_until_converged(&mut self) -> SimulationResult {
    let mut tick = 0;
    
    loop {
        // 1. All links deliver in-flight packets that have reached their delay threshold
        self.fabric.deliver_packets(tick);
        
        // 2. All routers process received packets and update their protocol state machines (OSPF/BGP)
        let mut converged = true;
        for router in &mut self.routers {
            let active = router.step(tick);
            if active { converged = false; }
        }
        
        // 3. Increment universal clock
        tick += 1;
        
        if converged { break; }
    }
    
    SimulationResult::Converged(tick)
}
```

### The Benefits of Simulation

By simulating the *protocols* rather than emulating the *hardware*, we gained several superpowers:

1. **Sub-second Execution:** We can boot a 50-node multi-area OSPF topology, inject a configuration change, run it to convergence, and assert that all loopbacks are reachable in under 100 milliseconds. This makes it viable to run the simulator *on every keystroke* while designing a network.
2. **Absolute Reproducibility:** Because the system is driven by a discrete, single-threaded "tick", the same configuration applied to the same topology will always produce the exact same routing tables, down to the exact tick of convergence.
3. **Time Travel & Chaos:** We can deterministically script chaos. "At tick 500, drop the link between Spine-1 and Leaf-2. Assert that traffic reroutes within 30 ticks."

### When to use which?

We didn't kill Containerlab; we shifted left. 

The `netcfg` engine still exports `clab.yaml` files. The workflow is:
1. **Design & Iterate:** Use `netsim` for instantaneous feedback while designing the architecture and policies.
2. **Final Verification:** Once the design passes the deterministic simulation, export the configs to Containerlab for a final syntax check against the real vendor OS before deploying to production.

---

[← Back to Architecture](../ecosystem)

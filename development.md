---
layout: default
title: Development Philosophy
description: A planning-first approach to building tools — structured project directories, type-safe Rust and Python, deterministic testing, and verification at every phase.
---

# Development Philosophy

I build tools to solve specific problems in network automation, data
visualization, signal processing, and intelligent systems. Each project starts
from a concrete need — type-safe topology modeling, rendering datasets too dense
to draw, an open alternative to closed astrophotography hardware — not from a
hypothetical use case. What follows is how that work is structured.

## Planning Before Code

Every project carries a `.planning/` directory:

- **PROJECT.md** — core value, requirements, constraints, decisions.
- **ROADMAP.md** — phase breakdown with goals and success criteria.
- **STATE.md** — current position, progress, decision log, blockers.
- **Phase plans** — execution detail, verified before any code is written.

Writing the plan first surfaces the hard decisions while they are still cheap to
change, and keeps the goal explicit once implementation begins.

## Verification Loops

Each phase closes with a verification step. Goal-backward analysis checks that
the codebase delivers what the phase promised; must-have coverage confirms every
requirement is met; a verification document records the result. When
verification fails, the gap is fixed before the next phase starts — a phase is
not "done" because its code compiles.

## Technology Choices

- **Rust** for performance-critical and long-lived code — the rendering and
  simulation engines, the graph and astronomy libraries. The type system and
  ownership model rule out whole classes of error at compile time.
- **Python** for scientific computing and rapid iteration, where the ecosystem
  (signal processing, data analysis) earns its place. Compiled extensions cross
  into Rust through PyO3 where Python overhead would dominate.
- **Swift** for native Apple integration — the iPhone and Apple TV apps, the
  HealthKit collectors.

Recurring tools: **NATS** as a message bus (TLS 1.3, per-subject ACLs, JetStream
for durability), **Pydantic** for type-safe Python models, **Polars** for
columnar data, and **petgraph** for Rust graph structures.

## Architecture Patterns

**Message-bus coordination.** Agents, simulators, and services communicate
through typed NATS messages rather than direct calls. This allows independent
deployment, enforces security boundaries with per-subject ACLs, and leaves the
message flow observable for debugging.

**Layered abstraction.** Network tools separate physical, logical, and protocol
layers; astrophotography tools separate coordinate math from device drivers from
capture logic. Each layer can be reasoned about, and tested, on its own.

**Determinism and type safety.** Simulators are tick-based and reproducible —
same input, same result. Rust's type system and Pydantic validation catch
invalid states before they reach runtime. Test suites are substantial and run in
CI; the Network Simulator alone carries 2,192 tests.

## Constraints

Projects run on commodity hardware — a Mac mini M4 Pro and Raspberry Pi nodes —
which keeps the design honest about efficiency. Multi-agent systems assume an
agent may be compromised, so defense is layered: containers, network policies,
scoped credentials, audit trails. Code is open source where possible.

---

[Back to Projects](projects)

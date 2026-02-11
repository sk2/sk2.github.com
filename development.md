---
layout: default
---

# Development Philosophy

## Motivation

I build tools to solve real problems in network automation and intelligent systems. Projects address specific needs: type-safe topology modeling, open astrophotography alternatives, robust biometric signal processing.

## Planning-First Approach

Projects use `.planning/` directories with structured planning:
- **PROJECT.md**: Core value, requirements, constraints, decisions.
- **ROADMAP.md**: Phase breakdown, goals, success criteria.
- **STATE.md**: Current position, progress, decision log, blockers.
- **Phase plans**: Detailed execution, verified before implementation.

This systematic approach prevents rework and maintains clear goals.

## Verification Loops

Formal verification concludes each phase:
- Goal-backward analysis confirms codebase delivery.
- Must-have coverage ensures all requirements are met.
- Verification documents create a permanent record of completion.

If verification fails, I fix gaps before advancing.

## Technology Choices

**Core Languages:**
- **Rust**: For performance-critical code (netvis, netsim, topogen, astro). Ensures type safety, zero-cost abstractions, robust error handling.
- **Python**: For rapid development and scientific computing (ank-pydantic, healthypi). Leverages a rich ecosystem for signal processing and network automation.
- **Swift**: For native Apple ecosystem integration (multi-agent collectors, cycle agent). Provides first-class support for iOS/tvOS/macOS.

**Key Tools:**
- **NATS**: Universal message bus for agent coordination. Features TLS 1.3, per-subject ACLs, JetStream for durability.
- **Pydantic**: Type-safe Python models with validation at definition time.
- **PyO3**: Rust-Python FFI for high-performance Python extensions.
- **petgraph**: Production-ready graph data structures in Rust.
- **FastAPI**: Modern async Python web framework.

**Testing:**
- Comprehensive test suites (286 tests in HealthyPi, 582 in netvis).
- Unit tests validate algorithms and logic.
- Integration tests verify component interaction.
- Parity tests ensure interface consistency across CLI/API/config.

## Architecture Patterns

**Message Bus Coordination:**
Projects use NATS as a universal communication layer. Agents, simulators, and services communicate via typed messages, not direct calls. This enables:
- Independent agent development and deployment.
- Security boundaries with per-subject ACLs.
- Observable message flows for debugging.
- Clean separation of concerns.

**Multi-Layer Abstraction:**
Network tools separate physical, logical, and protocol layers. This mirrors network engineering thought processes and enables independent reasoning.

**Type Safety:**
Rust's type system and Pydantic validation catch errors at compile/definition time, preventing invalid runtime states.

**Modular Design:**
Components expose clean interfaces and minimize coupling. Libraries separate core logic from rendering/export, enabling reuse and independent evolution.

## Documentation Practice

**Code-Level:**
- Clear, intent-explaining function/type names.
- Comments for non-obvious decisions.
- Doc-tests serving as examples.

**Architecture-Level:**
- PROJECT.md captures design decisions and rationale.
- STATE.md logs decision history and blockers.
- README.md provides quick-start guides and overviews.

**Research-Level:**
- RESEARCH.md documents exploration before planning.
- Links to relevant papers, tools, and prior art.
- Captures findings.

## Workflow

**Development Cycle:**
1. Research and planning (understand problem).
2. Phase design (break work into verifiable chunks).
3. Implementation (write code with tests).
4. Verification (confirm goals met).
5. Documentation (capture decisions).

**Commit Practice:**
- Atomic commits: one logical change per commit.
- Clear messages: state what and why.
- Co-authored commits credit Claude Sonnet.

**Tools:**
- Git for version control.
- pytest for Python testing.
- cargo test for Rust testing.
- GitHub Actions for CI.
- Docker for containerized agents.
- uv for Python dependency management.

## Constraints

**Resource Limits:**
Projects run on commodity hardware (Mac mini M4 Pro, Raspberry Pi). This drives efficient design.

**Security First:**
Multi-agent systems assume agents are potentially compromised. Defense-in-depth includes containers, network policies, capability tokens, and audit trails.

**Open Source:**
Code is open where possible. Tools are inspectable, modifiable, and improvable by users.

## Principles

1. **Solve real problems**: Tools address specific needs, not hypothetical use cases.
2. **Type safety**: Catch errors early through strong typing.
3. **Test thoroughly**: Comprehensive tests validate correctness.
4. **Document decisions**: Capture rationale for future reference.
5. **Plan systematically**: Phase-based execution with verification.
6. **Keep it simple**: Avoid over-engineering and unnecessary abstraction.
7. **Make it fast**: Performance matters for large-scale network topologies.
8. **Build modularly**: Clean interfaces enable reuse and evolution.

---

[Back to Projects](projects)
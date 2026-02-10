---
layout: default
---

# Development Philosophy

## Motivation

I build tools to solve real problems in network automation and intelligent systems. Each project starts from a specific need: network engineers require type-safe topology modeling, astrophotographers need open alternatives to proprietary systems, health monitoring requires robust signal processing.

## Planning-First Approach

Projects use `.planning/` directories with structured planning:

- **PROJECT.md**: Core value, requirements, constraints, key decisions
- **ROADMAP.md**: Phase breakdown with goals and success criteria
- **STATE.md**: Current position, progress tracking, decision log, blockers
- **Phase plans**: Detailed execution plans verified before implementation

This systematic approach prevents rework and maintains clear goals.

## Verification Loops

Each phase ends with formal verification:

- Goal-backward analysis: does the codebase deliver what the phase promised?
- Must-have coverage: all requirements satisfied
- Verification documents: permanent record of completion

If verification fails, I fix gaps before advancing.

## Technology Choices

**Core Languages:**
- **Rust**: Performance-critical code (netvis, netsim, topogen, astro). Type safety, zero-cost abstractions, excellent error handling.
- **Python**: Rapid development, scientific computing (ank-pydantic, healthypi). Rich ecosystem for signal processing and network automation.
- **Swift**: Native Apple ecosystem integration (multi-agent collectors, cycle agent). First-class for iOS/tvOS/macOS.

**Key Tools:**
- **NATS**: Universal message bus for agent coordination. TLS 1.3, per-subject ACLs, JetStream for durability.
- **Pydantic**: Type-safe Python models with validation at definition time.
- **PyO3**: Rust-Python FFI for high-performance Python extensions.
- **petgraph**: Production-ready graph data structures in Rust.
- **FastAPI**: Modern async Python web framework.

**Testing:**
- Comprehensive test suites (286 tests in HealthyPi, 582 in netvis)
- Unit tests validate algorithms and logic
- Integration tests verify component interaction
- Parity tests ensure interface consistency (CLI/API/config)

## Architecture Patterns

**Message Bus Coordination:**
Projects use NATS as universal communication layer. Agents, simulators, and services communicate through typed messages rather than direct calls. This enables:
- Independent agent development and deployment
- Security boundaries with per-subject ACLs
- Observable message flows for debugging
- Clean separation of concerns

**Multi-Layer Abstraction:**
Network tools separate physical, logical, and protocol layers. This mirrors how network engineers think and enables independent reasoning about each layer.

**Type Safety:**
Rust's type system and Pydantic validation catch errors at compile/definition time rather than runtime. Invalid states become unrepresentable.

**Modular Design:**
Components expose clean interfaces and minimize coupling. Libraries separate core logic from rendering/export. This enables reuse and independent evolution.

## Documentation Practice

**Code-Level:**
- Clear function/type names that explain intent
- Comments for non-obvious decisions
- Doc-tests that serve as examples

**Architecture-Level:**
- PROJECT.md captures design decisions with rationale
- STATE.md logs decision history and blockers
- README.md provides quick-start and overview

**Research-Level:**
- RESEARCH.md documents exploration before planning
- Links to relevant papers, tools, and prior art
- Captures what works and what doesn't

## Workflow

**Development Cycle:**
1. Research and planning (understand problem space)
2. Phase design (break work into verifiable chunks)
3. Implementation (write code with tests)
4. Verification (confirm goals met)
5. Documentation (capture decisions)

**Commit Practice:**
- Atomic commits: one logical change per commit
- Clear messages: what and why
- Co-authored commits credit Claude Sonnet

**Tools:**
- Git for version control
- pytest for Python testing
- cargo test for Rust testing
- GitHub Actions for CI (where applicable)
- Docker for containerized agents
- uv for Python dependency management

## Constraints

**Resource Limits:**
Projects run on commodity hardware (Mac mini M4 Pro, Raspberry Pi). This constraint drives efficient design and prevents bloat.

**Security First:**
Multi-agent systems assume agents are potentially compromised. Defense in depth with containers, network policies, capability tokens, and audit trails.

**Open Source:**
Code is open where possible. Tools should be inspectable, modifiable, and improvable by users.

## Principles

1. **Solve real problems**: Tools address specific needs, not hypothetical use cases
2. **Type safety**: Catch errors early through strong typing
3. **Test thoroughly**: Comprehensive tests validate correctness
4. **Document decisions**: Capture rationale for future reference
5. **Plan systematically**: Phase-based execution with verification
6. **Keep it simple**: Avoid over-engineering and unnecessary abstraction
7. **Make it fast**: Performance matters for large-scale network topologies
8. **Build modularly**: Clean interfaces enable reuse and evolution

---

[Back to Projects](projects)

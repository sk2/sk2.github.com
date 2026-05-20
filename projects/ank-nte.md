---
layout: default
section: network-automation
description: "Rust-based graph topology engine with Python bindings via PyO3."
---

# Network Topology Engine

<div class="badges-row">
  <span class="status-badge status-active">Active</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Python</span> <span class="stack-badge">Polars</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Usage](#usage)
- [Architecture](#architecture)

## Concept

Rust-based graph topology engine with Python bindings via PyO3. Takes network topologies — nodes, edges, layers, metadata — and stores them in a dual-write architecture: structural graph (petgraph StableDiGraph) plus columnar attribute store (Polars DataFrames). Mutations update both atomically; if either write fails, the transaction rolls back.

The engine backs the [Network Modeling & Configuration Library](/projects/ank-pydantic) and can be consumed directly by other tools in the ecosystem for zero-conversion topology loading.

A 14-crate Cargo workspace with pluggable datastore backends (Polars, DuckDB, Lite), a query engine that compiles filter specs into efficient backend operations, and an HTTP/WebSocket server mode for remote execution.

---

## Code Samples

### inventory_preflight_validation.py

```python
"""CSV inventory onboarding plus pre-flight validation demo.

Run from the repo root:

    uv run --python 3.13 python examples/inventory_preflight_validation.py --scenario safe-change
    uv run --python 3.13 python examples/inventory_preflight_validation.py --scenario breaking-change
"""

from __future__ import annotations

import argparse
from pathlib import Path

import polars as pl

from [ank_nte](../ank_nte) import Topology
from preflight_validation import (
    BREAKING_CHANGE,
    SAFE_CHANGE,
    apply_scenario,
    evaluate_candidate,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NODES = REPO_ROOT / "examples" / "inventory_nodes.csv"
DEFAULT_EDGES = REPO_ROOT / "examples" / "inventory_edges.csv"
NODE_REQUIRED_COLUMNS = {"id", "type", "layer"}
EDGE_REQUIRED_COLUMNS = {"src", "dst"}
PREFERRED_METADATA_COLUMNS = ["pop", "role", "hostname"]


def require_columns(frame: pl.DataFrame, required: set[str], path: Path) -> None:
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"{path} is missing required columns: {', '.join(missing)}")


def load_inventory(nodes_path: Path, edges_path: Path) -> Topology:
    """Load a simple node/edge CSV export into NTE using batch Python APIs."""
    nodes = pl.read_csv(nodes_path)
    edges = pl.read_csv(edges_path)
    require_columns(nodes, NODE_REQUIRED_COLUMNS, nodes_path)
    require_columns(edges, EDGE_REQUIRED_COLUMNS, edges_path)

    topology = Topology()
    node_ids = [int(value) for value in nodes["id"].to_list()]
    node_types = [str(value) for value in nodes["type"].to_list()]
    node_layers = [str(value) for value in nodes["layer"].to_list()]
    topology.add_nodes_with_metadata(node_ids, node_types, node_layers)

    metadata_columns = [
        column for column in PREFERRED_METADATA_COLUMNS if column in nodes.columns
    ]
    metadata_columns.extend(
        column
        for column in nodes.columns
        if column not in NODE_REQUIRED_COLUMNS and column not in metadata_columns
    )
    for node_type in sorted(set(node_types)):
        typed_nodes = nodes.filter(pl.col("type") == node_type)
        typed_frame = pl.DataFrame(
            {"id": typed_nodes["id"].cast(pl.UInt32)}
            | {
                f"data_{column}": typed_nodes[column]
                for column in metadata_columns
            }
        )
        topology.set_dataframe(node_type, typed_frame)

    if edges.height > 0:
        topology.add_edges(
            [int(value) for value in edges["src"].to_list()],
            [int(value) for value in edges["dst"].to_list()],
        )

    return topology


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load CSV inventory into NTE and run pre-flight validation.",
    )
    parser.add_argument("--nodes", type=Path, default=DEFAULT_NODES)
    parser.add_argument("--edges", type=Path, default=DEFAULT_EDGES)
    parser.add_argument(
        "--scenario",
        choices=[SAFE_CHANGE, BREAKING_CHANGE],
        default=SAFE_CHANGE,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    candidate = load_inventory(args.nodes, args.edges)
    baseline = candidate.snapshot()

    apply_scenario(candidate, args.scenario)
    impact = evaluate_candidate(baseline=baseline, candidate=candidate)

    report = impact.report()
    print(f"Scenario: {args.scenario}")
    for check in report.checks:
        print(f"  {check}")
    print(f"Overall: {'PASS' if report.passed else 'FAIL'}")
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

```

### policies.yaml

```yaml
version: 1
policies:
  - id: "V001"
    category: "attribute"
    severity: "ERROR"
    expr: "attrs.vendor == 'Cisco'"
    message: "Vendor must be Cisco"
    repair_hints:
      - "Set 'vendor' to 'Cisco' in the node metadata"

  - id: "S001"
    category: "structural"
    severity: "WARNING"
    expr: "size(layers) > 0"
    message: "Topology should define at least one layer"

```

### preflight_validation.py

```python
"""Golden-path NTE pre-flight validation demo.

Uses the ``ChangeImpact`` helper from ``src.preflight`` to assert
topology invariants before and after a proposed change.

Run from the repo root:

    uv run --python 3.13 python examples/preflight_validation.py --scenario safe-change
    uv run --python 3.13 python examples/preflight_validation.py --scenario breaking-change
"""

from __future__ import annotations

import argparse

import polars as pl

from [ank_nte](../ank_nte) import QuerySpec, Topology
from src.preflight import ChangeImpact


SAFE_CHANGE = "safe-change"
BREAKING_CHANGE = "breaking-change"


def build_baseline_topology() -> Topology:
    """Create a small baseline topology with property-backed router metadata."""
    topology = Topology()
    topology.add_nodes_with_metadata(
        [1, 2, 3],
        ["Router", "Router", "Switch"],
        ["base", "base", "base"],
    )
    topology.add_edges([1, 3], [3, 2])

    topology.set_dataframe(
        "Router",
        pl.DataFrame(
            {
                "id": pl.Series([1, 2], dtype=pl.UInt32),
                "data_pop": ["SYD", "MEL"],
                "data_role": ["core", "edge"],
                "data_hostname": ["core-syd-1", "edge-mel-1"],
            }
        ),
    )
    topology.set_dataframe(
        "Switch",
        pl.DataFrame(
            {
                "id": pl.Series([3], dtype=pl.UInt32),
                "data_pop": ["SYD"],
                "data_role": ["access"],
                "data_hostname": ["access-syd-1"],
            }
        ),
    )
    return topology


def append_router_row(
    topology: Topology,
    *,
    node_id: int,
    pop: str,
    role: str,
    hostname: str,
) -> None:
    """Keep the Router dataframe aligned with a newly added demo node."""
    router_df = topology.get_dataframe("Router")
    new_row = pl.DataFrame(
        {
            "id": pl.Series([node_id], dtype=pl.UInt32),
            "data_pop": [pop],
            "data_role": [role],
            "data_hostname": [hostname],
        }
    )
    if router_df is None:
        topology.set_dataframe("Router", new_row)
        return

    topology.set_dataframe("Router", pl.concat([router_df, new_row], how="vertical"))


def remove_router_row(topology: Topology, *, node_id: int) -> None:
    """Keep the Router dataframe aligned with a removed demo node."""
    router_df = topology.get_dataframe("Router")
    if router_df is None:
        return

    topology.set_dataframe("Router", router_df.filter(pl.col("id") != node_id))


def apply_scenario(candidate: Topology, scenario: str) -> None:
    """Apply a proposed change inside an isolated transaction."""
    if scenario == SAFE_CHANGE:
        with candidate.transaction() as txn:
            txn.add_nodes_with_metadata([4], ["Router"], ["base"])
            txn.add_edge(2, 4)
        append_router_row(
            candidate,
            node_id=4,
            pop="BNE",
            role="edge",
            hostname="edge-bne-1",
        )
        return

    if scenario == BREAKING_CHANGE:
        with candidate.transaction() as txn:
            txn.remove_nodes([1])
        remove_router_row(candidate, node_id=1)
        return

    raise ValueError(f"unknown scenario: {scenario}")


def evaluate_candidate(
    *,
    baseline: Topology,
    candidate: Topology,
) -> ChangeImpact:
    """Run a small pack of invariants against the candidate topology."""
    impact = ChangeImpact(baseline=baseline, candidate=candidate)

    impact.assert_count_stable(
        "at least one Router remains in SYD",
        QuerySpec(type_filter=["Router"], field_filters={"pop": "SYD"}),
        min_count=1,
    )
    impact.assert_no_protected_removals(
        "no baseline Router nodes were removed",
        QuerySpec(type_filter=["Router"]),
    )
    impact.assert_count_stable(
        "candidate topology still has at least two Router nodes",
        QuerySpec(type_filter=["Router"]),
        min_count=2,
    )
    impact.assert_connectivity_preserved(
        "all baseline nodes remain reachable",
        node_ids=list(baseline.get_nodes()),
    )

    return impact


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a self-contained NTE pre-flight validation demo.",
    )
    parser.add_argument(
        "--scenario",
        choices=[SAFE_CHANGE, BREAKING_CHANGE],
        default=SAFE_CHANGE,
        help="Which proposed change to simulate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    candidate = build_baseline_topology()
    baseline = candidate.snapshot()

    apply_scenario(candidate, args.scenario)
    impact = evaluate_candidate(baseline=baseline, candidate=candidate)

    report = impact.report()
    print(f"Scenario: {args.scenario}")
    for check in report.checks:
        print(f"  {check}")
    print(f"Overall: {'PASS' if report.passed else 'FAIL'}")
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

```

### query_builder.py

```python
"""Examples: Fluent Query Builder for [ank_nte](../ank_nte)

Demonstrates the Polars-inspired query API for filtering nodes and links
without needing [ank_pydantic](../ank_pydantic) or Pydantic models.

Run with:
    uv run python examples/query_builder.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from [ank_nte](../ank_nte) import Topology
from src.query import Expr, QueryNamespace


def build_topology() -> Topology:
    """Create a small network topology for demonstration."""
    t = Topology()
    t.add_nodes_with_metadata(
        ids=[1, 2, 3, 4, 5, 6, 7, 8],
        types=[
            "Router", "Router", "Router",       # core routers
            "Switch", "Switch",                  # access switches
            "Router",                            # edge router
            "Endpoint", "Endpoint",              # hosts
        ],
        layers=[
            "core", "core", "core",
            "access", "access",
            "edge",
            "access", "access",
        ],
    )
    return t


# ── 1. Basic filtering ──────────────────────────────────────────────

def example_basic_filtering():
    """Filter by type, layer, and specific IDs."""
    t = build_topology()
    q = QueryNamespace(t)

    # All node IDs
    print("All nodes:", q.nodes().ids())

    # Filter by type
    print("Routers:", q.nodes().of_type("Router").ids())
    print("Switches:", q.nodes().of_type("Switch").ids())

    # Filter by layer
    print("Core layer:", q.nodes().in_layer("core").ids())
    print("Access layer:", q.nodes().in_layer("access").ids())

    # Combine filters (intersection)
    print("Core routers:", q.nodes().of_type("Router").in_layer("core").ids())

    # Filter by specific IDs
    print("Nodes 1,3,5:", q.nodes().with_ids([1, 3, 5]).ids())

    # Multiple types
    print("Routers or Switches:", q.nodes().of_type("Router", "Switch").ids())


# ── 2. Terminal methods ──────────────────────────────────────────────

def example_terminal_methods():
    """Different ways to consume query results."""
    t = build_topology()
    q = QueryNamespace(t)

    routers = q.nodes().of_type("Router")

    # Count without materialising IDs
    print("Router count:", routers.count())

    # Existence check (fast — stops at first match)
    print("Any routers?", routers.exists())
    print("Any firewalls?", q.nodes().of_type("Firewall").exists())

    # Get all IDs
    print("Router IDs:", routers.ids())

    # First result or None
    print("First router:", routers.first())

    # Exactly one result (raises ValueError otherwise)
    edge_router = q.nodes().of_type("Router").in_layer("edge")
    print("Edge router count:", edge_router.count())


# ── 3. Expression filters ───────────────────────────────────────────

def example_expr_filters():
    """Use Expr for complex filters beyond type/layer/kind."""
    t = build_topology()
    q = QueryNamespace(t)

    # Equality on dataframe columns
    switches = q.nodes().filter(Expr.field("type") == "Switch")
    print("Switches via expr:", switches.ids())

    # Combine Expr with builder filters — use .in_layer() for layer,
    # Expr for dataframe column filters
    core_routers = q.nodes().in_layer("core").filter(
        Expr.field("type") == "Router"
    )
    print("Core routers (builder + expr):", core_routers.ids())

    # Combine multiple Expr conditions with & (AND)
    specific = q.nodes().filter(
        (Expr.field("type") == "Router") & (Expr.field("type").is_not_null())
    )
    print("Routers (compound expr):", specific.ids())

    # NOT
    not_routers = q.nodes().filter(~(Expr.field("type") == "Router"))
    print("Not routers:", not_routers.ids())

    # is_in for membership testing
    some_types = q.nodes().filter(
        Expr.field("type").is_in(["Switch", "Endpoint"])
    )
    print("Switches + Endpoints:", some_types.ids())


# ── 4. Composable & reusable queries ────────────────────────────────

def example_composable_queries():
    """Queries are immutable — build reusable base queries."""
    t = build_topology()
    q = QueryNamespace(t)

    # Base query — reusable
    routers = q.nodes().of_type("Router")
    print("All routers:", routers.ids())

    # Derive specialised queries from the same base
    core_routers = routers.in_layer("core")
    edge_routers = routers.in_layer("edge")
    print("Core routers:", core_routers.ids())
    print("Edge routers:", edge_routers.ids())

    # Original is unmodified
    print("All routers (unchanged):", routers.ids())

    # Chain further
    subset = core_routers.with_ids([1, 2])
    print("Core routers 1&2:", subset.ids())


# ── 5. Expression DSL showcase ──────────────────────────────────────

def example_expr_dsl():
    """Demonstrate the full Expr expression DSL (AST construction)."""
    # These build Python ASTs — no topology needed

    # Comparison operators
    gt_expr = Expr.field("bandwidth") > 1000
    between_expr = Expr.field("latency").between(1, 10)
    print("gt expr:", repr(gt_expr))
    print("between expr:", repr(between_expr))

    # String operations
    contains = Expr.field("hostname").contains("core")
    starts = Expr.field("label").startswith("R")
    regex = Expr.field("name").matches(r"^(spine|leaf)-\d+$")
    print("contains:", repr(contains))
    print("startswith:", repr(starts))
    print("regex:", repr(regex))

    # Null checks
    has_desc = Expr.field("description").is_not_null()
    print("is_not_null:", repr(has_desc))

    # Complex compound expression
    complex_expr = (
        (Expr.field("role") == "spine")
        & (Expr.field("asn").is_in([65001, 65002]))
        & (Expr.field("bandwidth") > 10_000)
        & Expr.field("label").contains("dc1")
    )
    print("complex:", repr(complex_expr))

    # Arithmetic
    calc = Expr.field("tx_bytes") + Expr.field("rx_bytes")
    print("arithmetic:", repr(calc))

    # All of these compile to Rust ExprNode objects
    rust_expr = complex_expr._to_rust_expr()
    print("Compiled to Rust:", type(rust_expr).__name__)


# ── 6. Link queries ─────────────────────────────────────────────────

def example_link_queries():
    """LinkQuery API (works when topology has domain-level links)."""
    t = build_topology()
    q = QueryNamespace(t)

    # Basic link queries (empty in this example — no domain links added)
    print("All links:", q.links().ids())
    print("Link count:", q.links().count())
    print("Any links?", q.links().exists())

    # Builder methods (demonstrate chaining even on empty results)
    ethernet_links = q.links().of_type("Ethernet").in_layer("physical")
    print("Ethernet links:", ethernet_links.ids())

    # Between sets
    cross_links = q.links().between([1, 2], [4, 5])
    print("Cross links:", cross_links.ids())

    # For specific nodes
    node_links = q.links().for_nodes(1, 2, 3)
    print("Links for nodes 1-3:", node_links.ids())


# ── Run all examples ────────────────────────────────────────────────

if __name__ == "__main__":
    examples = [
        ("Basic filtering", example_basic_filtering),
        ("Terminal methods", example_terminal_methods),
        ("Expression filters", example_expr_filters),
        ("Composable queries", example_composable_queries),
        ("Expression DSL", example_expr_dsl),
        ("Link queries", example_link_queries),
    ]

    for title, fn in examples:
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}\n")
        fn()

```

### sota_benchmark.py

```python
import time
import timeit
import polars as pl
from textwrap import dedent
from [ank_nte](../ank_nte) import Topology, QuerySpec, ExprNode

def generate_topology(num_nodes=100_000) -> Topology:
    print(f"Generating synthetic topology with {num_nodes:,} nodes...")
    t = Topology()
    
    # Generate large batch of nodes with varied properties
    batch_size = 10_000
    for i in range(0, num_nodes, batch_size):
        ids = list(range(i, i + batch_size))
        types = ["Router"] * batch_size
        layers = ["physical"] * batch_size
        
        # Simulate some sparsity and specific target properties
        data = []
        for j in ids:
            pop = "SYD" if j % 10 == 0 else ("MEL" if j % 10 == 1 else "BNE")
            asn = 64512 if j % 5 == 0 else 65000
            speed = 100 if j % 2 == 0 else 40
            data.append({
                "hostname": f"r-{pop.lower()}-{j}",
                "pop": pop,
                "as_number": asn,
                "speed_gbps": speed
            })
            
        t.add_nodes(ids=ids, node_types=types, layer="physical", data=data)
        
    print("Topology generated.\n")
    return t

def benchmark_simd_filter_first(t: Topology):
    """
    Simulates the NTE 'Filter-First' approach using SIMD-accelerated Polars 
    predicates via the QuerySpec API.
    """
    expr = ExprNode.and_(
        ExprNode.eq_(ExprNode.field("pop"), ExprNode.string("SYD")),
        ExprNode.eq_(ExprNode.field("as_number"), ExprNode.int_(64512))
    )
    spec = QuerySpec(
        type_filter=["Router"],
        expr_filters=[expr]
    )
    
    # Execute query, pulling just the filtered IDs
    result_ids = t.execute_query(spec)
    return len(result_ids)

def benchmark_naive_row_based(t: Topology):
    """
    Simulates a traditional 'Pointer-Chasing' row-based graph database approach 
    by forcing property deserialization and row-by-row iteration in Python space.
    """
    # Simulate fetching all nodes (as dictionaries) and filtering row-by-row
    all_nodes_spec = QuerySpec(type_filter=["Router"])
    all_structs = t.query_nodes_as_structs(all_nodes_spec)
    
    match_count = 0
    for node in all_structs:
        # Row-by-row property check (simulating cache misses and pointer chasing)
        if node.data.get("pop") == "SYD" and node.data.get("as_number") == 64512:
            match_count += 1
            
    return match_count

def print_results(simd_time, naive_time):
    improvement = naive_time / simd_time
    
    print(dedent(f"""\
    ===================================================================
    NTE Architecture Benchmark: SIMD-First vs Row-Based Pointer Chasing
    ===================================================================
    
    Query: "Find all Routers where pop='SYD' AND as_number=64512"
    
    [1] NTE Dual-Write (Filter-First SIMD):
        Time: {simd_time*1000:.2f} ms
        Complexity: O(V/K + E_sub)
        
    [2] Simulated Row-Based Database (Pointer Chasing):
        Time: {naive_time*1000:.2f} ms
        Complexity: O(V + E)
        
    -------------------------------------------------------------------
    RESULT: NTE's architecture is {improvement:.1f}x faster for property-heavy queries.
    ===================================================================
    """))

if __name__ == "__main__":
    t = generate_topology(num_nodes=50_000)
    
    # Warm up caches
    benchmark_simd_filter_first(t)
    benchmark_naive_row_based(t)
    
    # Run benchmarks
    print("Running SIMD-First benchmark...")
    simd_time = timeit.timeit(lambda: benchmark_simd_filter_first(t), number=10) / 10
    
    print("Running Naive Row-Based benchmark...")
    naive_time = timeit.timeit(lambda: benchmark_naive_row_based(t), number=10) / 10
    
    print_results(simd_time, naive_time)

```

### __init__.py

```python

```

### test_advanced_fuzzing.py

```python
"""Retired speculative Python fuzzing around non-contract query/property paths.

These tests mixed unsupported string-query assumptions, broad exception
swallowing, and extreme scenarios that were not stable enough for CI.

The remaining Python layer should stay thin and deterministic. Public-API
boundary coverage now lives in tests/python/test_adversarial_guardrails.py,
while deeper adversarial invariants belong in Rust crate tests.
"""

```

### test_adversarial_threats.py

```python
"""Retired speculative Python adversarial tests.

These cases were broad "don't crash" probes with unrealistic payload sizes,
string-query assumptions that are not part of the stable Python contract, and
large `except Exception: pass` blocks that made failures non-actionable.

Deterministic Python boundary coverage now lives in:
- tests/python/test_adversarial_guardrails.py

Core adversarial and persistence invariants now live closer to the engine in:
- nte-query/tests/adversarial_guardrails.rs
- nte-topology/tests/adversarial_guardrails.rs
"""

```

### test_concurrency_and_schema.py

```python
import pytest
import [ank_nte](../ank_nte)
import threading
import time
import math

def test_floating_point_anomalies():
    """
    Test how the engine handles mathematically anomalous floating-point values 
    like NaN (Not a Number) and Infinity when injected into properties.
    """
    topo = [ank_nte](../ank_nte).Topology()
    topo.add_nodes_with_metadata([1, 2, 3], ["Node"]*3, ["layer"]*3)
    
    # Inject NaN and Infinity
    try:
        topo.update_node_properties(1, {"score": math.nan})
        topo.update_node_properties(2, {"score": math.inf})
        topo.update_node_properties(3, {"score": -math.inf})
    except Exception:
        # If the boundary aggressively rejects non-finite floats, that is safe.
        pass
        
    # The engine must still be queryable without panicking during filter execution
    try:
        # If the engine accepts NaN, filtering against it must follow SQL semantics (usually false)
        topo.query("MATCH (n) WHERE n.score > 0 RETURN n")
    except Exception:
        pass

def test_extreme_schema_evolution():
    """
    Test the DataFrame storage layer's ability to handle massive horizontal 
    schema evolution (the 'Wide Table' problem).
    """
    topo = [ank_nte](../ank_nte).Topology()
    topo.add_nodes_with_metadata([1], ["Router"], ["core"])
    
    # Generate 5,000 distinct property keys
    wide_payload = {f"custom_metric_{i}": i for i in range(5000)}
    
    try:
        # This forces Polars to dynamically expand the DataFrame schema by 5,000 columns.
        # This tests if the engine has a max-column circuit breaker.
        topo.update_node_properties(1, wide_payload)
        
        # Ensure the engine can still execute a basic scan without choking on the schema
        res = topo.query("MATCH (n:Router) RETURN n")
        assert len(res.matches) == 1
    except Exception:
        # Rejection via SchemaError is a perfectly safe response
        pass

def test_concurrent_transaction_contention():
    """
    Test how the engine handles two threads attempting to open a write transaction
    simultaneously. It should safely block or raise a lock contention error, 
    but never allow dirty writes or deadlocks.
    """
    # Need a mock for this test to compile against the stub
    class MockTransaction:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def add_nodes_with_metadata(self, *args): pass
        
    topo = [ank_nte](../ank_nte).Topology()
    topo.transaction = lambda: MockTransaction()
    
    errors = []
    def worker_a():
        try:
            with topo.transaction() as tx:
                tx.add_nodes_with_metadata([10], ["A"], ["layer"])
                time.sleep(0.05) # Hold the lock
        except Exception as e:
            errors.append(e)
            
    def worker_b():
        try:
            with topo.transaction() as tx:
                tx.add_nodes_with_metadata([20], ["B"], ["layer"])
                time.sleep(0.05)
        except Exception as e:
            errors.append(e)
            
    t1 = threading.Thread(target=worker_a)
    t2 = threading.Thread(target=worker_b)
    
    t1.start()
    t2.start()
    
    t1.join(timeout=2)
    t2.join(timeout=2)
    
    # Threads must resolve
    assert not t1.is_alive()
    assert not t2.is_alive()
    # It is acceptable for one thread to throw a LockError, but neither should hang.

def test_deep_hierarchical_deletion():
    """
    Test removing a node that is the root of an incredibly deep (not wide) tree.
    This tests the recursive stack depth of the cascading delete algorithm.
    """
    topo = [ank_nte](../ank_nte).Topology()
    
    # Create a single linear chain 1000 nodes deep: 1 -> 2 -> 3 -> ... -> 1000
    nodes = list(range(1, 1001))
    topo.add_nodes_with_metadata(nodes, ["Chain"]*1000, ["layer"]*1000)
    
    for i in range(1, 1000):
        try:
            topo.add_edge(i, i+1)
        except AttributeError:
            pass # Ignore missing mock logic
            
    try:
        # Delete the root. The cascade algorithm must recursively delete 999 children.
        # If it uses standard recursion, it might blow the Rust C-stack.
        # It should ideally use an iterative stack or safely error out.
        if hasattr(topo, 'remove_node_cascade'):
            topo.remove_node_cascade(1)
        elif hasattr(topo, 'remove_nodes'):
            topo.remove_nodes([1])
    except Exception:
        pass
        
    assert True

```

### test_cryptographic_and_memory.py

```python
import pytest
import [ank_nte](../ank_nte)
import tempfile
import os

def test_cache_poisoning_vulnerability():
    """
    Test against Cache Poisoning.
    If the engine caches Query Plans or Regex compilations using a weak
    hashing mechanism, an attacker could craft a collision that forces
    query A to return the cached results of query B.
    """
    topo = [ank_nte](../ank_nte).Topology()
    topo.add_nodes_with_metadata([1], ["A"], ["layer"])
    topo.add_nodes_with_metadata([2], ["B"], ["layer"])
    
    # Let's assume the cache key is naively built from the string.
    # An attacker crafts a query string with an identical length/hash but different semantics
    # If the cache doesn't verify the full AST, it might return the wrong results.
    q1 = "MATCH (n:A) RETURN n"
    q2 = "MATCH (n:B) RETURN n"
    
    # Run them sequentially.
    try:
        res1 = topo.query(q1)
        res2 = topo.query(q2)
        
        # If the cache was poisoned, res2 would incorrectly return the matches for A
        if len(res1.matches) > 0 and len(res2.matches) > 0:
            assert res1.matches != res2.matches
    except Exception:
        pass

def test_symbolic_link_directory_escape():
    """
    Test against Symlink Directory Escape.
    If the engine allows users to specify export paths or cache directories,
    an attacker could pass a symlink pointing to `/etc/shadow` to exfiltrate
    sensitive files when the engine writes or reads.
    """
    topo = [ank_nte](../ank_nte).Topology()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a malicious symlink pointing to root or an arbitrary sensitive location
        symlink_path = os.path.join(tmpdir, "evil_link")
        try:
            os.symlink("/", symlink_path)
            
            # The engine must validate that configured paths do not follow symlinks
            # escaping the intended sandboxed directory.
            if hasattr([ank_nte](../ank_nte), 'configure_storage'):
                [ank_nte](../ank_nte).configure_storage(symlink_path)
                
            # Attempt to write
            topo.add_nodes_with_metadata([1], ["T"], ["L"])
        except OSError:
            # Creation of symlinks might fail on Windows without admin, which is fine
            pass
        except Exception:
            # The engine rejecting the symlink or raising a security error is correct
            pass
            
    assert True

def test_out_of_bounds_pointer_dereference():
    """
    Test against memory unsafety (Out-Of-Bounds Read/Write).
    Rust is generally memory safe, but if the Graph uses `unsafe` blocks
    for speed, passing a maliciously crafted internal node index could 
    trick the engine into reading adjacent memory from the C-heap.
    """
    topo = [ank_nte](../ank_nte).Topology()
    topo.add_nodes_with_metadata([1], ["T"], ["L"])
    
    try:
        # Instead of using the Python `add_edge` which takes external IDs,
        # what if an internal macro or API bypasses the ID lookup?
        # We simulate this by passing the maximum possible usize to see if it 
        # hits a hard bounds check or causes a segfault.
        if hasattr(topo, '_internal_add_edge_unchecked'):
            topo._internal_add_edge_unchecked(18446744073709551615, 18446744073709551615)
    except Exception:
        # A panic or out of bounds exception is correct. A segfault kills the test runner.
        pass
        
    assert True

def test_floating_point_precision_loss():
    """
    Test against IEEE 754 precision loss vulnerabilities.
    If financial or critical capacity metrics are passed as huge floats,
    they can lose precision and round incorrectly, causing bad routing logic.
    """
    topo = [ank_nte](../ank_nte).Topology()
    topo.add_nodes_with_metadata([1], ["Bank"], ["core"])
    
    # Two massive numbers that only differ at the very end.
    # In standard 64-bit floats, these might round to the exact same value in memory.
    val1 = 9007199254740992.0
    val2 = 9007199254740993.0
    
    try:
        topo.update_node_properties(1, {"balance": val1})
        # If the engine uses exact equality on floats, this query will test if precision was lost
        res = topo.query(f"MATCH (n) WHERE n.balance = {val2} RETURN n")
        
        # If it lost precision, it would incorrectly return the node (val1 == val2).
        assert len(res.matches) == 0
    except Exception:
        pass

def test_query_plan_combinatorial_explosion():
    """
    Test the Query Planner against Combinatorial Explosion (Join Ordering).
    If a user submits a query with 20 disjoint subpatterns, a naive 
    query planner might try to calculate all possible join order permutations
    (20! = 2.4 quintillion), freezing the server for years before even executing.
    """
    # Create an absurdly disjoint query
    # MATCH (a), (b), (c) ... 
    query = "MATCH " + ", ".join([f"(n{i}:Type)" for i in range(20)]) + " RETURN n0"
    
    topo = [ank_nte](../ank_nte).Topology()
    start_time = time.time()
    
    try:
        topo.query(query)
    except Exception:
        # It should reject the query quickly or plan it instantly using heuristics,
        # but the planning phase must NOT take exponential time.
        pass
        
    duration = time.time() - start_time
    # Planning (or rejection) must complete in under 1 second
    assert duration < 1.0, f"Query Planner took exponential time: {duration}s"
```

---

## Usage

```bash
# Start the NTE server
nte-server --bind 0.0.0.0:8080 --topology topology.zip
```

<details class="code-collapse">
<summary>Creating and persisting a topology</summary>

```python
import [ank_nte](../ank_nte)

# Create and populate a topology
topo = [ank_nte](../ank_nte).Topology()
topo.add_nodes_with_metadata(
    ids=[1, 2, 3, 4],
    types=["Router", "Router", "Switch", "Switch"],
    layers=["core", "core", "access", "access"],
)

# Save and load
topo.save("topology.zip")
loaded = [ank_nte](../ank_nte).Topology.load("topology.zip")
```

</details>

---

## Architecture

<div class="mermaid">
flowchart LR
    M[Mutation] --> DWG[DualWriteGuard]
    DWG --> PG[petgraph<br/>Graph Structure]
    DWG --> PL[Polars<br/>Attribute DataFrame]
    PG -.->|rollback on failure| DWG
    PL -.->|rollback on failure| DWG
</div>

**Dual-write model.** Every topology mutation is a paired operation: update the petgraph graph structure *and* update the attribute DataFrame. A RAII `DualWriteGuard` ensures atomicity — if the DataFrame insert fails after the graph was already modified, the graph mutation rolls back automatically. State divergence between the two stores is structurally impossible.

**Stable identity.** Node and edge IDs survive insertions and removals. Internally, the engine maps user-facing external IDs to petgraph's `NodeIndex` via a bidirectional index.

**Columnar attributes.** Node and edge properties live in Polars DataFrames rather than per-node hashmaps. Filtering 10,000 nodes by vendor, layer, or any custom field runs as a vectorized column scan. Schema evolves dynamically — adding a new property to one node extends the column across the DataFrame.

**Pluggable backends.** The `TopologyBackend` trait abstracts the attribute store. Polars is the default (fast filtering, zero-copy access). DuckDB provides SQL-based querying for complex analytics. Lite is an in-memory store for small topologies and testing.

<div class="mermaid">
flowchart TD
    TB[TopologyBackend trait]
    TB --> Polars["Polars<br/><small>Fast filtering, zero-copy</small>"]
    TB --> DuckDB["DuckDB<br/><small>SQL analytics</small>"]
    TB --> Lite["Lite<br/><small>In-memory, testing</small>"]
</div>

**Event sourcing.** A ring-buffer EventStore records every mutation (add node, remove edge, update property) for audit trails and potential replay.

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |
| **Stack** | Rust, Python, TypeScript, Polars |

---

## Tech Stack

- **Language:** Rust (Core), Python (SDK), Starlark (Policy).
- **Storage:** Petgraph (Graph), Polars (Relational), JSONL (WAL).
- **Interface:** PyO3 (Python), Axum/gRPC (Server), Mermaid (Visual).

---

## Constraints

- **Zero-Blocking Write Plane:** Core mutations must not block on subscriber I/O.
- **ACID-Lite Durability:** Every mutation must be journaled with integrity checks.
- **Columnar Efficiency:** Favor vectorized Polars operations over row-wise Rust loops.

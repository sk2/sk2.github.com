---
layout: default
section: data-analytics
description: "DataRaster turns massive spatial datasets into density maps, raster tiles, and analysis outputs."
---

# DataRaster (data-raster)

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-03-22</span>
  <span class="stack-badge">Rust</span> <span class="stack-badge">Polars</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Visuals](#visuals)
- [Architecture](#architecture)
- [Current Status](#current-status)

## Concept

DataRaster turns massive spatial datasets into density maps, raster tiles, and
analysis outputs. It is built for the point where browser-side SVG, notebook
scripts, and hand-rolled Python pipelines stop scaling — a compiled backend for
dense point, line, and polygon rendering.

The shortest framing, for anyone who knows Datashader: DataRaster is a
deployment-friendly backend for the same class of dense spatial rendering, with
a tile server, Python bindings, and diagnostics built around it. It replaces the
rendering-and-serving middle of a typical stack — query, pull into Python,
render with Datashader or matplotlib, export tiles, serve them — with one engine
that reads the source data and renders or serves directly.

![Global earthquake density rendered by DataRaster](/images/datavis-earthquakes.png)
*Every recorded earthquake epicentre as a density map. Plate boundaries emerge
from the raw point cloud with no point-by-point drawing.*

---

## Code Samples

### README.md

```markdown
# DataRaster Examples

Checked-in showcase documents for the current `2.0` feature set.

Run the commands below from the repo root.

## Visual Gallery

Start here if you want output you can look at immediately.

Files:

- `examples/gallery/showcase/README.md` is the real-data hero gallery.
- `examples/gallery/README.md` explains the full gallery split.
- `examples/gallery/generate-gallery.sh` regenerates the synthetic/fixture feature artifacts.

Coverage:

- real-data density and line renders from earthquakes, AIS shipping, flights, and Citibike
- small reproducible feature demos for declarative render, geospatial projection, adaptive clip selection, weighted aggregation, outlier-aware bounds, line bundling, and temporal frame sequences

## Case Studies

Start here if you want a user-shaped story rather than a raw example.

Files:

- `examples/case-studies/README.md` indexes the adoption-oriented case studies.
- `examples/case-studies/datashader-migration.md` covers the Python/Datashader migration path.
- `examples/case-studies/live-map-tiles.md` covers external MapLibre tile consumption.
- `examples/case-studies/cloud-tiles.md` covers object-storage rendering and PMTiles.
- `examples/case-studies/operational-benchmark.md` covers the benchmark protocol.
- `examples/case-studies/dense-mobility.md`, `maritime-ais.md`, and `earthquake-catalog.md` package the real-data showcase images into domain stories.

What this demonstrates:

- how the existing test data maps to real adoption questions
- which visualization mode fits each data shape
- what to ask users when validating the wedge

## Visualization Cookbook

Start here if you want to know every useful way to visualize the local test data.

Files:

- `examples/cookbook/README.md` maps data shapes to visualization modes and commands.

What this demonstrates:

- density, weighted density, adaptive clipping, contours, outlier-safe bounds, line bundling, temporal frames, projections, choropleths, live tiles, and diff/review workflows
- which checked-in fixtures and generated outputs exercise each mode

## Movement Insights

Start here if you want time-series plots, origin/destination lines, isometric
arc views, and ffmpeg-ready frames from local fixtures.

Files:

- `examples/movement-insights/README.md` explains the generated plates and movie
  workflow.
- `examples/movement-insights/generate_movement_insights.py` regenerates the
  stills, PNG frame sequence, and MP4 when `ffmpeg` is installed.

What this demonstrates:

- common start/end points in OD data
- straight-line corridor density versus isometric arc readability
- temporal counts, moving centroids, and frame rendering for video compression

## Scale And Profiling

Start here if you want the large-dataset workflow.

Files:

- `examples/profile/README.md` explains the `profile -> scaffold -> render` path.
- `examples/profile/generate-profile-artifacts.sh` regenerates the checked-in 1M artifacts and optional 5M profile outputs.

What this demonstrates:

- profiling large local datasets before guessing render settings
- scaffold generation for starter specs
- a first-pass million-row render with captured outputs
- a clean escalation path to `benchmark_5m.parquet`

## Tile Server Quickstart

Start here if you want the shortest backend-to-map path.

Files:

- `examples/tiles/README.md` walks through `benchmark_1m.parquet -> tile server -> TileJSON -> MapLibre`
- `examples/tiles/maplibre-demo.html` is a checked-in external MapLibre consumer page

What this demonstrates:

- single-dataset tile serving from a local parquet file
- the built-in viewer as a local smoke test
- the real adoption path: feeding tiles into an existing frontend

## Python Quickstart

Start here if your current workflow is dataframe-first.

Files:

- `examples/python/README.md` walks through `benchmark_1m.parquet -> Polars -> rendered PNG`

What this demonstrates:

- replacing a Datashader-style raster step without changing the rest of the Python workflow
- rendering directly from an in-memory dataframe
- using the same large local benchmark dataset as the tile and profiling guides

## Benchmark Comparison

Start here if you want a reproducible Datashader-style baseline.

Files:

- `examples/benchmark/README.md` explains the protocol and fairness rules
- `examples/benchmark/compare_renderers.py` runs the end-to-end harness
- `examples/benchmark/render_with_datashader.py` is the reference Datashader runner

What this demonstrates:

- same parquet input, same dimensions, same count-aggregation contract
- CPU-only subprocess timing for DataRaster vs a Datashader reference pipeline
- generated JSON output with timing, memory, and command metadata

## Geospatial Projection

Start here if you want a small map-like example with a real underlay.

Files:

- `examples/geospatial/README.md` explains the projection comparison.
- `examples/geospatial/world-graticule.geojson` is the checked-in line underlay.

What this demonstrates:

- direct rendering from GeoJSON point features
- line-underlay compositing from GeoJSON
- the visual difference between `linear` and `web-mercator`

## Workbench Walkthrough

Start here if you want to exercise the document workflow end to end.

Files:

- `examples/workbench/README.md` walks through lint, fix previews, save, and semantic diff.
- `examples/diagnostic-fixes/fixable-diff.dr.yaml` intentionally triggers `W002`, `W003`, and `diff_requires_diverging_style`.
- `examples/diagnostic-fixes/fixed-diff.dr.yaml` shows the same document after applying the suggested fixes.

Try the flow:

```bash
cargo run -p data-raster-cli -- lint examples/diagnostic-fixes/fixable-diff.dr.yaml
cargo run -p data-raster-ui --bin data-raster-workbench -- examples/diagnostic-fixes/fixable-diff.dr.yaml
cargo run -p data-raster-cli -- diff \
  examples/diagnostic-fixes/fixable-diff.dr.yaml \
  examples/diagnostic-fixes/fixed-diff.dr.yaml
```

What this demonstrates:

- `lint` surfaces the same fixable diagnostics the workbench exposes
- the diagnostics panel can apply individual fixes or `Apply All`
- `diff` shows the semantic review surface for the before/after document pair

## Dataset Tiers

Keep the repo examples opinionated:

- tiny checked-in fixtures for docs and tests
- medium checked-in gallery data for visually compelling renders
- larger benchmark inputs for profiling and scale testing

Existing large local data already fits that last bucket:

- `benchmark_1m.parquet`
- `benchmark_5m.parquet`

```

### README.md

```markdown
# DataRaster Benchmark Comparison

This benchmark compares the same class of work in two end-to-end CPU paths:

- DataRaster CLI rendering `benchmark_1m.parquet` directly to PNG
- a reference Datashader pipeline that reads the same parquet file and writes a PNG

It is intentionally a static render comparison, not a tile server benchmark.

## What This Demonstrates

- the baseline `Parquet -> aggregate count -> shade -> PNG` path
- one cold run plus repeated warm runs for both renderers
- wall-clock timing and peak RSS captured the same way for both subprocesses
- generated PNG outputs and a machine-readable JSON report

## Fairness Rules

This first-pass benchmark stays narrow on purpose:

- dataset: `benchmark_1m.parquet`
- columns: `x`, `y`
- projection: linear
- output size: `818x407`
- aggregation: count
- execution mode: CPU-only
- deliverable: PNG image

The two outputs are not expected to be pixel-identical. They are benchmarked as
equivalent reference pipelines, not as exact renderer clones.

DataRaster uses:

- `--transfer eq-hist`
- `--colormap plasma`
- `--clip standard`

The Datashader reference uses:

- `shade(..., how="eq_hist")`
- a fixed plasma-like palette
- black background applied before PNG export

## Prerequisites

Build the release CLI once from the repo root:

```bash
cargo build --release -p data-raster-cli
```

The Python side expects these packages in the active environment:

- `datashader`
- `pandas`
- `psutil`

The local benchmark harness also applies a small `numba` compatibility shim
before importing Datashader so the reference pipeline still runs under this
Python 3.13 environment.

## Run The Benchmark

From the repo root:

```bash
python3 examples/benchmark/compare_renderers.py \
  --dataset benchmark_1m.parquet \
  --dataraster-bin target/release/data-raster
```

Default policy:

- `1` cold run
- `5` warm runs
- JSON report written to `examples/benchmark/generated/benchmark_1m-results.json`

If you want a faster smoke run while iterating on the harness:

```bash
python3 examples/benchmark/compare_renderers.py \
  --dataset benchmark_1m.parquet \
  --dataraster-bin target/release/data-raster \
  --warm-runs 1
```

## Generated Outputs

The harness writes:

- per-run PNGs for each renderer
- a JSON report with environment metadata, exact commands, and per-run metrics

The default output directory is:

- `examples/benchmark/generated/`

## Notes

- this benchmark is scoped to the first adoption story, not full feature parity
- GPU numbers should be recorded separately if added later
- `benchmark_5m.parquet` can be used later as the stretch dataset once the 1M path is stable

```

### compare_renderers.py

```python
#!/usr/bin/env python3
"""Compare DataRaster CLI and a Datashader reference pipeline.

This harness measures end-to-end subprocess runs from parquet input to PNG
output. It records one cold run plus a configurable number of warm runs for
both renderers and writes a JSON report with timing, peak RSS, and command
metadata.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import statistics
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import psutil


DEFAULT_WIDTH = 818
DEFAULT_HEIGHT = 407
DEFAULT_TRANSFER = "eq_hist"
DEFAULT_COLORMAP = "plasma"
DEFAULT_CLIP = "standard"
DEFAULT_BG_COLOR = "000000"
DEFAULT_X_COL = "x"
DEFAULT_Y_COL = "y"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def cargo_target_directory(root: Path) -> Path | None:
    try:
        metadata = json.loads(
            subprocess.check_output(
                ["cargo", "metadata", "--no-deps", "--format-version", "1"],
                cwd=root,
                text=True,
            )
        )
    except Exception:
        return None
    return Path(metadata["target_directory"])


def import_datashader_with_compat():
    """Import Datashader after stripping numba's cache=True decorators."""
    import numba

    orig_jit = numba.jit
    orig_njit = numba.njit

    def no_cache_jit(*args, **kwargs):
        kwargs.pop("cache", None)
        return orig_jit(*args, **kwargs)

    def no_cache_njit(*args, **kwargs):
        kwargs.pop("cache", None)
        return orig_njit(*args, **kwargs)

    numba.jit = no_cache_jit
    numba.njit = no_cache_njit

    import datashader as ds

    return ds


@dataclass
class RunResult:
    renderer: str
    phase: str
    index: int
    command: list[str]
    returncode: int
    wall_seconds: float
    peak_rss_bytes: int
    output_path: str
    output_size_bytes: int | None
    stdout: str
    stderr: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", required=True, help="Path to parquet dataset")
    parser.add_argument(
        "--dataraster-bin",
        default="target/release/data-raster",
        help="Path to the built DataRaster CLI binary",
    )
    parser.add_argument(
        "--output-dir",
        default="examples/benchmark/generated",
        help="Directory for generated PNGs and JSON reports",
    )
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH)
    parser.add_argument("--height", type=int, default=DEFAULT_HEIGHT)
    parser.add_argument("--x-col", default=DEFAULT_X_COL)
    parser.add_argument("--y-col", default=DEFAULT_Y_COL)
    parser.add_argument("--cold-runs", type=int, default=1)
    parser.add_argument("--warm-runs", type=int, default=5)
    return parser.parse_args()


def require_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    root = repo_root()
    dataset = (root / args.dataset).resolve()
    if not dataset.exists():
        raise SystemExit(f"Missing dataset: {dataset}")

    dataraster_bin = (root / args.dataraster_bin).resolve()
    if not dataraster_bin.exists() and not Path(args.dataraster_bin).is_absolute():
        target_dir = cargo_target_directory(root)
        if target_dir is not None:
            relative = Path(args.dataraster_bin)
            if relative.parts and relative.parts[0] == "target":
                dataraster_bin = (target_dir / Path(*relative.parts[1:])).resolve()
    if not dataraster_bin.exists():
        raise SystemExit(
            f"Missing DataRaster binary: {dataraster_bin}\n"
            "Build it first with: cargo build --release -p data-raster-cli"
        )

    output_dir = (root / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    return dataset, dataraster_bin, output_dir


def dataraster_command(
    binary: Path,
    dataset: Path,
    output: Path,
    x_col: str,
    y_col: str,
    width: int,
    height: int,
) -> list[str]:
    return [
        str(binary),
        "render",
        str(dataset),
        "-o",
        str(output),
        "--quiet",
        "--x-col",
        x_col,
        "--y-col",
        y_col,
        "--width",
        str(width),
        "--height",
        str(height),
        "--projection",
        "linear",
        "--transfer",
        "eq-hist",
        "--colormap",
        DEFAULT_COLORMAP,
        "--clip",
        DEFAULT_CLIP,
        "--spread",
        "0",
        "--bg-color",
        DEFAULT_BG_COLOR,
    ]


def datashader_command(
    dataset: Path,
    output: Path,
    x_col: str,
    y_col: str,
    width: int,
    height: int,
) -> list[str]:
    script = repo_root() / "examples/benchmark/render_with_datashader.py"
    return [
        sys.executable,
        str(script),
        "--input",
        str(dataset),
        "--output",
        str(output),
        "--x-col",
        x_col,
        "--y-col",
        y_col,
        "--width",
        str(width),
        "--height",
        str(height),
    ]


def current_tree_state(root: Path) -> dict[str, Any]:
    try:
        commit = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                text=True,
            )
            .strip()
        )
        dirty = subprocess.run(
            ["git", "diff", "--quiet"],
            cwd=root,
            check=False,
        ).returncode != 0
        return {"git_commit": commit, "git_dirty": dirty}
    except Exception:
        return {"git_commit": None, "git_dirty": None}


def environment_metadata() -> dict[str, Any]:
    ds = import_datashader_with_compat()
    import numba
    import pyarrow

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "platform": platform.platform(),
        "python": sys.version,
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "cpu_count_physical": psutil.cpu_count(logical=False),
        "pandas_version": pd.__version__,
        "psutil_version": psutil.__version__,
        "pyarrow_version": pyarrow.__version__,
        "numba_version": numba.__version__,
        "datashader_version": ds.__version__,
    }


def total_rss_bytes(proc: psutil.Process) -> int:
    total = 0
    procs = [proc]
    try:
        procs.extend(proc.children(recursive=True))
    except (psutil.Error, PermissionError):
        pass
    for child in procs:
        try:
            total += child.memory_info().rss
        except psutil.Error:
            continue
    return total


def measure_command(command: list[str], cwd: Path, output: Path, phase: str, index: int, renderer: str) -> RunResult:
    if output.exists():
        output.unlink()

    started = time.perf_counter()
    process = psutil.Popen(
        command,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    peak_rss = 0
    while process.poll() is None:
        try:
            peak_rss = max(peak_rss, total_rss_bytes(process))
        except psutil.Error:
            pass
        time.sleep(0.05)

    stdout, stderr = process.communicate()
    elapsed = time.perf_counter() - started
    peak_rss = max(peak_rss, total_rss_bytes(process))

    size = output.stat().st_size if output.exists() else None
    return RunResult(
        renderer=renderer,
        phase=phase,
        index=index,
        command=command,
        returncode=process.returncode,
        wall_seconds=elapsed,
        peak_rss_bytes=peak_rss,
        output_path=str(output),
        output_size_bytes=size,
        stdout=stdout,
        stderr=stderr,
    )


def summarize_runs(runs: list[RunResult]) -> dict[str, Any]:
    cold = [run for run in runs if run.phase == "cold"]
    warm = [run for run in runs if run.phase == "warm"]
    warm_wall = [run.wall_seconds for run in warm]
    warm_rss = [run.peak_rss_bytes for run in warm]

    return {
        "cold_wall_seconds": cold[0].wall_seconds if cold else None,
        "cold_peak_rss_bytes": cold[0].peak_rss_bytes if cold else None,
        "warm_median_wall_seconds": statistics.median(warm_wall) if warm_wall else None,
        "warm_median_peak_rss_bytes": statistics.median(warm_rss) if warm_rss else None,
        "warm_runs": len(warm),
    }


def print_summary(renderer: str, summary: dict[str, Any]) -> None:
    def fmt_seconds(value: float | None) -> str:
        return f"{value:.4f}s" if value is not None else "n/a"

    def fmt_mib(value: float | None) -> str:
        return f"{value / (1024 * 1024):.2f} MiB" if value is not None else "n/a"

    print(f"{renderer}:")
    print(f"  cold wall: {fmt_seconds(summary['cold_wall_seconds'])}")
    print(f"  cold peak RSS: {fmt_mib(summary['cold_peak_rss_bytes'])}")
    print(f"  warm median wall: {fmt_seconds(summary['warm_median_wall_seconds'])}")
    print(f"  warm median peak RSS: {fmt_mib(summary['warm_median_peak_rss_bytes'])}")


def main() -> None:
    args = parse_args()
    root = repo_root()
    dataset, dataraster_bin, output_dir = require_paths(args)

    phases = ["cold"] * args.cold_runs + ["warm"] * args.warm_runs
    all_runs: list[RunResult] = []

    for renderer in ("dataraster", "datashader"):
        for index, phase in enumerate(phases, start=1):
            output = output_dir / f"{renderer}-{phase}-{index}.png"
            if renderer == "dataraster":
                command = dataraster_command(
                    dataraster_bin,
                    dataset,
                    output,
                    args.x_col,
                    args.y_col,
                    args.width,
                    args.height,
                )
            else:
                command = datashader_command(
                    dataset,
                    output,
                    args.x_col,
                    args.y_col,
                    args.width,
                    args.height,
                )

            result = measure_command(command, root, output, phase, index, renderer)
            all_runs.append(result)
            if result.returncode != 0:
                raise SystemExit(
                    f"{renderer} {phase} run {index} failed with code {result.returncode}\n"
                    f"stderr:\n{result.stderr}"
                )

    grouped: dict[str, list[RunResult]] = {"dataraster": [], "datashader": []}
    for run in all_runs:
        grouped[run.renderer].append(run)

    report = {
        "dataset": str(dataset),
        "width": args.width,
        "height": args.height,
        "x_col": args.x_col,
        "y_col": args.y_col,
        "comparison_contract": {
            "aggregation": "count",
            "projection": "linear",
            "execution_mode": "cpu_only",
            "output_type": "png",
            "dataraster_transfer": DEFAULT_TRANSFER,
            "dataraster_colormap": DEFAULT_COLORMAP,
            "dataraster_clip": DEFAULT_CLIP,
            "datashader_transfer": DEFAULT_TRANSFER,
            "datashader_palette": "plasma_like_fixed_palette",
        },
        "environment": environment_metadata(),
        "repo_state": current_tree_state(root),
        "summaries": {
            renderer: summarize_runs(runs) for renderer, runs in grouped.items()
        },
        "runs": [asdict(run) for run in all_runs],
    }

    report_path = output_dir / f"{dataset.stem}-results.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {report_path}")
    for renderer, runs in grouped.items():
        print_summary(renderer, summarize_runs(runs))


if __name__ == "__main__":
    main()

```

### render_with_datashader.py

```python
#!/usr/bin/env python3
"""Reference Datashader renderer for the benchmark harness."""

from __future__ import annotations

import argparse
from pathlib import Path

import numba
import pandas as pd


PLASMA_LIKE = [
    "#0d0887",
    "#5b02a3",
    "#9a179b",
    "#cc4778",
    "#ed7953",
    "#fdb42f",
    "#f0f921",
]


def import_datashader_with_compat():
    orig_jit = numba.jit
    orig_njit = numba.njit

    def no_cache_jit(*args, **kwargs):
        kwargs.pop("cache", None)
        return orig_jit(*args, **kwargs)

    def no_cache_njit(*args, **kwargs):
        kwargs.pop("cache", None)
        return orig_njit(*args, **kwargs)

    numba.jit = no_cache_jit
    numba.njit = no_cache_njit

    import datashader as ds
    from datashader import transfer_functions as tf

    return ds, tf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input parquet path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--x-col", default="x")
    parser.add_argument("--y-col", default="y")
    parser.add_argument("--width", type=int, default=818)
    parser.add_argument("--height", type=int, default=407)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ds, tf = import_datashader_with_compat()

    df = pd.read_parquet(args.input, columns=[args.x_col, args.y_col])
    canvas = ds.Canvas(plot_width=args.width, plot_height=args.height)
    agg = canvas.points(df, args.x_col, args.y_col, agg=ds.count())
    image = tf.shade(agg, how="eq_hist", cmap=PLASMA_LIKE)
    image = tf.set_background(image, "black")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.to_pil().save(output)


if __name__ == "__main__":
    main()

```

### README.md

```markdown
# DataRaster Case Studies

These case studies package the existing test data, gallery renders, and
quickstarts into adoption-oriented demos.

They are intentionally concrete:

- start from one data shape or user workflow
- pick the visualization that answers the workflow question
- point to the checked-in asset or command that proves the path exists
- call out the next missing proof when the example is not yet a full user story

## Start Here

| Case study | Data shape | Best visualization | Why it matters |
| --- | --- | --- | --- |
| [Datashader migration](datashader-migration.md) | dataframe points | Python PNG render | Tests the easiest switch path for notebook users |
| [Live map tiles](live-map-tiles.md) | large parquet points | raster XYZ tiles in MapLibre | Tests the backend adoption path |
| [Cloud tiles](cloud-tiles.md) | object-store parquet | render or PMTiles from S3/R2 | Tests deployment without local staging |
| [Operational benchmark](operational-benchmark.md) | 1M parquet points | comparable DataRaster/Datashader render | Tests performance claims under a written protocol |
| [Dense mobility](dense-mobility.md) | millions of trip starts | urban density map | Tests a high-volume city/mobility story |
| [Maritime AIS](maritime-ais.md) | millions of vessel positions | route and hotspot density | Tests global dense event rendering |
| [Earthquake catalog](earthquake-catalog.md) | event catalog over geography | projected density with underlay | Tests geospatial event density |
| [Tech report showcase map](tech-report-showcase-map.md) | current repo fixtures | report idea -> runnable demo mapping | Prevents overclaiming and guides the next demos |

## Demo Surfaces

Use these with the case studies:

- [../tiles/maplibre-demo.html](../tiles/maplibre-demo.html) is a checked-in
  external MapLibre consumer for the tile server.
- [../cookbook/README.md](../cookbook/README.md) maps local test datasets to
  the visualization modes they exercise.
- [../gallery/showcase/README.md](../gallery/showcase/README.md) contains the
  current real-data hero images.

## What Is Still Not Validation

These case studies are local evidence and outreach assets. They do not replace
the `datavis-u97` requirement for 3-5 real target users to review the story or
try the quickstarts.

```

### cloud-tiles.md

```markdown
# Case Study: Cloud Tiles

## User Question

"Can I render or tile data where it already lives, without copying it through a
notebook machine?"

This is the deployment case for teams whose source files and tile caches live in
S3-compatible object storage.

## Test Data Shape

The local equivalent is:

- `benchmark_1m.parquet`
- `benchmark_5m.parquet`

In production, the same shape becomes an object-storage URI:

```text
s3://bucket/path/events.parquet
```

## Visualization

Use the same density render or tile pyramid as the local examples, but read from
cloud storage and optionally write PMTiles or cache artifacts back to cloud
storage.

## Commands

Credential check:

```bash
data-raster cloud whoami --uri s3://my-bucket/data.parquet
```

Direct image render:

```bash
data-raster render s3://my-bucket/data.parquet -o out.png
```

PMTiles archive:

```bash
data-raster tile-pyramid \
  s3://my-bucket/data.parquet \
  --pmtiles \
  -o s3://my-bucket/tiles.pmtiles
```

R2 uses the S3 protocol with an explicit endpoint:

```bash
data-raster --endpoint "https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com" \
  render s3://my-r2-bucket/data.parquet -o r2-out.png
```

## What This Proves

- the visualization path is not tied to local files
- the same render and tile commands can be used in deployment environments
- object-store budgets and credential diagnostics are part of the workflow

## What To Ask A Platform User

1. Which storage system owns the source data?
2. Do you need dynamic tiles, static PMTiles, or both?
3. What request, byte, or runtime budget would make this safe?
4. Should the first production path be direct rendering, tile cache warming, or
   batch PMTiles generation?

See [../cloud/README.md](../cloud/README.md) for the cloud-native quickstart.

```

### datashader-migration.md

```markdown
# Case Study: Datashader Migration

## User Question

"Can I keep my dataframe or notebook workflow and replace only the raster step?"

This is the most direct path for users who already rely on Datashader, custom
NumPy raster code, or Python glue that writes PNGs for reports and frontends.

## Test Data

- `benchmark_1m.parquet`
- `benchmark_5m.parquet` when a larger local fixture is available

The 1M fixture is the canonical first test because it is large enough to make
rendering meaningful and small enough to run locally.

## Visualization

Use a density PNG from `x`/`y` point columns:

- aggregation: `count`
- transfer: `eq_hist`
- colormap: `plasma`
- canvas: `818x407`

## DataRaster Path

Use the dataframe-first quickstart:

```bash
python examples/python/datashader_parity.py
```

Or use the minimal Python path from
[../python/README.md](../python/README.md):

```python
import data_raster
import polars as pl

df = pl.read_parquet("benchmark_1m.parquet")

data_raster.render_to_file(
    df,
    "x",
    "y",
    output="examples/python/generated/benchmark_1m-python.png",
    width=818,
    height=407,
    transfer="eq_hist",
    colormap="plasma",
)
```

For common Datashader-shaped notebooks, start with:

```python
from data_raster.compat import datashader as ds

agg = ds.Canvas(plot_width=800, plot_height=600).points(df, "x", "y")
img = ds.tf.shade(agg, cmap="fire", how="log")
```

## What This Proves

- the user can keep Python as the orchestration layer
- the dataframe remains the handoff object
- DataRaster owns the heavy raster step
- migration can be tested one notebook at a time

## What To Ask A Datashader User

1. Which existing notebook would you try this on first?
2. Do you use `Canvas.points`, lines, rasters, areas, or categorical aggregation?
3. Which colormap and transfer settings are non-negotiable?
4. Would a partial shim help, or would you prefer a native DataRaster API?

## Current Limits To Show Honestly

The compatibility surface is intentionally partial. Use
[../../crates/data-raster-python/compat/SURFACE.md](../../crates/data-raster-python/compat/SURFACE.md)
and
[../../crates/data-raster-python/compat/CMAP_MAP.md](../../crates/data-raster-python/compat/CMAP_MAP.md)
when asking for migration feedback.

```

### dense-mobility.md

```markdown
# Case Study: Dense Mobility

## User Question

"Can I turn millions of trip or telemetry events into a readable density layer?"

This is the story for city mobility, logistics, fleet telemetry, and operations
dashboards.

## Existing Showcase

The current real-data gallery includes:

- Citibike trip starts for October 2024
- 5.1M trips
- inferno colormap
- histogram-equalized transfer
- spread 4px

![Citibike trip starts](../gallery/showcase/citibike.png)

## Best Visualization Modes

Start with density:

- shows where activity concentrates
- hides individual trips, which is often the right privacy posture
- works as a static image, report artifact, or raster tile layer

Then compare alternatives:

- weighted aggregation when events have value, duration, load, or severity
- temporal frames when the operational question depends on time of day
- tile serving when the user needs interactive map navigation

## Local Test Fixtures To Use

- `examples/gallery/weighted-clusters.csv` for count-versus-sum behavior
- `examples/gallery/temporal-pulse.csv` and `temporal-pulse.yaml` for movement
  over time
- `benchmark_1m.parquet` for the tile and Python quickstarts

## What This Proves

- dense event data can be summarized without plotting every point as a marker
- transfer and spread choices materially affect readability
- the same data shape can become a static PNG, a temporal sequence, or live
  tiles

## What To Ask A Mobility User

1. Is the main question demand, congestion, coverage, anomaly detection, or
   operational monitoring?
2. Does the map need absolute counts, relative density, or weighted values?
3. Is time-of-day comparison essential?
4. Would the first useful output be a notebook PNG, a dashboard layer, or a tile
   service?

```

### earthquake-catalog.md

```markdown
# Case Study: Earthquake Catalog

## User Question

"Can I render a large event catalog over geography without hiding the spatial
pattern?"

This is the story for earthquakes, incidents, observations, and sensor events.

## Existing Showcase

The current real-data gallery includes:

- USGS earthquake catalogue from 2020-2024
- 782K events
- Web Mercator projection
- count aggregation
- inferno colormap
- histogram-equalized transfer
- circular spread 2px
- coastline underlay

![USGS earthquake catalogue](../gallery/showcase/earthquakes.png)

## Best Visualization Modes

Start with projected density plus a geographic underlay:

- the density layer shows event concentration
- the underlay gives geographic orientation
- the projection choice avoids misleading map shape for longitude/latitude data

Then explore:

- contours for density thresholds
- hotspots or peak extraction for candidate regions
- temporal frames for event waves or before/after comparisons
- visual diff for comparing two render settings or time windows

## Local Test Fixtures To Use

- `examples/geospatial/world-graticule.geojson` for underlay behavior
- `examples/gallery/hello-contours.dr.yaml` for contour rendering
- `examples/gallery/temporal-pulse.yaml` for temporal frame output
- `examples/diagnostic-fixes/` for visual or semantic comparison workflows

## What This Proves

- DataRaster can combine projected point density with a geographic reference
- analysis overlays can turn a density map into a threshold or hotspot review
- the same event-catalog shape supports static, temporal, and comparison views

## What To Ask A Geospatial User

1. Is a density image enough, or do they need extracted regions?
2. Which projection and underlay are required?
3. Do they need to compare time windows?
4. Should the output be a PNG, GeoJSON contour result, or tile layer?

```

### live-map-tiles.md

```markdown
# Case Study: Live Map Tiles

## User Question

"Can this replace the custom rendering service behind my map frontend?"

This is the backend adoption path for teams already serving raster layers into
MapLibre, deck.gl, or an internal map application.

## Test Data

- `benchmark_1m.parquet`
- `benchmark_5m.parquet` for local scale escalation

## Visualization

Serve the point dataset as raster XYZ tiles and consume the TileJSON from a
plain MapLibre page.

## Run The Server

```bash
cargo run -p data-raster-server -- serve \
  benchmark_1m.parquet \
  --port 3000 \
  --public-url http://localhost:3000
```

Smoke test:

```bash
curl http://localhost:3000/health
curl "http://localhost:3000/benchmark_1m/tilejson.json?format=webp"
```

## Open The Demo

Serve the checked-in MapLibre page:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/examples/tiles/maplibre-demo.html
```

The page fetches TileJSON from the local DataRaster server and adds the returned
tile template as a raster source.

## What This Proves

- the server can expose a standard tile endpoint
- a separate frontend can consume the TileJSON without project-specific glue
- the built-in viewer is not the only browser path

## What To Ask A Backend User

1. Would this fit your current tile serving topology?
2. Do you need XYZ directories, PMTiles, dynamic tiles, or all three?
3. What cache behavior would decide adoption?
4. Which deployment target matters first: container, serverless, object storage,
   or long-running internal service?

```

---

## Visuals

![Global earthquake density rendered by DataRaster](/images/datavis-earthquakes.png)
*Every recorded earthquake epicentre as a density map. Plate boundaries emerge from the raw point cloud with no point-by-point drawing.*

![Flight-path density rendered by DataRaster](/images/datavis-flights.jpg)
*Line rendering: hundreds of thousands of great-circle flight paths aggregated into a single density layer.*

![Urban trip density rendered by DataRaster](/images/datavis-citibike.png)
*Point density at city scale — bike-share trip endpoints across a metro area.*

---

## Architecture

A ten-crate Rust workspace — roughly 60,000 lines, 555 tests — separating the
core engine from its delivery surfaces:

- **Core engine** — point, line, and polygon rasterization; CPU execution with an
  optional `wgpu` GPU path.
- **Spec and plan** — a declarative document model describing views, layers, and
  projections, compiled into a render plan.
- **CLI, server, Python, WASM** — four front ends over the same engine.
- **Polars plugin** — rendering exposed as a native dataframe operation.

Datasets are read from Parquet and CSV, including directly from S3, R2, GCS, and
Azure Blob Storage as first-class sources — the same backend serves a local file
and a cloud-hosted table without a separate ingestion step.

![Flight-path density rendered by DataRaster](/images/datavis-flights.jpg)
*Line rendering: hundreds of thousands of great-circle flight paths aggregated
into a single density layer.*

---

## Quick Facts

| | |
|---|---|
| **Status** | Last Active: 2026-03-22 |
| **Stack** | Rust, Polars |

---

## Current Status

2026-03-22 — Completed 30-05: real data-raster render pipeline wired into workbench, analysis overlay population, timeline scrub re-render

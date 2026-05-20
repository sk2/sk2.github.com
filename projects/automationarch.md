---
layout: default
section: network-automation
description: "This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed."
sitemap: false
hand_written: true
---

# Network Automation Ecosystem - Overall Architecture Definition

<div class="badges-row">
  <span class="status-badge status-active">Last Active: 2026-04-11</span>
  <span class="stack-badge">Python</span> <span class="stack-badge">TypeScript</span>
</div>

---

## Contents

- [Concept](#concept)
- [Code Samples](#code-samples)
- [Current Status](#current-status)

## Concept

This project defines the architecture of the Network Automation Ecosystem: how its tools connect, what data flows between them, and where the system is headed.

The ecosystem comprises nine repositories that form a composable toolchain. Each tool handles one concern -- topology generation, simulation, configuration parsing, visualization, analysis -- and communicates through pinned contract schemas (RFC-01, RFC-02). The architecture document formalizes these relationships and identifies future sub-projects.

---

## Code Samples

### README.md

```markdown
# Examples: Canonical Fixture Projects

This directory holds canonical, reviewable fixture *projects* for the pinned RFC contracts.

Each fixture is intended to be:

- Self-contained (inputs + committed expected outputs)
- Deterministic (expected outputs are stable for re-audit)
- Enforceable by one repo-local command

See also: [RFC-01.md](RFC-01.md), [RFC-02.md](RFC-02.md), [rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md](rfc/rfc-02/live-overlay-stream/v1.0/ACCEPTANCE.md).

## Fixture Layout (Canonical)

One directory per fixture project:

```
examples/
  minimal-lab/
    netauto.project
    network.topo.yaml
    network.design.yaml
    README.md
    expected/
      *.operational.json
      overlay/
        golden.ndjson
        overlay.view.json
```

`scripts/check-fixtures` considers a directory a *fixture root* if it is under `examples/*/` and contains `netauto.project`.

## Inputs vs Expected Outputs

Inputs (human-authored or tool inputs):

- `netauto.project` (RFC-02 manifest concept)
- `*.topo.yaml` (RFC-01 topology sidecar)
- `*.design.yaml` (RFC-01 design sidecar)
- Optional `README.md` narrative per fixture

Expected outputs (committed, stable artifacts for review and re-audit):

- `expected/**/*.operational.json`
  - Must validate against the pinned OperationalTopology v1.0 schema: `rfc/rfc-01/operational-topology/v1.0/schema.json`
- `expected/overlay/golden.ndjson`
  - Must validate line-by-line against the pinned Live Overlay Stream v1.0 schema: `rfc/rfc-02/live-overlay-stream/v1.0/schema.json`
- `expected/overlay/overlay.view.json`
  - Must match a deterministic fold of `golden.ndjson` as recomputed by `scripts/check-fixtures`

## Derived Overlay View Contract (`netauto/overlay-view/v0`)

The fixture gate recomputes a derived overlay view from `expected/overlay/golden.ndjson` and compares it (semantic JSON equality) to `expected/overlay/overlay.view.json`.

The derived view is a plain JSON object with stable top-level keys:

- `schema`: constant `netauto/overlay-view/v0`
- `topology_id`: final scoped topology id
- `fold`: `{dedupe_by: "event_id", order: "transcript", last_event_id: ...}`
- `topology`: `{nodes: [...], edges: [...]}` (sorted lists)
- `telemetry`: `{nodes: {...}, edges: {...}}` (maps)
- `errors`: list (may be empty)

High-level fold rules:

- Process events in transcript order.
- Dedupe by `event_id` (first occurrence wins).
- `topology.snapshot` replaces the topology node/edge sets.
- `topology.node.add/remove` and `topology.edge.add/remove` mutate topology idempotently.
- `telemetry.snapshot` replaces node/edge telemetry maps.
- `telemetry.delta` merges metrics (keys present overwrite; absent unchanged; `null` allowed).
- `error` events append to `errors` and do not mutate topology or telemetry.

Lightweight cross-checks enforced by the gate:

- All overlay events in a fixture must share the same `topology_id`.
- Telemetry references must exist in the final folded topology state.

## Reviewer Workflow (One Command)

Install pinned validation dependencies:

```bash
python3 -m pip install -r rfc/rfc-02/live-overlay-stream/v1.0/requirements.txt
```

Validate all fixtures:

```bash
python3 scripts/check-fixtures
```

Validate one fixture:

```bash
python3 scripts/check-fixtures --fixture examples/minimal-lab
```

## CLI Capture Packs

Some example directories are capture packs rather than fixture roots. They hold
real terminal output for website and documentation use.

- [`umbrella-cli/`](umbrella-cli/) captures the current `ank` Rust umbrella CLI
  skeleton from `/Users/simonknight/dev/[autonetkit](../autonetkit)-rs`.
- [`e2e-demo-screencaps/`](e2e-demo-screencaps/) captures terminal and web
  screenshots for the current end-to-end demo surfaces.

```

### CONTRIBUTING.md

```markdown
# Contributing to brownfield-real

This corpus aims to surface parser failures and audit-logic gaps that
synthetic fixtures cannot. New entries are welcome; rules below.

## Rules for any corpus entry

1. **Anonymized before commit.** Run `scripts/sanitize.py` on any raw
   capture before it lands in `corpus/`. Spot-check the output for
   residual hostnames, public IPs, or domain names. If you are not
   sure, do not commit.
2. **Source declared.** Every entry has a row in `corpus/manifest.yaml`
   describing: vendor, software version, topology shape, source path
   (e.g. `containerlab fabric.clab.yml @ HEAD`), and date captured.
3. **Reproducible if synthetic-source.** If the entry came from this
   directory's containerlab topology, the manifest references the topo
   commit hash so the entry can be re-derived.
4. **No customer / employer identifiers.** Even after sanitization, no
   project codenames, internal site IDs, or customer brand strings.

## Why we did not adopt Path A (GitHub scrape)

Public GitHub configs have three problems that the bead's discussion
flagged:

- **License clarity.** A config in a public repo is not necessarily
  licensed for redistribution. Even with sanitization, the original
  copyright applies.
- **Completeness.** Most public configs are partial — a snippet
  illustrating a feature, not a running-config. The audit relies on
  cross-referenced state (an interface is referenced by a route-map
  which is bound to a peer).
- **Drift.** A config posted to GitHub in 2019 reflects 2019 syntax. A
  containerlab boot today produces 2026-current syntax.

Path A may resurface as a complement — *targeted* fetches of canonical
fixtures (e.g. RFC examples re-typed into vendor syntax) — but it is
not the spine of the corpus.

## Why we did not adopt Path B (Reddit / Discord asks)

The economics make sense (free audit in exchange for a corpus) but the
relationship-building lead time pushes the bead's "1–2 days for sourcing"
estimate into multi-week territory. Path B is good for *quality
expansion* once Path C is in place; it is not the path to v1.

## Adding a Path C entry (containerlab boot)

1. Edit `topology/fabric.clab.yml` if you need a different shape.
2. Edit `topology/boot-configs/<device>.cfg` if you need different
   starting state.
3. `sudo containerlab deploy -t topology/fabric.clab.yml`
4. Wait for convergence (90s default).
5. `scripts/capture-configs.sh corpus/raw/`
6. `scripts/sanitize.py corpus/raw/ --output corpus/`
7. Update `corpus/manifest.yaml` with the new entries.
8. `scripts/run-audit.sh corpus/ --output audit-report/`
9. Commit.

## Adding a Path E entry (operator donation)

1. Operator runs `scripts/sanitize.py raw-configs/ --output sanitized/`
   on their own machine.
2. They review the output for residual identifiers.
3. They send the `sanitized/` directory plus a one-paragraph description
   (vendor, version, shape, why it surfaces something interesting).
4. Maintainer reviews, runs `scripts/run-audit.sh`, and commits with a
   manifest entry crediting the donor (or anonymous, by donor preference).

## Sanitizer extension policy

When the sanitizer needs to handle a new construct (a vendor-specific
syntax it does not yet recognize):

- Add a regex rule with a comment showing one real example of what it
  matches.
- Add a unit test in `scripts/test_sanitize.py` (or extend the existing
  one) covering the new rule.
- Document the rule in `README.md`'s "Anonymization contract" table if
  it changes the strip-vs-preserve boundary.

```

### README.md

```markdown
# brownfield-real — Real (non-synthetic) configuration corpus

This directory holds running-config captures from devices that genuinely
booted, exchanged routes, and converged. Where every other fixture in the
repo is hand-authored, every config under `corpus/` was *produced by a
network operating system*.

## Why this exists

Until 2026-05, the brownfield audit pipeline (`ank_ncp` with 16+ checks) was
validated against `fixtures/brownfield/eos-pilot-corpus/` — twenty Arista
EOS configs hand-authored to seed deterministic defects. That corpus is
sufficient to prove the *check logic* works, but it cannot prove the
*parser holds up against real configs*.

Real configs differ from synthetic ones in three ways that have surprised
every parser ever shipped:

1. **Undocumented legacy syntax.** Vendors keep parsing decade-old forms
   for backward compatibility. Synthetic configs use only the forms the
   author knew about.
2. **Vendor-version drift.** EOS 4.30 emits subtly different config lines
   than EOS 4.20 for the same feature. NX-OS does the same across N9K
   train transitions. JunOS emits different display formats depending on
   `display set` vs hierarchical.
3. **Operator patches.** Real configs accumulate one-line workarounds
   nobody documented — a `no shutdown` somewhere unexpected, a `description
   "do not touch"`, a route-map with two clauses where one is dead code.

Bead `br-3ux4.17` calls this gap "the #1 failure mode ( probability of
parser collapse on first real corpus)." The fix is not better synthetic
fixtures. The fix is configs that came off devices.

## What "real" means here

Two paths produce material that lives under `corpus/`:

- **Path C: Containerlab boot.** A topology in `topology/fabric.clab.yml`
  boots cEOS + crpd nodes, applies operator-style patches, lets routing
  converge, then captures the running-config out of each device. The
  configs are real in the sense that *they came out of a routing OS*,
  not in the sense that they came from a production fleet.
- **Path E: Operator donations** (future). A future workflow lets a
  network engineer donate a sanitized corpus from their fleet in exchange
  for a free audit. Donations land here after running through
  `scripts/sanitize.py`.

Path A (GitHub scrape) and Path B (Reddit/Discord asks) were considered
but not adopted; see `CONTRIBUTING.md` for the rationale.

## Topology library

Three CCNP-style topologies cover the shapes a brownfield audit needs to
handle. Each topology has a self-contained boot-config set and a header
comment describing the protocols it exercises.

| Topology | Devices | Vendors | Stresses |
| --- | --- | --- | --- |
| `fabric.clab.yml` | 10 (2 spine + 4 leaf + 2 edge + 2 host) | cEOS + crpd | EVPN-style leaf-spine, OSPF underlay, iBGP RR overlay, eBGP edges. The "DC fabric" slot. |
| `enterprise-edge.clab.yml` | 4 + 2 hosts | cEOS only | NAT44 source-NAT, OSPF area 0, static-default redistribution, VLAN segmentation (users + guest SVIs), dual-stack IPv4/IPv6. The "enterprise edge" slot. |
| `isp-backbone.clab.yml` | 5 | cEOS + crpd | BGP confederation (outer 64500 → sub-AS 65001 + 65002), IS-IS L2, MPLS-LDP, mixed-vendor IS-IS/LDP adjacencies, partial mesh. The "ISP backbone" slot. |

## Layout

```
brownfield-real/
  README.md                    # this file
  CONTRIBUTING.md               # how to add a corpus entry; sanitization rules
  topology/
    fabric.clab.yml            # DC fabric (containerlab v0.59+)
    enterprise-edge.clab.yml   # enterprise edge with NAT + VLANs + dual-stack
    isp-backbone.clab.yml      # ISP backbone with BGP confed + IS-IS + LDP
    boot-configs/              # per-device starting config applied at boot
      spine-1.cfg              # fabric.clab.yml — Arista EOS startup-config
      spine-2.cfg
      leaf-1.cfg .. leaf-4.cfg
      edge-1.conf              # fabric.clab.yml — Juniper JunOS (crpd) startup-config
      edge-2.conf
      enterprise-edge/         # enterprise-edge.clab.yml — Arista EOS
        edge-fw.cfg
        edge-router.cfg
        internal-router.cfg
        access-switch.cfg
      isp-backbone/            # isp-backbone.clab.yml — mixed
        pe1.cfg                # Arista EOS, sub-AS 65001
        p1.cfg
        pe2.cfg
        p2.conf                # Juniper crpd, sub-AS 65002
        pe3.conf
    overlay-patches/           # operator-style post-boot mutations
      ops-patches.sh           # applied via vendor CLI after convergence
  scripts/
    sanitize.py                # structure-preserving anonymizer
    capture-configs.sh         # post-convergence config extraction
    run-audit.sh               # ank_ncp wrapper; writes audit-report/
  corpus/                      # captured + sanitized configs (commit these)
    manifest.yaml              # describes each entry: vendor, shape, source
    <captured-files>.cfg
  audit-report/                # ank_ncp output (commit findings)
    findings.json
    findings.md
```

## End-to-end flow

```
boot lab           capture configs       sanitize           audit
═════════          ════════════════      ════════           ═════
clab deploy   ─►   capture-configs.sh ─► sanitize.py    ─► run-audit.sh
fabric.clab.yml    raw/*.cfg             corpus/*.cfg       audit-report/
                                                            findings.json
```

Every step is reproducible from inputs already in this directory. The
only external requirements are `containerlab`, `docker`, and the cEOS-lab
+ crpd images (free downloads from Arista / Juniper with vendor-account
login).

## Regenerating

Two paths. Pick by whether you have the vendor images locally.

**Via `make harvest`** — the friction-free path, drives `tools/ank_harvester/`.
Defaults to dry-run synthesis; set `HARVEST_LIVE=1` to actually boot the lab.

```sh
make harvest HARVEST_TOPOLOGY=fabric              # dry-run; no docker required
make harvest HARVEST_TOPOLOGY=fabric HARVEST_LIVE=1   # boot containerlab
```

**Manually** — the explicit path, useful for debugging individual steps:

```sh
# 1. Pull / register images one-time:
#    cEOS-lab    → https://www.arista.com/en/support/software-download
#    crpd        → https://www.juniper.net/us/en/dm/crpd-trial/
docker images | grep -E 'ceos|crpd'

# 2. Deploy the lab (creates a Linux network namespace per device).
sudo containerlab deploy -t topology/fabric.clab.yml

# 3. Wait for OSPF + BGP convergence (~90s).
sleep 90

# 4. Capture running configs.
scripts/capture-configs.sh corpus/raw/

# 5. Sanitize: strip hostnames, IPs, ASNs, secrets; preserve audit signal.
scripts/sanitize.py corpus/raw/ --output corpus/

# 6. Run the brownfield audit against the sanitized corpus.
scripts/run-audit.sh corpus/ --output audit-report/

# 7. Review findings.
cat audit-report/findings.md
```

## Adding a topology

See `tools/ank_harvester/README.md` for the five-file checklist (clab
spec, boot-configs, image registration, per-topology `metadata.json`,
output-layout test). The schema for `metadata.json` lives at
`schemas/netauto/harvest-metadata/v1.0/schema.json` — it pins per-topology
identity (vendor list, image versions, topology hash, device list) so
downstream tooling can attribute findings without reparsing the
`.clab.yml`.

## Anonymization contract

The sanitizer is **structure-preserving renaming**, not redaction. It
strips identity but keeps every byte an audit parser uses as signal:

| Stripped | Preserved |
| --- | --- |
| Hostnames (`leaf-prod-paris-3a` → `leaf-3`) | Device-role prefix; numeric position |
| IPv4 addresses → 10.0.0.0/8 (private) | Subnet structure; same /N within a /16 |
| IPv6 addresses → 2001:db8::/32 (RFC 3849 doc) | Low 96 bits preserved; prefix [signals](../signals) "doc" |
| ASNs (real public/private numbers) → 64512+ | Relationships (same AS still same; eBGP still eBGP) |
| UUIDs (RFC 4122 8-4-4-4-12 hex) | UUID-shaped output; field-format intact |
| MAC addresses (colon, dash, dotted-quad) → `02:…:NN` | Locally-administered prefix; separator format preserved |
| SNMP communities, RADIUS/TACACS keys | Indicator that these features are *configured* |
| Encrypted passwords (type 7 / MD5 / SHA) | Hash-type indicator; field structure |
| Public domain names, certificates | TLS / domain-config indicator |
| Customer / site / VLAN names | Position; type; tag values |
|  | All routing-protocol structure |
|  | Route-map / prefix-list / ACL shape |
|  | MTU, interface types, timer values |
|  | VRF structure (just renamed) |

**Note on IPv4 ranges:** RFC 5737 (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) would be the ideal "obviously documentation" output range, but it has only 768 host addresses across three /24s. With 8 bits of host space per /24, two source IPs that share a host octet (.1, .2, .10 are very common) and hash to the same output /24 collide — and the audit relies on per-interface IP uniqueness. We keep 10.0.0.0/8 (16M addresses) for IPv4 to preserve audit signal at the cost of less-obvious "doc" framing. IPv6 has no such constraint (96 bits of low-portion in 2001:db8::/32) so we use the doc prefix there.

Why this matters: an audit that says "this leaf has an MTU mismatch on the
spine-facing link" must still be derivable after sanitization. If the
sanitizer collapsed all MTU values to 1500, the corpus would be useless.

## Defensive check before commit

Even with structure-preserving sanitization, mistakes can slip through —
a missed regex, a contributor pasting raw input. `scripts/check-anonymization.py`
is the safety net:

```sh
# Manual run before commit
scripts/check-anonymization.py corpus/

# Or wire as a git pre-commit hook (one-time setup):
cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
set -e
staged=$(git diff --cached --name-only --diff-filter=ACM \
         | grep '^examples/brownfield-real/corpus/' || true)
[ -z "$staged" ] && exit 0
python3 examples/brownfield-real/scripts/check-anonymization.py $staged
HOOK
chmod +x .git/hooks/pre-commit
```

The check refuses commits that contain IPv4/IPv6 addresses or MAC
addresses outside the sanitizer's documented output ranges. See the
script header for the exact allowlists. Exit code 1 = leak detected;
commit is blocked.

## Acceptance for `br-3ux4.17`

This directory closes `br-3ux4.17` when:

1. `topology/fabric.clab.yml` boots end-to-end with both vendors present
   (`docker ps` shows ≥10 containers, all healthy).
2. `scripts/capture-configs.sh` produces ≥10 raw config files spanning
   ≥2 vendors after a successful boot.
3. `scripts/sanitize.py` round-trips: parsing each output as YAML/text
   succeeds; spot-checked diff against raw shows only renamed strings.
4. `scripts/run-audit.sh` returns exit 0 (audit-tool ran) and writes a
   `findings.json` with at least one finding *or* a documented
   no-findings record.
5. `corpus/manifest.yaml` exists and describes every committed config.

Until items 1–5 are ticked, the bead stays `in_progress`. Findings (or
panic backtraces, if the parser does collapse) are recorded in
`audit-report/`.

## Citation

If you reference this corpus in a paper, report, or bug filing,
please cite it as:

> ANK Real-Config Harvest Corpus, AutoNetkit, retrieved <date>, commit `<sha>`.
>
> `https://github.com/sk2/automationarch/tree/<sha>/examples/brownfield-real`

The commit SHA pins both the topology specs and the harvest pipeline
that produced the configs. Per-topology metadata.json files record
the vendor image versions at capture time.

## Pointers

- Bead: `br br-3ux4.17`
- Harvester orchestrator: `tools/ank_harvester/README.md`
- Per-topology metadata schema: `schemas/netauto/harvest-metadata/v1.0/`
- Synthetic baseline this replaces: `fixtures/brownfield/eos-pilot-corpus/`
- Audit tool source: `~/dev/ank/ncp/crates/ncp-brownfield`

```

### manifest.yaml

```yaml
# brownfield-real corpus manifest
#
# One entry per file in this directory (excluding manifest.yaml itself and
# .gitkeep). The manifest is the index `run-audit.sh` and any future
# corpus-management tools read to know what they are looking at.
#
# Schema
# ------
# entries[].file              relative filename inside corpus/
# entries[].vendor             arista_eos | cisco_ios | juniper_junos
# entries[].vendor_version     OS version string at capture time
# entries[].source             how the config was obtained
# entries[].source_topology    if Path C, the .clab.yml + commit it came from
# entries[].source_donor       if Path E, donor identifier (or "anonymous")
# entries[].captured_at        ISO 8601 UTC timestamp
# entries[].seeded_defects     list of intentional defects (Path C only)
# entries[].notes              free-form
#
# This file is empty until a lab is actually booted and configs are captured.
# When that happens, populate from `scripts/capture-configs.sh` output and
# `scripts/sanitize.py` output (the sanitizer can be extended to emit this
# manifest automatically — currently it does not).

corpus_version: 1
entries: []

# Example (uncomment and adapt after a real run):
#
# entries:
#   - file: spine-1.cfg
#     vendor: arista_eos
#     vendor_version: "4.32.0F"
#     source: containerlab
#     source_topology: topology/fabric.clab.yml@<commit-sha>
#     captured_at: "2026-05-09T10:00:00Z"
#     seeded_defects: []
#     notes: "Clean baseline, 4 OSPF adjacencies, 2 eBGP neighbors."
#   - file: spine-2.cfg
#     vendor: arista_eos
#     vendor_version: "4.32.0F"
#     source: containerlab
#     source_topology: topology/fabric.clab.yml@<commit-sha>
#     captured_at: "2026-05-09T10:00:00Z"
#     seeded_defects:
#       - "MTU 9100 on Ethernet5 (vs 9214 elsewhere) — operator drift"
#     notes: ""

```

### check-anonymization.py

```python
#!/usr/bin/env python3
"""
check-anonymization.py — refuse commits that would leak real network identifiers.

Scans config files for IPv4 addresses, IPv6 addresses, and MAC addresses
that fall *outside* the sanitizer's documented output ranges. Any token
outside the allowlist is treated as a potential leak.

Allowed IPv4 ranges:
- 10.0.0.0/8        (sanitizer output range, RFC 1918 — see scripts/sanitize.py)
- 192.0.2.0/24      (RFC 5737 TEST-NET-1 — documentation-marked, never real)
- 198.51.100.0/24   (RFC 5737 TEST-NET-2 — documentation-marked)
- 203.0.113.0/24    (RFC 5737 TEST-NET-3 — documentation-marked)
- 0.0.0.0           (OSPF area, default route, listen-on-any)
- 127.0.0.0/8       (loopback)
- 224.0.0.0/4       (multicast)
- 255.255.255.255   (broadcast)

Other RFC 1918 ranges (172.16.0.0/12, 192.168.0.0/16) are NOT allowed —
the sanitizer does not output them, so their presence in the corpus
indicates sanitization did not cover that input.

Allowed IPv6 ranges:
- 2001:db8::/32     (RFC 3849 documentation prefix; sanitizer output)
- ::                (unspecified)
- ::1               (loopback)
- ff00::/8          (multicast)
- fe80::/10         (link-local; often present in IS-IS / OSPFv3)

Allowed MAC patterns (locally-administered or well-known broadcast/multicast):
- 02:*                       (sanitizer output, locally-administered)
- 0200.*                     (Cisco/Arista dotted-quad form of 02:*)
- ff:ff:ff:ff:ff:ff          (broadcast)
- 00:00:00:00:00:00          (null)
- 01:00:5e:*                 (IPv4 multicast prefix)
- 33:33:*                    (IPv6 multicast prefix)

Usage:
    check-anonymization.py <path>...
    check-anonymization.py corpus/

Exit codes:
    0 — no leaks detected
    1 — leak detected (commit should be blocked)
    2 — usage / IO error
"""

import argparse
import ipaddress
import re
import sys
from pathlib import Path


# Network identifier patterns. Same shapes as scripts/sanitize.py — kept
# inline here so this script is standalone (zero-dep, no shared module).
IPV4_PATTERN = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d{1,2})\b"
)
# Permissive IPv6 pre-filter: any token with hex + colons containing the ::
# compression (so common forms like 2001:db8::1 match, not just uncompressed).
# Each match is then validated by ipaddress.IPv6Address; non-IPv6 tokens are
# skipped. Looser than the sanitize.py pattern by design — over-detection
# is fine because the validator is the gatekeeper.
IPV6_PATTERN = re.compile(
    r"(?:[0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}"
)
MAC_COLON_DASH_PATTERN = re.compile(
    r"\b([0-9a-f]{2}([:-])[0-9a-f]{2}\2[0-9a-f]{2}\2[0-9a-f]{2}\2[0-9a-f]{2}\2[0-9a-f]{2})\b",
    re.IGNORECASE,
)
MAC_DOTQUAD_PATTERN = re.compile(
    r"\b([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\b",
    re.IGNORECASE,
)


# Allowed IPv4 ranges as ipaddress networks
ALLOWED_IPV4_NETWORKS = [
    ipaddress.IPv4Network("10.0.0.0/8"),
    ipaddress.IPv4Network("127.0.0.0/8"),
    ipaddress.IPv4Network("224.0.0.0/4"),
    ipaddress.IPv4Network("192.0.2.0/24"),
    ipaddress.IPv4Network("198.51.100.0/24"),
    ipaddress.IPv4Network("203.0.113.0/24"),
]
ALLOWED_IPV4_SINGLES = {
    ipaddress.IPv4Address("0.0.0.0"),
    ipaddress.IPv4Address("255.255.255.255"),
}

# Allowed IPv6 ranges
ALLOWED_IPV6_NETWORKS = [
    ipaddress.IPv6Network("2001:db8::/32"),
    ipaddress.IPv6Network("ff00::/8"),
    ipaddress.IPv6Network("fe80::/10"),
]
ALLOWED_IPV6_SINGLES = {
    ipaddress.IPv6Address("::"),
    ipaddress.IPv6Address("::1"),
}


def ipv4_is_leaked(ip_str: str) -> bool:
    try:
        addr = ipaddress.IPv4Address(ip_str)
    except ipaddress.AddressValueError:
        return False
    if addr in ALLOWED_IPV4_SINGLES:
        return False
    return not any(addr in net for net in ALLOWED_IPV4_NETWORKS)


def ipv6_is_leaked(ip_str: str) -> bool:
    try:
        addr = ipaddress.IPv6Address(ip_str)
    except ipaddress.AddressValueError:
        return False
    if addr in ALLOWED_IPV6_SINGLES:
        return False
    return not any(addr in net for net in ALLOWED_IPV6_NETWORKS)


def mac_is_leaked(mac_str: str) -> bool:
    """Return True if the MAC is not in the sanitizer's allowed-output set."""
    canonical = re.sub(r"[.:-]", "", mac_str.lower())
    if len(canonical) != 12:
        return False
    if canonical == "ffffffffffff" or canonical == "000000000000":
        return False
    if canonical.startswith("02"):
        return False
    if canonical.startswith("01005e"):
        return False
    if canonical.startswith("3333"):
        return False
    return True


def scan_file(path: Path) -> list[tuple[str, str, int]]:
    """Return a list of (kind, value, line_number) tuples for any leak found."""
    leaks = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"check-anonymization: cannot read {path}: {e}", file=sys.stderr)
        return leaks

    for line_no, line in enumerate(text.splitlines(), start=1):
        for m in IPV4_PATTERN.finditer(line):
            if ipv4_is_leaked(m.group(0)):
                leaks.append(("ipv4", m.group(0), line_no))
        for m in IPV6_PATTERN.finditer(line):
            if ipv6_is_leaked(m.group(0)):
                leaks.append(("ipv6", m.group(0), line_no))
        for m in MAC_COLON_DASH_PATTERN.finditer(line):
            if mac_is_leaked(m.group(1)):
                leaks.append(("mac", m.group(1), line_no))
        for m in MAC_DOTQUAD_PATTERN.finditer(line):
            if mac_is_leaked(m.group(1)):
                leaks.append(("mac", m.group(1), line_no))
    return leaks


def iter_targets(args: list[Path]):
    for arg in args:
        if arg.is_dir():
            for p in sorted(arg.rglob("*")):
                if not p.is_file() or p.name.startswith("."):
                    continue
                if p.suffix not in (".cfg", ".conf", ".txt"):
                    continue
                yield p
        elif arg.is_file():
            yield arg
        else:
            print(f"check-anonymization: skipping non-existent {arg}",
                  file=sys.stderr)


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paths", nargs="+", type=Path,
                   help="Files or directories to scan")
    args = p.parse_args(argv)

    total_leaks = 0
    files_with_leaks = 0
    for path in iter_targets(args.paths):
        leaks = scan_file(path)
        if leaks:
            files_with_leaks += 1
            total_leaks += len(leaks)
            for kind, value, line_no in leaks:
                print(f"{path}:{line_no}: leaked {kind}: {value}", file=sys.stderr)

    if total_leaks > 0:
        print(file=sys.stderr)
        print(f"check-anonymization: {total_leaks} leak(s) in "
              f"{files_with_leaks} file(s). Re-run sanitize.py before commit.",
              file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

```

### README.md

```markdown
# Campus Network Example

A small campus topology: 1 core switch, 2 distribution switches, and 6 access
switches running OSPF with inter-VLAN routing.

This example demonstrates:

- The three-tier campus hierarchy (core / distribution / access)
- OSPF area 0 as the routing underlay
- Inter-VLAN routing anchored at the core switch
- Redundant uplinks from access to distribution

---

## Topology

    [Users/Voice/Servers/Mgmt]
           |
    +------+------+
    |  core-01    |  Cisco Catalyst 9500
    |             |  Inter-VLAN routing
    +------+------+
           |  \
           |   \
    +------+   +------+
    | dist-01| | dist-02|  Cisco Catalyst 9300
    +------+   +------+
      / \         / \
     /   \       /   \
    a01  a02   a03  a04   a05  a06
                             Cisco Catalyst 9200

Full diagram (dual uplinks shown):

                        campus-core-01
                       /              \
                 dist-01  ----  dist-02
                 /    \        /    \
           acc-01  acc-02   acc-03  acc-04
                             acc-05  acc-06

    Nodes : 9 (1 core, 2 distribution, 6 access)
    Links : 11
    VLANs : 10 (users), 20 (servers), 30 (voice), 40 (management)
    Routing: OSPF area 0

---

## Files

    topology.yaml        Physical topology (nodes + links)
    design.yaml          Design intent (OSPF, VLANs, addressing pools)
    run.sh               Run the pipeline
    expected-output/     Golden validation output

---

## How to Run

    cd examples/campus
    ./run.sh

Or step by step:

    # Validate the topology
    netauto validate topology.yaml

    # Run the pre-flight pipeline (validate-only)
    netauto run topology.yaml --skip-simulate

The campus, WAN, and DC worked examples are written as RFC-01 sidecars
(`topology.yaml` + `design.yaml`). The current `netauto run` simulation lane is
still [netsim](../netsim)-native, so this example uses the validate-only pipeline path.
Use `examples/hello-world/` for the end-to-end simulation + visualization demo.

---

## What to Expect

The validate stage checks:

- All 9 nodes are present with valid roles.
- All 11 links reference existing nodes.
- No duplicate node or link IDs.
- No overlapping subnets in design.yaml.

The pre-flight pipeline reruns validation through the unified `netauto run`
entry point and should end with:

    [VALIDATE] PASSED
    [SIMULATE] SKIPPED

Warnings are expected for:

- The redundant triangle between the core and distribution switches
- Single-homed access blocks that are still single points of failure

---

## Design Notes

**Why OSPF area 0 for everything?**

For a campus this size (< 50 nodes), a single area is simpler and still
converges quickly. If the campus grows, move access switches to stub areas.

**Inter-VLAN routing at the core**

The core switch is the default gateway for all four VLANs. This is the
traditional "router-on-a-stick" campus model. For higher throughput, move
routing to the distribution layer.

**Dual uplinks from access to distribution**

Each access switch has two uplinks, one to each distribution switch. OSPF
provides automatic failover if one distribution switch goes down.

```

### design.yaml

```yaml
schema: netauto/design/v2.0
base_topology: topology.yaml
topology_id: campus-01
description: "OSPF underlay + inter-VLAN routing for campus-01."

protocols:
  ospf:
    area: 0
    interfaces:
      # Core uplinks
      - node: campus-core-01:p1
        cost: 10
      - node: campus-core-01:p2
        cost: 10
      - node: campus-dist-01:p1
        cost: 10
      - node: campus-dist-01:p2
        cost: 10
      - node: campus-dist-02:p1
        cost: 10
      - node: campus-dist-02:p2
        cost: 10
      # Distribution-to-access uplinks
      - node: campus-dist-01:p3
        cost: 20
      - node: campus-dist-01:p4
        cost: 20
      - node: campus-dist-02:p3
        cost: 20
      - node: campus-dist-02:p4
        cost: 20

vlans:
  - id: 10
    name: users
    subnet: "10.10.10.0/24"
    gateway: "10.10.10.1"
    gateway_node: campus-core-01
  - id: 20
    name: servers
    subnet: "10.10.20.0/24"
    gateway: "10.10.20.1"
    gateway_node: campus-core-01
  - id: 30
    name: voice
    subnet: "10.10.30.0/24"
    gateway: "10.10.30.1"
    gateway_node: campus-core-01
  - id: 40
    name: management
    subnet: "10.10.40.0/24"
    gateway: "10.10.40.1"
    gateway_node: campus-core-01

addressing:
  loopbacks:
    pool: "10.0.0.0/24"
    strategy: sequential
  point_to_point:
    pool: "10.1.0.0/16"
    mask: /30
    strategy: deterministic

```

### topology.yaml

```yaml
schema: netauto/topology/v2.0
topology_id: campus-01
description: "Small campus: 1 core, 2 distribution, 6 access switches. OSPF + inter-VLAN routing."

nodes:
  - id: campus-core-01
    role: core
    site: campus
    vendor: cisco
    model: "Catalyst 9500"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2
      - id: p3
        vendor_name: GigabitEthernet1/0/3
      - id: p4
        vendor_name: GigabitEthernet1/0/4

  - id: campus-dist-01
    role: distribution
    site: campus
    vendor: cisco
    model: "Catalyst 9300"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2
      - id: p3
        vendor_name: GigabitEthernet1/0/3
      - id: p4
        vendor_name: GigabitEthernet1/0/4

  - id: campus-dist-02
    role: distribution
    site: campus
    vendor: cisco
    model: "Catalyst 9300"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2
      - id: p3
        vendor_name: GigabitEthernet1/0/3
      - id: p4
        vendor_name: GigabitEthernet1/0/4

  - id: campus-access-01
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

  - id: campus-access-02
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

  - id: campus-access-03
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

  - id: campus-access-04
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

  - id: campus-access-05
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

  - id: campus-access-06
    role: access
    site: campus
    vendor: cisco
    model: "Catalyst 9200"
    interfaces:
      - id: p1
        vendor_name: GigabitEthernet1/0/1
      - id: p2
        vendor_name: GigabitEthernet1/0/2

links:
  # Core uplinks to distribution (redundant)
  - id: campus-core-01:p1--campus-dist-01:p1
    endpoints:
      - node_id: campus-core-01
        interface_id: p1
      - node_id: campus-dist-01
        interface_id: p1

  - id: campus-core-01:p2--campus-dist-02:p1
    endpoints:
      - node_id: campus-core-01
        interface_id: p2
      - node_id: campus-dist-02
        interface_id: p1

  # Cross-link between distribution switches
  - id: campus-dist-01:p2--campus-dist-02:p2
    endpoints:
      - node_id: campus-dist-01
        interface_id: p2
      - node_id: campus-dist-02
        interface_id: p2

  # Access switches dual-homed to both distribution switches
  - id: campus-dist-01:p3--campus-access-01:p1
    endpoints:
      - node_id: campus-dist-01
        interface_id: p3
      - node_id: campus-access-01
        interface_id: p1

  - id: campus-dist-02:p3--campus-access-01:p2
    endpoints:
      - node_id: campus-dist-02
        interface_id: p3
      - node_id: campus-access-01
        interface_id: p2

  - id: campus-dist-01:p4--campus-access-02:p1
    endpoints:
      - node_id: campus-dist-01
        interface_id: p4
      - node_id: campus-access-02
        interface_id: p1

  - id: campus-dist-02:p4--campus-access-02:p2
    endpoints:
      - node_id: campus-dist-02
        interface_id: p4
      - node_id: campus-access-02
        interface_id: p2

  - id: campus-core-01:p3--campus-access-03:p1
    endpoints:
      - node_id: campus-core-01
        interface_id: p3
      - node_id: campus-access-03
        interface_id: p1

  - id: campus-dist-01:p3--campus-access-04:p1
    endpoints:
      - node_id: campus-dist-01
        interface_id: p3
      - node_id: campus-access-04
        interface_id: p1

  - id: campus-dist-02:p3--campus-access-05:p1
    endpoints:
      - node_id: campus-dist-02
        interface_id: p3
      - node_id: campus-access-05
        interface_id: p1

  - id: campus-dist-02:p4--campus-access-06:p1
    endpoints:
      - node_id: campus-dist-02
        interface_id: p4
      - node_id: campus-access-06
        interface_id: p1

```

### README.md

```markdown
# Compositional Failure Demo

**The single most important demo in this repository.**

This example shows why per-device validation is not enough. Three
scenarios demonstrate failures that only appear when you analyse the
*composition* of device configurations — never on any single device.

## Run it

Canonical first-user proof:

```bash
python3 -m tools.netauto_cli.main demo --scenario compositional-failure
```

This writes:

- `artifacts/latest/change-safety-gate-report.json`
- `artifacts/latest/change-safety-gate-report.md`
- `artifacts/latest/change-safety-gate-report.html`

The older `decision-report.json` and `decision-report.md` filenames are also
written as compatibility aliases.

Narrative walkthrough:

```bash
bash examples/compositional-failure/run.sh
```

If `ank_ncp` is installed, the demo runs live. Otherwise it displays
pre-baked output from `expected/`.

For deterministic smoke tests or demos on machines without the sibling toolchain:

```bash
bash examples/compositional-failure/run.sh --prebaked
```

To require a live compiler run:

```bash
bash examples/compositional-failure/run.sh --live
```

## What you will see

### 1. Happy path (clean OSPF)

A spine-leaf topology compiles, validates, and renders to Cisco IOS.
No findings. This is what a correct network looks like.

### 2. VRF Duplicate RD (caught today)

Two PE routers share RD `65000:1` with the same route-targets. Each
device is individually valid. The compiler catches the conflict
because it analyses the RD+RT space across all devices simultaneously:

```
FATAL: Duplicate VRF RD '65000:1' on devices [0, 1] without distinct route-targets
```

Deployment is blocked before any config reaches a device.

### 3. OSPF Missing Area (caught today)

A router has OSPF enabled but no interface bound to an area. The
router will start an OSPF process, form no adjacencies, and be
silently unreachable. The compiler catches the gap:

```
FATAL: Device 0 has OSPF configuration but no interface-scoped OSPF area membership
```

### 4. Transitive RT Leak (the killer demo)

Three EVPN leaf switches. Each device passes validation individually.

```
leaf-01 (VRF-BLUE):   exports RT 100:1
leaf-02 (VRF-SHARED): imports RT 100:1, exports RT 300:1
leaf-04 (VRF-RED):    imports RT 300:1
```

Each import was individually reviewed and approved. No duplicate RTs.
No per-device error. But the composition creates a transitive path:

```
BLUE --(100:1)--> SHARED --(300:1)--> RED
```

Tenant A routes transit through the shared-services VRF into Tenant B.
Silent data sovereignty violation. No alarm.

The generated Arista EOS configs in `expected/rt-leak-render-arista.txt`
show the dangerous import chains in real vendor syntax.

**Status:** The structural VRF checks (sections 2-3) are live today.
The canonical Python demo also blocks the transitive RT leak with repo-local
route-target closure analysis.

## Files

| File | Purpose |
|------|---------|
| `intent-clean.yaml` | Correct OSPF topology (passes all checks) |
| `intent-broken-vrf.yaml` | Duplicate RD compositional failure |
| `intent-broken-ospf.yaml` | OSPF completeness failure |
| `intent-rt-leak.yaml` | Transitive RT leak (3 VRFs, 3 tenants) |
| `artifacts/latest/` | Generated decision reports from the canonical demo |
| `run.sh` | Demo runner (live or pre-baked) |
| `expected/` | Pre-baked outputs for offline viewing |

## Why this matters

 of network outages are caused by compositional failures —
independently correct configurations that interact to create faults.

See [content/evidence/EVIDENCE-PORTFOLIO.md](../../content/evidence/EVIDENCE-PORTFOLIO.md)
for the full catalogue of failure modes, path properties, and
compliance mappings.

```

### change-safety-gate-report.md

```markdown
# Change Safety Gate Report

## Decision

- Scenario: `compositional-failure`
- Status: `PASS`
- Gate boundary: repo-local compositional analyzer classifies intent before deployment.

| Fixture | Verdict | Expected | Result |
| --- | --- | --- | --- |
| `intent-clean.yaml` | `ALLOW` | `ALLOW` | matched |
| `intent-broken-vrf.yaml` | `STOP` | `STOP` | matched |
| `intent-broken-ospf.yaml` | `STOP` | `STOP` | matched |
| `intent-rt-leak.yaml` | `STOP` | `STOP` | matched |

## Findings

### intent-clean.yaml

Verdict: `ALLOW`

Clean OSPF topology has usable area bindings.

- No findings.

### intent-broken-vrf.yaml

Verdict: `STOP`

RD 65000:1 is reused with overlapping route-targets.

- `DUPLICATE_RD_OVERLAPPING_RT`: RD 65000:1 is reused with overlapping route-targets. Nodes: pe1, pe2.

### intent-broken-ospf.yaml

Verdict: `STOP`

OSPF node has no usable interface area binding.

- `OSPF_MISSING_AREA_BINDING`: OSPF node has no usable interface area binding. Nodes: router1.

### intent-rt-leak.yaml

Verdict: `STOP`

Route-target imports create a transitive path from tenant-a to tenant-b.

- `TRANSITIVE_RT_TENANT_LEAK`: Route-target imports create a transitive path from tenant-a to tenant-b. Path: VRF-BLUE -> VRF-SHARED -> VRF-RED.

```

---

## Quick Facts

| | |
|---|---|
| **Status** | Recently Updated |

---

## What This Is

This project aims to comprehensively define the **overall architecture of the Network Automation Ecosystem**. This involves understanding how the existing and planned tools (such as `[topogen](../topogen)`, `[autonetkit](../autonetkit)`, `[netsim](../netsim)`, `[netflowsim](../netflowsim)`, `[netvis](../netvis)`, and the `Workbench`), along with strategic initiatives like the "Intelligence Layer," integrate to form a cohesive, unified, and differentiated product.

The output of this project will be a clearer, more formalized architectural understanding, enabling the identification and discussion of future sub-projects that contribute to the ecosystem's evolution.

---

## Why We're Doing This

The Network Automation Ecosystem is evolving from a collection of specialized tools into a "Composable Network Toolchain." To effectively manage this evolution and ensure strategic alignment, it is critical to:

*   **Formalize Architectural Understanding:** Document the relationships, data flows, and integration points between all components.
*   **Identify Future Sub-Projects:** Clearly define opportunities for new tools or major enhancements (e.g., the Intelligence Layer, legacy ingestion, multi-interface orchestration) and their place within the ecosystem.
*   **Ensure Product Differentiation:** Research the broader ecosystem to identify unique selling points and areas for competitive advantage.
*   **Guide Strategic Development:** Provide a foundational architectural blueprint for decision-making regarding technology choices, integration patterns, and development priorities.
*   **Enhance Collaboration:** Create a shared understanding for all stakeholders, from engineers to product management.

This project directly supports the strategic vision outlined in `STRATEGY.md` and deepens the insights from `README.md`, `DATAFLOWS.md`, and `ECOSYSTEM_INTEROP.md`.

---

## Success Metrics

*   **Comprehensive Architectural Mapping:** Produce a clear and detailed architectural overview that integrates all current and proposed tools, data flows, and strategic pillars.
*   **Identified Sub-Projects:** Define at least 3-5 high-level future sub-projects with clear scope and rationale.
*   **Differentiated Value Proposition:** Clearly articulate the unique competitive advantages and differentiators of the ecosystem based on research.
*   **Stakeholder Alignment:** Achieve consensus among key stakeholders on the architectural vision and roadmap for the ecosystem.
*   **Foundational Research:** Complete thorough research into the general domain ecosystem, standard practices, and competitive landscape.

---

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| **Project Scope** | To address the need for a holistic view of the Network Automation Ecosystem, the project will focus on defining the overall architecture, rather than a single component like the GNN. This provides a necessary foundation for future sub-projects. | Capture overall architecture and future sub-projects. |
| **Research Focus** | Initial research will prioritize understanding the general ecosystem, competitor offerings, and best practices in network automation to inform product differentiation and strategic direction. | Focus research on broader ecosystem and differentiation. |

---

## Documentation conventions

- Internal doc links use repo-root relative paths (no leading `/`), e.g. `.planning/research/ARCHITECTURE.md`.
- Use anchors (`#...`) when it improves precision.
- Do not use `./` or `../` for internal doc links.
- Run `.planning/scripts/check-links` before completing doc-heavy phases.
- Roadmap parity: `ROADMAP.md` and `.planning/ROADMAP.md` must remain byte-identical.

---

## Current State

**Latest Milestone:** v4.0 Deployment, Operations & Scaling (shipped 2026-03-01)

**What Was Delivered:**
- **Observability & Telemetry Pipeline :** Standard telemetry schema (netauto/telemetry/v1.0), anomaly detection loop (Inference -> UI overlays), retention & keyframing strategy.
- **CI/CD & Shadow Network Patterns :** CI/CD validation gates (GitHub Actions/GitLab CI), "Shadow Network" digital twin architecture, artifact provenance & signing (Ed25519).
- **Scale-Out & Visualization Services :** Headless GPU-accelerated layout service (wgpu compute), progressive coordinate streaming, stateless worker node pattern for simulations.
- **Governance & Multi-Tenant Operations :** Workspace namespace isolation, RBAC model for RFC artifacts, centralized immutable audit logging.

**Quality Metrics:**
- 26/26 phases complete
- 67/67 plans executed
- ~45,000 lines of architecture documentation across 120+ files
-  requirements coverage across all milestones

**Codebase State:**
- 9 tool repositories documented
- 5 ADRs, 6 RFCs
- 10+ Implementation & Operations Guides added in v3.0/v4.0

---

## # v1.1 Architecture Evolution & Refinement (shipped 2026-02-28)

- Resolved 3 open architectural questions (OQ-02, OQ-03, OQ-04) with ADRs and RFCs
- Created 9-tool ecosystem architecture (added [netassure](../netassure) as standalone advanced analysis engine)
- Defined comprehensive intelligence layer (telemetry infrastructure, GNN training pipeline, dual deployment, Live Hook integration)
- Architected CLI scrape tool (8-vendor legacy ingestion, normalization, diff engine, multi-VRF)
- Established Live Hook architecture (multiplexed WebSocket, fold-on-client state, retention/keyframes for timeline scrubbing)
- Documented 5 advanced analysis paradigms in [netassure](../netassure) (formal verification, graph algorithms, failure cascades, ML/GNN, optimization)
- Maintained architecture integrity across 38,206 lines of documentation (100+ Markdown files with passing link checks)

---

## # v1.0 Initial Architecture Definition (shipped 2026-02-21)

- Architecture spine establishment (README, STRATEGY, DATAFLOWS alignment)
- Requirements traceability (ARCH-01 through ARCH-07 with evidence links)
- RFC-01 OperationalTopology Contract (pinned schema v1.0)
- RFC-02 Live Overlay Stream Contract (pinned schema + NDJSON validator)
- Canonical RFC fixture projects (minimal-lab, leaf-spine, edge-cases)
- All validation gates passing (check-fixtures, check-links)

</details>

---

## Requirements



---

## # Validated

<!-- Milestone v1.0: Initial Architecture Definition  -->

- ✓ **ARCH-01**: Document current state architecture of the Network Automation Ecosystem, including all existing tools and their interactions. — v1.0
- ✓ **ARCH-02**: Identify and document key data flows and integration interfaces between all ecosystem components. — v1.0
- ✓ **ARCH-03**: Research the broader network automation domain to identify current trends, competitor offerings, and best practices. — v1.0
- ✓ **ARCH-04**: Articulate the unique value proposition and product differentiation strategy for the ecosystem. — v1.0
- ✓ **ARCH-05**: Define high-level architectural principles and tenets guiding future development. — v1.0
- ✓ **ARCH-06**: Propose a structured approach for identifying and prioritizing future sub-projects (e.g., GNN Intelligence Layer, Legacy Ingestion). — v1.0
- ✓ **ARCH-07**: Summarize open architectural questions and areas requiring further deep-dive exploration. — v1.0

<!-- Milestone v1.1: Architecture Evolution & Refinement  -->

- ✓ **OQ-REQ-01, OQ-REQ-02, OQ-REQ-03**: Interface representation investigation (benchmarks, prototypes, RFC-03 decision) — v1.1
- ✓ **INT-REQ-01, INT-REQ-02, INT-REQ-03, INT-REQ-04**: Intelligence Layer architecture (telemetry, GNN training, inference, Live Hook) — v1.1
- ✓ **CLI-REQ-01, CLI-REQ-02, CLI-REQ-03, CLI-REQ-04**: CLI Scrape architecture (8-vendor, normalization, diff, multi-VRF) — v1.1
- ✓ **VIS-REQ-01, VIS-REQ-02, VIS-REQ-03**: [netvis](../netvis) decomposition (5 use cases, OQ-04 decision, Live Hook architecture) — v1.1
- ✓ **WB-REQ-01, WB-REQ-02, WB-REQ-03, WB-REQ-04**: Workbench orchestration (OQ-03 decision, workflows, parity, error handling) — v1.1

---

## # Active

<!-- Milestone v3.0: Implementation & Developer Enablement  -->

(Will be defined during v3.0 requirements phase)

---

## # Out of Scope

- **Immediate Code Changes:** The primary output is documentation and strategic guidance, not direct code modification.
- **Specific Model Training:** While the Intelligence Layer architecture will be defined, actual model training and tuning is implementation work.

*Last updated: 2026-02-28 after starting milestone v2.0*

---

## Current Status

2026-04-11 —  Agentic Translation Layer shipped; UUID Registry and Pessimistic Locking live.

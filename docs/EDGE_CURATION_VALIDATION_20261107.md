This adds an immutable native GTDB-to-NCBI mapping adapter for EdgeMech.
Complete source rows, mapping orientation and predicates, lexical genome
counts, source positions and source-file hashes are retained. This native
inventory lacks assertion-level approval proofs, so every assertion remains
unassessed. Generated record status does not become mapping approval.

The shared source pin is CLAW `1b5391d083ba85ac94e5279c3cba25ac4fde243c`
(prerequisite CLAW PR #962). A dedicated integration workflow verifies that
pin and requires the feature tests. This implements the TaxonMech slice of
[CLAW #767](https://github.com/CultureBotAI/culturebotai-claw/issues/767).

Validation on 2026-11-07:

- 18 focused tests passed in mandatory shared-contract mode. These cover
  native predicate orientation, preserved lexical fields, unassessed scope,
  real exporter mutation by valid-row reversal/duplication, exclusive
  publication, interrupted publication and directory durability.
- Real spawn tests verify serial/four-worker byte identity and worker failure
  without publication. The bounded-submission test verifies source order and
  a maximum window of 256 selected rows. Ruff passed for the new code.
- A position-1 canary and complete export used the same module launcher,
  exact shared checkout, native source commit
  `ab35a0d0a0a2b47d250145db0c15b414fccbfdb8` and `--workers 4` mode.
- Every generated envelope passed the shared validator. Exact persisted
  bytes, ordered assertion-ID/source-position membership and status counters
  were reconciled before manifest-last publication. Identical persisted
  bytes do not undergo a redundant second schema pass.
- The full export contains all 322,327 native mapping rows, all unassessed.
  Zero independent scientific reviews or KG occurrence approvals were
  produced. Final files, hashes, line/byte counts and last source position
  were checked on disk after publication.

| Export under `build/edge-curation-20261107/` | Rows | JSONL bytes | Manifest SHA256 | JSONL SHA256 |
|---|---:|---:|---|---|
| `canary-parallel` | 1 | 3,926 | `34a76d1a74315faca828c76180d7da28a2e8f6ad8e7d559209abb6a737a286c1` | `819663bf1f8ed46b89a02700699cc1054e11b37e12cfb78f8863865e48f80903` |
| `full-parallel` | 322,327 | 1,270,205,665 | `c12ca30e4adec18849311946fbbb27ee3045c1b3a2b845ef178f2db0ed6960a5` | `5627142eca97036834c6b717927a0bab1670554a1acb183402b0528c5e408f68` |

The full ordered assertion-ID/source-position membership digest is
`c864515e8f1cebf163b072565181932bcec82bb41eb875780b63a2894c3d6d01`.
Its complete native input is 36,331,768 bytes with SHA256
`bf62441b1b76abb16dd92e795c020ff30fc24e37e195b862fb9beda567277225`;
the committed native provenance manifest independently declares that hash,
size and row count.

Reproduce after the shared pin check described in `docs/EDGE_CURATION.md`:

```bash
python -m taxonmech.edge_curation --root . --source-commit ab35a0d0a0a2b47d250145db0c15b414fccbfdb8 --workers 4 --positions 1 --output build/edge-curation/canary
python -m taxonmech.edge_curation --root . --source-commit ab35a0d0a0a2b47d250145db0c15b414fccbfdb8 --workers 4 --all --output build/edge-curation/full
```

Verify the first output before running the second command. Analytical
payloads stay outside Git; no per-assertion record or Pages artifact is added.

Independent read-only review filed #227 for persisted byte/membership
verification and #228 for redundant serial validation cost. Both repairs,
their mutation/parallelism tests and the four-worker real canary passed
independent reinspection. Fixes #227. Fixes #228.

Issue #226 remains open for exact native review proofs and distinct
strain/deposit, assembly/genome and nomenclature assertion surfaces.
Unassessed mappings and unavailable review evidence must not be reported as
absence of biological overlap or as reviewed equivalence.

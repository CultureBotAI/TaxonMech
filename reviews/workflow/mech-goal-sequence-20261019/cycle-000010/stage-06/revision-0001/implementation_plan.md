# Cycle 10 Stage 6 (`infrastructure`) — Dependency-Aware Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `10`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **Supervisor-Frozen `infra_scope`**:
  - `frozen_at`: `2026-11-10T04:43:08Z`
  - `sha256`: `e0ad8a4e0d70365132924802c3aef51d0101476a45e2c3aafab582f53af3f8ef`
  - Snapshot artifact: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-06/revision-0001/infra_snapshot.md`

---

## 1. Frozen Intake Summary (`INFRA_TASKS.md` at `2026-11-10T04:43:08Z`)

| Task ID | Priority | Dependencies | Frozen Status | Linked Issue(s) | Cycle 10 Stage 6 Action & Disposition |
|---|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | `deferred` | `#78`, `#249` | **Selected for targeted Cycle 10 Stage 6 hardening** (`#249`): enforce `CausalNode.grounding` prefix-to-`node_type` domain isolation (`NCBITaxon:` exclusively on `TAXON`, `UniProtKB:` matching `UNIPROT_ID_PATTERN` exclusively on `GENE_OR_PROTEIN`) and single `RO:0002292` (`expresses`) edge per `GENE_OR_PROTEIN` `object` (`seen_expressed_objects`) in `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 516–730), plus required host-subtree `strain_id` binding whenever the host `TaxonRecord.identifier` has a lineage-compatible BacDive strain in its subtree (`scripts/check_provenance.py` lines 218–241). **Carried forward as `deferred` to Cycle 11** under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion. |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | `deferred` | `#78` | **Explicitly carried forward as `deferred` to Cycle 11** under open umbrella issue `#78`. `extract_taxon_trait_edges()` and `TRAIT_EDGE_FIELDS` remain implemented and unit-tested in `src/taxonmech/extract.py`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 phenotype/trait/medium-attested records requires an upstream local `kg-microbe` checkout re-extraction (`just extract-inventory`). |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | `deferred` | `#78`, `#249` | **Selected for targeted Cycle 10 Stage 6 hardening** (`#249`): enforce per-organism `(organism_taxon_id, gene_symbol)` uniqueness (`seen_org_genes`), per-organism `(organism_taxon_id, sequence_crc64)` uniqueness (`seen_org_crc64`), per-organism `entry_name` `_<org_code>` suffix consistency (`seen_org_mnemonic_suffix`), and `entry_status`↔`entry_name` prefix alignment (`TREMBL` prefix equals bare accession; `SWISS_PROT` prefix differs from bare accession) in `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 339–484). **Carried forward as `deferred` to Cycle 11** under open umbrella issue `#78` pending a corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot. |
| `taxonmech-infra-0004` | `medium` | None | `deferred` | `#8` | **Explicitly carried forward as `deferred` to Cycle 11** under open issue `#8`. Upstream `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` edge-table SHA-256 digests and direct-taxid vs BacDive-subtree attestation semantics remain documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 `pass_with_limitations` records is deferred pending a dedicated 626,048-record YAML and `pages/` regeneration pass. |

---

## 2. Dependency Graph & Issue Grouping

1. **Issue [#249](https://github.com/CultureBotAI/TaxonMech/issues/249)** (*"Enforce UniProt per-organism gene/CRC64/mnemonic consistency, CausalNode grounding prefix isolation, single RO:0002292 expression, and subtree strain_id provenance gates (#78)"*, child of open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)):
   - Groups the repository-local Cycle 10 Stage 6 validation and provenance upgrades for `taxonmech-infra-0001` and `taxonmech-infra-0003` following the Cycle 10 Stage 2 (`PR #240`, 389 edges), Cycle 10 Stage 3 (`PR #243`, 426 edges, 119 `GENE_OR_PROTEIN` nodes, 54 UniProtKB accessions), and Cycle 10 Stage 5 (`#246`, `PR #247`) expansions.
2. **Umbrella Issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)** (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`):
   - Remains open to track upstream `kg-microbe` raw trait-edge extraction (`taxonmech-infra-0002`) and corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot integration (`taxonmech-infra-0003`).
3. **Issue [#8](https://github.com/CultureBotAI/TaxonMech/issues/8)** (`taxonmech-infra-0004`):
   - Remains open to track the corpus-wide 626,048-record `source_attestations` re-seeding and `pages/` regeneration pass.

---

## 3. Selected Implementation Scope & Acceptance Criteria (`#249`)

### 3.1 `load_uniprot_proteins()` Per-Organism Gene/CRC64 Uniqueness & Mnemonic Consistency (`src/taxonmech/seed.py`)
- **Implementation**:
  - In `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 339–484), enforce:
    1. Per-organism `(organism_taxon_id, gene_symbol)` uniqueness (`seen_org_genes`) when `gene_symbol` is populated.
    2. Per-organism `(organism_taxon_id, sequence_crc64)` uniqueness (`seen_org_crc64`).
    3. Per-organism `entry_name` `_<org_code>` suffix consistency (`seen_org_mnemonic_suffix`, requiring every entry for a given `organism_taxon_id` to share the same organism suffix) and `entry_status`↔`entry_name` prefix alignment (`TREMBL` entries must have `<mnemonic> == bare_accession`, whereas `SWISS_PROT` entries must have `<mnemonic> != bare_accession`).
- **Acceptance Criteria**:
  - All 54 rows in `curation/uniprot_proteins.tsv` (52 `SWISS_PROT`, 2 `TREMBL`) pass `load_uniprot_proteins()` with `data/raw/ncbitaxon_taxa.tsv`.
  - Synthetic TSV inputs with duplicate `(organism_taxon_id, gene_symbol)`, duplicate `(organism_taxon_id, sequence_crc64)`, inconsistent `entry_name` organism suffix, or mismatched `TREMBL`/`SWISS_PROT` `entry_name` prefix raise `SystemExit` with explicit diagnostics.

### 3.2 `validate_causal_graph_structure()` Prefix-to-`node_type` Isolation & Single `RO:0002292` Expression (`src/taxonmech/seed.py`)
- **Implementation**:
  - In `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 516–730):
    1. Reject any non-`TAXON` node (`ntype != "TAXON"`) using an `NCBITaxon:` `grounding`, reject any non-`GENE_OR_PROTEIN` node (`ntype != "GENE_OR_PROTEIN"`) using a `UniProtKB:` `grounding`, and require any `GENE_OR_PROTEIN` node with `grounding` to match `UNIPROT_ID_PATTERN`.
    2. Track `seen_expressed_objects: set[str]` and reject duplicate `RO:0002292` (`expresses`) edges targeting the same `GENE_OR_PROTEIN` `object` within a `CausalGraph`.
- **Acceptance Criteria**:
  - All 15 maintained overlays (`curation/causal_graphs/*.yaml`, 426 edges, 119 `GENE_OR_PROTEIN` nodes) pass `validate_causal_graph_structure()`.
  - Synthetic graphs with a non-`TAXON` `NCBITaxon:` grounding, a non-`GENE_OR_PROTEIN` `UniProtKB:` grounding, a `GENE_OR_PROTEIN` with non-`UNIPROT_ID_PATTERN` grounding, or duplicate `RO:0002292` edges targeting the same `GENE_OR_PROTEIN` `object` raise `SystemExit`.

### 3.3 `causal_graph_provenance_problems()` Required Host-Subtree `strain_id` Gate (`scripts/check_provenance.py`)
- **Implementation**:
  - In `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 218–241), when `strains is not None and taxa is not None`, check whether the host `TaxonRecord.identifier` (`tid`) has any BacDive strain in its subtree (`s_tid == tid or tid in _taxon_lineage(taxa, s_tid)`) that is lineage-compatible (`_taxa_lineage_compatible(taxa, s_tid, org_tid)`) with the `GENE_OR_PROTEIN` node's `organism_taxon_id`; if so, require the `GENE_OR_PROTEIN` node to declare a non-empty `strain_id` (`#246`, `#197`).
- **Acceptance Criteria**:
  - `python3 scripts/check_provenance.py` exits `0` on the repository.
  - Synthetic overlays omitting `strain_id` on a host taxon with a lineage-compatible subtree BacDive strain are reported by `causal_graph_provenance_problems()`.

### 3.4 Documentation, Ledger Reconciliation & Unit Tests
- Update `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, and `docs/CURATION.md` with the new `#249` gates and updated `src/taxonmech/seed.py` (`lines 339–484`, `lines 803–808, 903–920`) and `scripts/check_provenance.py` (`lines 218–241`, `lines 244–256`) line ranges.
- Update `INFRA_TASKS.md` (both machine-readable YAML block and markdown task sections) to record Cycle 10 Stage 2 (`PR #240`), Stage 3 (`PR #243`), Stage 5 (`#246`, `PR #247`), and Stage 6 (`#249`) dispositions and carry `taxonmech-infra-0001..0004` forward to Cycle 11.
- Add `test_cycle10_stage6_uniprot_gene_crc64_mnemonic_and_causal_graph_prefix_strain_id_gates` in `tests/test_causal_graph_overlays.py`.

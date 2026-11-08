# Cycle 9 Stage 6 (`infrastructure`) — Dependency-Aware Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `9`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **Supervisor-Frozen `infra_scope`**:
  - `frozen_at`: `2026-11-08T17:17:06Z`
  - `sha256`: `0df9141042e64ab44338bb6e8beec7933b770847a8f3deb5fc0cb77de1cd77fa`
  - Snapshot artifact: `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-06/revision-0001/infra_snapshot.md`

---

## 1. Frozen Intake Summary (`INFRA_TASKS.md` at `2026-11-08T17:17:06Z`)

| Task ID | Priority | Dependencies | Frozen Status | Linked Issue(s) | Cycle 9 Stage 6 Action & Disposition |
|---|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | `deferred` | `#78`, `#236` | **Selected for targeted Cycle 9 Stage 6 hardening** (`#236`): enforce per-graph `CausalNode.label` uniqueness (`seen_node_labels`), rejection of edges targeting a `TAXON` node as `object`, and `RO:0002292` (`expresses`) object `GENE_OR_PROTEIN` typing in `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 479–670), plus required non-empty `grounding` on every `CausalNode`, `TAXON` node `label` correspondence with `ncbitaxon_taxa.tsv`, and host-`TAXON` subject validation on `RO:0002292` edges in `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 154–265). **Carried forward as `deferred` to Cycle 10** under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion. |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | `deferred` | `#78` | **Explicitly carried forward as `deferred` to Cycle 10** under open umbrella issue `#78`. `extract_taxon_trait_edges()` and `TRAIT_EDGE_FIELDS` remain implemented and unit-tested in `src/taxonmech/extract.py`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 phenotype/trait/medium-attested records requires an upstream local `kg-microbe` checkout re-extraction (`just extract-inventory`). |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | `deferred` | `#78`, `#236` | **Selected for targeted Cycle 9 Stage 6 hardening** (`#236`): enforce `UNIPROT_RELEASE_PATTERN` (`^20[0-9]{2}_(?:0[1-9]\|1[0-2])$`), catalog-wide `organism_taxon_id`→`(organism_label, proteome_id)` consistency (`seen_org_meta`), 1:1 `proteome_id`→`organism_taxon_id` mapping (`seen_proteome_org`), and `organism_label` correspondence with `ncbitaxon_taxa.tsv` in `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 84, 339–447). **Carried forward as `deferred` to Cycle 10** under open umbrella issue `#78` pending a corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot. |
| `taxonmech-infra-0004` | `medium` | None | `deferred` | `#8` | **Explicitly carried forward as `deferred` to Cycle 10** under open issue `#8`. Upstream `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` edge-table SHA-256 digests and direct-taxid vs BacDive-subtree attestation semantics remain documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 `pass_with_limitations` records is deferred pending a dedicated 626,048-record YAML and `pages/` regeneration pass. |

---

## 2. Dependency Graph & Issue Grouping

1. **Issue [#236](https://github.com/CultureBotAI/TaxonMech/issues/236)** (*"Enforce UniProt release/organism/proteome consistency, per-graph node label uniqueness, RO:0002292 domain/range typing, and TAXON label/node grounding provenance gates (#78)"*, child of open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)):
   - Groups the repository-local Cycle 9 Stage 6 validation and provenance upgrades for `taxonmech-infra-0001` and `taxonmech-infra-0003` following the Cycle 9 Stage 2 (`PR #231`, 345 edges), Cycle 9 Stage 3 (`PR #232`, 378 edges, 108 `GENE_OR_PROTEIN` nodes, 49 UniProtKB accessions), and Cycle 9 Stage 5 (`#234`, `PR #235`) expansions.
2. **Umbrella Issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)** (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`):
   - Remains open to track upstream `kg-microbe` raw trait-edge extraction (`taxonmech-infra-0002`) and corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot integration (`taxonmech-infra-0003`).
3. **Issue [#8](https://github.com/CultureBotAI/TaxonMech/issues/8)** (`taxonmech-infra-0004`):
   - Remains open to track the corpus-wide 626,048-record `source_attestations` re-seeding and `pages/` regeneration pass.

---

## 3. Selected Implementation Scope & Acceptance Criteria (`#236`)

### 3.1 `load_uniprot_proteins()` Release Syntax & Organism/Proteome Consistency (`src/taxonmech/seed.py`)
- **Implementation**:
  - Define `UNIPROT_RELEASE_PATTERN = re.compile(r"^20[0-9]{2}_(?:0[1-9]|1[0-2])$")` at `src/taxonmech/seed.py` line 84.
  - In `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 339–447), validate that every row's `release_version` matches `UNIPROT_RELEASE_PATTERN`, every `organism_taxon_id` maps consistently to `(organism_label, proteome_id)` across `curation/uniprot_proteins.tsv` (`seen_org_meta`), every non-empty `proteome_id` maps 1:1 to a single `organism_taxon_id` (`seen_proteome_org`), and `organism_label` equals `taxa[organism_taxon_id]["label"]` when `taxa` provides a label.
- **Acceptance Criteria**:
  - All 49 rows in `curation/uniprot_proteins.tsv` pass `load_uniprot_proteins()` with `data/raw/ncbitaxon_taxa.tsv`.
  - Synthetic TSV inputs with a malformed `release_version`, mismatched `organism_label`, inconsistent `(organism_label, proteome_id)`, or shared `proteome_id` across organisms raise `SystemExit` with explicit diagnostics.

### 3.2 `validate_causal_graph_structure()` Per-Graph Label Uniqueness & `TAXON` / `RO:0002292` Edge Typing (`src/taxonmech/seed.py`)
- **Implementation**:
  - In `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 479–670), track `seen_node_labels: set[str]` and `node_types_by_id: dict[str, str]` across all `CausalNode` entries in each `CausalGraph` and reject duplicate node `label` strings within the same graph.
  - Reject any `CausalEdge` whose `object` targets a `TAXON` node (`node_types_by_id.get(obj) == "TAXON"`) or any `RO:0002292` (`expresses`) edge whose `object` is not a `GENE_OR_PROTEIN` node (`node_types_by_id.get(obj) != "GENE_OR_PROTEIN"`).
- **Acceptance Criteria**:
  - All 15 maintained overlays (`curation/causal_graphs/*.yaml`, 378 edges, 108 `GENE_OR_PROTEIN` nodes) pass `validate_causal_graph_structure()`.
  - Synthetic graphs with duplicate node `label` values, an edge targeting a `TAXON` node, or an `RO:0002292` edge targeting a non-`GENE_OR_PROTEIN` node raise `SystemExit`.

### 3.3 `causal_graph_provenance_problems()` Node Grounding, `TAXON` Label & `RO:0002292` Subject Gates (`scripts/check_provenance.py`)
- **Implementation**:
  - In `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 154–265):
    - Require every `CausalNode` in `curation/causal_graphs/*.yaml` to carry a non-empty `grounding` CURIE.
    - Require every `TAXON` node's `label` to match `taxa[n_grounding]["label"]` in `data/raw/ncbitaxon_taxa.tsv`.
    - Require every `RO:0002292` (`expresses`) edge to originate from a host `TAXON` node (`subject in host_taxon_nids`).
- **Acceptance Criteria**:
  - `python3 scripts/check_provenance.py` exits `0` on the repository.
  - Synthetic overlays with an ungrounded node, a `TAXON` node label mismatch against `ncbitaxon_taxa.tsv`, or a non-host-`TAXON` `RO:0002292` subject are reported by `causal_graph_provenance_problems()`.

### 3.4 Documentation, Ledger Reconciliation & Unit Tests
- Update `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, and `docs/CURATION.md` with the new `#236` gates and updated `src/taxonmech/seed.py` (`lines 339–447`, `lines 743–748, 843–860`) and `scripts/check_provenance.py` (`lines 218–230`) line ranges.
- Update `INFRA_TASKS.md` (both machine-readable YAML block and markdown task sections) to record Cycle 9 Stage 2 (`PR #231`), Stage 3 (`PR #232`), Stage 5 (`#234`, `PR #235`), and Stage 6 (`#236`) dispositions and carry `taxonmech-infra-0001..0004` forward to Cycle 10.
- Add `test_cycle9_stage6_uniprot_release_org_proteome_consistency_and_causal_graph_node_label_edge_typing_gates` in `tests/test_causal_graph_overlays.py`.

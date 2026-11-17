# Cycle 8 Stage 6 (`infrastructure`) — Dependency-Aware Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `8`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **Supervisor-Frozen `infra_scope`**:
  - `frozen_at`: `2026-11-07T19:37:19Z`
  - `sha256`: `52d673554dbe32f05a8deb95fa673b274e86934b82dfba9df124cc395dcb0a76`
  - Snapshot artifact: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`

---

## 1. Frozen Intake Summary (`INFRA_TASKS.md` at `2026-11-07T19:37:19Z`)

| Task ID | Priority | Dependencies | Frozen Status | Linked Issue(s) | Cycle 8 Stage 6 Action & Disposition |
|---|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | `deferred` | `#78`, `#224` | **Selected for targeted Cycle 8 Stage 6 hardening** (`#224`): enforce per-graph `CausalNode.grounding` uniqueness across all grounded nodes (`seen_node_groundings`) and per-graph `predicate`↔`predicate_id` pairing consistency (`seen_pred_by_id`, `seen_id_by_pred`) in `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 448–624), plus required non-empty `predicate_id` on every `CausalEdge` in `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 210–222). **Carried forward as `deferred` to Cycle 9** under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion. |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | `deferred` | `#78` | **Explicitly carried forward as `deferred` to Cycle 9** under open umbrella issue `#78`. `extract_taxon_trait_edges()` and `TRAIT_EDGE_FIELDS` remain implemented and unit-tested in `src/taxonmech/extract.py`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 phenotype/trait/medium-attested records requires an upstream local `kg-microbe` checkout re-extraction (`just extract-inventory`). |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | `deferred` | `#78`, `#224` | **Selected for targeted Cycle 8 Stage 6 hardening** (`#224`): enforce `UNIPROT_ENTRY_NAME_PATTERN` (`^[A-Z0-9]{1,11}_[A-Z0-9]{2,5}$`) and catalog-wide `entry_name` and `(organism_taxon_id, locus_tag)` uniqueness in `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 83, 338–416), and require every `GENE_OR_PROTEIN` node in `curation/causal_graphs/*.yaml` to have an incoming `RO:0002292` (`expresses`) edge from a host `TAXON` node (`grounding == tid`) and at least one outgoing functional/regulatory/causal edge (`edge.subject == node_id`) in `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 156–194). **Carried forward as `deferred` to Cycle 9** under open umbrella issue `#78` pending a corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot. |
| `taxonmech-infra-0004` | `medium` | None | `deferred` | `#8` | **Explicitly carried forward as `deferred` to Cycle 9** under open issue `#8`. Upstream `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` edge-table SHA-256 digests and direct-taxid vs BacDive-subtree attestation semantics remain documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 `pass_with_limitations` records is deferred pending a dedicated 626,048-record YAML and `pages/` regeneration pass. |

---

## 2. Dependency Graph & Issue Grouping

1. **Issue [#224](https://github.com/CultureBotAI/TaxonMech/issues/224)** (*"Enforce UniProt entry_name/locus uniqueness, per-graph node grounding and predicate_id consistency, and GENE_OR_PROTEIN expression/outgoing-edge provenance gates (#78)"*, child of open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)):
   - Groups the repository-local Cycle 8 Stage 6 validation and provenance upgrades for `taxonmech-infra-0001` and `taxonmech-infra-0003` following the Cycle 8 Stage 2 (`PR #219`, 301 edges), Cycle 8 Stage 3 (`PR #220`, 334 edges, 97 `GENE_OR_PROTEIN` nodes, 44 UniProtKB accessions), and Cycle 8 Stage 5 (`#222`, `PR #223`) expansions.
2. **Umbrella Issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78)** (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`):
   - Remains open to track upstream `kg-microbe` raw trait-edge extraction (`taxonmech-infra-0002`) and corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot integration (`taxonmech-infra-0003`).
3. **Issue [#8](https://github.com/CultureBotAI/TaxonMech/issues/8)** (`taxonmech-infra-0004`):
   - Remains open to track the corpus-wide 626,048-record `source_attestations` re-seeding and `pages/` regeneration pass.

---

## 3. Selected Implementation Scope & Acceptance Criteria (`#224`)

### 3.1 `load_uniprot_proteins()` Catalog Uniqueness & `entry_name` Syntax (`src/taxonmech/seed.py`)
- **Implementation**:
  - Define `UNIPROT_ENTRY_NAME_PATTERN = re.compile(r"^[A-Z0-9]{1,11}_[A-Z0-9]{2,5}$")` at `src/taxonmech/seed.py` line 83.
  - In `load_uniprot_proteins()` (`src/taxonmech/seed.py` lines 338–416), validate that every row's `entry_name` matches `UNIPROT_ENTRY_NAME_PATTERN`, is unique across `curation/uniprot_proteins.tsv` (`seen_entry_names`), and that every non-empty `(organism_taxon_id, locus_tag)` pair is unique across `curation/uniprot_proteins.tsv` (`seen_org_loci`).
- **Acceptance Criteria**:
  - All 44 rows in `curation/uniprot_proteins.tsv` pass `load_uniprot_proteins()`.
  - Synthetic TSV inputs with a malformed `entry_name`, duplicate `entry_name`, or duplicate `(organism_taxon_id, locus_tag)` raise `SystemExit` with explicit diagnostics.

### 3.2 `validate_causal_graph_structure()` Per-Graph Grounding Uniqueness & `predicate`↔`predicate_id` Consistency (`src/taxonmech/seed.py`)
- **Implementation**:
  - In `validate_causal_graph_structure()` (`src/taxonmech/seed.py` lines 448–624), track `seen_node_groundings: set[str]` across all grounded `CausalNode` entries in each `CausalGraph` and reject duplicate `grounding` CURIEs within the same graph.
  - Track `seen_pred_by_id: dict[str, str]` and `seen_id_by_pred: dict[str, str]` across all edges in each `CausalGraph` and reject any edge that maps the same `predicate_id` to different `predicate` labels or the same `predicate` label to different `predicate_id` CURIEs within the same graph.
- **Acceptance Criteria**:
  - All 15 maintained overlays (`curation/causal_graphs/*.yaml`, 334 edges, 97 `GENE_OR_PROTEIN` nodes) pass `validate_causal_graph_structure()`.
  - Synthetic graphs with duplicate non-protein `grounding` CURIEs or inconsistent `predicate`↔`predicate_id` pairings raise `SystemExit`.

### 3.3 `causal_graph_provenance_problems()` Edge `predicate_id` & `GENE_OR_PROTEIN` Topology Gates (`scripts/check_provenance.py`)
- **Implementation**:
  - In `causal_graph_provenance_problems()` (`scripts/check_provenance.py` lines 154–233):
    - Require every `CausalEdge` in `curation/causal_graphs/*.yaml` to carry a non-empty `predicate_id` CURIE.
    - Require every `GENE_OR_PROTEIN` node in `curation/causal_graphs/*.yaml` to be linked from a host `TAXON` node (`grounding == tid`) via an incoming `RO:0002292` (`expresses`) edge and to appear as the `subject` of at least one outgoing functional/regulatory/causal `CausalEdge`.
- **Acceptance Criteria**:
  - `python3 scripts/check_provenance.py` exits `0` on the repository.
  - Synthetic overlays missing `predicate_id`, missing the host-`TAXON` `RO:0002292` (`expresses`) edge to a `GENE_OR_PROTEIN` node, or lacking an outgoing edge from a `GENE_OR_PROTEIN` node are reported by `causal_graph_provenance_problems()`.

### 3.4 Documentation, Ledger Reconciliation & Unit Tests
- Update `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, and `docs/CURATION.md` with the new `#224` gates and updated `src/taxonmech/seed.py` (`lines 338–416`, `lines 697–702, 797–814`) and `scripts/check_provenance.py` (`lines 197–209`) line ranges.
- Update `INFRA_TASKS.md` (both machine-readable YAML block and markdown task sections) to record Cycle 8 Stage 2 (`PR #219`), Stage 3 (`PR #220`), Stage 5 (`#222`, `PR #223`), and Stage 6 (`#224`) dispositions and carry `taxonmech-infra-0001..0004` forward to Cycle 9.
- Add `test_cycle8_stage6_uniprot_catalog_node_grounding_and_protein_edge_topology_gates` in `tests/test_causal_graph_overlays.py`.

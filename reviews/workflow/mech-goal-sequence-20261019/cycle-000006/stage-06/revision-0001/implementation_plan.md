# Cycle 6 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `0415ba3062aee129825160f6f6dae5d0748eddb3`
- **Frozen Intake Cutoff**: `2026-11-05T11:40:45Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md` (`sha256: ecb7de0cd54fb576b2a5bbe72e733ebe1bbcb3a1c1789f8385294909feab760a`)

## 1. Frozen Intake Inventory and Dependency Graph

At the Stage 6 cutoff (`2026-11-05T11:40:45Z`), `INFRA_TASKS.md` contains four tracked tasks (`taxonmech-infra-0001` through `taxonmech-infra-0004`):

| Task ID | Priority | Dependencies | Umbrella / Linked Issue | Stage 6 Action |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | `#78`, `#208` | **Selected (incremental structural & provenance gate hardening)**; bulk overlay expansion carried forward (`deferred`) to Cycle 7 under `#78` |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | `#78` | **Carried forward (`deferred`)** to Cycle 7 pending an upstream `kg-microbe` re-extraction of `data/raw/taxon_trait_edges.tsv` |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | `#78`, `#208` | **Selected (host-subtree `strain_id` binding & unreferenced `uniprot_proteins.tsv` catalog-row gate)**; full corpus-wide UniProt Reference Proteomes raw snapshot carried forward (`deferred`) to Cycle 7 under `#78` |
| `taxonmech-infra-0004` | `medium` | None | `#8` | **Carried forward (`deferred`)** to Cycle 7 pending a dedicated 626,048-record YAML and `pages/` regeneration pass |

## 2. Issue Deduplication and Grouping

We searched open and closed issues in `CultureBotAI/TaxonMech` (`gh issue list -R CultureBotAI/TaxonMech --state all --limit 100`):

- `#78` (`OPEN`): Umbrella tracking issue for causal-graph overlays, granular trait edge extraction, and pinned UniProtKB protein-grounding infrastructure (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`).
- `#189` (`CLOSED` via PR `#190` in Cycle 4 Stage 6): Enforced `CausalNode`/`CausalEdge` schema invariants, protein-only slot isolation, and UniProtKB EC/metadata completeness.
- `#199` (`CLOSED` via PR `#200` in Cycle 5 Stage 6): Enforced `CausalGraph` node connectivity, `graph_id`/`node_id`/`UniProtKB`/`proteome_id` regexes, species-or-below scope, and `check_provenance.py` cross-table validation.
- `#208` (created for Cycle 6 Stage 6 under umbrella `#78`): *Enforce CausalGraph required title/nodes/edges, TAXON NCBITaxon regex, host-subtree strain_id binding, and uniprot_proteins.tsv orphan-row gate (#78)*.
- `#8` (`OPEN`): Tracks `taxonmech-infra-0004` (upstream `kg-microbe` edge-multiplicity provenance and direct-taxid vs BacDive-subtree attestation counts).

## 3. Selected Implementation Scope (`#208` under `#78`)

 Following Cycle 6 Stage 2 (PR `#203`, expanding the 15 overlays from 204 to 213 evidence-backed edges) and Cycle 6 Stage 3 (PR `#204`, expanding the 15 overlays to 246 evidence-backed edges and 75 `GENE_OR_PROTEIN` nodes across 34 live-verified UniProtKB accessions), four structural and provenance validation gaps remained across `src/taxonmech/seed.py` and `scripts/check_provenance.py`:

1. **Per-taxon `graph_id` uniqueness and `TAXON` node `NCBITAXON_ID_PATTERN` enforcement in `validate_causal_graph_structure()` (`src/taxonmech/seed.py`)**:
   - `validate_causal_graph_structure()` previously did not track `seen_graph_ids` per taxon (relying solely on `load_causal_graphs()`), and only checked `grounding.startswith("NCBITaxon:")` when `grounding` was present on a `TAXON` node—allowing `TAXON` nodes with omitted `grounding` or malformed identifiers such as `NCBITaxon:0`.
   - **Upgrade**: Track `seen_graph_ids` per `tid` directly in `validate_causal_graph_structure()` and require every `TAXON` node (`node_type == "TAXON"`) to carry a non-empty `grounding` matching `NCBITAXON_ID_PATTERN` (`^NCBITaxon:[1-9][0-9]*$`).
2. **Required `title`, `nodes`, and `edges` on overlays loaded by `load_causal_graphs()` (`src/taxonmech/seed.py`)**:
   - `load_causal_graphs()` previously validated `graph_id` on each loaded `CausalGraph` entry without verifying that `title` is a non-empty string or that `nodes` and `edges` are non-empty lists (since `validate_causal_graph_structure()` only validated `nodes` and `edges` when `not None`).
   - **Upgrade**: Require every `CausalGraph` entry loaded from `curation/causal_graphs/*.yaml` via `load_causal_graphs()` to declare a non-empty `title`, a non-empty `nodes` list, and a non-empty `edges` list.
3. **Host-subtree `strain_id` binding in `validate_causal_graph_proteins()` (`src/taxonmech/seed.py`)**:
   - `curation/causal_graphs/README.md` specifies that when `strain_id` is declared on a `GENE_OR_PROTEIN` node, it must appear on the host `TaxonRecord.strains[]` list (which `build_document()` populates from `tid` and `descendants(tid)`, i.e. `s_tid == tid or tid in _taxon_lineage(taxa, s_tid)`). Previously, `validate_causal_graph_proteins()` used the symmetric `_taxa_lineage_compatible(taxa, s_tid, tid)` check, which also permitted `s_tid in _taxon_lineage(taxa, tid)` (an ancestor species' `strain_id` declared on an infraspecific strain overlay whose `strains` list is `[]`).
   - **Upgrade**: Require at least one taxon `s_tid` linked to `strain_id` in `data/raw/bacdive_strains.tsv` to satisfy `s_tid == tid or tid in _taxon_lineage(taxa, s_tid)` as well as `_taxa_lineage_compatible(taxa, s_tid, org_tid)`.
4. **Unreferenced `uniprot_proteins.tsv` catalog-row and committed overlay `curation_history` gates in `causal_graph_provenance_problems()` (`scripts/check_provenance.py`)**:
   - `causal_graph_provenance_problems()` previously verified that every `GENE_OR_PROTEIN` node in `curation/causal_graphs/*.yaml` existed in `curation/uniprot_proteins.tsv`, but did not check the converse (whether any orphan/unreferenced `uniprot_id` row existed in `curation/uniprot_proteins.tsv`) or verify that every committed overlay in `curation/causal_graphs/*.yaml` carried a non-empty `curation_history` list.
   - **Upgrade**: Report any `uniprot_id` in `curation/uniprot_proteins.tsv` not referenced by at least one `GENE_OR_PROTEIN` node across `curation/causal_graphs/*.yaml`, and report any committed overlay in `curation/causal_graphs/*.yaml` with a missing or empty `curation_history`.

## 4. Acceptance Criteria and Carry-Forward Policy

- All 15 committed `curation/causal_graphs/NCBITaxon_*.yaml` overlays (246 edges, 75 `GENE_OR_PROTEIN` nodes) and all 34 rows in `curation/uniprot_proteins.tsv` pass `load_causal_graphs()`, `validate_causal_graph_structure()`, `validate_causal_graph_proteins()`, and `scripts/check_provenance.py` (`causal_graph_provenance_problems(REPO_ROOT) == []`).
- Unit tests in `tests/test_causal_graph_overlays.py` (`test_cycle6_stage6_causal_graph_and_uniprot_provenance_invariants`) cover all positive and negative controls for `#208`.
- `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, and `INFRA_TASKS.md` are synchronized with the Cycle 6 Stage 6 gates and carry-forward dispositions.
- Unfinished bulk/upstream portions of `taxonmech-infra-0001..0004` remain explicitly `deferred` to Cycle 7 under open issues `#78` and `#8`.

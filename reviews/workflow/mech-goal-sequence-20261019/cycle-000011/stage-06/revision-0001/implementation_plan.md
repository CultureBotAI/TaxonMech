# Cycle 11 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

## 1. Frozen Intake Scope

- **Frozen Ledger File**: `INFRA_TASKS.md`
- **Frozen Snapshot Output**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-06/revision-0001/infra_snapshot.md`
- **Frozen SHA-256**: `f273690c4b45f4e8a64754d6728450b18583598290fcecf58e0a35e000c85299`
- **Scope Frozen At**: `2026-11-11T01:50:28Z`
- **Source Revision**: `7c53e40736ff440358543ad7009b8ef242332954` (Cycle 11 Stage 5 merge commit on `main`)

| Task ID | Frozen Status | Linked Issue | Cycle 11 Stage 6 Action & Disposition |
|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) (Cycle 11 Stage 6 sub-issue [#259](https://github.com/CultureBotAI/TaxonMech/issues/259)) | Implement `CHEBI_ID_PATTERN` (`^CHEBI:[1-9][0-9]*$`) and `GO_ID_PATTERN` (`^GO:[0-9]{7}$`) node-grounding and domain-isolation gates plus non-empty optional `CausalGraph.description`, `CausalNode.description`, and `EvidenceItem.snippet`/`notes` validation in `validate_causal_graph_structure()` (`src/taxonmech/seed.py`), and enforce host-taxon `TAXON` node exclusivity (`n_grounding == tid`) in `causal_graph_provenance_problems()` (`scripts/check_provenance.py`); carry forward as `deferred` to Cycle 12 under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` |
| `taxonmech-infra-0002` | `deferred` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | Carry forward as `deferred` to Cycle 12 under open umbrella issue `#78` (requires upstream local `kg-microbe` checkout re-extraction to generate `data/raw/taxon_trait_edges.tsv` across 38,357 trait/medium-attested records) |
| `taxonmech-infra-0003` | `deferred` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) (Cycle 11 Stage 6 sub-issue [#259](https://github.com/CultureBotAI/TaxonMech/issues/259)) | Implement strict ascending `uniprot_id` row ordering and single uniform `release_version` catalog pin enforcement in `load_uniprot_proteins()` (`src/taxonmech/seed.py`) and within-graph `GENE_OR_PROTEIN` `organism_taxon_id` and `strain_id` homogeneity enforcement in `causal_graph_provenance_problems()` (`scripts/check_provenance.py`); carry forward as `deferred` to Cycle 12 under open umbrella issue `#78` for full corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot |
| `taxonmech-infra-0004` | `deferred` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | Carry forward as `deferred` to Cycle 12 under open issue `#8` (requires dedicated 626,048-record corpus YAML and `pages/` regeneration pass) |

## 2. Dependency-Aware Implementation Steps

1. **GitHub Issue Grouping (`#259` under `#78`)**:
   - Created issue [#259](https://github.com/CultureBotAI/TaxonMech/issues/259) (`Enforce UniProt catalog sort/release-pin/EC uniqueness, CHEBI/GO grounding patterns, and per-graph organism/strain homogeneity (#78)`) grouping the Cycle 11 Stage 6 validation and provenance upgrades for `taxonmech-infra-0001` and `taxonmech-infra-0003`.
2. **UniProtKB Catalog Ordering & Single-Release-Pin Validation (`src/taxonmech/seed.py`)**:
   - In `load_uniprot_proteins()` (lines 341–501):
     - Enforce strict ascending `uniprot_id` row ordering (`prev_uid` check), rejecting out-of-order rows with `SystemExit`.
     - Enforce a single uniform `release_version` pin across the entire `curation/uniprot_proteins.tsv` catalog (`pinned_release_version` check), rejecting mixed-release rows with `SystemExit`.
3. **Causal-Graph `CHEBI:`/`GO:` Grounding & Optional Text-Slot Validation (`src/taxonmech/seed.py`)**:
   - Define `CHEBI_ID_PATTERN = re.compile(r"^CHEBI:[1-9][0-9]*$")` and `GO_ID_PATTERN = re.compile(r"^GO:[0-9]{7}$")` (lines 87–88).
   - In `validate_causal_graph_structure()` (lines 533–789):
     - Require any grounded `CHEMICAL` node to match `CHEBI_ID_PATTERN` and forbid non-`CHEMICAL` nodes from using `CHEBI:` groundings.
     - Require any grounded `BIOLOGICAL_PROCESS`, `MOLECULAR_FUNCTION`, or `CELLULAR_COMPONENT` node (and any `GO:`-grounded node) to match `GO_ID_PATTERN`.
     - Reject empty/whitespace-only or non-string optional `CausalGraph.description`, `CausalNode.description`, and `EvidenceItem.snippet`/`notes` values when present.
4. **Host-Taxon `TAXON` Exclusivity & Within-Graph `GENE_OR_PROTEIN` Homogeneity (`scripts/check_provenance.py`)**:
   - In `causal_graph_provenance_problems()` (lines 99–340):
     - Reject any `TAXON` node in `curation/causal_graphs/<slug>.yaml` whose `grounding` does not equal the overlay's host taxon `tid`.
     - Enforce within-graph `organism_taxon_id` and `strain_id` homogeneity across all `GENE_OR_PROTEIN` nodes in a `CausalGraph` (`graph_org_tid`, `graph_strain_id`), preventing chimeric multi-strain mechanism graphs.
5. **Documentation, Ledger Dispositions, & Unit Tests**:
   - Update `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md` (carrying `taxonmech-infra-0001..0004` forward to Cycle 12 under open `#78` and `#8`).
   - Add `test_cycle11_stage6_uniprot_sort_release_pin_and_causal_graph_chebi_go_homogeneity_gates` in `tests/test_causal_graph_overlays.py` and update the line-range assertion in `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract`.

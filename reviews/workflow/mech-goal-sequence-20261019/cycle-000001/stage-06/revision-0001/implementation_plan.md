# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 1, Stage 6)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `c520694e483373bf5274bac5bc08327d4f0d364c`
- **Scope Frozen At**: `2026-10-22T06:01:22Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` (`sha256: bd905426fcef930be22a4c7f878278a60f629a9e2106521380577ee6bb62efb4`)

## 1. Frozen Intake Scope and Dependency Graph

At `2026-10-22T06:01:22Z`, `INFRA_TASKS.md` contained four open tasks:

| Task ID | Priority | Dependencies | Linked GitHub Issue | Stage 6 Disposition |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | https://github.com/CultureBotAI/TaxonMech/issues/78 | `resolved` (fully implemented & validated) |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (`extract_taxon_trait_edges` helper & unit tests implemented; full `data/raw/` extraction deferred pending local `kg-microbe` re-extraction) |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (LinkML `CausalNode` structured `GENE_OR_PROTEIN` scope slots, `UniProtEntryStatusEnum`, and `UniProtKB`/`EC`/`OMP`/`UP` prefixes implemented; raw UniProtKB snapshot in `data/raw/` deferred pending upstream bulk release capture) |
| `taxonmech-infra-0004` | `medium` | None | https://github.com/CultureBotAI/TaxonMech/issues/8 | `deferred` (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 provenance and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred pending a dedicated 626,048-record YAML + `pages/` regeneration pass) |

## 2. Dependency-Aware Execution Order and Acceptance Criteria

### Wave 1: Core Mechanism Overlay Pipeline & Grounding Prefix Coverage (`taxonmech-infra-0001` — Resolved)

- **Implementation Steps**:
  1. Add `CAUSAL_GRAPHS_DIR = REPO_ROOT / "curation" / "causal_graphs"` and `load_causal_graphs(path: Path = CAUSAL_GRAPHS_DIR)` in `src/taxonmech/seed.py` to load maintained `curation/causal_graphs/*.yaml` overlays keyed by `identifier`, validate top-level keys (`identifier`, `causal_graphs`, `curation_history`) and unique `graph_id` values, and merge them deterministically into `doc["causal_graphs"]` and `doc["curation_history"]` in `build_document()`.
  2. Update `scripts/verify_corpus.py` so the corpus reproducibility verifier documents and enforces `data/raw/ + curation/seed_scope.tsv + curation/causal_graphs/`.
  3. Register `OMP`, `UniProtKB`, `EC`, and `UP` prefixes in `src/taxonmech/schema/taxonmech.yaml` (`prefixes`) and `conf/id_label_targets.yaml` (`ignored_prefixes`) so `scripts/validate_id_label_correspondence.py` and `tests/test_schema.py` accept grounded `CausalNode` CURIEs without raising `UNKNOWN_PREFIX`.
  4. Document the overlay file contract in `curation/causal_graphs/README.md` and `docs/HARMONIZATION.md`.
  5. Add `tests/test_causal_graph_overlays.py` exercising all five Stage 2 / Stage 3 exemplars (`NCBITaxon:562`, `NCBITaxon:1423`, `NCBITaxon:287`, `NCBITaxon:2190`, `NCBITaxon:1859096`) through `load_causal_graphs()`, `build_document()`, `write_validated_taxon()`, `emit_taxon_yaml()` byte-for-byte reproducibility, `conf/id_label_targets.yaml` prefix checks, and `src/taxonmech/templates/taxon-content.html` rendering.
- **Acceptance Criteria**:
  - `load_causal_graphs()` and `build_document()` merge overlays cleanly and pass `write_validated_taxon()`.
  - All five exemplar causal graphs pass round-trip YAML emission, schema prefix checks, `conf/id_label_targets.yaml` checks, and HTML template rendering.
  - Existing 626,048 committed `data/taxa/` records and `pages/` remain 100% reproducible without drift.

### Wave 2: Structured `GENE_OR_PROTEIN` Scope Slots (`taxonmech-infra-0003` — Schema & Prefix Layer Implemented; Raw Snapshot Deferred)

- **Implementation Steps**:
  1. Extend `CausalNode` in `src/taxonmech/schema/taxonmech.yaml` with optional structured `GENE_OR_PROTEIN` scope slots: `organism_taxon_id` (`^NCBITaxon:[0-9]+$`), `strain_id` (`^kgmicrobe\.strain:\S+$`), `proteome_id` (`^UP:UP[0-9]{9}$`), `gene_symbol`, `locus_tag`, `sequence_length`, `sequence_crc64` (`^[0-9A-F]{16}$`), `sequence_version`, and `entry_status` (`UniProtEntryStatusEnum`: `SWISS_PROT`, `TREMBL`).
  2. Update `tests/test_schema.py` to validate `entry_status` against `UniProtEntryStatusEnum`, check CURIE prefixes on `organism_taxon_id`, `strain_id`, `proteome_id`, and `xrefs`, and verify the `CausalNode` slots in `test_causal_node_protein_scope_slots_and_prefixes`.
- **Carry-Forward Scope (`deferred`)**:
  - Populating a release-pinned UniProtKB / Reference Proteomes raw snapshot in `data/raw/` and offline accession-to-taxon validation against that snapshot is carried forward to Cycle 2.

### Wave 3: Granular Trait, Substrate, Habitat, and Growth-Medium Edge Extractor (`taxonmech-infra-0002` — Extractor Helper Implemented; Bulk Re-Extraction Deferred)

- **Implementation Steps**:
  1. Add `TRAIT_EDGE_FIELDS` and `extract_taxon_trait_edges(path: Path, source: str) -> list[dict[str, str]]` in `src/taxonmech/extract.py` to preserve per-taxon `(taxon_id, predicate, object_id, relation, source, publications, primary_knowledge_source, aggregator_knowledge_source)` rows from KGX `edges.tsv` files (`madin_etal`, `bactotraits`, `mediadive`).
  2. Add unit tests in `tests/test_causal_graph_overlays.py` (`test_extract_taxon_trait_edges_preserves_granular_assertions`).
- **Carry-Forward Scope (`deferred`)**:
  - Running `extract_taxon_trait_edges` against an upstream local `kg-microbe` checkout to commit `data/raw/taxon_trait_edges.tsv` and update `data/raw/MANIFEST.yaml` across 38,357 trait/medium-attested records is carried forward to Cycle 2.

### Wave 4: Upstream `kg-microbe` Edge-Multiplicity Provenance & Subtree Rollup Contract (`taxonmech-infra-0004` — Documentation Aligned; Corpus Re-Seed Deferred)

- **Implementation Steps**:
  1. Document the pinned `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests (`gold/edges.tsv`, `mediadive/edges.tsv`, `madin_etal/edges.tsv`, `bactotraits/edges.tsv`) from `data/raw/MANIFEST.yaml` and the asymmetric direct-taxid vs BacDive-subtree attestation contract in `docs/HARMONIZATION.md`.
- **Carry-Forward Scope (`deferred`)**:
  - Re-seeding `source_attestations[].notes` across the 27,118 multi-edge records and regenerating all 626,048 YAML records and `pages/` shards is carried forward to Cycle 2.

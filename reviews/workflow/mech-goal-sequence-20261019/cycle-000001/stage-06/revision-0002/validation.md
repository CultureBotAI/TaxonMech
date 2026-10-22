# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 1, Stage 6, Revision 2)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `2` (`revision-0002`, superseding `revision-0001`)
- **Source Revision**: `d71f01639aed21d9ea6b4f910813578e4cff666b` (incorporating PR `#152` on `main` from `c520694e483373bf5274bac5bc08327d4f0d364c`)
- **Scope Frozen At**: `2026-10-22T06:01:22Z`

## 1. Summary of Implemented Changes and Validation Outcomes

| Task ID | Status | Linked Issue | Implemented Artifacts | Validation Result |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/seed.py`, `scripts/verify_corpus.py`, `src/taxonmech/schema/taxonmech.yaml`, `conf/id_label_targets.yaml`, `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (Repository Pipeline Landed in PR `#152`; Task Deferred Under Open Umbrella Issue `#78`)** — `load_causal_graphs()` and `build_document()` merge overlays deterministically; all 5 Stage 2 / Stage 3 exemplars (`NCBITaxon:562`, `NCBITaxon:1423`, `NCBITaxon:287`, `NCBITaxon:2190`, `NCBITaxon:1859096`) pass `write_validated_taxon`, `emit_taxon_yaml` byte-exact roundtrip, `conf/id_label_targets.yaml` prefix checks, and `taxon-content.html` rendering; task remains `deferred` under open umbrella issue `#78` until companion tasks `0002` and `0003` and production overlay seeding complete in Cycle 2. |
| `taxonmech-infra-0002` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/extract.py` (`TRAIT_EDGE_FIELDS`, `extract_taxon_trait_edges`), `tests/test_causal_graph_overlays.py`, `docs/HARMONIZATION.md` | **PASS (Partial / Deferred)** — `test_extract_taxon_trait_edges_preserves_granular_assertions` verifies granular per-taxon predicate/CURIE/publication extraction; full `data/raw/taxon_trait_edges.tsv` extraction deferred to Cycle 2 pending local `kg-microbe` checkout re-extraction. |
| `taxonmech-infra-0003` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/schema/taxonmech.yaml` (`CausalNode` structured `GENE_OR_PROTEIN` slots, `UniProtEntryStatusEnum`, `UniProtKB`/`EC`/`OMP`/`UP` prefixes), `conf/id_label_targets.yaml`, `tests/test_schema.py`, `tests/test_causal_graph_overlays.py` | **PASS (Partial / Deferred)** — `test_causal_node_protein_scope_slots_and_prefixes` and `test_five_exemplar_causal_graph_overlays_roundtrip_and_render` pass LinkML closed-schema validation; raw UniProtKB/Reference Proteomes snapshot in `data/raw/` deferred to Cycle 2. |
| `taxonmech-infra-0004` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/8 | `docs/HARMONIZATION.md`, `INFRA_TASKS.md` | **PASS (Partial / Deferred)** — `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding deferred to Cycle 2. |

## 2. Executed Validation Commands

1. **Causal-graph overlay, extractor, and schema unit tests**:
   ```
   .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py tests/test_schema.py -v
   ```
   - `tests/test_causal_graph_overlays.py`: 3 passed (`test_five_exemplar_causal_graph_overlays_roundtrip_and_render`, `test_load_causal_graphs_rejects_invalid_or_duplicate_overlays`, `test_extract_taxon_trait_edges_preserves_granular_assertions`).
   - `tests/test_schema.py`: all schema structure, enum, prefix, and `CausalNode` protein scope slot tests passed.

2. **Ruff linter**:
   ```
   .venv/bin/ruff check src/taxonmech/seed.py src/taxonmech/extract.py scripts/verify_corpus.py tests/test_schema.py tests/test_causal_graph_overlays.py
   ```
   - 0 errors.

3. **Repository provenance, vendored schema sync, history, and docs checks**:
   - `python3 scripts/check_provenance.py`: PASS (`data/raw/MANIFEST.yaml` matches all committed `data/raw/*.tsv` inventories).
   - `bash scripts/check_vendored_sync.sh`: PASS (vendored `mech_shared.yaml` and `history.yaml` byte-identical to pinned ref).
   - `python3 scripts/validate_history.py`: PASS.
   - `python3 scripts/record_review.py check`: PASS.

4. **Workflow evidence and infrastructure ledger validation**:
   ```
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0002/evidence.yaml --effective-workflow /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/taxonmech/effective-workflow.json
   ```
   - Verified `valid: true`, `status: ok`, `supersedes_evidence` chain from `revision-0001/evidence.yaml` (`sha256: 04658ba968475a6099f9654fb6defcb33e212611d9cb0fb2670841f579630470`), and exact match with frozen `infra_snapshot.md` (`sha256: bd905426fcef930be22a4c7f878278a60f629a9e2106521380577ee6bb62efb4`) and `INFRA_TASKS.md`.

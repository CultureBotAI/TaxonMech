# Cycle 7 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `c6c16699bb346b4ae2a31b786295ad1fae7c8ca5`
- **Frozen Intake Cutoff**: `2026-11-06T06:01:39Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md` (`sha256: e11e92a2fd18f7789d079a1415f8516cef9c1bf7bdc4435ed7797776120c4ec3`)

## 1. Frozen Intake Inventory and Dependency Graph

At the Stage 6 cutoff (`2026-11-06T06:01:39Z`), `INFRA_TASKS.md` contains four tracked tasks (`taxonmech-infra-0001` through `taxonmech-infra-0004`):

| Task ID | Priority | Dependencies | Umbrella / Linked Issue | Stage 6 Action |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | `#78`, `#216` | **Selected (closed-key object schemas, chronological `CurationEvent` validation, host `TAXON` node anchoring, and non-empty edge evidence `notes`/`snippet` gates)**; bulk overlay expansion carried forward (`deferred`) to Cycle 8 under `#78` |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | `#78` | **Carried forward (`deferred`)** to Cycle 8 pending an upstream `kg-microbe` re-extraction of `data/raw/taxon_trait_edges.tsv` |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | `#78`, `#216` | **Selected (per-graph `GENE_OR_PROTEIN` `grounding` uniqueness & required full 4-part `EC:` xref completeness gates)**; full corpus-wide UniProt Reference Proteomes raw snapshot carried forward (`deferred`) to Cycle 8 under `#78` |
| `taxonmech-infra-0004` | `medium` | None | `#8` | **Carried forward (`deferred`)** to Cycle 8 pending a dedicated 626,048-record YAML and `pages/` regeneration pass |

## 2. Issue Deduplication and Grouping

We searched open and closed issues in `CultureBotAI/TaxonMech` (`gh issue list -R CultureBotAI/TaxonMech --state all --limit 100`):

- `#78` (`OPEN`): Umbrella tracking issue for causal-graph overlays, granular trait edge extraction, and pinned UniProtKB protein-grounding infrastructure (`taxonmech-infra-0001`, `taxonmech-infra-0002`, `taxonmech-infra-0003`).
- `#189` (`CLOSED` via PR `#190` in Cycle 4 Stage 6): Enforced `CausalNode`/`CausalEdge` schema invariants, protein-only slot isolation, and UniProtKB EC/metadata completeness.
- `#199` (`CLOSED` via PR `#200` in Cycle 5 Stage 6): Enforced `CausalGraph` node connectivity, `graph_id`/`node_id`/`UniProtKB`/`proteome_id` regexes, species-or-below scope, and `check_provenance.py` cross-table validation.
- `#208` (`CLOSED` via PR `#209` in Cycle 6 Stage 6): Enforced `CausalGraph` required `title`/`nodes`/`edges`, `TAXON` `NCBITaxon:` regex, host-subtree `strain_id` binding, and `uniprot_proteins.tsv` orphan-row gate.
- `#216` (created for Cycle 7 Stage 6 under umbrella `#78`): *Enforce CausalGraph/CausalNode/CausalEdge/EvidenceItem/CurationEvent closed-key schemas, per-graph UniProtKB uniqueness, and host-TAXON/evidence-text/4-part-EC provenance gates (#78)*.
- `#8` (`OPEN`): Tracks `taxonmech-infra-0004` (upstream `kg-microbe` edge-multiplicity provenance and direct-taxid vs BacDive-subtree attestation counts).

## 3. Selected Implementation Scope (`#216` under `#78`)

Following Cycle 7 Stage 2 (PR `#211`, expanding the 15 overlays from 246 to 257 evidence-backed edges) and Cycle 7 Stage 3 (PR `#212`, expanding the 15 overlays to 290 evidence-backed edges and 86 `GENE_OR_PROTEIN` nodes across 39 live-verified UniProtKB accessions), four structural, schema, and provenance validation gaps remained across `src/taxonmech/seed.py`, `scripts/check_provenance.py`, and `curation/causal_graphs/README.md`:

1. **Closed-key validation on `CausalGraph`, `CausalNode`, `CausalEdge`, and `EvidenceItem` in `validate_causal_graph_structure()` (`src/taxonmech/seed.py`)**:
   - `build_document()` (`src/taxonmech/seed.py` lines 1091–1160) reconstructs `CausalGraph`, `CausalNode`, `CausalEdge`, and `EvidenceItem` mappings from known keys before calling `write_validated_taxon()`. As a result, any unknown or misspelled key in a `curation/causal_graphs/*.yaml` overlay (or in the `curation/causal_graphs/README.md` YAML example and synthetic test fixtures) was silently dropped rather than rejected by `load_causal_graphs()` or `validate_causal_graph_structure()`.
   - **Upgrade**: Define `CAUSAL_GRAPH_KEYS`, `CAUSAL_NODE_KEYS`, `CAUSAL_EDGE_KEYS`, and `EVIDENCE_ITEM_KEYS` matching the induced LinkML schema slots in `src/taxonmech/schema/taxonmech.yaml` and reject any unexpected keys in `validate_causal_graph_structure()`.
2. **Closed-key and chronological `CurationEvent` validation in `validate_causal_graph_events()` (`src/taxonmech/seed.py`)**:
   - `load_causal_graphs()` previously appended `curation_history` mappings without validating `CurationEvent` slot names (`CURATION_EVENT_KEYS`: `timestamp`, `curator`, `action`, `changes`, `llm_assisted`), ISO-8601 UTC `timestamp` syntax (`ISO_UTC_TIMESTAMP_PATTERN`: `^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`), non-decreasing chronological order, non-empty `curator`/`action`/`changes`, or boolean `llm_assisted`. This caught both a stale `date`/`notes` example in `curation/causal_graphs/README.md` and an `agent`/`summary` fixture in `tests/test_causal_graph_overlays.py`.
   - **Upgrade**: Add `validate_causal_graph_events()` and invoke it from `load_causal_graphs()`, and align the `curation/causal_graphs/README.md` YAML example and `STAGE2_STAGE3_EXEMPLAR_OVERLAYS` test fixture with `CURATION_EVENT_KEYS`.
3. **Per-graph `GENE_OR_PROTEIN` `grounding` (`UniProtKB:<accession>`) uniqueness in `validate_causal_graph_proteins()` (`src/taxonmech/seed.py`)**:
   - `validate_causal_graph_proteins()` previously allowed two distinct `node_id`s within the same `CausalGraph` to ground to the same `UniProtKB:<accession>`.
   - **Upgrade**: Track `seen_protein_groundings` per `CausalGraph` in `validate_causal_graph_proteins()` and raise `SystemExit` on duplicate `GENE_OR_PROTEIN` `grounding` within a graph.
4. **Host `TAXON` node anchoring, non-empty edge evidence `notes`/`snippet`, and full 4-part `EC:` xref completeness in `causal_graph_provenance_problems()` (`scripts/check_provenance.py`)**:
   - Require every committed `CausalGraph` in `curation/causal_graphs/*.yaml` to include at least one `TAXON` node grounded to the host `TaxonRecord.identifier` (`tid`), require every `GENE_OR_PROTEIN` node to include all full 4-part (non-wildcard) `EC:` numbers from its `curation/uniprot_proteins.tsv` row in `xrefs`, and require every `CausalEdge.evidence[]` item to carry non-empty `notes` or `snippet`.

## 4. Acceptance Criteria and Carry-Forward Policy

- All 15 committed `curation/causal_graphs/NCBITaxon_*.yaml` overlays (290 edges, 86 `GENE_OR_PROTEIN` nodes) and all 39 rows in `curation/uniprot_proteins.tsv` pass `load_causal_graphs()`, `validate_causal_graph_structure()`, `validate_causal_graph_events()`, `validate_causal_graph_proteins()`, and `scripts/check_provenance.py` (`causal_graph_provenance_problems(REPO_ROOT) == []`).
- Unit tests in `tests/test_causal_graph_overlays.py` (`test_cycle7_stage6_closed_keys_curation_events_and_provenance_invariants`) cover all positive and negative controls for `#216`, including LinkML `SchemaView` slot parity and validation of the `curation/causal_graphs/README.md` YAML example.
- `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md` are synchronized with the Cycle 7 Stage 6 gates and carry-forward dispositions.
- Unfinished bulk/upstream portions of `taxonmech-infra-0001..0004` remain explicitly `deferred` to Cycle 8 under open issues `#78` and `#8`.

# TaxonMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `taxonmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/TaxonMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: taxonmech-infra-0001
    summary: >-
      Implement maintained curation/causal_graphs/ overlay input, validated seeder merge in
      src/taxonmech/seed.py, seeder-owned verification in scripts/verify_corpus.py, and
      CausalNode.grounding prefix coverage (UniProtKB, EC, METPO/OMP) in conf/id_label_targets.yaml
    status: note
    disposition: pending_issue_link
  - task_id: taxonmech-infra-0002
    summary: >-
      Extend src/taxonmech/extract.py to preserve granular per-taxon trait, substrate, habitat,
      and growth-medium assertions (madin_etal, bactotraits, mediadive) with predicate, ontology
      object CURIE, and literature/source provenance
    status: note
    disposition: pending_issue_link
```
<!-- mech-infra-tasks:end -->

## Tasks

### `taxonmech-infra-0001` — Native causal-graph overlay writer, corpus verifier, and OAK grounding prefix coverage

- **Origin**: `run_id: mech-goal-sequence-20261019`, `cycle: 1`, `stage: 2` (`causal_graphs`)
- **Status**: `note` (`pending_issue_link` — to be promoted to a tracked GitHub issue during Stage 5 review remediation or Stage 6 infrastructure implementation)
- **Priority**: `high`
- **Dependencies**: None
- **Observation**:
  1. `src/taxonmech/seed.py` (`build_document`, lines 344–646; `seed`, lines 713–780) constructs `TaxonRecord` dicts solely from `TaxonConcept` and `SeedInventory` and never reads a maintained `curation/causal_graphs/` overlay directory or emits `causal_graphs`.
  2. `scripts/verify_corpus.py` (lines 22–25, 67–73) compares every `data/taxa/<domain>/<slug>.yaml` byte-for-byte against `emit_taxon_yaml(build_document(concept, corpus.inventory))`, rejecting any out-of-band edit to `data/taxa/<domain>/*.yaml`.
  3. While `conf/id_label_targets.yaml` (`grounded_nodes`, lines 52–60) and `src/taxonmech/templates/taxon-content.html` (line 80) are already aligned with `CausalNode.grounding` and `CausalNode.node_id` (`src/taxonmech/schema/taxonmech.yaml`, lines 1190–1216), `conf/id_label_targets.yaml` omits `UniProtKB` and `EC` (and `METPO`/`OMP`) from `adapters` (lines 14–23) and `ignored_prefixes` (lines 25–42), causing `scripts/validate_id_label_correspondence.py` to raise `UnknownPrefixError` when `CausalNode.grounding` references a `UniProtKB:` or `EC:` CURIE.
  4. `scripts/render_pages.py --check` enforces zero drift between committed `pages/` and `data/taxa/<domain>/*.yaml`, so derived HTML causal-graph tables cannot be rendered until the maintained overlay input and seeder merge (`src/taxonmech/seed.py` + `scripts/verify_corpus.py`) are wired.
- **Desired Outcome**:
  1. Introduce a maintained, schema-validated `curation/causal_graphs/` overlay input ingested by `src/taxonmech/seed.py` into `TaxonRecord.causal_graphs` (using `CausalGraph` / `CausalNode` / `CausalEdge` slots defined at `src/taxonmech/schema/taxonmech.yaml` lines 1160–1258 and `CausalNodeTypeEnum` at lines 1467–1504) and verified by `scripts/verify_corpus.py`.
  2. Update `conf/id_label_targets.yaml` with explicit adapter or prefix handling for `UniProtKB` and `EC` (and `METPO`/`OMP` if grounded in `CausalNode.grounding`) alongside `NCBITaxon`, `ENVO`, `UBERON`, `FOODON`, `CHEBI`, `GO`, `MONDO`, `HP`, and `PATO`.
  3. Add a round-trip canary test exercising the five Stage 2 exemplars (`NCBITaxon:562`, `NCBITaxon:1423`, `NCBITaxon:287`, `NCBITaxon:2190`, `NCBITaxon:1859096`) through LinkML validation, `validate_id_label_correspondence.py`, `verify_corpus.py`, and HTML rendering (`scripts/render_pages.py --check`).
- **Evidence Paths**:
  - `src/taxonmech/seed.py`
  - `scripts/verify_corpus.py`
  - `conf/id_label_targets.yaml`
  - `src/taxonmech/templates/taxon-content.html`
  - `src/taxonmech/schema/taxonmech.yaml`
  - `reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment/review.yaml`
  - `history/infrastructure/stage2-causal-graphs-assessment/2026-10-21T043201Z-Antigravity-c2a701.yaml`

### `taxonmech-infra-0002` — Granular trait, substrate, habitat, and growth-medium edge extraction in `src/taxonmech/extract.py`

- **Origin**: `run_id: mech-goal-sequence-20261019`, `cycle: 1`, `stage: 2` (`causal_graphs`)
- **Status**: `note` (`pending_issue_link` — to be promoted to a tracked GitHub issue during Stage 5 review remediation or Stage 6 infrastructure implementation)
- **Priority**: `medium`
- **Dependencies**: `taxonmech-infra-0001`
- **Observation**:
  - `src/taxonmech/extract.py` (`count_taxon_subjects`, lines 412–417, 677–678, 840–841) collapses `kg-microbe` `madin_etal/edges.tsv` and `bactotraits/edges.tsv` into 2-column `(taxon_id, assertion_count)` tables (`data/raw/madin_taxa.tsv` for 34,148 in-scope taxa; `data/raw/bactotraits_taxa.tsv` for 9,626 in-scope taxa), discarding predicates, `METPO:`/`ENVO:`/`CHEBI:`/`GO:` object CURIEs, and primary literature (`PMID:`/`DOI:`) citations.
  - `src/taxonmech/seed.py` (line 618) reads only `medium_count` from `data/raw/mediadive_taxa.tsv` (14,154 in-scope taxa) and discards the `media_ids` column (`mediadive.medium:*`).
- **Desired Outcome**:
  - Extend `src/taxonmech/extract.py` (or a dedicated causal-graph extraction stage) to retain granular per-taxon subject–predicate–object assertions and provenance locators from `kg-microbe` (`madin_etal`, `bactotraits`, `mediadive`, and UniProt/GO annotations) so that evidence-backed `CausalGraph` overlays can be populated reproducibly across the 38,357 phenotype/trait/medium-attested records.
- **Evidence Paths**:
  - `src/taxonmech/extract.py`
  - `src/taxonmech/seed.py`
  - `data/raw/madin_taxa.tsv`
  - `data/raw/bactotraits_taxa.tsv`
  - `data/raw/mediadive_taxa.tsv`
  - `reviews/structured/20261021T043201Z-stage2-causal-graphs-assessment/review.yaml`
  - `history/infrastructure/stage2-causal-graphs-assessment/2026-10-21T043201Z-Antigravity-c2a701.yaml`


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
    status: deferred
    issue_url: https://github.com/CultureBotAI/TaxonMech/issues/78
    disposition: >-
      Deferred to Cycle 2 Stage 6 under open umbrella issue #78 after landing repository-local
      pipeline in Cycle 1 Stage 6 (PR #152) and seeding 10 maintained overlays (44 evidence-backed
      edges across 5 cross-domain species and 5 reference-proteome strain records) in Cycle 2 Stage 2:
      implemented load_causal_graphs() and build_document() merge in src/taxonmech/seed.py, updated
      scripts/verify_corpus.py, registered UniProtKB/EC/OMP/UP prefixes in
      src/taxonmech/schema/taxonmech.yaml and conf/id_label_targets.yaml, documented
      curation/causal_graphs/README.md, and added roundtrip/render and committed-overlay tests in
      tests/test_causal_graph_overlays.py; umbrella issue #78 remains open pending companion tasks
      taxonmech-infra-0002 and taxonmech-infra-0003 for corpus-wide raw trait and UniProt extraction
  - task_id: taxonmech-infra-0002
    summary: >-
      Extend src/taxonmech/extract.py to preserve granular per-taxon trait, substrate, habitat,
      and growth-medium assertions (madin_etal, bactotraits, mediadive) with predicate, ontology
      object CURIE, and literature/source provenance
    status: deferred
    issue_url: https://github.com/CultureBotAI/TaxonMech/issues/78
    disposition: >-
      Deferred to Cycle 2 after partial implementation in Cycle 1 Stage 6: implemented and
      unit-tested extract_taxon_trait_edges() and TRAIT_EDGE_FIELDS in src/taxonmech/extract.py;
      full data/raw/taxon_trait_edges.tsv extraction across 38,357 trait/medium-attested records
      requires an upstream local kg-microbe checkout re-extraction
  - task_id: taxonmech-infra-0003
    summary: >-
      Add a release-pinned UniProtKB / UniProt Reference Proteomes raw source snapshot in
      data/raw/, declare UniProtKB and EC prefixes in src/taxonmech/schema/taxonmech.yaml and
      conf/id_label_targets.yaml, and add structured GENE_OR_PROTEIN organism/strain/proteome/locus/checksum
      scope slots and accession-to-taxon validation
    status: deferred
    issue_url: https://github.com/CultureBotAI/TaxonMech/issues/78
    disposition: >-
      Deferred to Cycle 2 after partial implementation in Cycle 1 Stage 6: declared UniProtKB, EC,
      OMP, and UP prefixes and added structured GENE_OR_PROTEIN scope slots (organism_taxon_id,
      strain_id, proteome_id, gene_symbol, locus_tag, sequence_length, sequence_crc64,
      sequence_version, entry_status) and UniProtEntryStatusEnum to CausalNode in
      src/taxonmech/schema/taxonmech.yaml; raw UniProtKB/Reference Proteomes TSV snapshot in
      data/raw/ deferred pending upstream bulk release capture
  - task_id: taxonmech-infra-0004
    summary: >-
      Pin reproducible upstream kg-microbe edge-multiplicity provenance and document or align
      direct-only vs subtree-rolled-up source attestation counts for GOLD, MEDIADIVE, MADIN,
      and BACTOTRAITS across the 27,118 pass_with_limitations and 30 blocked corpus review records
    status: deferred
    issue_url: https://github.com/CultureBotAI/TaxonMech/issues/8
    disposition: >-
      Deferred to Cycle 2 after documentation alignment in Cycle 1 Stage 6: documented pinned
      kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd edge-table SHA-256 digests and asymmetric
      direct-taxid vs BacDive-subtree attestation contract in docs/HARMONIZATION.md; corpus-wide
      re-seeding of source_attestations[].notes across 27,118 records deferred pending a dedicated
      626,048-record YAML and pages/ regeneration pass
```
<!-- mech-infra-tasks:end -->

## Tasks

### `taxonmech-infra-0001` — Native causal-graph overlay writer, corpus verifier, and OAK grounding prefix coverage

- **Origin**: `run_id: mech-goal-sequence-20261019`, `cycle: 1`, `stage: 2` (`causal_graphs`)
- **Status**: `deferred` (`issue_url`: https://github.com/CultureBotAI/TaxonMech/issues/78)
- **Disposition**: Deferred to Cycle 2 Stage 6 under open umbrella issue `#78` after landing repository-local pipeline in `mech-goal-sequence-20261019` Cycle 1 Stage 6 PR `#152` (`src/taxonmech/seed.py`, `scripts/verify_corpus.py`, `src/taxonmech/schema/taxonmech.yaml`, `conf/id_label_targets.yaml`, `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py`) and seeding 10 maintained production overlays (44 evidence-backed edges across 5 cross-domain species and 5 reference-proteome strain records) in Cycle 2 Stage 2; umbrella issue `#78` remains open pending companion tasks `taxonmech-infra-0002` and `taxonmech-infra-0003` for corpus-wide raw trait and UniProt extraction.
- **Priority**: `high`
- **Dependencies**: None
- **Observation**:
  1. `src/taxonmech/seed.py` (`build_document`, lines 344–646; `seed`, lines 713–780) constructs `TaxonRecord` dicts solely from `TaxonConcept` and `SeedInventory` and never reads a maintained `curation/causal_graphs/` overlay directory or emits `causal_graphs`.
  2. `scripts/verify_corpus.py` (lines 22–25, 67–73) compares every `data/taxa/<domain>/<slug>.yaml` byte-for-byte against `emit_taxon_yaml(build_document(concept, corpus.inventory))`, rejecting any out-of-band edit to `data/taxa/<domain>/*.yaml`.
  3. While `conf/id_label_targets.yaml` (`grounded_nodes`, lines 52–60) and `src/taxonmech/templates/taxon-content.html` (line 80) are already aligned with `CausalNode.grounding` and `CausalNode.node_id` (`src/taxonmech/schema/taxonmech.yaml`, lines 1190–1216), `conf/id_label_targets.yaml` omits `UniProtKB` and `EC` (and `METPO`/`OMP`) from `adapters` (lines 18–25) and `ignored_prefixes` (lines 27–47), causing `scripts/validate_id_label_correspondence.py` to raise `UnknownPrefixError` when `CausalNode.grounding` references a `UniProtKB:` or `EC:` CURIE.
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
- **Status**: `deferred` (`issue_url`: https://github.com/CultureBotAI/TaxonMech/issues/78)
- **Disposition**: Deferred to Cycle 2 after partial implementation in Cycle 1 Stage 6 (`extract_taxon_trait_edges` and `TRAIT_EDGE_FIELDS` implemented in `src/taxonmech/extract.py` and tested in `tests/test_causal_graph_overlays.py`; full `data/raw/taxon_trait_edges.tsv` generation deferred pending a local `kg-microbe` checkout re-extraction).
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

### `taxonmech-infra-0003` — Pinned UniProtKB / Reference Proteomes raw source snapshot, schema prefix declarations, and structured `GENE_OR_PROTEIN` organism/strain/sequence scope validation

- **Origin**: `run_id: mech-goal-sequence-20261019`, `cycle: 1`, `stage: 3` (`protein_examples`)
- **Status**: `deferred` (`issue_url`: https://github.com/CultureBotAI/TaxonMech/issues/78)
- **Disposition**: Deferred to Cycle 2 after partial implementation in Cycle 1 Stage 6 (`UniProtKB`, `EC`, `OMP`, and `UP` prefixes declared in `src/taxonmech/schema/taxonmech.yaml` and `conf/id_label_targets.yaml`; structured `GENE_OR_PROTEIN` scope slots and `UniProtEntryStatusEnum` added to `CausalNode` and tested in `tests/test_schema.py` and `tests/test_causal_graph_overlays.py`; raw UniProtKB/Reference Proteomes TSV snapshot in `data/raw/` deferred pending upstream bulk release capture).
- **Priority**: `high`
- **Dependencies**: `taxonmech-infra-0001`
- **Observation**:
  1. `TaxonRecord` (`src/taxonmech/schema/taxonmech.yaml` lines 105–313) has no dedicated `protein_examples` slot; the sole native protein representation surface is `TaxonRecord.causal_graphs[].nodes[]` (`CausalNode`, lines 1190–1216) with `node_type: GENE_OR_PROTEIN` (`CausalNodeTypeEnum`, lines 1487–1488). Meanwhile, `strains[].related_records[]` with `record_type: NUCLEOTIDE_SEQUENCE` (`GenomeRelatedRecordLink`, lines 953–1102) is restricted by regex (`^INSDC:(?:[A-Z][0-9]{5}|[A-Z]{2}[0-9]{6}|[A-Z]{2}[0-9]{8}|[A-Z]{4}[0-9]{8,}|[A-Z]{6}[0-9]{9,}|[A-Z]{5}[0-9]{7}|(?:AC|NC|NG|NT|NW|NZ|NM|NR|XM|XR)_[0-9]+)(?:\.[1-9][0-9]*)?$`, lines 1023–1035 and 1081) to INSDC nucleotide accessions from `source: STRAININFO` (9,241 records, 78,785 links across 51,467 unique INSDC accessions in `data/straininfo/related_records.tsv.gz`).
  2. Neither `conf/sources.yaml` (lines 1–80) nor `data/raw/MANIFEST.yaml` (lines 1–343) includes a pinned UniProtKB (Swiss-Prot/TrEMBL) or UniProt Reference Proteomes inventory, and `src/taxonmech/schema/taxonmech.yaml` (`prefixes`, lines 43–88) omits `UniProtKB` and `EC`.
  3. TaxonMech seeds both species-level `TaxonRecord` files (e.g., `NCBITaxon:562`, `NCBITaxon:1423`, `NCBITaxon:287`, `NCBITaxon:2190`, `NCBITaxon:1859096`, `NCBITaxon:40410`, `NCBITaxon:5207`) and strain-level `TaxonRecord` files (e.g., `NCBITaxon:83333`, `NCBITaxon:511145`, `NCBITaxon:224308`, `NCBITaxon:208964`, `NCBITaxon:243232`, `NCBITaxon:294750`, `NCBITaxon:283643`, `NCBITaxon:235443`). Because UniProtKB reference proteomes (`UP000000625`, `UP000001570`, `UP000002438`, `UP000000805`, `UP000029445`, `UP000010091`) are annotated at the strain-level NCBI Taxon ID and `CausalNode` currently provides only `node_id`, `label`, `node_type`, `grounding`, `xrefs`, and free-text `description`, there are no structured slots to record the UniProt entry's exact `organism_taxon_id`, `strain_id`, `proteome_id`, `gene_symbol`, `locus_tag`, `sequence_length`, `sequence_crc64`, `sequence_version`, or `entry_status` (`SWISS_PROT` vs `TREMBL`).
  4. Live UniProt REST API verification during Stage 3 caught 2 accession/gene mismatches in committed Stage 2 `review.yaml` lines 514–665 (`UniProtKB:Q9I4X3` at line 583 is `pqsA` rather than `phzM` `UniProtKB:Q9HWH2`; `UniProtKB:Q58254` at line 613 is `mcrC` rather than `mcrA` `UniProtKB:Q58256`) and 4 additional accession/gene/species/fragment mismatches during expanded unpinned candidate screening (`UniProtKB:P0A858` is `tpiA` rather than `tnaA` `UniProtKB:P0A853`; `UniProtKB:Q9I4X2` is `pqsB` rather than `phzS` `UniProtKB:Q9HWG9`; `UniProtKB:Q58255` is `mcrG` rather than `mcrB` `UniProtKB:Q58252`; `UniProtKB:Q55P57` belongs to sibling species *Cryptococcus deneoformans* B-3501A `NCBITaxon:283643` rather than *C. deuterogattii* `NCBITaxon:1859096`/`NCBITaxon:294750`; and `UniProtKB:A0A1S6LQA8` is an 87-aa partial fragment), demonstrating why offline pinned UniProtKB validation is essential.
- **Desired Outcome**:
  1. Add a release-pinned UniProtKB / UniProt Reference Proteomes TSV inventory in `data/raw/` (registered in `conf/sources.yaml` and `data/raw/MANIFEST.yaml`) storing accession, entry name, review status (`SWISS_PROT`/`TREMBL`), recommended protein name, gene symbol, locus tag, EC numbers, NCBI Taxon ID, UniProt Proteome ID (`UP...`), sequence length, CRC64 checksum, and sequence version.
  2. Declare `UniProtKB` and `EC` in `src/taxonmech/schema/taxonmech.yaml` `prefixes` and configure `conf/id_label_targets.yaml` and `scripts/validate_strict.py` to validate `UniProtKB:` accessions against the pinned raw inventory, enforcing organism/strain lineage consistency (`TaxonRecord.identifier` matches or is the parent species of the UniProt organism taxon ID) and rejecting gene/locus/checksum mismatches or unflagged fragments.
  3. Extend `CausalNode` (or a dedicated `ProteinAnnotation` / `protein_examples` subobject) with optional structured metadata slots (`organism_taxon_id`, `proteome_id`, `gene_symbol`, `locus_tag`, `sequence_length`, `sequence_crc64`, `sequence_version`, `entry_status`) so species-level exemplar projections vs strain-exact reference proteome bindings are machine-distinguishable.
- **Evidence Paths**:
  - `src/taxonmech/schema/taxonmech.yaml`
  - `conf/id_label_targets.yaml`
  - `conf/sources.yaml`
  - `data/raw/MANIFEST.yaml`
  - `data/straininfo/related_records.tsv.gz`
  - `reviews/structured/20261021T094500Z-stage3-protein-examples-assessment/review.yaml`
  - `history/infrastructure/stage3-protein-examples-assessment/2026-10-21T094500Z-Antigravity-p3e901.yaml`

### `taxonmech-infra-0004` — Reproducible upstream `kg-microbe` edge-multiplicity provenance and subtree count rollup contract

- **Origin**: `run_id: mech-goal-sequence-20261019`, `cycle: 1`, `stage: 4` (`record_review`)
- **Status**: `deferred` (`issue_url`: https://github.com/CultureBotAI/TaxonMech/issues/8)
- **Disposition**: Deferred to Cycle 2 after documentation alignment in Cycle 1 Stage 6 (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` edge-table SHA-256 provenance and direct-taxid vs BacDive-subtree attestation contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred pending a dedicated 626,048-record YAML and `pages/` regeneration pass).
- **Priority**: `medium`
- **Dependencies**: None
- **Observation**:
  - Across `docs/structured-review-inventory/part-00.tsv..part-13.tsv` (602,165 structured-inventory records) and `docs/legacy-review-inventory.tsv` (23,883 legacy-inventory records), 27,118 records carry `pass_with_limitations` and 30 records carry `blocked` because:
    1. `data/raw/gold_taxa.tsv`, `data/raw/mediadive_taxa.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/bactotraits_taxa.tsv` store pre-aggregated 2-column count tables extracted from an uncommitted local `kg-microbe` build (`src/taxonmech/extract.py` lines 412–417, 677–678, 840–841), so `evidence_item.snippet` edge counts cannot be independently re-derived from committed raw files alone.
    2. Only `BACDIVE` rolls strain counts up across descendant strain taxids in `src/taxonmech/seed.py`, while `GOLD`, `MEDIADIVE`, `MADIN`, `BACTOTRAITS`, `GTDB`, and `SILVA` report direct-taxid-only counts without explicit scope qualification in `source_attestations[].evidence[]`.
- **Desired Outcome**:
  - Pin reproducible upstream edge-multiplicity provenance (digest/manifest or per-taxon predicate summary) in `data/raw/MANIFEST.yaml` and clarify or align direct-taxid vs subtree-rolled-up attestation count semantics in `src/taxonmech/seed.py`.
- **Evidence Paths**:
  - `src/taxonmech/extract.py`
  - `src/taxonmech/seed.py`
  - `data/raw/MANIFEST.yaml`
  - `docs/legacy-review-inventory.tsv`
  - `docs/structured-review-inventory/part-00.tsv`
  - `docs/structured-review-inventory/part-13.tsv`
  - `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`



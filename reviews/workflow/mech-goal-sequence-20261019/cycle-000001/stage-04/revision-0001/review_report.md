# Stage 4 (`record_review`) Full-Corpus Review Report — TaxonMech (`mech-goal-sequence-20261019`, Cycle 1)

- **Repository**: `CultureBotAI/TaxonMech`
- **Source Revision**: `a4696c9f0cb7400fb95ffd7ce1bfc9bff9eae520`
- **Native Structured Review Bundle**: `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml` (`SHA256: 662dfeb645f1aaa7527f3fb1b4d5abad072b8c4c054dcd31c43a9dbad7cd0544`)
- **Native Rendered Report**: `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.md` (`SHA256: 7e436600b13d0a936fc58289e13de75860177ce2bc0327f22852a62f0a234719`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Rubric**: `.claude/skills/curate-yaml-record/references/review-checklist.md`

## 1. Frozen Corpus Coverage & SHA-256 Inventory Verification

`.venv/bin/python scripts/corpus_review_inventory.py --check --verify-target-sha256` verified **100.0% coverage** of all **626,048** in-scope `TaxonRecord` YAML files in `data/taxa/` (`data/taxa/PATHS.tsv` and `curation/seed_scope.tsv`):

| Metric | Count | Notes |
| --- | ---: | --- |
| Total in-scope `TaxonRecord` files | `626,048` | `Bacteria: 605,695`, `Archaea: 14,013`, `Eukaryota: 6,331`, `other: 9` |
| Legacy-reviewed records (`docs/legacy-review-inventory.tsv`) | `23,883` | `Archaea: 555`, `Bacteria: 17,085`, `Eukaryota: 6,243`, `Other: 0` |
| Structured-reviewed records (`docs/structured-review-inventory/part-00.tsv`..`part-13.tsv`) | `602,165` | `611` batches in `docs/structured-review-batches.tsv` (`Archaea: 13,458`, `Bacteria: 588,610`, `Eukaryota: 88`, `other: 9`) |
| Unreviewed records | `0` | Verified against `data/taxa/PATHS.tsv` |
| Overlapping records between legacy and structured inventories | `0` | Disjoint partition |
| Target YAML SHA-256 mismatches | `0` | All 626,048 files verified on disk |

### Structured Review Verdict Distribution (`602,165` records)

| Verdict | Record Count | Share | Primary Driver |
| --- | ---: | ---: | --- |
| `pass` | `479,251` | `79.59%` | Clean NCBI/BacDive/GTDB/LPSN/StrainInfo/ATB alignment |
| `needs_curation` | `95,766` | `15.90%` | `skos:closeMatch` GTDB species-cluster promotion to `EXACT_SYNONYM` and `xrefs` (`#124`, `#63`) |
| `pass_with_limitations` | `27,118` | `4.50%` | Uncommitted upstream `kg-microbe` raw edge tables for `GOLD`/`MEDIADIVE`/`MADIN`/`BACTOTRAITS` (`#8`) |
| `blocked` | `30` | `0.005%` | Multi-source attestation count verification blocked on uncommitted upstream raw edge tables (`#8`) |

## 2. Directly Bound Exemplar Records (`20` targets across all 4 domains)

The native bundle `reviews/structured/20261021T163800Z-stage4-corpus-record-review/review.yaml` binds 20 representative `TaxonRecord` files (`role: target`) spanning `Bacteria` (10), `Archaea` (3), `Eukaryota` (4), and `other` (3):
- **Bacteria (`10`)**: `NCBITaxon:562` (`Escherichia coli`), `NCBITaxon:83333` (`Escherichia coli K-12`), `NCBITaxon:1423` (`Bacillus subtilis`), `NCBITaxon:287` (`Pseudomonas aeruginosa`), `NCBITaxon:751889` (`Achromobacter sp. JSK4`), `NCBITaxon:345927` (`Acidovorax sp. JS777`), `NCBITaxon:68987` (`Acinetobacter sp. ATCC 11171`), `NCBITaxon:700537` (`Achromobacter sp. YM-M-55`), `NCBITaxon:206` (`Campylobacter sputorum`), `NCBITaxon:33952` (`Acetobacterium woodii`).
- **Archaea (`3`)**: `NCBITaxon:2190` (`Methanocaldococcus jannaschii`), `NCBITaxon:243232` (`Methanocaldococcus jannaschii DSM 2661`), `NCBITaxon:2287` (`Saccharolobus solfataricus`).
- **Eukaryota (`4`)**: `NCBITaxon:4932` (`Saccharomyces cerevisiae`), `NCBITaxon:5207` (`Cryptococcus neoformans`), `NCBITaxon:5755` (`Acanthamoeba castellanii`, Stage 1 part-13 expansion), `NCBITaxon:1859096` (`Cryptococcus deuterogattii`, Stage 1 part-13 expansion).
- **Other (`3`)**: `NCBITaxon:155900` (`uncultured organism`), `NCBITaxon:408170` (`human gut metagenome`), `NCBITaxon:32644` (`unidentified`).

## 3. Consolidated Findings Carried Forward to Stage 5 (`resolve_review_findings`)

| `finding_id` | Issue | Category | Severity | Status | Summary & Stage 5 / Stage 6 Disposition |
| --- | --- | --- | --- | --- | --- |
| `causal-node-type-enum-and-mech-family-nav-drift` | [#76](https://github.com/CultureBotAI/TaxonMech/issues/76) | `schema` | `minor` | `open` | `CausalNodeTypeEnum` omits `GENETIC_ELEMENT`, `ORGANELLE`, `RNA`; Mech family nav omits `NaturalProductMech`. Remediate directly in Stage 5. |
| `validate-history-bare-linkml-validate-path` | [#83](https://github.com/CultureBotAI/TaxonMech/issues/83) | `provenance` | `minor` | `open` | `scripts/validate_history.py` line 48 invokes `linkml-validate` by bare name instead of checking `Path(sys.executable).with_name("linkml-validate")`. Remediate directly in Stage 5. |
| `gtdb-closematch-exact-promotion` | [#124](https://github.com/CultureBotAI/TaxonMech/issues/124) | `grounding` | `major` | `open` | `95,766` records carry `needs_curation` from `skos:closeMatch` GTDB promotion to `EXACT_SYNONYM` and `xrefs` (`#124`, `#63`). Requires full-corpus regeneration. |
| `gtdb-polyphyly-suffix-synonym-mangling` | [#65](https://github.com/CultureBotAI/TaxonMech/issues/65) | `nomenclature` | `major` | `open` | `src/taxonmech/seed.py:468` mangles 15,704 GTDB polyphyly suffixes into fake trinomials (`Campylobacter F sputorum`). Requires corpus regeneration. |
| `gtdb-pooled-broadmatch-attestation-and-note` | [#118](https://github.com/CultureBotAI/TaxonMech/issues/118) | `evidence` | `major` | `open` | 6,335 pooled-only GTDB records report largest pooled cluster's genome count (`#118`) and 8,587 pooled records invert the `broadMatch` direction note (`#119`). Requires corpus regeneration. |
| `curation-history-stale-scope-strain-count` | [#69](https://github.com/CultureBotAI/TaxonMech/issues/69) | `provenance` | `minor` | `open` | `SEEDED_FROM_SOURCES` `curation_history` embeds static `curation/seed_scope.tsv` strain count (`1861` vs `1975` on `NCBITaxon:562`). Requires corpus regeneration. |
| `upstream-edge-multiplicity-and-subtree-count-scope` | [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) | `completeness` | `minor` | `open` | `27,118` `pass_with_limitations` and `30` `blocked` records reflect uncommitted upstream `kg-microbe` raw edge tables and direct-only non-BacDive counts (`#8`). |
| `mechanism-and-protein-representation-prerequisites` | [#78](https://github.com/CultureBotAI/TaxonMech/issues/78) | `completeness` | `major` | `open` | `0` of `626,048` records populate `causal_graphs` or `UniProtKB:` `GENE_OR_PROTEIN` nodes pending `INFRA_TASKS.md` `taxonmech-infra-0001..0003` (Stage 6). |

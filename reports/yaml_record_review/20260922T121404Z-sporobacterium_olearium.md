# YAML Record Review: Sporobacterium olearium
## Target
- Path: `data/taxa/bacteria/sporobacterium_olearium.yaml`
- Identifier: `NCBITaxon:100133`
- Label: `Sporobacterium olearium`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/sporobacterium_olearium.yaml`
- PASS: `just validate-strict data/taxa/bacteria/pseudomonas_sp_br_9131.yaml data/taxa/bacteria/pseudomonas_sp_br_9133.yaml data/taxa/bacteria/sporobacterium_olearium.yaml data/taxa/bacteria/anaerocolumna_xylanovorans.yaml`
  - `files scanned: 4`
  - `files with ERROR: 0`
  - `total ERROR rows: 0`
- SKIPPED: `just validate-history`
  - This was a read-only review of a generated record and did not add a `history/` decision.
- SKIPPED: `just verify-corpus`
  - The record was unchanged; full-corpus verification was not rerun for this four-record review batch.
- NOT APPLICABLE: `just validate-products`
  - The record has no `causal_graphs`.

## Identity and Grounding
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, authority synonym, and six direct source families match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:100133	Sporobacterium olearium	SPECIES	NCBITaxon:100132	11		Sporobacterium olearium Mechichi et al. 1999		ncbitaxon|lpsn|mediadive|gold|madin_etal|bactotraits		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the raw rows that seed the species.
- `mapping_status: SEEDED` accurately reflects a generated seed from local NCBI, LPSN, MediaDive, GOLD, MADIN, BacDive, and BactoTraits inputs.
- `parent_taxon: NCBITaxon:100132` is represented in the lineage as `Sporobacterium`.
- The lineage is internally coherent for a Sporobacterium species:
  - `Bacteria` -> `Bacillati` -> `Bacillota` -> `Clostridia` -> `Lachnospirales` -> `Lachnospiraceae` -> `Sporobacterium`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI `NAME`, LPSN `NAME`, BacDive `STRAIN`, MediaDive `MEDIUM`, GOLD `ORGANISM`, MADIN `TRAIT_ASSERTION`, and BactoTraits `TRAIT_ASSERTION` entries.
- Local source counts agree with the attestation counts: `data/raw/mediadive_taxa.tsv` reports one medium, `data/raw/gold_organisms.tsv` reports one organism, `data/raw/madin_taxa.tsv` reports one trait assertion, and `data/raw/bactotraits_taxa.tsv` reports two trait assertions.
- The LPSN nomenclature block matches `data/raw/lpsn_names.tsv`, including authority `Mechichi et al. 1999`, both publication DOIs, PMID `10555356`, sequence accession `INSDC:AF116854`, and type strain designation `DSM-12504`.
- The descendant BacDive strain `bacdive:6371` is filed under `NCBITaxon:1123283`, which is a strain under `NCBITaxon:100133`; the YAML records that with `classified_as: NCBITaxon:1123283`.
- The GOLD organism and StrainInfo deposit/strain/nucleotide related records are backed by exact rows in `data/raw/strain_related_records.tsv` and `data/straininfo/strain_links.tsv`.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested seven-source seed on `2026-09-12`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 1` is consistent with the one same-species descendant BacDive strain row.
- The record includes the local LPSN nomenclature, BacDive strain, GOLD organism, MediaDive, MADIN and BactoTraits attestations, and source-related strain records visible in the inspected raw inputs.
- No causal graphs are present in the record or required by the inspected seed evidence.

## Findings
- No blocking findings.
- No major findings.
- No minor findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds assemblies, GTDB mappings, or changed LPSN nomenclature for `NCBITaxon:100133`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.

# YAML Record Review: Francisella endosymbiont of Dermacentor variabilis
## Target
- Path: `data/taxa/bacteria/francisella_endosymbiont_of_dermacentor_variabilis.yaml`
- Identifier: `NCBITaxon:100120`
- Label: `Francisella endosymbiont of Dermacentor variabilis`
- Domain: `BACTERIA`
- Rank: `SPECIES`

## Validation
- PASS: `just validate data/taxa/bacteria/francisella_endosymbiont_of_dermacentor_variabilis.yaml`
- PASS: `just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_amitus_hesperidum.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_encarsia_lutea.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_eretmocerus_nr_furuhashii.yaml data/taxa/bacteria/francisella_endosymbiont_of_dermacentor_variabilis.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, and exact synonym match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:100120	Francisella endosymbiont of Dermacentor variabilis	SPECIES	NCBITaxon:2610885	11	Dermacentor variabilis symbiont	...	ncbitaxon		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `mapping_status: SEEDED` accurately reflects a generated NCBI-only seed.
- `parent_taxon: NCBITaxon:2610885` is represented in the lineage as `unclassified Francisella`.
- The lineage is internally coherent for a Francisella record:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Gammaproteobacteria` -> `Thiotrichales` -> `Francisellaceae` -> `Francisella` -> `unclassified Francisella`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI-only name assertion.
- `data/raw/ncbi_merged_ids.tsv` contains an old `NCBITaxon:255918` identifier merged into `NCBITaxon:100120`; the YAML correctly uses the current NCBITaxon identifier.
- The exact synonym `Dermacentor variabilis symbiont` is present in the NCBI row and is represented in the YAML as an `EXACT_SYNONYM`.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested NCBI-only seed on `2026-09-13`.
- An ignored-file-inclusive exact CURIE scan of BacDive, GOLD, LPSN, MediaDive, MADIN, GTDB, ATB, and StrainInfo raw inputs found no same-taxon auxiliary evidence for `NCBITaxon:100120`; other Dermacentor endosymbiont rows in the same scan were separate Arsenophonus or Rickettsia taxa.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 0` is consistent with the absence of local BacDive, ATB, and StrainInfo same-taxon rows.
- No LPSN nomenclature, GTDB mapping, publications, strain inventory, source-related strain records, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds non-NCBI attestations or a more resolved parent for `NCBITaxon:100120`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.

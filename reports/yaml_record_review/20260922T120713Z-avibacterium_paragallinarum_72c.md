# YAML Record Review: Avibacterium paragallinarum 72C
## Target
- Path: `data/taxa/bacteria/avibacterium_paragallinarum_72c.yaml`
- Identifier: `NCBITaxon:1001223`
- Label: `Avibacterium paragallinarum 72C`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/avibacterium_paragallinarum_72c.yaml`
- PASS: `just validate-strict data/taxa/bacteria/francisella_endosymbiont_of_ornitnodoros_porcinus.yaml data/taxa/bacteria/avibacterium_paragallinarum_72c.yaml data/taxa/bacteria/avibacterium_paragallinarum_72c1.yaml data/taxa/bacteria/bacillus_thuringiensis_serovar_chinensis.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, and exact synonyms match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1001223	Avibacterium paragallinarum 72C	STRAIN	NCBITaxon:728	11	Avibacterium paragallinarum str. 72C|Avibacterium paragallinarum strain 72C	...	ncbitaxon|madin_etal		2026-09-13`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as both source attestations.
- `mapping_status: SEEDED` accurately reflects a generated seed from local NCBI and MADIN inputs.
- `parent_taxon: NCBITaxon:728` is represented in the lineage as `Avibacterium paragallinarum`, and the strain sits below that species.
- The lineage is internally coherent for an Avibacterium strain:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Gammaproteobacteria` -> `Pasteurellales` -> `Pasteurellaceae` -> `Avibacterium` -> `Avibacterium paragallinarum`
- An ignored-file-inclusive exact scan against `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv` found the expected generated path and seed-scope rows for this taxon.

## Evidence
- `source_attestations` contains the expected NCBI `NAME` assertion and MADIN `TRAIT_ASSERTION`.
- `data/raw/madin_taxa.tsv` contains one same-CURIE row for `NCBITaxon:1001223`, matching the MADIN attestation count of `1`.
- The exact synonyms `Avibacterium paragallinarum str. 72C` and `Avibacterium paragallinarum strain 72C` are present in the NCBI row and represented in the YAML as `EXACT_SYNONYM` entries.
- `curation_history` is consistent with `curation/seed_scope.tsv`: the record was in scope as an attested two-source seed on `2026-09-12`.
- An ignored-file-inclusive exact CURIE scan of local BacDive, GOLD, LPSN, MediaDive, GTDB, and StrainInfo raw inputs found no same-taxon auxiliary evidence for `NCBITaxon:1001223`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- `strain_count: 0` is consistent with the absence of local BacDive and StrainInfo same-taxon rows.
- No LPSN nomenclature, GTDB mapping, GOLD organism row, publications, strain inventory, source-related strain records, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.
- No major findings.
- No minor findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding if a future source snapshot adds BacDive, GTDB, GOLD, LPSN, or StrainInfo support for `NCBITaxon:1001223`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.

# YAML Record Review: Vibrio cholerae HC-55C1
## Target
- Path: `data/taxa/bacteria/vibrio_cholerae_hc_55c1.yaml`
- Identifier: `NCBITaxon:1000950`
- Label: `Vibrio cholerae HC-55C1`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/vibrio_cholerae_hc_55c1.yaml`
- PASS: `just validate-strict data/taxa/bacteria/anaplasma_marginale_str_south_idaho.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl69.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl7.yaml data/taxa/bacteria/vibrio_cholerae_hc_55c1.yaml`
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
- `identifier`, `label`, `rank`, `parent_taxon`, `genetic_code`, the two NCBI synonyms, and the source list match the pinned NCBI source row in `data/raw/ncbitaxon_taxa.tsv`:
  - `NCBITaxon:1000950	Vibrio cholerae HC-55C1	STRAIN	NCBITaxon:666	11	Vibrio cholerae str. HC-55C1|Vibrio cholerae strain HC-55C1	...	ncbitaxon|madin_etal`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `parent_taxon: NCBITaxon:666` is represented in the lineage as `Vibrio cholerae`, and the Vibrionales lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Gammaproteobacteria` -> `Vibrionales` -> `Vibrionaceae` -> `Vibrio` -> `Vibrio cholerae`
- The absence of a `taxonomy_mappings` block and `xrefs` is consistent with the NCBI source row's provenance list and with an ignored-file-inclusive exact scan of GTDB raw inputs for `NCBITaxon:1000950`, which found no GTDB crosswalk evidence.

## Evidence
- `source_attestations` contains the two expected source rows from `curation/seed_scope.tsv`: NCBI name count 1 and MADIN trait-assertion count 5.
- An exact keyed scan of `data/raw/madin_taxa.tsv` found the same assertion count represented in the YAML.
- An ignored-file-inclusive exact scan of `data/atb`, `data/straininfo`, GOLD, and GTDB raw inputs found no same-taxon auxiliary strain, GOLD, or GTDB rows for `NCBITaxon:1000950`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the expected NCBI and MADIN seed evidence for this `Vibrio cholerae` strain.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- No GTDB mapping, GOLD organism count, strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, GOLD, or GTDB snapshot links rows to `NCBITaxon:1000950`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.

# YAML Record Review: Vibrio cholerae HC-72A2
## Target
- Path: `data/taxa/bacteria/vibrio_cholerae_hc_72a2.yaml`
- Identifier: `NCBITaxon:1000953`
- Label: `Vibrio cholerae HC-72A2`
- Domain: `BACTERIA`
- Rank: `STRAIN`

## Validation
- PASS: `just validate data/taxa/bacteria/vibrio_cholerae_hc_72a2.yaml`
- PASS: `just validate-strict data/taxa/bacteria/vibrio_cholerae_hc_81a2.yaml data/taxa/bacteria/vibrio_cholerae_hc_17a2.yaml data/taxa/bacteria/vibrio_cholerae_hc_72a2.yaml data/taxa/bacteria/uncultured_marine_eubacterium_hstpl70.yaml`
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
  - `NCBITaxon:1000953	Vibrio cholerae HC-72A2	STRAIN	NCBITaxon:666	11	Vibrio cholerae str. HC-72A2|Vibrio cholerae strain HC-72A2	...	ncbitaxon|gtdb|madin_etal`
- `grounding_status: EXACT` is appropriate because the record identifier is the same NCBITaxon CURIE as the source attestation.
- `parent_taxon: NCBITaxon:666` is represented in the lineage as `Vibrio cholerae`, and the Vibrionales lineage is internally coherent:
  - `Bacteria` -> `Pseudomonadati` -> `Pseudomonadota` -> `Gammaproteobacteria` -> `Vibrionales` -> `Vibrionaceae` -> `Vibrio` -> `Vibrio cholerae`
- The `GTDB:s__Vibrio_cholerae` cross-reference, `skos:closeMatch` taxonomy mapping, GTDB synonym, and `genome_count: 2275` all match the exact local `data/raw/gtdb_mappings.tsv` and `data/raw/gtdb_species.tsv` rows for `NCBITaxon:1000953`.

## Evidence
- `source_attestations` contains the three expected source rows from `curation/seed_scope.tsv`: NCBI name count 1, GTDB genome count 2275, and MADIN trait-assertion count 5.
- Exact keyed scans of `data/raw/madin_taxa.tsv` and `data/raw/gtdb_mappings.tsv` found the same assertion counts and mapping predicate represented in the YAML.
- An ignored-file-inclusive exact scan of `data/atb`, `data/straininfo`, and GOLD raw inputs found no same-taxon auxiliary strain or GOLD rows for `NCBITaxon:1000953`.
- Live NCBI lookup was unavailable during this review; the local `data/raw/ncbitaxon_taxa.tsv` snapshot is the pinned primary source that seeded the record.

## Completeness
- The record carries the expected NCBI, GTDB, and MADIN seed evidence for this `Vibrio cholerae` strain.
- `strain_count: 0` is consistent with the absence of local ATB and StrainInfo same-taxon links.
- No GOLD organism count, strain inventory, publications, or causal graphs are present in the local evidence inspected for this record.

## Findings
- No blocking findings.

## Recommended Edits
- None.

## Follow-up Checks
- Re-run source seeding or scope expansion if a future ATB, StrainInfo, or GOLD snapshot links rows to `NCBITaxon:1000953`.

## Additional Notes
- Before this report was written, exact `find reports/yaml_record_review` probes for this stem and its batchmates found no prior reports; `find` includes ignored report files.

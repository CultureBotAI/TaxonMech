# YAML Record Review: Pseudomonas sp. DAC9
- Repository: TaxonMech
- Record: data/taxa/bacteria/pseudomonas_sp_dac9.yaml
- Started UTC: 2026-09-23T11:49:13Z
- Finished UTC: 2026-09-23T11:49:13Z
- Verdict: pass

## Target

Reviewed `NCBITaxon:1008304`, the NCBI-sourced species placeholder `Pseudomonas sp. DAC9`, encoded at `data/taxa/bacteria/pseudomonas_sp_dac9.yaml`.

## Validation

`just validate-strict data/taxa/bacteria/pseudomonas_sp_dac9.yaml data/taxa/bacteria/fervidobacterium_thailandense.yaml data/taxa/bacteria/thermotoga_sp_fc1002.yaml data/taxa/bacteria/maricurvus_nonylphenolicus.yaml` scanned the batch and returned 0 errors.

`just validate data/taxa/bacteria/pseudomonas_sp_dac9.yaml` returned `No issues found`.

## Identity and Grounding

The record is grounded to `NCBITaxon:1008304` with label `Pseudomonas sp. DAC9`. Its parent is `NCBITaxon:196821`, `unclassified Pseudomonas`, which matches an NCBI placeholder species that is not resolved to a formally named Pseudomonas species.

`data/taxa/PATHS.tsv` maps the identifier to `pseudomonas_sp_dac9`, matching the reviewed YAML path. A gitignore-independent `find` of `reports/yaml_record_review` found no pre-existing report for this exact slug before this report was written.

## Evidence

The local NCBI source row in `data/raw/ncbitaxon_taxa.tsv` is the source of truth for the accepted identifier, label, rank, parentage, and NCBI-only source attribution. An exact `rg --no-ignore --hidden` search over `data/taxa/PATHS.tsv`, `data/raw`, `data/atb`, and `data/straininfo` found the PATHS entry and the expected `ncbitaxon_taxa.tsv` row for `NCBITaxon:1008304`.

The same gitignore-independent source search did not reveal BacDive, GTDB, LPSN, GOLD, ATB, or StrainInfo auxiliary rows that should have been projected into this placeholder record.

## Completeness

The YAML is intentionally minimal: it captures a placeholder species asserted by NCBI and does not invent strain, type-material, assembly, synonym, or culture-collection data that are absent from the pinned local inputs.

The `source_at` and `source` fields are consistent with an NCBITAXON-only record.

## Findings

No curation findings.

## Recommended Edits

None.

## Follow-up Checks

None.

## Additional Notes

Live external lookups were unavailable during this review, so the pinned rows under `data/raw`, `data/atb`, and `data/straininfo` were treated as authoritative. The absence checks for prior reports and same-taxon auxiliary rows included ignored files where applicable.

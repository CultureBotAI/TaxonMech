# YAML Record Review: Komvophoron apiculatum
- Repository: TaxonMech
- Record: data/taxa/bacteria/komvophoron_apiculatum.yaml
- Started UTC: 2026-09-23T01:35:17Z
- Finished UTC: 2026-09-23T01:35:17Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/komvophoron_apiculatum.yaml`
- Identifier: `NCBITaxon:1005720`
- Label: `Komvophoron apiculatum`
- Rank: `SPECIES`
- Parent: `NCBITaxon:358711`
- Registry row: `data/taxa/PATHS.tsv:1824`
- Scope row: `curation/seed_scope.tsv:311206`
- A pre-write `find reports/yaml_record_review ... -name '*-komvophoron_apiculatum.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml data/taxa/bacteria/pseudanabaena_belizensis.yaml data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml data/taxa/bacteria/komvophoron_apiculatum.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/komvophoron_apiculatum.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, and NCBI related synonym agree with `data/raw/ncbitaxon_taxa.tsv:210486`.
- The stored lineage terminates at the asserted genus `NCBITaxon:358711` / `Komvophoron`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210486` attests `NCBITaxon:1005720` as `Komvophoron apiculatum`, rank `SPECIES`, parent `NCBITaxon:358711`, genetic code `11`, a nomenclatural related synonym, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv` and `data/raw/gtdb_mappings.tsv` found no same-taxon rows for `NCBITaxon:1005720`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005720`, `Komvophoron apiculatum`, or `komvophoron_apiculatum`.

## Completeness

- The generated NCBI identity, lineage, related synonym, source attestation, and seed history are complete for the local source row.
- The record has no GTDB mapping, xref, Madin, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/komvophoron_apiculatum.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

# YAML Record Review: Pseudanabaena apiculato-flexuosa
- Repository: TaxonMech
- Record: data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml
- Started UTC: 2026-09-23T01:35:17Z
- Finished UTC: 2026-09-23T01:35:17Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml`
- Identifier: `NCBITaxon:1005719`
- Label: `Pseudanabaena apiculato-flexuosa`
- Rank: `SPECIES`
- Parent: `NCBITaxon:1152`
- Registry row: `data/taxa/PATHS.tsv:1823`
- Scope row: `curation/seed_scope.tsv:311205`
- A pre-write `find reports/yaml_record_review ... -name '*-pseudanabaena_apiculato_flexuosa.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/streptococcus_dysgalactiae_subsp_equisimilis_sk1250.yaml data/taxa/bacteria/pseudanabaena_belizensis.yaml data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml data/taxa/bacteria/komvophoron_apiculatum.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, and NCBI related synonym agree with `data/raw/ncbitaxon_taxa.tsv:210485`.
- The stored lineage terminates at the asserted genus `NCBITaxon:1152` / `Pseudanabaena`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210485` attests `NCBITaxon:1005719` as `Pseudanabaena apiculato-flexuosa`, rank `SPECIES`, parent `NCBITaxon:1152`, genetic code `11`, a nomenclatural related synonym, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv` and `data/raw/gtdb_mappings.tsv` found no same-taxon rows for `NCBITaxon:1005719`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005719`, `Pseudanabaena apiculato-flexuosa`, or `pseudanabaena_apiculato_flexuosa`.

## Completeness

- The generated NCBI identity, lineage, related synonym, source attestation, and seed history are complete for the local source row.
- The record has no GTDB mapping, xref, Madin, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/pseudanabaena_apiculato_flexuosa.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

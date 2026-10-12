# YAML Record Review: Burkholderia sp. DRS11A
- Repository: TaxonMech
- Record: data/taxa/bacteria/burkholderia_sp_drs11a.yaml
- Started UTC: 2026-09-23T01:20:59Z
- Finished UTC: 2026-09-23T01:20:59Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/burkholderia_sp_drs11a.yaml`
- Identifier: `NCBITaxon:1005627`
- Label: `Burkholderia sp. DRS11A`
- Rank: `SPECIES`
- Parent: `NCBITaxon:2613784`
- Registry row: `data/taxa/PATHS.tsv:1803`
- Scope row: `curation/seed_scope.tsv:311191`
- A pre-write `find reports/yaml_record_review ... -name '*-burkholderia_sp_drs11a.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/enterobacter_sp_ippbc_w27.yaml data/taxa/bacteria/burkholderia_sp_drs10a.yaml data/taxa/bacteria/burkholderia_sp_drs11a.yaml data/taxa/bacteria/burkholderia_sp_drs13a.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/burkholderia_sp_drs11a.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, and genetic code agree with `data/raw/ncbitaxon_taxa.tsv:210465`.
- The stored lineage terminates at the asserted parent `NCBITaxon:2613784` / `unclassified Burkholderia`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210465` attests `NCBITaxon:1005627` as `Burkholderia sp. DRS11A`, rank `SPECIES`, parent `NCBITaxon:2613784`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv` and `data/raw/gtdb_mappings.tsv` found no same-taxon rows for `NCBITaxon:1005627`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005627`, `Burkholderia sp. DRS11A`, or `burkholderia_sp_drs11a`.

## Completeness

- The generated NCBI identity, lineage, source attestation, and seed history are complete for the local source row.
- The record has no GTDB mapping, synonym, xref, Madin, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/burkholderia_sp_drs11a.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

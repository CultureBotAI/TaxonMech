# YAML Record Review: Burkholderia sp. DJM5B8
- Repository: TaxonMech
- Record: data/taxa/bacteria/burkholderia_sp_djm5b8.yaml
- Started UTC: 2026-09-23T01:56:51Z
- Finished UTC: 2026-09-23T01:56:51Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/burkholderia_sp_djm5b8.yaml`
- Identifier: `NCBITaxon:1005761`
- Label: `Burkholderia sp. DJM5B8`
- Rank: `SPECIES`
- Parent: `NCBITaxon:2613784`
- Registry row: `data/taxa/PATHS.tsv:1849`
- Scope row: `curation/seed_scope.tsv:311229`
- A pre-write `find reports/yaml_record_review ... -name '*-burkholderia_sp_djm5b8.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/burkholderia_sp_djm5b8.yaml data/taxa/bacteria/burkholderia_sp_djm5c9.yaml data/taxa/bacteria/cohnella_sp_djm4h6.yaml data/taxa/bacteria/cupriavidus_sp_djm4g1.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/burkholderia_sp_djm5b8.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, empty synonym set, and NCBI-only source attestation agree with `data/raw/ncbitaxon_taxa.tsv:210513`.
- The stored lineage terminates at the asserted parent `NCBITaxon:2613784` / `unclassified Burkholderia`.
- `grounding_status: EXACT` is appropriate for the NCBI placeholder species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210513` attests `NCBITaxon:1005761` as `Burkholderia sp. DJM5B8`, rank `SPECIES`, parent `NCBITaxon:2613784`, genetic code `11`, no NCBI synonyms, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` found no same-taxon rows for `NCBITaxon:1005761`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005761`, `Burkholderia sp. DJM5B8`, or `burkholderia_sp_djm5b8`.

## Completeness

- The generated NCBI identity, lineage, source attestation, and seed history are complete for the local source row.
- The record has no synonyms, GTDB mapping, xref, Madin, GOLD, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/burkholderia_sp_djm5b8.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

# YAML Record Review: Wolbachia endosymbiont of Podisma tyatiensis
- Repository: TaxonMech
- Record: data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml
- Started UTC: 2026-09-23T01:29:24Z
- Finished UTC: 2026-09-23T01:29:24Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml`
- Identifier: `NCBITaxon:1005652`
- Label: `Wolbachia endosymbiont of Podisma tyatiensis`
- Rank: `SPECIES`
- Parent: `NCBITaxon:2640676`
- Registry row: `data/taxa/PATHS.tsv:1815`
- Scope row: `curation/seed_scope.tsv:311203`
- A pre-write `find reports/yaml_record_review ... -name '*-wolbachia_endosymbiont_of_podisma_tyatiensis.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/pseudomonas_sp_afb_9.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_sapporensis.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml data/taxa/bacteria/kosakonia_oryzendophytica.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, and genetic code agree with `data/raw/ncbitaxon_taxa.tsv:210477`.
- The stored lineage terminates at the asserted parent `NCBITaxon:2640676` / `unclassified Wolbachia`.
- `grounding_status: EXACT` is appropriate for the NCBI species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210477` attests `NCBITaxon:1005652` as `Wolbachia endosymbiont of Podisma tyatiensis`, rank `SPECIES`, parent `NCBITaxon:2640676`, genetic code `11`, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv` and `data/raw/gtdb_mappings.tsv` found no same-taxon rows for `NCBITaxon:1005652`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005652`, `Wolbachia endosymbiont of Podisma tyatiensis`, or `wolbachia_endosymbiont_of_podisma_tyatiensis`.

## Completeness

- The generated NCBI identity, lineage, source attestation, and seed history are complete for the local source row.
- The record has no GTDB mapping, synonym, xref, Madin, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_podisma_tyatiensis.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

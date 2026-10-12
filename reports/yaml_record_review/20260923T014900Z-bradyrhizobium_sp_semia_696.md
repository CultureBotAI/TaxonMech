# YAML Record Review: Bradyrhizobium sp. SEMIA 696
- Repository: TaxonMech
- Record: data/taxa/bacteria/bradyrhizobium_sp_semia_696.yaml
- Started UTC: 2026-09-23T01:49:00Z
- Finished UTC: 2026-09-23T01:49:00Z
- Verdict: pass

## Target

- YAML record: `data/taxa/bacteria/bradyrhizobium_sp_semia_696.yaml`
- Identifier: `NCBITaxon:1005743`
- Label: `Bradyrhizobium sp. SEMIA 696`
- Rank: `SPECIES`
- Parent: `NCBITaxon:2631580`
- Registry row: `data/taxa/PATHS.tsv:1837`
- Scope row: `curation/seed_scope.tsv:311217`
- A pre-write `find reports/yaml_record_review ... -name '*-bradyrhizobium_sp_semia_696.md'` check found no existing report for this stem; `find` includes ignored reports.

## Validation

- `just validate-strict data/taxa/bacteria/bradyrhizobium_sp_semia_696.yaml data/taxa/bacteria/modestobacter_sp_cgmcc1_11143.yaml data/taxa/bacteria/modestobacter_sp_cgmcc1_11191.yaml data/taxa/bacteria/rhodococcus_sp_tmg025_ii.yaml` passed for this four-record batch.
- `just validate data/taxa/bacteria/bradyrhizobium_sp_semia_696.yaml` passed.

## Identity and Grounding

- The YAML identifier, label, rank, parent, genetic code, empty synonym set, and NCBI-only source attestation agree with `data/raw/ncbitaxon_taxa.tsv:210501`.
- The stored lineage terminates at the asserted parent `NCBITaxon:2631580` / `unclassified Bradyrhizobium`.
- `grounding_status: EXACT` is appropriate for the NCBI placeholder species taxon.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:210501` attests `NCBITaxon:1005743` as `Bradyrhizobium sp. SEMIA 696`, rank `SPECIES`, parent `NCBITaxon:2631580`, genetic code `11`, no NCBI synonyms, and NCBI snapshot `2026-09-13`.
- Exact, gitignore-independent scans of `data/raw/madin_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gold_organisms.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` found no same-taxon rows for `NCBITaxon:1005743`.
- An exact, gitignore-independent scan of `data/atb` and `data/straininfo` found no same-taxon rows for `NCBITaxon:1005743`, `Bradyrhizobium sp. SEMIA 696`, or `bradyrhizobium_sp_semia_696`.

## Completeness

- The generated NCBI identity, lineage, source attestation, and seed history are complete for the local source row.
- The record has no synonyms, GTDB mapping, xref, Madin, GOLD, ATB, or StrainInfo material, matching the pinned local rows.

## Findings

- No findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run `just validate data/taxa/bacteria/bradyrhizobium_sp_semia_696.yaml` if the record is regenerated from updated sources.

## Additional Notes

- This review used pinned local sources under `data/raw/`, `data/atb/`, and `data/straininfo/`; live upstream lookup was not used.
- `just validate-history` was not run because this review added no `history/` curation decision.
- `just validate-products` was not applicable because the record has no `causal_graphs`.

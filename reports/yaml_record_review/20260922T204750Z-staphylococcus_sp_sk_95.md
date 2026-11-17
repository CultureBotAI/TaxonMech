# YAML Record Review: Staphylococcus sp. SK 95
- Repository: TaxonMech
- Record: `data/taxa/bacteria/staphylococcus_sp_sk_95.yaml`
- Started UTC: 2026-09-22T20:46:19Z
- Finished UTC: 2026-09-22T20:47:52Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005103` / `staphylococcus_sp_sk_95`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Staphylococcus sp. SK 95` under `NCBITaxon:91994` (`unclassified Staphylococcus`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/staphylococcus_sp_sk_95.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/nocardia_sp_sk_34.yaml data/taxa/bacteria/bacillus_sp_sk_94.yaml data/taxa/bacteria/staphylococcus_sp_sk_95.yaml data/taxa/bacteria/bacillus_sp_3lf_5t.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005103`, `label: Staphylococcus sp. SK 95`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:91994`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Bacillota`, `Bacilli`, `Caryophanales`, `Staphylococcaceae`, `Staphylococcus`, and `unclassified Staphylococcus`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005103`.
- No exact-ID GTDB, GOLD, MADIN, LPSN, BacDive, MediaDive, ATB, StrainInfo, or culture-collection rows were present in the pinned local source rows.
- The generated `source_attestations` entry is therefore correctly limited to the NCBITAXON name attestation.

## Completeness
- The record carries the available identity, parent, lineage, genetic-code, and source-attestation evidence.
- `strain_count: 0`, no synonyms, and absent nomenclature, GTDB mapping, xref, strain, and genome sections are expected for this NCBI-only seed.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-staphylococcus_sp_sk_95.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

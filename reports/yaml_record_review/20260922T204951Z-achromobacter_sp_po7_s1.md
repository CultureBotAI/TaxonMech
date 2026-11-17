# YAML Record Review: Achromobacter sp. PO7_S1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/achromobacter_sp_po7_s1.yaml`
- Started UTC: 2026-09-22T20:48:52Z
- Finished UTC: 2026-09-22T20:49:53Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005105` / `achromobacter_sp_po7_s1`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Achromobacter sp. PO7_S1` under `NCBITaxon:2626865` (`unclassified Achromobacter`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/achromobacter_sp_po7_s1.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/achromobacter_sp_po7_s1.yaml data/taxa/bacteria/acinetobacter_sp_ka1ph_s1.yaml data/taxa/bacteria/acinetobacter_sp_ka1ph_s2.yaml data/taxa/bacteria/acinetobacter_sp_pl15a_s1.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005105`, `label: Achromobacter sp. PO7_S1`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2626865`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Betaproteobacteria`, `Burkholderiales`, `Alcaligenaceae`, `Achromobacter`, and `unclassified Achromobacter`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005105`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-achromobacter_sp_po7_s1.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

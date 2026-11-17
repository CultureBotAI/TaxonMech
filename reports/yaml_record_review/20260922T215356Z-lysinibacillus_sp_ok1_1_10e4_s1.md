# YAML Record Review: Lysinibacillus sp. ok1_1_10e4_S1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/lysinibacillus_sp_ok1_1_10e4_s1.yaml`
- Started UTC: 2026-09-22T21:52:50Z
- Finished UTC: 2026-09-22T21:53:56Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005226` / `lysinibacillus_sp_ok1_1_10e4_s1`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Lysinibacillus sp. ok1_1_10e4_S1` under `NCBITaxon:2636778` (`unclassified Lysinibacillus`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/lysinibacillus_sp_ok1_1_10e4_s1.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/klebsiella_sp_ok1_1_9_s9.yaml data/taxa/bacteria/lysinibacillus_sp_ok1_1_10e4_s1.yaml data/taxa/bacteria/massilia_sp_pl13e3_s1.yaml data/taxa/bacteria/massilia_sp_pl13e3_s10.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005226`, `label: Lysinibacillus sp. ok1_1_10e4_S1`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2636778`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Bacillaceae`, `Lysinibacillus`, and `unclassified Lysinibacillus`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID, exact-label, and exact-slug gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005226`.
- No exact GTDB, GOLD, MADIN, LPSN, BacDive, MediaDive, ATB, StrainInfo, or culture-collection rows were present in the pinned local source rows.
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
- Before writing this report, an exact-stem `find reports/yaml_record_review -maxdepth 1 -type f` preflight for `*-klebsiella_sp_ok1_1_9_s9.md`, `*-lysinibacillus_sp_ok1_1_10e4_s1.md`, `*-massilia_sp_pl13e3_s1.md`, and `*-massilia_sp_pl13e3_s10.md` returned no prior ignored reports for these four stems; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

# YAML Record Review: Clostridium sp. BJ2
- Repository: TaxonMech
- Record: `data/taxa/bacteria/clostridium_sp_bj2.yaml`
- Started UTC: 2026-09-22T20:42:32Z
- Finished UTC: 2026-09-22T20:43:24Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005093` / `clostridium_sp_bj2`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Clostridium sp. BJ2` under `NCBITaxon:2614128` (`unclassified Clostridium`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/clostridium_sp_bj2.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/buchnera_aphidicola_str_ak_acyrthosiphon_kondoi.yaml data/taxa/bacteria/clostridium_sp_bj1.yaml data/taxa/bacteria/clostridium_sp_bj2.yaml data/taxa/bacteria/streptomyces_sp_udsc1.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005093`, `label: Clostridium sp. BJ2`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2614128`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Clostridiaceae`, `Clostridium`, and `unclassified Clostridium`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005093`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-clostridium_sp_bj2.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

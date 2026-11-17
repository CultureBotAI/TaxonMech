# YAML Record Review: Aeromicrobium sp. PL34a1_S1
- Repository: TaxonMech
- Record: `data/taxa/bacteria/aeromicrobium_sp_pl34a1_s1.yaml`
- Started UTC: 2026-09-22T21:11:26Z
- Finished UTC: 2026-09-22T21:12:38Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005148` / `aeromicrobium_sp_pl34a1_s1`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Aeromicrobium sp. PL34a1_S1` under `NCBITaxon:2633570` (`unclassified Aeromicrobium`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/aeromicrobium_sp_pl34a1_s1.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/acinetobacter_sp_pl15a_s8.yaml data/taxa/bacteria/acinetobacter_sp_pl15a_s9.yaml data/taxa/bacteria/aerococcus_sp_pk35_s1.yaml data/taxa/bacteria/aeromicrobium_sp_pl34a1_s1.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005148`, `label: Aeromicrobium sp. PL34a1_S1`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2633570`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Actinomycetes`, `Propionibacteriales`, `Nocardioidaceae`, `Aeromicrobium`, and `unclassified Aeromicrobium`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID, exact-label, and exact-slug gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005148`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-aeromicrobium_sp_pl34a1_s1.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

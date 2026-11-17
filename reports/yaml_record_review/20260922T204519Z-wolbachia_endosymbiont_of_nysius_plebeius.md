# YAML Record Review: Wolbachia endosymbiont of Nysius plebeius
- Repository: TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_nysius_plebeius.yaml`
- Started UTC: 2026-09-22T20:44:20Z
- Finished UTC: 2026-09-22T20:45:20Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1005097` / `wolbachia_endosymbiont_of_nysius_plebeius`.
- The record is a generated `SPECIES`-rank `BACTERIA` record for `Wolbachia endosymbiont of Nysius plebeius` under `NCBITaxon:2640676` (`unclassified Wolbachia`).
- The record is seeded from the pinned NCBITAXON inventory only.

## Validation
- `just validate data/taxa/bacteria/wolbachia_endosymbiont_of_nysius_plebeius.yaml` completed successfully with no LinkML issues.
- `just validate-strict data/taxa/bacteria/streptomyces_sp_udsc2.yaml data/taxa/bacteria/streptomyces_sp_udsc3.yaml data/taxa/bacteria/wolbachia_endosymbiont_of_nysius_plebeius.yaml data/taxa/bacteria/candidatus_lariskella_arthropodorum.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was skipped because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `identifier: NCBITaxon:1005097`, `label: Wolbachia endosymbiont of Nysius plebeius`, `rank: SPECIES`, `taxon_domain: BACTERIA`, `parent_taxon: NCBITaxon:2640676`, and `genetic_code: 11` match the exact NCBI row in `data/raw/ncbitaxon_taxa.tsv`.
- The lineage follows the local NCBI backbone through `Anaplasmataceae`, `Wolbachieae`, `Wolbachia`, and `unclassified Wolbachia`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon record.

## Evidence
- The exact-ID gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, and `data/straininfo` found only the NCBITAXON source row for `NCBITaxon:1005097`.
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
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name '*-wolbachia_endosymbiont_of_nysius_plebeius.md'` returned no prior ignored report for this stem; `find` includes ignored reports.
- Live NCBI lookup was not used; the pinned local NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

# YAML Record Review: Tetragenococcus halophilus HO
- Repository: TaxonMech
- Record: `data/taxa/bacteria/tetragenococcus_halophilus_ho.yaml`
- Started UTC: 2026-09-22T20:11:01Z
- Finished UTC: 2026-09-22T20:12:46Z
- Verdict: pass

## Target
- Reviewed `NCBITaxon:1004777` / `tetragenococcus_halophilus_ho`.
- The record is a `STRAIN`-rank `BACTERIA` record for `Tetragenococcus halophilus HO`.
- Parentage is the seeded NCBI placement under `NCBITaxon:51669` (`Tetragenococcus halophilus`), with lineage through `Bacillota`, `Bacilli`, `Lactobacillales`, `Enterococcaceae`, and `Tetragenococcus`.

## Validation
- `just validate data/taxa/bacteria/tetragenococcus_halophilus_ho.yaml` completed successfully.
- `just validate-strict data/taxa/bacteria/tetragenococcus_halophilus_ho.yaml data/taxa/archaea/desulfurococcaceae_archaeon_ebi_244.yaml data/taxa/archaea/desulfurococcaceae_archaeon_csc_16s.yaml data/taxa/bacteria/alteromonas_macleodii_str_black_sea_11.yaml` scanned the four-file batch and reported `0` files with `ERROR` rows.
- `just validate-history` was not applicable because this was a read-only review and no `history/` decision was added.
- `just validate-products` was not applicable because this record has no `causal_graphs`.

## Identity and Grounding
- `id: NCBITaxon:1004777`, `label: Tetragenococcus halophilus HO`, `rank: STRAIN`, `domain: BACTERIA`, `parent: NCBITaxon:51669`, and `genetic_code: 11` match the pinned row in `data/raw/ncbitaxon_taxa.tsv`.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for a directly seeded NCBI Taxon strain.
- Both exact synonyms, `Tetragenococcus halophilus str. HO` and `Tetragenococcus halophilus strain HO`, are carried from the NCBI synonym field for this taxon.

## Evidence
- The exact same-taxon source rows for `NCBITaxon:1004777` and `tetragenococcus_halophilus_ho` were limited to `data/raw/ncbitaxon_taxa.tsv`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv`.
- The gitignore-independent `rg --no-ignore --hidden` search across `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` found no GTDB, GOLD, MADIN, ATB, or StrainInfo rows for this taxon.
- The generated `sources` entry is therefore correctly limited to one NCBITAXON attestation.

## Completeness
- `strain_count: 0` is consistent with the absence of same-taxon strain rows in the local pinned StrainInfo tables.
- The record has the NCBI strain name and synonyms expected from the source row.
- The empty GTDB, ATB, strain, and assembly sections are expected for this one-source seed.

## Findings
- No findings.

## Recommended Edits
- None.

## Follow-up Checks
- None required for this record.

## Additional Notes
- Before writing this report, `find reports/yaml_record_review -maxdepth 1 -type f -name *-tetragenococcus_halophilus_ho.md` returned no prior ignored report for this stem.
- Live NCBI lookup was not used; the local pinned NCBI Taxon row dated `2026-09-13` was treated as the source of truth.

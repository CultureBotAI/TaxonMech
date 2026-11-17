# YAML Record Review: Paenibacillus sp. ok_1_1_1a5_S1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_ok_1_1_1a5_s1.yaml
- Started UTC: 2026-09-22T22:44:33Z
- Finished UTC: 2026-09-22T22:44:41Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005306`
- Label: `Paenibacillus sp. ok_1_1_1a5_S1`
- Class/rank/domain: `TaxonRecord` / `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:185978` / `unclassified Paenibacillus`
- Maintained owner: generated from `data/raw/ncbitaxon_taxa.tsv` plus `curation/seed_scope.tsv`

The filename is pinned by `data/taxa/PATHS.tsv:1602`, and `curation/seed_scope.tsv:311156` keeps this taxon in scope from the `2026-09-13` attested NCBI rule.

## Validation

- `just validate data/taxa/bacteria/paenibacillus_sp_ok_1_1_1a5_s1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/paenibacillus_sp_px23a_s2.yaml data/taxa/bacteria/paenibacillus_sp_ok_1_1_1a5_s1.yaml data/taxa/bacteria/paenibacillus_sp_ok_1_1_1a5_s2.yaml data/taxa/bacteria/pedobacter_sp_px8b_s1.yaml`: passed; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- `just validate-products`: skipped because this full-corpus graph-label gate has no `causal_graphs` to inspect here.
- `just validate-history`: skipped because this read-only review did not add `history/`.
- `just verify-corpus`: skipped for this report; the earlier full-corpus verifier over 625,960 records was clean, and this review did not edit `data/taxa/`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:210264` exactly supports `NCBITaxon:1005306`, `Paenibacillus sp. ok_1_1_1a5_S1`, rank `SPECIES`, parent `NCBITaxon:185978`, genetic code `11`, `attested_by` = `ncbitaxon`, and snapshot `2026-09-13`. The ancestor rows for `Bacillati`, `Bacillota`, `Bacilli`, `Caryophanales`, `Paenibacillaceae`, `Paenibacillus`, and `unclassified Paenibacillus` are present in `data/raw/ncbitaxon_taxa.tsv`. `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for this NCBI-grounded generated record.

## Evidence

The single `NCBITAXON` source attestation for `NCBITaxon:1005306` with `assertion_count: 1` and `assertion_unit: NAME` is supported by the exact NCBI row. No unsupported, stale, or over-scoped evidence was found.

## Completeness

- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 -type f '(' -name '*-paenibacillus_sp_ok_1_1_1a5_s1.md' -o ... ')' -print` probe found no prior report for this stem; `find` includes ignored reports.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005306`, `Paenibacillus sp. ok_1_1_1a5_S1`, and `paenibacillus_sp_ok_1_1_1a5_s1` found no same-taxon auxiliary source rows.
- The pinned NCBI row has no exact, related, or broad synonyms, and no GTDB, LPSN, BacDive, AllTheBacteria, or StrainInfo rows were found that would support nomenclature, taxonomy mappings, strains, genome links, related records, or causal graphs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is required. If future source refreshes change this taxon, rerun `just seed --only NCBITaxon:1005306`, the strict validator on the emitted YAML, `just verify-corpus`, and `just render-check`.

## Additional Notes

Live NCBI lookup was unavailable; the pinned local `2026-09-13` NCBI projection in `data/raw/ncbitaxon_taxa.tsv` is the reviewed source of truth.

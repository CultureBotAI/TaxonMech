# YAML Record Review: Brevundimonas sp. PL46b_S2

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/brevundimonas_sp_pl46b_s2.yaml
- Started UTC: 2026-09-22T23:07:39Z
- Finished UTC: 2026-09-22T23:07:47Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005334`
- Label: `Brevundimonas sp. PL46b_S2`
- Class/rank/domain: `TaxonRecord` / `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:2622653` / `unclassified Brevundimonas`
- Maintained owner: generated from `data/raw/ncbitaxon_taxa.tsv` plus `curation/seed_scope.tsv`

The filename is pinned by `data/taxa/PATHS.tsv:1630`, and `curation/seed_scope.tsv:311184` keeps this taxon in scope from the `2026-09-13` attested NCBI rule.

## Validation

- `just validate data/taxa/bacteria/brevundimonas_sp_pl46b_s2.yaml`: passed.
- `just validate-strict data/taxa/bacteria/zhihengliuella_sp_pl35a5b_s1.yaml data/taxa/bacteria/brevundimonas_sp_pl46b_s2.yaml data/taxa/bacteria/brevundimonas_sp_pl46b_s3.yaml data/taxa/bacteria/brevundimonas_sp_pl46b_s4.yaml`: passed; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- `just validate-products`: skipped because this full-corpus graph-label gate has no `causal_graphs` to inspect here.
- `just validate-history`: skipped because this read-only review did not add `history/`.
- `just verify-corpus`: skipped for this report; the earlier full-corpus verifier over 625,960 records was clean, and this review did not edit `data/taxa/`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:210292` exactly supports `NCBITaxon:1005334`, `Brevundimonas sp. PL46b_S2`, rank `SPECIES`, parent `NCBITaxon:2622653`, genetic code `11`, `attested_by` = `ncbitaxon`, and snapshot `2026-09-13`. The ancestor rows for `Pseudomonadati`, `Pseudomonadota`, `Alphaproteobacteria`, `Caulobacterales`, `Caulobacteraceae`, `Brevundimonas`, and `unclassified Brevundimonas` are present in `data/raw/ncbitaxon_taxa.tsv`. `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for this NCBI-grounded generated record.

## Evidence

The single `NCBITAXON` source attestation for `NCBITaxon:1005334` with `assertion_count: 1` and `assertion_unit: NAME` is supported by the exact NCBI row. No unsupported, stale, or over-scoped evidence was found.

## Completeness

- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 -type f '(' -name '*-brevundimonas_sp_pl46b_s2.md' -o ... ')' -print` probe found no prior report for this stem; `find` includes ignored reports.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/atb` and `data/straininfo` for `NCBITaxon:1005334`, `Brevundimonas sp. PL46b_S2`, and `brevundimonas_sp_pl46b_s2` found no same-taxon auxiliary source rows.
- The pinned NCBI row has no exact, related, or broad synonyms, and no GTDB, LPSN, BacDive, AllTheBacteria, or StrainInfo rows were found that would support nomenclature, taxonomy mappings, strains, genome links, related records, or causal graphs.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is required. If future source refreshes change this taxon, rerun `just seed --only NCBITaxon:1005334`, the strict validator on the emitted YAML, `just verify-corpus`, and `just render-check`.

## Additional Notes

Live NCBI lookup was unavailable; the pinned local `2026-09-13` NCBI projection in `data/raw/ncbitaxon_taxa.tsv` is the reviewed source of truth.

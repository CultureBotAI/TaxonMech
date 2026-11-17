# YAML Record Review: Paenibacillus sp. PX23a_S1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/bacteria/paenibacillus_sp_px23a_s1.yaml
- Started UTC: 2026-09-22T22:38:41Z
- Finished UTC: 2026-09-22T22:38:48Z
- Verdict: pass

## Target

- Identifier: `NCBITaxon:1005304`
- Label: `Paenibacillus sp. PX23a_S1`
- Class/rank/domain: `TaxonRecord` / `SPECIES` / `BACTERIA`
- Parent: `NCBITaxon:185978` / `unclassified Paenibacillus`
- Maintained owner: generated from `data/raw/ncbitaxon_taxa.tsv` plus `curation/seed_scope.tsv`

The filename is pinned by `data/taxa/PATHS.tsv:1600`, and `curation/seed_scope.tsv:311154` keeps this taxon in scope from the `2026-09-13` attested NCBI rule.

## Validation

- `just validate data/taxa/bacteria/paenibacillus_sp_px23a_s1.yaml`: passed.
- `just validate-strict data/taxa/bacteria/massilia_sp_ox3b1_s4.yaml data/taxa/bacteria/massilia_sp_ox3b1_s5.yaml data/taxa/bacteria/massilia_sp_ox3b1_s6.yaml data/taxa/bacteria/paenibacillus_sp_px23a_s1.yaml`: passed; 4 files scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- `just validate-products`: skipped because this full-corpus graph-label gate has no `causal_graphs` to inspect here.
- `just validate-history`: skipped because this read-only review did not add `history/`.
- `just verify-corpus`: skipped for this report; the earlier full-corpus verifier over 625,960 records was clean, and this review did not edit `data/taxa/`.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:210262` exactly supports `NCBITaxon:1005304`, `Paenibacillus sp. PX23a_S1`, rank `SPECIES`, parent `NCBITaxon:185978`, genetic code `11`, `attested_by` = `ncbitaxon`, and snapshot `2026-09-13`. Exact NCBI ancestor rows support the `Bacillati` -> `Bacillota` -> `Bacilli` -> `Caryophanales` -> `Paenibacillaceae` -> `Paenibacillus` -> `unclassified Paenibacillus` chain. `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate.

## Evidence

The single `NCBITAXON` source attestation for `NCBITaxon:1005304` with `assertion_count: 1` and `assertion_unit: NAME` is supported by the exact NCBI row. No unsupported, stale, or over-scoped evidence was found.

## Completeness

- Exact ignored-report probe: `find reports/yaml_record_review -maxdepth 1 -type f -name '*-paenibacillus_sp_px23a_s1.md'` found no prior report; `find` includes ignored reports.
- A gitignore-independent `rg --no-ignore --hidden` scan of `data/raw`, `data/atb`, `data/straininfo`, `curation/seed_scope.tsv`, and `data/taxa/PATHS.tsv` for `NCBITaxon:1005304`, `Paenibacillus sp. PX23a_S1`, and `paenibacillus_sp_px23a_s1` found only the expected NCBI inventory, scope, and path rows.
- No auxiliary rows support additional attestations, synonyms, nomenclature, mappings, strains, genomes, related records, or causal graphs for this taxon.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No record-specific follow-up is required. If future source refreshes change this taxon, rerun `just seed --only NCBITaxon:1005304`, the strict validator on the emitted YAML, `just verify-corpus`, and `just render-check`.

## Additional Notes

Live authority lookups were unavailable; the pinned local `2026-09-13` NCBI projection in `data/raw/ncbitaxon_taxa.tsv` is the reviewed source of truth.

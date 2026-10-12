# YAML Record Review: Arcocellulus cornucervis

## Target

- File: `data/taxa/eukaryota/arcocellulus_cornucervis.yaml`
- Identifier: `NCBITaxon:1155433`
- Label: `Arcocellulus cornucervis`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:420263` / `Arcocellulus`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Stramenopiles` -> `Ochrophyta` -> `Bacillariophyta` -> `Thalassiosirophyceae` -> `Eupodiscaphycidae` -> `Cymatosirales` -> `Cymatosiraceae` -> `Arcocellulus`
- Existing review report: none found for `*arcocellulus_cornucervis.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/arcocellulus_cornucervis.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/arcocellulus_cornucervis.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:1155433`, labelled `Arcocellulus cornucervis` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:1155433` is a `SPECIES` child of `NCBITaxon:420263` / `Arcocellulus`.
- The generated NCBI synonym block matches the raw NCBI row: it has no exact synonyms and one related synonym, `Arcocellulus cornucervis G.R.Hasle, H.A.von Stosch & E.E.Syvertsen, 1983`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Arcocellulus cornucervis, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:1155433`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:1155433`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:1155433`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:1155433` with count `1`.
- Exact native GOLD inspection of `data/gold/organisms.jsonl.gz` found 0 organism rows with `ORGANISM NCBI TAX ID = 1155433`; broader searches for `Arcocellulus` and the target NCBI number also found no matching organism, project, or analysis rows in local `data/gold/*.jsonl.gz`.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `1155433`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `1155433`.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:1155433` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonym, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive, StrainInfo, and native GOLD checks: neither strain source has an exact NCBI match, and the aggregate GOLD count has no matching native organism row in the local `data/gold` snapshot.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/arcocellulus_cornucervis.yaml`; it is generated and validates strictly.
- Preserve the NCBI related synonym, count-consistent aggregate GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If the local native GOLD snapshot is refreshed, recheck whether the aggregate GOLD count for `NCBITaxon:1155433` resolves to a `data/gold/organisms.jsonl.gz` row and whether that row acquires projects or analysis rows.
- Rerun `just validate data/taxa/eukaryota/arcocellulus_cornucervis.yaml` and `just validate-strict data/taxa/eukaryota/arcocellulus_cornucervis.yaml` after regenerating the taxon record.

## Additional Notes

- The GOLD source attestation for this generated taxon is supported by the aggregate `data/raw/gold_organisms.tsv` row; the local native GOLD snapshot does not currently contain an inspectable organism row for the same NCBI taxon.

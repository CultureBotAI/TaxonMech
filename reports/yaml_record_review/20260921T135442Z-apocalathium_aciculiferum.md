# YAML Record Review: Apocalathium aciculiferum

## Target

- File: `data/taxa/eukaryota/apocalathium_aciculiferum.yaml`
- Identifier: `NCBITaxon:268820`
- Label: `Apocalathium aciculiferum`
- Rank: `SPECIES`
- Domain: `EUKARYOTA`
- Parent: `NCBITaxon:2137288` / `Apocalathium`
- Lineage: `root` -> `cellular organisms` -> `Eukaryota` -> `Sar` -> `Alveolata` -> `Dinophyceae` -> `Thoracosphaerales` -> `Thoracosphaeraceae` -> `Apocalathium`
- Existing review report: none found for `*apocalathium_aciculiferum.md` under the ignored `reports/yaml_record_review/` tree.

## Validation

- `just validate data/taxa/eukaryota/apocalathium_aciculiferum.yaml`: passed with `No issues found`.
- `just validate-strict data/taxa/eukaryota/apocalathium_aciculiferum.yaml`: passed with 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows, and a refreshed `reports/instance_validation_failures.tsv`.
- `just validate-history`: not rerun for this single generated record; it passed earlier on this checkout.
- `just verify-corpus`: not rerun for this single generated record; it passed earlier on this checkout with 625,960 expected records, 625,960 records on disk, and 0 missing, extra, or differing records.
- `just validate-products`: not run. This generated record has no `causal_graphs` block, so the product validator has no curator-added causal graph nodes to walk.

## Identity and Grounding

- The record is exactly grounded to the NCBI species `NCBITaxon:268820`, labelled `Apocalathium aciculiferum` in the 2026-09-13 NCBI snapshot.
- The generated lineage matches `data/raw/ncbitaxon_taxa.tsv`: `NCBITaxon:268820` is a `SPECIES` child of `NCBITaxon:2137288` / `Apocalathium`.
- The generated NCBI synonym block matches the raw NCBI row: exact synonym `Peridinium aciculiferum`, plus related synonym `Peridinium aciculiferum Lemmermann, 1900`.
- `curation/seed_scope.tsv` has one matching scope row, dated 2026-09-12, with the generated reason `attested rule: Apocalathium aciculiferum, 2 sources incl. NCBI`.
- `data/raw/ncbi_merged_ids.tsv` has no row for `NCBITaxon:268820`, so this identifier is not currently represented as a merged-away NCBI ID in the local raw snapshot.
- A bounded no-ignore, hidden-file search over `data/`, `curation/`, and `reports/` for `NCBITaxon:268820`, the exact label, and the slug found only the generated taxon and path rows, the raw NCBI/GOLD/scope rows, and no duplicate review report. Ignored files were included.

## Evidence

- The generated `NCBITAXON` source attestation is count-consistent with `data/raw/ncbitaxon_taxa.tsv`, which has one row for `NCBITaxon:268820`.
- The generated `GOLD` source attestation is count-consistent with `data/raw/gold_organisms.tsv`, which has `NCBITaxon:268820` with count `1`.
- Exact native GOLD inspection found one organism row for the same taxon: `Go0368789`, `Peridinium aciculiferum PAER-2`, strain `PAER-2`, and no culture collection ID.
- No native GOLD project or genome analysis rows linked to organism `Go0368789` were present in the local `data/gold/projects.jsonl.gz` and `data/gold/analyses.jsonl.gz` snapshots.
- Numeric-tolerant exact StrainInfo inspection of `data/straininfo/records.jsonl.gz` found 0 direct or deposit-only strain rows for `268820`.
- Exact BacDive inspection of `data/bacdive/records.jsonl.gz` found 0 records whose `General` NCBI tax ID matched `268820`.
- A `PAER-2` token lookup found 0 BacDive rows and 0 StrainInfo rows.
- `data/raw/ncbi_type_material.tsv` has no row for `NCBITaxon:268820` in the local NCBI type-material snapshot.

## Completeness

- The compact generated record has the expected identifier, label, rank, domain, parent, lineage, grounding, mapping status, NCBI synonyms, genetic code, `strain_count`, two source attestations, and generation history.
- There are no taxonomy mappings, strains, evidence rows, nomenclature rows, or causal graphs in the generated YAML.
- The absence of `strains` is consistent with the exact BacDive and StrainInfo source checks: neither source has an exact NCBI match, and the GOLD `PAER-2` token does not join to either local strain source.
- The absence of `nomenclature` is expected for this eukaryotic species because generated `nomenclature` entries currently come from LPSN only, and NCBI has no type-material rows for this taxon in the local raw snapshot.

## Findings

- No curator-actionable defects found.

## Recommended Edits

- No direct edit to `data/taxa/eukaryota/apocalathium_aciculiferum.yaml`; it is generated and validates strictly.
- Preserve the NCBI synonyms, count-consistent one-organism GOLD source attestation, and empty local BacDive/StrainInfo behavior when regenerating the record.

## Follow-up Checks

- If GOLD project or analysis linking changes, recheck whether organism `Go0368789` acquires project or analysis rows and whether those rows remain source evidence only or can join into strain-related records.
- Rerun `just validate data/taxa/eukaryota/apocalathium_aciculiferum.yaml` and `just validate-strict data/taxa/eukaryota/apocalathium_aciculiferum.yaml` after regenerating the taxon record.

## Additional Notes

- The native GOLD organism uses the older synonym `Peridinium aciculiferum` in `ORGANISM NAME`, but it is still an exact NCBI taxon match through `ORGANISM NCBI TAX ID = 268820`.

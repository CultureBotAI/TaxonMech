# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_nivariensis_cbs_9983.yaml`
- Taxon: `NCBITaxon:1279115` (`Nakaseomyces nivariensis CBS 9983`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1279115`, label `Nakaseomyces nivariensis CBS 9983`.
- It is grounded exactly under `NCBITaxon:418086` (`Nakaseomyces nivariensis`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Nakaseomyces nivariensis`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_nivariensis_cbs_9983.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_nivariensis_cbs_9983.yaml data/taxa/eukaryota/nakaseomyces_uthaithaninus.yaml data/taxa/eukaryota/nakataea_oryzae.yaml data/taxa/eukaryota/nakazawaea_anatomiae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58875` contains the seeded identifier with reason `attested rule: Nakaseomyces nivariensis CBS 9983, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:298700` matches the YAML identity: parent `NCBITaxon:418086`, rank `STRAIN`, and exact synonym `Candida nivariensis CBS 9983`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:298700` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:6509`, where `NCBITaxon:1279115` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0041974` / `Candida nivariensis CBS 9983`, linked to project `Gp0041974` and one native analysis.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1279115`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1279115`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1279115`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains, exact type-material side inventories, or retained retired IDs.

## Additional Notes

- The native GOLD organism/project/analysis rows still use the older `Candida nivariensis CBS 9983` label but carry the exact current NCBI taxon ID.

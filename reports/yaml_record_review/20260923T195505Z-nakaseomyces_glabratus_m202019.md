# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_glabratus_m202019.yaml`
- Taxon: `NCBITaxon:1398155` (`Nakaseomyces glabratus M202019`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:1398155`, label `Nakaseomyces glabratus M202019`.
- It is grounded exactly under `NCBITaxon:5478` (`Nakaseomyces glabratus`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 14 lineage entries from `root` through `Nakaseomyces glabratus`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_glabratus_m202019.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_glabratus_m202019.yaml data/taxa/eukaryota/nakaseomyces_glabratus_uob301.yaml data/taxa/eukaryota/nakaseomyces_kungkrabaensis.yaml data/taxa/eukaryota/nakaseomyces_nivariensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59906` contains the seeded identifier with reason `attested rule: Nakaseomyces glabratus M202019, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:344249` matches the YAML identity: parent `NCBITaxon:5478`, rank `STRAIN`, and exact synonym `Candida glabrata M202019`.
- All 14 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:344249` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:9443`, where `NCBITaxon:1398155` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0047966` / `Candida glabrata M202019`, linked to project `Gp0047966` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:1398155`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1398155`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:1398155`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains, exact type-material side inventories, or retained retired IDs.

## Additional Notes

- The native GOLD organism/project rows still use the older `Candida glabrata M202019` label but carry the exact current NCBI taxon ID.

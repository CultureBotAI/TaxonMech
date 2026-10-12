# YAML Record Review

- Target: `data/taxa/eukaryota/navicula_arenaria.yaml`
- Taxon: `NCBITaxon:355634` (`Navicula arenaria`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:355634`, label `Navicula arenaria`.
- It is grounded exactly under `NCBITaxon:50949` (`Navicula`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Navicula`.

## Validation

- `just validate data/taxa/eukaryota/navicula_arenaria.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naumovozyma_castellii.yaml data/taxa/eukaryota/naumovozyma_dairenensis.yaml data/taxa/eukaryota/navicula_arenaria.yaml data/taxa/eukaryota/necromortierella_dichotoma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55333` contains the seeded identifier with reason `attested rule: Navicula arenaria, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:73413` matches the YAML identity: parent `NCBITaxon:50949`, rank `SPECIES`, related synonym `Navicula arenaria Donkin, 1861`, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:73413` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33080`, where `NCBITaxon:355634` has `organism_count` 2.
- The current native GOLD catalogs have no exact organism, project, or analysis rows for `NCBITaxon:355634`; the retained GOLD aggregate in `data/raw/gold_organisms.tsv` supplies the GOLD assertion.

## Completeness

- Exact ignored-file-inclusive scans of `data/raw/ncbi_type_material.tsv` and `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:355634`.
- Exact StrainInfo side inventory has 4 direct rows and 4 deposit entries for `NCBITaxon:355634`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventory or retained retired-ID provenance.

## Additional Notes

- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from current native GOLD exact rows.

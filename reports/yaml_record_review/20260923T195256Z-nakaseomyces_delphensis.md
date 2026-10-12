# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_delphensis.yaml`
- Taxon: `NCBITaxon:51657` (`Nakaseomyces delphensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:51657`, label `Nakaseomyces delphensis`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_delphensis.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_delphensis.yaml data/taxa/eukaryota/nakaseomyces_glabratus.yaml data/taxa/eukaryota/nakaseomyces_glabratus_cab52_4041.yaml data/taxa/eukaryota/nakaseomyces_glabratus_cctcc_m202019.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52836` contains the seeded identifier with reason `attested rule: Nakaseomyces delphensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6484` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, two exact synonyms, and one related synonym.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6484` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37625`, where `NCBITaxon:51657` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705378` / `Nakaseomyces delphensis NRRL Y-2379`, linked to project `Gp0831419` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 15 rows for `NCBITaxon:51657`, under synonym name `Saccharomyces delphensis`.
- Exact StrainInfo side inventory has 2 direct rows and 19 deposit entries for `NCBITaxon:51657`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:51657`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

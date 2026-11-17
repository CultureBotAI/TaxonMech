# YAML Record Review

- Target: `data/taxa/eukaryota/nemania_abortiva.yaml`
- Taxon: `NCBITaxon:561989` (`Nemania abortiva`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:561989`, label `Nemania abortiva`.
- It is grounded exactly under `NCBITaxon:109374` (`Nemania`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nemania`.

## Validation

- `just validate data/taxa/eukaryota/nemania_abortiva.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nectriaceae_sp.yaml data/taxa/eukaryota/nectriopsis_sporangiicola.yaml data/taxa/eukaryota/nectriopsis_tremellicola.yaml data/taxa/eukaryota/nemania_abortiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56040` contains the seeded identifier with reason `attested rule: Nemania abortiva, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:131871` matches the YAML identity: parent `NCBITaxon:109374`, rank `SPECIES`, three related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:131871` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38868`, where `NCBITaxon:561989` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0454035` / `Nemania abortiva FL1152`, linked to projects `Gp0322181` and `Gp0345650`, and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 8 type-material rows for `NCBITaxon:561989`, covering variants of `ATCC MYA-4108`, `467`, `BISH Rogers 467`, and `YMJ467`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:561989`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1180901` and `NCBITaxon:1180955`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.

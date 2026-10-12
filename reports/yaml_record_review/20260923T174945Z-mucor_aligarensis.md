# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_aligarensis.yaml`
- Taxon: `NCBITaxon:1197866` (`Mucor aligarensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1197866`, label `Mucor aligarensis`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_aligarensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucidula_mucida.yaml ... mucor_alternans.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58305` contains the seeded identifier with reason `attested rule: Mucor aligarensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:269692` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor aligarensis B.S. Mehrotra & B.R. Mehrotra, 1970`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:269692` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4768`, where `NCBITaxon:1197866` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0456309` / `Mucor aligarensis NRRL 3099`, linked to project `Gp0325319`; no native analysis row linked to that project.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found six rows for `NCBITaxon:1197866`: `CBS 993.70` culture-from-type-material aliases plus `ATCC 28928` and `NRRL 3099` type-material aliases.

## Completeness

- Exact StrainInfo has two direct records and 11 deposit rows for `NCBITaxon:1197866`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1197866`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1197866`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `NRRL 3099` appears in NCBI type material and the native GOLD culture collection ID for `Mucor aligarensis NRRL 3099`.

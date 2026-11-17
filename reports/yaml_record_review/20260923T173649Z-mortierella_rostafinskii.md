# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_rostafinskii.yaml`
- Taxon: `NCBITaxon:64566` (`Mortierella rostafinskii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64566`, label `Mortierella rostafinskii`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_rostafinskii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_rishikesha.yaml ... mortierella_sepedonioides.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53094` contains the seeded identifier with reason `attested rule: Mortierella rostafinskii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8188` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella rostafinskii Bref., 1881`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8188` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40338`, where `NCBITaxon:64566` has `organism_count` 3.
- Native GOLD has two exact current-taxid organism rows, `Go0145959` / `Mortierella rostafinskii NRRL 28263` and `Go0583292` / `Mortierella rostafinskii FSU 9844`, linked to three projects; no native analysis row linked to those projects.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found six culture-from-neotype rows for `NCBITaxon:64566`: `ATCC 24025`, `CBS 522.70`, and `SZMC 11249` aliases.

## Completeness

- Exact StrainInfo has two direct records and three deposit rows for `NCBITaxon:64566`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64566`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:64566`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The transformed GOLD aggregate asserts three organisms, while the local native exact current-taxid scan currently exposes two organism JSONL rows.
- `CBS 522.70` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella rostafinskii FSU 9844`.

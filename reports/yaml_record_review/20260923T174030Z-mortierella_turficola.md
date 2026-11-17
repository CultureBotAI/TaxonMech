# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_turficola.yaml`
- Taxon: `NCBITaxon:311241` (`Mortierella turficola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:311241`, label `Mortierella turficola`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_turficola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_sp.yaml ... mortierella_turficola.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55134` contains the seeded identifier with reason `attested rule: Mortierella turficola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:63727` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella turficola Y. Ling, 1930`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:63727` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31417`, where `NCBITaxon:311241` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583288` / `Mortierella turficola FSU 9851`, linked to project `Gp0586877`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:168310-168313` has `CBS 432.76` and `SZMC 11207` culture-from-neotype aliases.

## Completeness

- Exact StrainInfo has seven direct records and eight deposit rows for `NCBITaxon:311241`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:311241`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:311241`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 432.76` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella turficola FSU 9851`.

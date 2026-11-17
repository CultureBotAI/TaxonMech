# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_paraensis.yaml`
- Taxon: `NCBITaxon:979718` (`Mortierella paraensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979718`, label `Mortierella paraensis`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_paraensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_kuhlmanii.yaml ... mortierella_parazychae.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57053` contains the seeded identifier with reason `attested rule: Mortierella paraensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204266` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella paraensis Pfenning & W. Gams, 1993`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204266` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45193`, where `NCBITaxon:979718` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583275` / `Mortierella paraensis FSU 9835`, linked to project `Gp0586864`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:275908-275911` has `SZMC 11272` culture-from-type-material aliases and `CBS 547.89` type-material aliases.

## Completeness

- Exact StrainInfo has three direct records and three deposit rows for `NCBITaxon:979718`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979718`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979718`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 547.89` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella paraensis FSU 9835`.

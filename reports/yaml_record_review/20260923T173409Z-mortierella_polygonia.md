# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_polygonia.yaml`
- Taxon: `NCBITaxon:979731` (`Mortierella polygonia`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979731`, label `Mortierella polygonia`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_polygonia.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_polycephala.yaml ... mortierella_reticulata.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57055` contains the seeded identifier with reason `attested rule: Mortierella polygonia, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204268` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella polygonia W. Gams & Veenb.-Rijks, 1976`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204268` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45196`, where `NCBITaxon:979731` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0145957` / `Mortierella polygonia AM948` and `Go0583262` / `Mortierella polygonia FSU 11382`, linked to projects `Gp0154318` and `Gp0586851`; no native analysis row linked to either project.
- `data/raw/ncbi_type_material.tsv:275914-275917` has `SZMC 11203` culture-from-type-material aliases and `CBS 685.71` type-material aliases.

## Completeness

- Exact StrainInfo has two direct records and two deposit rows for `NCBITaxon:979731`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979731`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979731`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 685.71` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella polygonia FSU 11382`.

# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_microzygospora.yaml`
- Taxon: `NCBITaxon:979714` (`Mortierella microzygospora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979714`, label `Mortierella microzygospora`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_microzygospora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_kuhlmanii.yaml ... mortierella_parazychae.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57051` contains the seeded identifier with reason `attested rule: Mortierella microzygospora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204264` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella microzygospora Degawa, 1998`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204264` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45191`, where `NCBITaxon:979714` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583268` / `Mortierella microzygospora FSU 11214`, linked to project `Gp0586857`; no native analysis row linked to that project.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found six rows for `NCBITaxon:979714`: `DM 015` and `SZMC 11248` culture-from-type-material aliases plus `CBS 880.97` type-material aliases.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:979714`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979714`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979714`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 880.97` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella microzygospora FSU 11214`.

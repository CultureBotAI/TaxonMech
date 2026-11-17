# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_zonata.yaml`
- Taxon: `NCBITaxon:979764` (`Mortierella zonata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979764`, label `Mortierella zonata`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_zonata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_umbellata.yaml ... mrakia_blollopis.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57061` contains the seeded identifier with reason `attested rule: Mortierella zonata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204278` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella zonata Linnem., 1936`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204278` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45203`, where `NCBITaxon:979764` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583295` / `Mortierella zonata FSU 9863`, linked to project `Gp0586884`; no native analysis row linked to that project.
- A complete exact `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found seven rows for `NCBITaxon:979764`: `SZMC 11228` culture-from-type-material aliases plus `CBS 228.35`, `VKM F-1409`, `VKM:F-1409`, and `VKM:F:1409` type-material aliases.

## Completeness

- Exact StrainInfo has four direct records and six deposit rows for `NCBITaxon:979764`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979764`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979764`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 228.35` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella zonata FSU 9863`.

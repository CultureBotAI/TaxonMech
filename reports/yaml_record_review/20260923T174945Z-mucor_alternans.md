# YAML Record Review

- Target: `data/taxa/eukaryota/mucor_alternans.yaml`
- Taxon: `NCBITaxon:2572688` (`Mucor alternans`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2572688`, label `Mucor alternans`.
- It is grounded exactly under `NCBITaxon:4830` (`Mucor`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mucor`.

## Validation

- `just validate data/taxa/eukaryota/mucor_alternans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mucidula_mucida.yaml ... mucor_alternans.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62840` contains the seeded identifier with reason `attested rule: Mucor alternans, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:532250` matches the YAML identity: parent `NCBITaxon:4830`, rank `SPECIES`, no exact synonyms, and related synonym `Mucor alternans Tiegh., 1876`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:532250` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23477`, where `NCBITaxon:2572688` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows, `Go0470806`, `Go0470807`, and `Go0527550`, linked to three projects; no native analysis row linked to those projects.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:2572688` type-material rows.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:2572688`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2572688`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:2572688`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The native GOLD rows are three separate resequencing projects for NRRL strains `A-15142`, `A-16397`, and `3358`.

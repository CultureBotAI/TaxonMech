# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_umbellata.yaml`
- Taxon: `NCBITaxon:64570` (`Mortierella umbellata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64570`, label `Mortierella umbellata`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_umbellata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_umbellata.yaml ... mrakia_blollopis.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53097` contains the seeded identifier with reason `attested rule: Mortierella umbellata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8191` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, exact synonym `Hydrophora umbellata`, and related synonym `Hydrophora umbellata Bonord., 1870`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8191` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40341`, where `NCBITaxon:64570` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0145963` / `Mortierella umbellata NRRL 5217`, linked to project `Gp0154324`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:64570` type-material rows.

## Completeness

- Exact StrainInfo has eight direct records and 23 deposit rows for `NCBITaxon:64570`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64570`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:64570`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The bounded scan fully covered the native GOLD evidence for this target.

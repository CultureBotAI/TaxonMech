# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_thaxteri.yaml`
- Taxon: `NCBITaxon:1896172` (`Mortierella thaxteri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1896172`, label `Mortierella thaxteri`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_thaxteri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_sp.yaml ... mortierella_turficola.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61483` contains the seeded identifier with reason `attested rule: Mortierella thaxteri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:491449` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella thaxteri Bjorl., 1936`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:491449` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:17105`, where `NCBITaxon:1896172` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0145902` / `Mortierella thaxteri NRRL 25716`, linked to project `Gp0154262`; no native analysis row linked to that project.
- A complete `rg --no-ignore --hidden` scan of `data/raw/ncbi_type_material.tsv` found no `NCBITaxon:1896172` type-material rows.

## Completeness

- Exact StrainInfo had no direct records or deposit rows for `NCBITaxon:1896172`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:1896172`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:1896172`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strain rows for `Mortierella thaxteri NRRL 25716`.

## Additional Notes

- The bounded scan fully covered the native GOLD evidence for this target.

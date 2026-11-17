# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_wuyishanensis.yaml`
- Taxon: `NCBITaxon:979763` (`Mortierella wuyishanensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979763`, label `Mortierella wuyishanensis`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_wuyishanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_umbellata.yaml ... mrakia_blollopis.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57060` contains the seeded identifier with reason `attested rule: Mortierella wuyishanensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204277` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella wuyishanensis F.J. Chen, 1992`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204277` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45202`, where `NCBITaxon:979763` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583260` / `Mortierella wuyishanensis FSU 9795`, linked to project `Gp0586849`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:275944-275947` has `AS Mo 185` and `CBS 370.95` type-material aliases.

## Completeness

- Exact StrainInfo had no direct records or deposit rows for `NCBITaxon:979763`.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979763`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979763`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if future curation materializes local strain rows for `Mortierella wuyishanensis FSU 9795`.

## Additional Notes

- `CBS 370.95` appears in NCBI type material and the native GOLD culture collection ID for `Mortierella wuyishanensis FSU 9795`.

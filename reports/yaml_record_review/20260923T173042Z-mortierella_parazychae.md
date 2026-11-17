# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_parazychae.yaml`
- Taxon: `NCBITaxon:979724` (`Mortierella parazychae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979724`, label `Mortierella parazychae`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_parazychae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_kuhlmanii.yaml ... mortierella_parazychae.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57054` contains the seeded identifier with reason `attested rule: Mortierella parazychae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204267` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella parazychae W. Gams, 1976`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204267` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45195`, where `NCBITaxon:979724` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583264` / `Mortierella parazychae FSU 9836`, linked to project `Gp0586853`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:275912-275913` has `CBS 868.71` type-material aliases.

## Completeness

- Exact StrainInfo has one direct record and one deposit row for `NCBITaxon:979724`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:979724`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:979724`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- `CBS 868.71` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella parazychae FSU 9836`.

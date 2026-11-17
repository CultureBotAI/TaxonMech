# YAML Record Review

- Target: `data/taxa/eukaryota/myriangium_duriaei.yaml`
- Taxon: `NCBITaxon:147570` (`Myriangium duriaei`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:147570`, label `Myriangium duriaei`.
- It is grounded exactly under `NCBITaxon:147569` (`Myriangium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Myriangium`.

## Validation

- `just validate data/taxa/eukaryota/myriangium_duriaei.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycotypha_africana.yaml data/taxa/eukaryota/mycotypha_indica.yaml data/taxa/eukaryota/mycotypha_microspora.yaml data/taxa/eukaryota/myriangium_duriaei.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54050` contains the seeded identifier with reason `attested rule: Myriangium duriaei, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:30120` matches the YAML identity: parent `NCBITaxon:147569`, rank `SPECIES`, and related synonym `Myriangium duriaei Montagne & Berkeley, 1845`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:30120` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:11407`, where `NCBITaxon:147570` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0019337` / `Myriangium duriaei CBS 260.36`, linked to projects `Gp0019273` and `Gp0019337` and one native analysis for `Myriangium duriaei CBS 260.36`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:147570`.
- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:147570`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:147570`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 1 side-inventory old ID merged into `NCBITaxon:147570`: `NCBITaxon:2082080`.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows for that old ID in `data/raw/ncbitaxon_taxa.tsv`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.

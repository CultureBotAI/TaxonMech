# YAML Record Review

- Target: `data/taxa/eukaryota/mycotypha_africana.yaml`
- Taxon: `NCBITaxon:64632` (`Mycotypha africana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64632`, label `Mycotypha africana`.
- It is grounded exactly under `NCBITaxon:64629` (`Mycotypha`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mycotypha`.

## Validation

- `just validate data/taxa/eukaryota/mycotypha_africana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycotypha_africana.yaml data/taxa/eukaryota/mycotypha_indica.yaml data/taxa/eukaryota/mycotypha_microspora.yaml data/taxa/eukaryota/myriangium_duriaei.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53106` contains the seeded identifier with reason `attested rule: Mycotypha africana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8205` matches the YAML identity: parent `NCBITaxon:64629`, rank `SPECIES`, and related synonym `Mycotypha africana R.O. Novak & Backus, 1963`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8205` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40358`, where `NCBITaxon:64632` has `organism_count` 8.
- Native GOLD has 8 exact current-taxid organism rows, 3 linked projects for `Go0118597`, and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 isotype rows for `NCBITaxon:64632`, both designations of `CBS 122.64`.
- Exact StrainInfo has 2 direct records and 14 deposit rows for `NCBITaxon:64632`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64632`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:64632`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- Native GOLD carries organism rows without linked projects for several exact `NCBITaxon:64632` organism IDs.

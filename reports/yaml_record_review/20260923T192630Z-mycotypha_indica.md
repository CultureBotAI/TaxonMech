# YAML Record Review

- Target: `data/taxa/eukaryota/mycotypha_indica.yaml`
- Taxon: `NCBITaxon:2053761` (`Mycotypha indica`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2053761`, label `Mycotypha indica`.
- It is grounded exactly under `NCBITaxon:64629` (`Mycotypha`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mycotypha`.

## Validation

- `just validate data/taxa/eukaryota/mycotypha_indica.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycotypha_africana.yaml data/taxa/eukaryota/mycotypha_indica.yaml data/taxa/eukaryota/mycotypha_microspora.yaml data/taxa/eukaryota/myriangium_duriaei.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62228` contains the seeded identifier with reason `attested rule: Mycotypha indica, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:514199` matches the YAML identity: parent `NCBITaxon:64629`, rank `SPECIES`, and related synonym `Mycotypha indica P.M. Kirk & Benny, 1985`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:514199` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19597`, where `NCBITaxon:2053761` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0401143` / `Mycotypha indica IMI 211999`, linked to projects `Gp0266131` and `Gp0435874` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:2053761`, both designations of `CBS 245.84`.
- Exact StrainInfo has 2 direct records and 7 deposit rows for `NCBITaxon:2053761`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:2053761`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:2053761`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

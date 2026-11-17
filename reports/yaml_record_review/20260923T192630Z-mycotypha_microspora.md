# YAML Record Review

- Target: `data/taxa/eukaryota/mycotypha_microspora.yaml`
- Taxon: `NCBITaxon:64633` (`Mycotypha microspora`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64633`, label `Mycotypha microspora`.
- It is grounded exactly under `NCBITaxon:64629` (`Mycotypha`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Mycotypha`.

## Validation

- `just validate data/taxa/eukaryota/mycotypha_microspora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycotypha_africana.yaml data/taxa/eukaryota/mycotypha_indica.yaml data/taxa/eukaryota/mycotypha_microspora.yaml data/taxa/eukaryota/myriangium_duriaei.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53107` contains the seeded identifier with reason `attested rule: Mycotypha microspora, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8206` matches the YAML identity: parent `NCBITaxon:64629`, rank `SPECIES`, and related synonym `Mycotypha microspora Fenner, 1932`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8206` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40359`, where `NCBITaxon:64633` has `organism_count` 4.
- Native GOLD has 4 exact current-taxid organism rows, 4 linked projects, and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for `NCBITaxon:64633`: 2 culture-from-type-material rows for `CBS 230.32`, 2 type-material rows for `ATCC 8982`, and 2 type-material rows for `IMI 139109`.
- Exact StrainInfo has 32 direct records and 35 deposit rows for `NCBITaxon:64633`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64633`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:64633`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_frontalis.yaml`
- Taxon: `NCBITaxon:4757` (`Neocallimastix frontalis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:4757`, label `Neocallimastix frontalis`.
- It is grounded exactly under `NCBITaxon:4756` (`Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_frontalis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_californiae.yaml data/taxa/eukaryota/neocallimastix_cameroonii.yaml data/taxa/eukaryota/neocallimastix_frontalis.yaml data/taxa/eukaryota/neocallimastix_lanati_nom_inval.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51838` contains the seeded identifier with reason `attested rule: Neocallimastix frontalis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2042` matches the YAML identity: parent `NCBITaxon:4756`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2042` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36561`, where `NCBITaxon:4757` has `organism_count` 9.
- Native GOLD has three exact current-taxid organism rows: `Go0496740` / `Neocallimastix frontalis var. stellae WI-3`, `Go0511068` / `Neocallimastix frontalis var. giraffae Gf-Ma`, and `Go0703559` / `Neocallimastix frontalis CoB3`.
- Those native organism IDs link to 160 complete project rows; the complete native GOLD analysis join found no rows for the linked projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:4757`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:4757`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:73817`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.

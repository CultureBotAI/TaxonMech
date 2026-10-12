# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_californiae.yaml`
- Taxon: `NCBITaxon:1754190` (`Neocallimastix californiae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1754190`, label `Neocallimastix californiae`.
- It is grounded exactly under `NCBITaxon:4756` (`Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_californiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_californiae.yaml data/taxa/eukaryota/neocallimastix_cameroonii.yaml data/taxa/eukaryota/neocallimastix_frontalis.yaml data/taxa/eukaryota/neocallimastix_lanati_nom_inval.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61198` contains the seeded identifier with reason `attested rule: Neocallimastix californiae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:457972` matches the YAML identity: parent `NCBITaxon:4756`, rank `SPECIES`, three related synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:457972` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15252`, where `NCBITaxon:1754190` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0050838` and `Go0050839`, both for `Neocallimastix californiae G1`.
- Those native organism IDs link to 99 complete project rows; the complete native GOLD analysis join found 2 analysis rows, both linked by `AP PROJECT GOLD IDS` to `Gp0050838`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 3 type-material rows for `NCBITaxon:1754190`, covering holotype `JMRC:SF:12176` and `G1` variants.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1754190`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:1550276`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.

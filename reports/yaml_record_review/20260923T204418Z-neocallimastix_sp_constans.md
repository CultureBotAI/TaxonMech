# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_sp_constans.yaml`
- Taxon: `NCBITaxon:3108450` (`Neocallimastix sp. 'constans'`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3108450`, label `Neocallimastix sp. 'constans'`.
- It is grounded exactly under `NCBITaxon:2628446` (`unclassified Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `unclassified Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_sp_constans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_patriciarum.yaml data/taxa/eukaryota/neocallimastix_sp.yaml data/taxa/eukaryota/neocallimastix_sp_constans.yaml data/taxa/eukaryota/neocamarosporium_betae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63555` contains the seeded identifier with reason `attested rule: Neocallimastix sp. 'constans', 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:599783` matches the YAML identity: parent `NCBITaxon:2628446`, rank `SPECIES`, no NCBI synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:599783` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31363`, where `NCBITaxon:3108450` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0579240` / `Neocallimastix constans G3`.
- That native organism ID links to 17 complete project rows; the complete native GOLD analysis join found no rows for the linked projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:3108450`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:3108450`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:3108450`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon.

## Additional Notes

- None.

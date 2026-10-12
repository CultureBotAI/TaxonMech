# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_patriciarum.yaml`
- Taxon: `NCBITaxon:4758` (`Neocallimastix patriciarum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:4758`, label `Neocallimastix patriciarum`.
- It is grounded exactly under `NCBITaxon:4756` (`Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_patriciarum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_patriciarum.yaml data/taxa/eukaryota/neocallimastix_sp.yaml data/taxa/eukaryota/neocallimastix_sp_constans.yaml data/taxa/eukaryota/neocamarosporium_betae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:51839` contains the seeded identifier with reason `attested rule: Neocallimastix patriciarum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2043` matches the YAML identity: parent `NCBITaxon:4756`, rank `SPECIES`, one related synonym, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2043` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36564`, where `NCBITaxon:4758` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0021087` / `Neocallimastix patriciarum 27`.
- That native organism ID links to project `Gp0021087`; no native GOLD analysis rows were found for the linked project.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:4758`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:4758`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:4758`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon.

## Additional Notes

- None.

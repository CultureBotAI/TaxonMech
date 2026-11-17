# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_cameroonii.yaml`
- Taxon: `NCBITaxon:1764037` (`Neocallimastix cameroonii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1764037`, label `Neocallimastix cameroonii`.
- It is grounded exactly under `NCBITaxon:4756` (`Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_cameroonii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_californiae.yaml data/taxa/eukaryota/neocallimastix_cameroonii.yaml data/taxa/eukaryota/neocallimastix_frontalis.yaml data/taxa/eukaryota/neocallimastix_lanati_nom_inval.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61230` contains the seeded identifier with reason `attested rule: Neocallimastix cameroonii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:461083` matches the YAML identity: parent `NCBITaxon:4756`, rank `SPECIES`, one related synonym, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:461083` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15371`, where `NCBITaxon:1764037` has `organism_count` 1.
- A complete scan of the local native GOLD `organisms`, `projects`, and `analyses` snapshots found no exact current-taxid organism rows for `NCBITaxon:1764037`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 1 type-material row for `NCBITaxon:1764037`, holotype `ABS CaDo3a`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1764037`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1764037`.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories, or if native GOLD rows for this exact current Taxon ID are restored locally.

## Additional Notes

- None.

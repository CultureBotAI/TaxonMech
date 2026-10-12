# YAML Record Review

- Target: `data/taxa/eukaryota/neocallimastix_sp.yaml`
- Taxon: `NCBITaxon:2230904` (`Neocallimastix sp.`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2230904`, label `Neocallimastix sp.`.
- It is grounded exactly under `NCBITaxon:2628446` (`unclassified Neocallimastix`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `unclassified Neocallimastix`.

## Validation

- `just validate data/taxa/eukaryota/neocallimastix_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocallimastix_patriciarum.yaml data/taxa/eukaryota/neocallimastix_sp.yaml data/taxa/eukaryota/neocallimastix_sp_constans.yaml data/taxa/eukaryota/neocamarosporium_betae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62495` contains the seeded identifier with reason `attested rule: Neocallimastix sp., 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:521910` matches the YAML identity: parent `NCBITaxon:2628446`, rank `SPECIES`, no NCBI synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:521910` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:21107`, where `NCBITaxon:2230904` has `organism_count` 1.
- A complete scan of the local native GOLD `organisms`, `projects`, and `analyses` snapshots found no exact current-taxid organism rows for `NCBITaxon:2230904`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:2230904`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:2230904`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:2230904`.
- The record has no generated local strain rows, and the checked side inventories do not contradict `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains for this taxon, or if native GOLD rows for this exact current Taxon ID are restored locally.

## Additional Notes

- None.

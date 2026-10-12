# YAML Record Review

- Target: `data/taxa/eukaryota/nemania_maritima.yaml`
- Taxon: `NCBITaxon:389662` (`Nemania maritima`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:389662`, label `Nemania maritima`.
- It is grounded exactly under `NCBITaxon:109374` (`Nemania`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nemania`.

## Validation

- `just validate data/taxa/eukaryota/nemania_maritima.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nemania_diffusa.yaml data/taxa/eukaryota/nemania_maritima.yaml data/taxa/eukaryota/nemania_serpens.yaml data/taxa/eukaryota/nematocida_ausubeli.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55468` contains the seeded identifier with reason `attested rule: Nemania maritima, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:82356` matches the YAML identity: parent `NCBITaxon:109374`, rank `SPECIES`, related synonym `Nemania maritima Y.M. Ju & J.D. Rogers, 2002`, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:82356` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:34070`, where `NCBITaxon:389662` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0498748` / `Nemania maritima AZJU`, linked to project `Gp0382960` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 3 type-material rows for `NCBITaxon:389662`, covering variants of `BCRC 33711` and `CCRC 33711`.
- Exact StrainInfo side inventory has 2 direct rows and 4 deposit entries for `NCBITaxon:389662`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows redirecting old IDs into `NCBITaxon:389662`, matching the absent `replaces` list.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/neodevriesia_sardiniae.yaml`
- Taxon: `NCBITaxon:1690599` (`Neodevriesia sardiniae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1690599`, label `Neodevriesia sardiniae`.
- It is grounded exactly under `NCBITaxon:1508290` (`Neodevriesia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Neodevriesia`.

## Validation

- `just validate data/taxa/eukaryota/neodevriesia_sardiniae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neoconidiobolus_thromboides_fsu_785.yaml data/taxa/eukaryota/neocucurbitaria_cava.yaml data/taxa/eukaryota/neodevriesia_sardiniae.yaml data/taxa/eukaryota/neofusicoccum_brasiliense.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61024` contains the seeded identifier with reason `attested rule: Neodevriesia sardiniae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:441158` matches the YAML identity: parent `NCBITaxon:1508290`, rank `SPECIES`, five synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:441158` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14596`, where `NCBITaxon:1690599` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0583380` / `Neodevriesia sardiniae CCFEE 6202`.
- That native organism ID links to project `Gp0587343`; no native GOLD analysis rows were found for the linked project.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for `NCBITaxon:1690599`, covering variants of `CBS 139724` and `CCFEE 6202`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:1690599`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:1690599`.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.

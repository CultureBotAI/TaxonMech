# YAML Record Review

- Target: `data/taxa/eukaryota/neoconidiobolus_osmodes.yaml`
- Taxon: `NCBITaxon:181044` (`Neoconidiobolus osmodes`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:181044`, label `Neoconidiobolus osmodes`.
- It is grounded exactly under `NCBITaxon:2878373` (`Neoconidiobolus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neoconidiobolus`.

## Validation

- `just validate data/taxa/eukaryota/neoconidiobolus_osmodes.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocatenulostroma_sp.yaml data/taxa/eukaryota/neoconidiobolus_osmodes.yaml data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml data/taxa/eukaryota/neoconidiobolus_thromboides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54345` contains the seeded identifier with reason `attested rule: Neoconidiobolus osmodes, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:36345` matches the YAML identity: parent `NCBITaxon:2878373`, rank `SPECIES`, three synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:36345` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:15993`, where `NCBITaxon:181044` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0402585` / `Conidiobolus osmodes ARSEF 79`.
- That native organism ID links to project `Gp0290210`; no native GOLD analysis rows were found for the linked project.

## Completeness

- An exact field scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for `NCBITaxon:181044`, covering variants of `ARSEF 447`, `ATCC 12590`, and `CBS 155.56`.
- Exact StrainInfo side inventory found 12 direct records and 13 exact deposit assertions, including `CBS 155.56`, `ATCC 12590`, `IMI 313580`, `ATCC 34292`, and `ATCC 38865`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no old IDs merged into `NCBITaxon:181044`.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:181044`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/neoconidiobolus_thromboides.yaml`
- Taxon: `NCBITaxon:76012` (`Neoconidiobolus thromboides`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:76012`, label `Neoconidiobolus thromboides`.
- It is grounded exactly under `NCBITaxon:2878373` (`Neoconidiobolus`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Neoconidiobolus`.

## Validation

- `just validate data/taxa/eukaryota/neoconidiobolus_thromboides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/neocatenulostroma_sp.yaml data/taxa/eukaryota/neoconidiobolus_osmodes.yaml data/taxa/eukaryota/neoconidiobolus_stromoideus.yaml data/taxa/eukaryota/neoconidiobolus_thromboides.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53288` contains the seeded identifier with reason `attested rule: Neoconidiobolus thromboides, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10893` matches the YAML identity: parent `NCBITaxon:2878373`, rank `SPECIES`, five synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10893` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42456`, where `NCBITaxon:76012` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows: `Go0402576` / `Conidiobolus thromboides ARSEF 4968` and `Go0452984` / `Conidiobolus thromboides NRRL 1224`.
- Those native organism IDs link to projects `Gp0290201` and `Gp0317609`; no native GOLD analysis rows were found for the linked projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 7 type-material rows for `NCBITaxon:76012`, covering variants of `ATCC 12587`, `CBS 159.56`, and `VKM F-2529`.
- Exact StrainInfo side inventory found 10 direct records and 16 exact deposit assertions, including `DSM 1221`, `CBS 159.56`, `ATCC 12587`, `VKM F-2529`, and `VKM F-1929`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:1225264`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, and all checked auxiliary source rows were empty for `NCBITaxon:76012`; the exact StrainInfo and type-material side inventories did not materialize local strain rows.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.

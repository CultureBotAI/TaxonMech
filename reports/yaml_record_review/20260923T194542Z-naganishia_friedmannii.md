# YAML Record Review

- Target: `data/taxa/eukaryota/naganishia_friedmannii.yaml`
- Taxon: `NCBITaxon:89922` (`Naganishia friedmannii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:89922`, label `Naganishia friedmannii`.
- It is grounded exactly under `NCBITaxon:1851509` (`Naganishia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naganishia`.

## Validation

- `just validate data/taxa/eukaryota/naganishia_friedmannii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naegleria_lovaniensis.yaml data/taxa/eukaryota/naematelia_encephala.yaml data/taxa/eukaryota/naganishia_albida.yaml data/taxa/eukaryota/naganishia_friedmannii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53482` contains the seeded identifier with reason `attested rule: Naganishia friedmannii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14428` matches the YAML identity: parent `NCBITaxon:1851509`, rank `SPECIES`, exact synonym `Cryptococcus friedmannii`, and two related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14428` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44073`, where `NCBITaxon:89922` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0588226` / `Naganishia friedmannii 6030m`, linked to 60 transcriptome projects from `Gp0597085` through `Gp0597144`; the complete exact native analysis scan found no matching rows.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 9 rows for `NCBITaxon:89922`, under synonym name `Cryptococcus friedmannii` and covering `CBS 7160`, `ATCC 56687`, `JCM 9426`, and `NRRL Y-17371` variants.
- Exact StrainInfo side inventory has 11 direct rows and 17 deposit entries for `NCBITaxon:89922`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old ID `NCBITaxon:2203763`; it was not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_glabratus.yaml`
- Taxon: `NCBITaxon:5478` (`Nakaseomyces glabratus`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5478`, label `Nakaseomyces glabratus`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_glabratus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_delphensis.yaml data/taxa/eukaryota/nakaseomyces_glabratus.yaml data/taxa/eukaryota/nakaseomyces_glabratus_cab52_4041.yaml data/taxa/eukaryota/nakaseomyces_glabratus_cctcc_m202019.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52005` contains the seeded identifier with reason `attested rule: Nakaseomyces glabratus, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2428` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, three exact synonyms, and three related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2428` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38486`, where `NCBITaxon:5478` has `organism_count` 32.
- A complete exact native GOLD rescan found 29 organism rows keyed to `NCBITaxon:5478`, 29 linked projects, and 21 native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 23 type-material rows for `NCBITaxon:5478`, under synonym name `Cryptococcus glabratus`.
- Exact StrainInfo side inventory has 647 direct rows and 709 deposit entries for `NCBITaxon:5478`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:5478`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- The YAML correctly files only records directly under `NCBITaxon:5478`; descendant strain taxa are not gathered into this species record.

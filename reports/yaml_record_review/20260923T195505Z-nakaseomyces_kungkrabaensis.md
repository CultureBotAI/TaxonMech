# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_kungkrabaensis.yaml`
- Taxon: `NCBITaxon:644822` (`Nakaseomyces kungkrabaensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:644822`, label `Nakaseomyces kungkrabaensis`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_kungkrabaensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_glabratus_m202019.yaml data/taxa/eukaryota/nakaseomyces_glabratus_uob301.yaml data/taxa/eukaryota/nakaseomyces_kungkrabaensis.yaml data/taxa/eukaryota/nakaseomyces_nivariensis.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56223` contains the seeded identifier with reason `attested rule: Nakaseomyces kungkrabaensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:148848` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, exact synonym `Candida kungkrabaensis`, and three related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:148848` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40300`, where `NCBITaxon:644822` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0704978` / `Nakaseomyces kungkrabaensis CBS 10927`, linked to project `Gp0830995` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 10 type-material rows for `NCBITaxon:644822`, covering variants of `BCC 23060`, `CBS 10927`, `EM 40`, and `NBRC 102179`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:644822`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:644822`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.

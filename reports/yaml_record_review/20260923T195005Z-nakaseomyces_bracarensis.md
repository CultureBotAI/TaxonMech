# YAML Record Review

- Target: `data/taxa/eukaryota/nakaseomyces_bracarensis.yaml`
- Taxon: `NCBITaxon:273131` (`Nakaseomyces bracarensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:273131`, label `Nakaseomyces bracarensis`.
- It is grounded exactly under `NCBITaxon:374468` (`Nakaseomyces`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nakaseomyces`.

## Validation

- `just validate data/taxa/eukaryota/nakaseomyces_bracarensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naganishia_vishniacii.yaml data/taxa/eukaryota/naganishia_vishniacii_ant03_052.yaml data/taxa/eukaryota/nakaseomyces_bracarensis.yaml data/taxa/eukaryota/nakaseomyces_bracarensis_cbs_10154.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54927` contains the seeded identifier with reason `attested rule: Nakaseomyces bracarensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:56295` matches the YAML identity: parent `NCBITaxon:374468`, rank `SPECIES`, 2 exact synonyms, and 2 related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:56295` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25449`, where `NCBITaxon:273131` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705536` / `Nakaseomyces bracarensis NRRL Y-48270`, linked to project `Gp0831579` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 14 culture-from-holotype or holotype rows for `NCBITaxon:273131`, under synonym name `Candida bracarensis`.
- Exact StrainInfo side inventory has 5 direct rows and 6 deposit entries for `NCBITaxon:273131`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:273131`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- The YAML correctly files only records directly under `NCBITaxon:273131`; descendant taxa, including `NCBITaxon:1279114`, are not gathered into this species record.

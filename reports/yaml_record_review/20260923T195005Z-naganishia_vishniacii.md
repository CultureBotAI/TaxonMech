# YAML Record Review

- Target: `data/taxa/eukaryota/naganishia_vishniacii.yaml`
- Taxon: `NCBITaxon:89929` (`Naganishia vishniacii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:89929`, label `Naganishia vishniacii`.
- It is grounded exactly under `NCBITaxon:1851509` (`Naganishia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naganishia`.

## Validation

- `just validate data/taxa/eukaryota/naganishia_vishniacii.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/naganishia_vishniacii.yaml data/taxa/eukaryota/naganishia_vishniacii_ant03_052.yaml data/taxa/eukaryota/nakaseomyces_bracarensis.yaml data/taxa/eukaryota/nakaseomyces_bracarensis_cbs_10154.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53485` contains the seeded identifier with reason `attested rule: Naganishia vishniacii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:14431` matches the YAML identity: parent `NCBITaxon:1851509`, rank `SPECIES`, 3 exact synonyms, and 4 related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:14431` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:44076`, where `NCBITaxon:89929` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0022517` / `Naganishia vishniacii ANT03-052`, linked to projects `Gp0022469` and `Gp0022517`; the single native analysis links through `Gp0022517`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 32 rows for `NCBITaxon:89929`, under `Cryptococcus consortionis`, `Cryptococcus socialis`, and `Cryptococcus vishniacii`.
- Exact StrainInfo side inventory has 13 direct rows and 36 deposit entries for `NCBITaxon:89929`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:104413` and `NCBITaxon:104671`; neither was retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if either side-inventory merged ID becomes a retained retired row.

## Additional Notes

- The YAML correctly files only records directly under `NCBITaxon:89929`; descendant taxa, including `NCBITaxon:1314774`, are not gathered into this species record.

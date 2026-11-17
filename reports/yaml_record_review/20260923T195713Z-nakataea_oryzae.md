# YAML Record Review

- Target: `data/taxa/eukaryota/nakataea_oryzae.yaml`
- Taxon: `NCBITaxon:165778` (`Nakataea oryzae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:165778`, label `Nakataea oryzae`.
- It is grounded exactly under `NCBITaxon:228882` (`Nakataea`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nakataea`.

## Validation

- `just validate data/taxa/eukaryota/nakataea_oryzae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakaseomyces_nivariensis_cbs_9983.yaml data/taxa/eukaryota/nakaseomyces_uthaithaninus.yaml data/taxa/eukaryota/nakataea_oryzae.yaml data/taxa/eukaryota/nakazawaea_anatomiae.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54226` contains the seeded identifier with reason `attested rule: Nakataea oryzae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:33963` matches the YAML identity: parent `NCBITaxon:228882`, rank `SPECIES`, 8 exact synonyms, and 5 related synonyms.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:33963` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:14269`, where `NCBITaxon:165778` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0449003` / `Nakataea oryzae M69`, linked to project `Gp0313395` and one native analysis.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 holotype rows for `NCBITaxon:165778`, under synonym name `Sclerotium oryzae`.
- Exact StrainInfo side inventory has 22 direct rows and 27 deposit entries for `NCBITaxon:165778`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1930697` and `NCBITaxon:54966`; neither was retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if either side-inventory merged ID becomes a retained retired row.

## Additional Notes

- None.

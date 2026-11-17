# YAML Record Review

- Target: `data/taxa/eukaryota/naumovozyma_dairenensis.yaml`
- Taxon: `NCBITaxon:27289` (`Naumovozyma dairenensis`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:27289`, label `Naumovozyma dairenensis`.
- It is grounded exactly under `NCBITaxon:278028` (`Naumovozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Naumovozyma`.

## Validation

- `just validate data/taxa/eukaryota/naumovozyma_dairenensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naumovozyma_castellii.yaml data/taxa/eukaryota/naumovozyma_dairenensis.yaml data/taxa/eukaryota/navicula_arenaria.yaml data/taxa/eukaryota/necromortierella_dichotoma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52130` contains the seeded identifier with reason `attested rule: Naumovozyma dairenensis, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2706` matches the YAML identity: parent `NCBITaxon:278028`, rank `SPECIES`, exact synonyms `Naumovia dairenensis` and `Saccharomyces dairenensis`, three related synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2706` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25380`, where `NCBITaxon:27289` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0323109` / `Naumovozyma dairenensis 763_NDAI` and `Go0705235` / `Naumovozyma dairenensis NRRL Y-1353`.
- Those two native organism IDs link to projects `Gp0171593` and `Gp0831265`; one native analysis is linked through `AP PROJECT GOLD IDS` to `Gp0171593`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 19 type-material rows for `NCBITaxon:27289`, covering variants of `CBS 421`, `NRRL Y-12639`, `ATCC 10597`, `BCRC 20456`, `CCRC 20456`, `DBVPG 6366`, `IFO 0211`, `NCYC 777`, and `NRRL Y-1353`.
- Exact StrainInfo side inventory has 10 direct rows and 25 deposit entries for `NCBITaxon:27289`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows redirecting old IDs into `NCBITaxon:27289`, matching the absent `replaces` list.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

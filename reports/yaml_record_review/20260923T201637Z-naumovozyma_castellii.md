# YAML Record Review

- Target: `data/taxa/eukaryota/naumovozyma_castellii.yaml`
- Taxon: `NCBITaxon:27288` (`Naumovozyma castellii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:27288`, label `Naumovozyma castellii`.
- It is grounded exactly under `NCBITaxon:278028` (`Naumovozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Naumovozyma`.

## Validation

- `just validate data/taxa/eukaryota/naumovozyma_castellii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naumovozyma_castellii.yaml data/taxa/eukaryota/naumovozyma_dairenensis.yaml data/taxa/eukaryota/navicula_arenaria.yaml data/taxa/eukaryota/necromortierella_dichotoma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52129` contains the seeded identifier with reason `attested rule: Naumovozyma castellii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2705` matches the YAML identity: parent `NCBITaxon:278028`, rank `SPECIES`, two exact synonyms, four related synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2705` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25365`, where `NCBITaxon:27288` has `organism_count` 3.
- The current native GOLD catalogs have one exact organism row, `Go0657902` / `Naumovozyma castellii Y1806`, linked to project `Gp0702170` and one native analysis for the same project.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 19 type-material rows for `NCBITaxon:27288`, covering variants of `AS 2.2404`, `ATCC 76901`, `BCRC 22586`, `CBS 4309`, `CCRC 22586`, `CGMCC 2.2404`, `DBVPG 6298`, `IFO 1992`, `NRRL Y-12630`, and `VKPM Y 1485`.
- Exact StrainInfo side inventory has 16 direct rows and 61 deposit entries for `NCBITaxon:27288`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found side-inventory old IDs `NCBITaxon:1064592`, `NCBITaxon:226301`, and `NCBITaxon:340169`; they were not retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if the side-inventory merged IDs become retained retired rows.

## Additional Notes

- The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and differs from the current native GOLD exact-organism count; the native JSONL rows are side evidence only.

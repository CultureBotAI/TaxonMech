# YAML Record Review

- Target: `data/taxa/eukaryota/nigrospora_oryzae.yaml`
- Taxon: `NCBITaxon:335854` (`Nigrospora oryzae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:335854`, label `Nigrospora oryzae`.
- It is grounded exactly under `NCBITaxon:114230` (`Nigrospora`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nigrospora`.

## Validation

- `just validate data/taxa/eukaryota/nigrospora_oryzae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nigrospora_oryzae.yaml data/taxa/eukaryota/nigrospora_sphaerica.yaml data/taxa/eukaryota/nilaparvata_lugens_yeast_like_symbiont.yaml data/taxa/eukaryota/nitzschia_captiva.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55271` contains the seeded identifier with reason `attested rule: Nigrospora oryzae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:68813` matches the YAML identity: parent `NCBITaxon:114230`, rank `SPECIES`, two exact synonyms, five related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:68813` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:32445`, where `NCBITaxon:335854` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0110145` / `Nigrospora oryzae ATCC 28132`, linked to projects `Gp0110616` and `Gp0113730`; no native analysis rows linked to those projects.

## Completeness

- `data/raw/ncbi_type_material.tsv:180395-180398` has holotype aliases for `IMI 79239` under `Khuskia oryzae` and `IMI 99832` under `Monotospora oryzae`.
- Exact StrainInfo side inventory found 30 direct records and 36 deposit entries, including sampled designations `MUCL 167`, `MUCL 7755`, `MUCL 8364`, `CBS 210.30`, `MUCL 8365`, `CBS 382.50`, and `MUCL 11451`.
- `data/raw/ncbi_merged_ids.tsv` maps side-inventory old IDs `NCBITaxon:1551522`, `NCBITaxon:631443`, and `NCBITaxon:668251` into `NCBITaxon:335854`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` generated `replaces` entries.
- Exact BacDive, generated raw strain rows, generated StrainInfo target rows, retained retired old-ID rows, and checked auxiliary source rows were empty for `NCBITaxon:335854`; the record correctly has `strain_count: 0`.
- The exact NCBI type-material, StrainInfo side-inventory, and native GOLD rows did not materialize local strain rows; strain-genome source linkers join through BacDive-derived local strain identifiers.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact NCBI type-material, StrainInfo, or native GOLD side inventories.

## Additional Notes

- None.

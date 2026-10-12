# YAML Record Review

- Target: `data/taxa/eukaryota/necromortierella_dichotoma.yaml`
- Taxon: `NCBITaxon:979691` (`Necromortierella dichotoma`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:979691`, label `Necromortierella dichotoma`.
- It is grounded exactly under `NCBITaxon:2779938` (`Necromortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Necromortierella`.

## Validation

- `just validate data/taxa/eukaryota/necromortierella_dichotoma.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naumovozyma_castellii.yaml data/taxa/eukaryota/naumovozyma_dairenensis.yaml data/taxa/eukaryota/navicula_arenaria.yaml data/taxa/eukaryota/necromortierella_dichotoma.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57043` contains the seeded identifier with reason `attested rule: Necromortierella dichotoma, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:204252` matches the YAML identity: parent `NCBITaxon:2779938`, rank `SPECIES`, exact synonym `Mortierella dichotoma`, two related synonyms, and genetic code `1`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:204252` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:45182`, where `NCBITaxon:979691` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0368104` / `Necromortierella dichotoma KOD 996` and `Go0583284` / `Necromortierella dichotoma KOD 1036`.
- Those two native organism IDs link to projects `Gp0586846` and `Gp0586873`; no native GOLD analyses are linked to those exact current projects.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 7 type-material rows for `NCBITaxon:979691`, covering variants of `CBS 221.35`, `SZMC 11269`, and `VKM F-1407`.
- Exact StrainInfo side inventory has 1 direct row and 2 deposit entries for `NCBITaxon:979691`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows redirecting old IDs into `NCBITaxon:979691`, matching the absent `replaces` list.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

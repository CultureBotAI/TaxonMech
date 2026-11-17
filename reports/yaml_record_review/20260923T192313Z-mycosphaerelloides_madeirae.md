# YAML Record Review

- Target: `data/taxa/eukaryota/mycosphaerelloides_madeirae.yaml`
- Taxon: `NCBITaxon:1873265` (`Mycosphaerelloides madeirae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1873265`, label `Mycosphaerelloides madeirae`.
- It is grounded exactly under `NCBITaxon:1873264` (`Mycosphaerelloides`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Mycosphaerelloides`.

## Validation

- `just validate data/taxa/eukaryota/mycosphaerelloides_madeirae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycosphaerellaceae_sp.yaml data/taxa/eukaryota/mycosphaerelloides_madeirae.yaml data/taxa/eukaryota/mycothermus_thermophilus.yaml data/taxa/eukaryota/mycothermus_thermophilus_atcc_16453.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:61416` contains the seeded identifier with reason `attested rule: Mycosphaerelloides madeirae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:489449` matches the YAML identity: parent `NCBITaxon:1873264`, rank `SPECIES`, exact synonyms `Mycosphaerella madeirae`, `Mycosphaerella madeirensis`, and `Paramycosphaerella madeirensis`, and six related synonyms.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:489449` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:16833`, where `NCBITaxon:1873265` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0451069` / `Mycosphaerelloides madeirae CBS 112895`, linked to project `Gp0315488` and one native analysis for `Mycosphaerelloides madeirae CBS 112895`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 6 culture-from-type-material rows for `NCBITaxon:1873265`, all designations that include `CBS 112895`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1873265`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 4 side-inventory old IDs merged into `NCBITaxon:1873265`: `NCBITaxon:306881`, `NCBITaxon:318862`, `NCBITaxon:318863`, and `NCBITaxon:318864`.
- The record has no `replaces` entries, which is consistent with the absence of retained retired rows for those old IDs in `data/raw/ncbitaxon_taxa.tsv`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.

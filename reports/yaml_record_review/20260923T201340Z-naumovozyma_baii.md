# YAML Record Review

- Target: `data/taxa/eukaryota/naumovozyma_baii.yaml`
- Taxon: `NCBITaxon:1209964` (`Naumovozyma baii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1209964`, label `Naumovozyma baii`.
- It is grounded exactly under `NCBITaxon:278028` (`Naumovozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Naumovozyma`.

## Validation

- `just validate data/taxa/eukaryota/naumovozyma_baii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nanofrustulum_trainorii.yaml data/taxa/eukaryota/naohidea_sebacea.yaml data/taxa/eukaryota/naohidea_sebacea_cbs_8477.yaml data/taxa/eukaryota/naumovozyma_baii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58410` contains the seeded identifier with reason `attested rule: Naumovozyma baii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:273674` matches the YAML identity: parent `NCBITaxon:278028`, rank `SPECIES`, two related synonyms, and genetic code `1`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:273674` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:4991`, where `NCBITaxon:1209964` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705056` / `Naumovozyma baii CBS 12642`, linked to project `Gp0831076` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for `NCBITaxon:1209964`, covering variants of `CBS 12642`, `CGMCC 2.04520`, and `BW22`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:1209964`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows redirecting old IDs into `NCBITaxon:1209964`, matching the absent `replaces` list.
- The record has no generated local strain rows despite exact type-material side inventory.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact type-material side inventories.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/nemania_serpens.yaml`
- Taxon: `NCBITaxon:109381` (`Nemania serpens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:109381`, label `Nemania serpens`.
- It is grounded exactly under `NCBITaxon:109374` (`Nemania`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Nemania`.

## Validation

- `just validate data/taxa/eukaryota/nemania_serpens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nemania_diffusa.yaml data/taxa/eukaryota/nemania_maritima.yaml data/taxa/eukaryota/nemania_serpens.yaml data/taxa/eukaryota/nematocida_ausubeli.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53741` contains the seeded identifier with reason `attested rule: Nemania serpens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:19681` matches the YAML identity: parent `NCBITaxon:109374`, rank `SPECIES`, exact synonyms `Geniculosporium serpens`, `Hypoxylon serpens`, and `Sphaeria serpens`, 49 related synonyms, and genetic code `1`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:19681` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:1707`, where `NCBITaxon:109381` has `organism_count` 3.
- Native GOLD has three exact current-taxid organism rows: `Go0454022` / `Nemania serpens AZ0576`, `Go0498739` / `Nemania serpens AK0226`, and `Go0498740` / `Nemania serpens CBS 679.86`.
- A complete exact native GOLD project join found 6 projects for those three organism IDs and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 4 neotype rows for `NCBITaxon:109381`, covering variants of `TROM 174`.
- Exact StrainInfo side inventory has 23 direct rows and 25 deposit entries for `NCBITaxon:109381`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 47 side-inventory old IDs redirecting into `NCBITaxon:109381`; none were retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if any side-inventory merged IDs become retained retired rows.

## Additional Notes

- None.

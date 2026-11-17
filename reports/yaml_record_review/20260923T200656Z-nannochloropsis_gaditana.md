# YAML Record Review

- Target: `data/taxa/eukaryota/nannochloropsis_gaditana.yaml`
- Taxon: `NCBITaxon:72520` (`Microchloropsis gaditana`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:72520`, current label `Microchloropsis gaditana`.
- The filename and seed-scope reason use `Nannochloropsis gaditana`, which NCBI now retains as an exact synonym of `NCBITaxon:72520`.
- It is grounded exactly under `NCBITaxon:2511164` (`Microchloropsis`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Microchloropsis`.

## Validation

- `just validate data/taxa/eukaryota/nannochloropsis_gaditana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nakazawaea_siamensis.yaml data/taxa/eukaryota/nakazawaea_wickerhamii.yaml data/taxa/eukaryota/nakazawaea_wyomingensis.yaml data/taxa/eukaryota/nannochloropsis_gaditana.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53242` contains `NCBITaxon:72520` with reason `attested rule: Nannochloropsis gaditana, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10140` matches the YAML identity: parent `NCBITaxon:2511164`, rank `SPECIES`, exact synonyms `Nannochloropsis gaditana` and `Nannochloropsis gaditana CCMP526`, two related synonyms, and genetic code `1`.
- The YAML `replaces` entry `NCBITaxon:1093141` is backed by a retained retired NCBI row at `data/raw/ncbitaxon_taxa.tsv:235163` for former strain `Nannochloropsis gaditana CCMP526`, which has `retired_into` `NCBITaxon:72520`.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10140` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42011`, where `NCBITaxon:72520` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0038531` / `Nannochloropsis gaditana B-31` and `Go0415761` / `Nannochloropsis gaditana CCMP1894`.
- Native GOLD links those two organism IDs to three projects, `Gp0038531`, `Gp0039150`, and `Gp0308854`, each with one analysis row linked by `AP PROJECT GOLD IDS`.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:72520`, covering `SAG 2.99` and `SAG:2.99`.
- Exact StrainInfo side inventory has 7 direct rows and 9 deposit entries for `NCBITaxon:72520`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found `NCBITaxon:1093141` redirected into `NCBITaxon:72520`; the old ID is retained in `ncbitaxon_taxa.tsv`, so the generated `replaces` list is consistent with local retired-ID provenance.
- The GOLD attestation explicitly covers records filed directly under `NCBITaxon:72520`; descendant taxa are not gathered, matching the attestation note.
- The record has no generated local strain rows despite exact StrainInfo and type-material side inventories, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if NCBI adds more retained retired rows that redirect into `NCBITaxon:72520`.

## Additional Notes

- None.

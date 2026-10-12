# YAML Record Review

- Target: `data/taxa/eukaryota/naganishia_albida.yaml`
- Taxon: `NCBITaxon:100951` (`Naganishia albida`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:100951`, label `Naganishia albida`.
- It is grounded exactly under `NCBITaxon:1851509` (`Naganishia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naganishia`.

## Validation

- `just validate data/taxa/eukaryota/naganishia_albida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/naegleria_lovaniensis.yaml data/taxa/eukaryota/naematelia_encephala.yaml data/taxa/eukaryota/naganishia_albida.yaml data/taxa/eukaryota/naganishia_friedmannii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53622` contains the seeded identifier with reason `attested rule: Naganishia albida, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:17351` matches the YAML identity: parent `NCBITaxon:1851509`, rank `SPECIES`, 10 exact synonyms, and 6 related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:17351` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:208`, where `NCBITaxon:100951` has `organism_count` 5.
- Native GOLD has four exact current-taxid organism rows, for `NT2002`, `JCM 2334`, `PT4301`, and `P1801B`, linked to four projects and four native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 48 type-material rows for `NCBITaxon:100951`, under synonym names `Cryptococcus albidus var. ovalis`, `Cryptococcus kuetzingii`, and `Torula albida`.
- Exact StrainInfo side inventory has 162 direct rows and 292 deposit entries for `NCBITaxon:100951`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found 9 side-inventory old IDs now merged into `NCBITaxon:100951`; none were retained in `ncbitaxon_taxa.tsv`, so the absent `replaces` list is consistent with local retired-ID provenance.
- The record has no generated local strain rows despite the large exact StrainInfo side inventory, which is consistent with StrainInfo only overlaying BacDive-derived local strains.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories, or if any side-inventory merged IDs become retained retired rows.

## Additional Notes

- The YAML GOLD assertion count matches transformed `data/raw/gold_organisms.tsv`; the local native GOLD exact scan currently finds four organism rows for this taxon.

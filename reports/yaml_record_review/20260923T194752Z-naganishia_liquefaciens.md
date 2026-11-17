# YAML Record Review

- Target: `data/taxa/eukaryota/naganishia_liquefaciens.yaml`
- Taxon: `NCBITaxon:104408` (`Naganishia liquefaciens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:104408`, label `Naganishia liquefaciens`.
- It is grounded exactly under `NCBITaxon:1851509` (`Naganishia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Naganishia`.

## Validation

- `just validate data/taxa/eukaryota/naganishia_liquefaciens.yaml` exited successfully.
- `just validate-strict data/taxa/eukaryota/naganishia_liquefaciens.yaml data/taxa/eukaryota/naganishia_sp_pg3902_1.yaml data/taxa/eukaryota/naganishia_sp_pt2105a.yaml data/taxa/eukaryota/naganishia_sp_pt2105a_2.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53682` contains the seeded identifier with reason `attested rule: Naganishia liquefaciens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:18663` matches the YAML identity: parent `NCBITaxon:1851509`, rank `SPECIES`, two exact synonyms, and two related synonyms.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:18663` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:648`, where `NCBITaxon:104408` has `organism_count` 2.
- Native GOLD has two exact current-taxid organism rows, `Go0632190` / `Naganishia liquefaciens N6` and `Go0647380` / `Naganishia liquefaciens I2-R1`, linked to two projects and two native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 16 rows for `NCBITaxon:104408`, under synonym name `Torulopsis liquefaciens` and covering `CBS 968`, `ATCC 32060`, `IFO 0434`, `IGC 2861`, `MUCL 30598`, `NRRL Y-1516`, and `VKM Y-744` variants.
- Exact StrainInfo side inventory has 3 direct rows and 7 deposit entries for `NCBITaxon:104408`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:104408`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

# YAML Record Review

- Target: `data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml`
- Taxon: `NCBITaxon:43970` (`Nadsonia starkeyi-henricii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:43970`, label `Nadsonia starkeyi-henricii`.
- It is grounded exactly under `NCBITaxon:45785` (`Nadsonia`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Nadsonia`.

## Validation

- `just validate data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml data/taxa/eukaryota/naegleria_fowleri.yaml data/taxa/eukaryota/naegleria_gruberi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52551` contains the seeded identifier with reason `attested rule: Nadsonia starkeyi-henricii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:5284` matches the YAML identity: parent `NCBITaxon:45785`, rank `SPECIES`, exact synonym `Schizoblastosporion starkeyi-henricii`, and two related synonyms.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:5284` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:35523`, where `NCBITaxon:43970` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705701` / `Nadsonia starkeyi-henricii NRRL YB-3963`, linked to project `Gp0831755` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 5 type-material rows for `NCBITaxon:43970`, under synonym name `Schizoblastosporion starkeyi-henricii` and covering variants of `CBS 2159` and `NRRL YB-3963`.
- Exact StrainInfo side inventory has 14 direct rows and 37 deposit entries for `NCBITaxon:43970`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:43970`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

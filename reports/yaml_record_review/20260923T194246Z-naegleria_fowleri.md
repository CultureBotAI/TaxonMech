# YAML Record Review

- Target: `data/taxa/eukaryota/naegleria_fowleri.yaml`
- Taxon: `NCBITaxon:5763` (`Naegleria fowleri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5763`, label `Naegleria fowleri`.
- It is grounded exactly under `NCBITaxon:5761` (`Naegleria`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 10 lineage entries from `root` through `Naegleria`.

## Validation

- `just validate data/taxa/eukaryota/naegleria_fowleri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/nadsonia_fulvescens_var_elongata_dsm_6958.yaml data/taxa/eukaryota/nadsonia_starkeyi_henricii.yaml data/taxa/eukaryota/naegleria_fowleri.yaml data/taxa/eukaryota/naegleria_gruberi.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52079` contains the seeded identifier with reason `attested rule: Naegleria fowleri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2565` matches the YAML identity: parent `NCBITaxon:5761`, rank `SPECIES`, and two related synonyms.
- All 10 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2565` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39291`, where `NCBITaxon:5763` has `organism_count` 4.
- Native GOLD has four exact current-taxid organism rows: `Go0047971` / `Naegleria fowleri`, `Go0384989` / `Naegleria fowleri ATCC 30863`, `Go0572156` / `Naegleria fowleri ATCC 30894`, and `Go0572210` / `Naegleria fowleri NF_KFSHRC_1`; those rows link to four projects and three native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:5763`.
- Exact StrainInfo side inventory has 27 direct rows and 27 deposit entries for `NCBITaxon:5763`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:5763`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo side inventories.

## Additional Notes

- None.

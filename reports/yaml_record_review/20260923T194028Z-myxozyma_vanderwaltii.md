# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_vanderwaltii.yaml`
- Taxon: `NCBITaxon:54101` (`Myxozyma vanderwaltii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:54101`, label `Myxozyma vanderwaltii`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_vanderwaltii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_udenii.yaml data/taxa/eukaryota/myxozyma_vanderwaltii.yaml data/taxa/eukaryota/nadsonia_commutata.yaml data/taxa/eukaryota/nadsonia_fulvescens.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52915` contains the seeded identifier with reason `attested rule: Myxozyma vanderwaltii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6845` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma vanderwaltii Spaaij, G. Weber & M.T. Sm., 1993`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6845` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38306`, where `NCBITaxon:54101` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705342` / `Myxozyma vanderwaltii NRRL Y-17727`, linked to project `Gp0831378` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 7 rows for `NCBITaxon:54101`: 5 culture-from-holotype variants of `NRRL Y-17727` and 2 holotype variants of `FS-HL-315`.
- Exact StrainInfo side inventory has 3 direct rows and 6 deposit entries for `NCBITaxon:54101`, but exact BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:54101`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

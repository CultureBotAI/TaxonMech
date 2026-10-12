# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_sirexii.yaml`
- Taxon: `NCBITaxon:383840` (`Myxozyma sirexii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:383840`, label `Myxozyma sirexii`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_sirexii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myxozyma_neglecta.yaml data/taxa/eukaryota/myxozyma_neotropica.yaml data/taxa/eukaryota/myxozyma_nipponensis.yaml data/taxa/eukaryota/myxozyma_sirexii.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55455` contains the seeded identifier with reason `attested rule: Myxozyma sirexii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:80595` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma sirexii Spaaij & G. Weber, 1992`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:80595` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33973`, where `NCBITaxon:383840` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705464` / `Myxozyma sirexii NRRL Y-27626`, linked to project `Gp0831507` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:383840`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:383840`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:383840`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains or exact type-material side inventories.

## Additional Notes

- None.

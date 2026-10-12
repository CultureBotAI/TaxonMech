# YAML Record Review

- Target: `data/taxa/eukaryota/mytilinidion_resinicola.yaml`
- Taxon: `NCBITaxon:574789` (`Mytilinidion resinicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:574789`, label `Mytilinidion resinicola`.
- It is grounded exactly under `NCBITaxon:574786` (`Mytilinidion`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 16 lineage entries from `root` through `Mytilinidion`.

## Validation

- `just validate data/taxa/eukaryota/mytilinidion_resinicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myrothecium_sp.yaml data/taxa/eukaryota/mytilinidion_resinicola.yaml data/taxa/eukaryota/myxozyma_geophila.yaml data/taxa/eukaryota/myxozyma_kluyveri.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56086` contains the seeded identifier with reason `attested rule: Mytilinidion resinicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:135743` matches the YAML identity: parent `NCBITaxon:574786`, rank `SPECIES`, exact synonym `Mytilidion resinicola`, and related synonyms `Mytilidion resinicola M.L. Lohman, 1933` and `Mytilinidion resinicola M.L. Lohman, 1933`.
- All 16 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:135743` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39239`, where `NCBITaxon:574789` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0111702` / `Mytilinidion resinicola 304.34`, linked to projects `Gp0113806` and `Gp0238559` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for `NCBITaxon:574789`, both designations of `CBS 304.34`.
- Exact StrainInfo has 1 direct record and 1 deposit row for `NCBITaxon:574789`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:574789`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:574789`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

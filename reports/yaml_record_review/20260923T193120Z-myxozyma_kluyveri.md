# YAML Record Review

- Target: `data/taxa/eukaryota/myxozyma_kluyveri.yaml`
- Taxon: `NCBITaxon:54099` (`Myxozyma kluyveri`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:54099`, label `Myxozyma kluyveri`.
- It is grounded exactly under `NCBITaxon:54096` (`Myxozyma`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 13 lineage entries from `root` through `Myxozyma`.

## Validation

- `just validate data/taxa/eukaryota/myxozyma_kluyveri.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/myrothecium_sp.yaml data/taxa/eukaryota/mytilinidion_resinicola.yaml data/taxa/eukaryota/myxozyma_geophila.yaml data/taxa/eukaryota/myxozyma_kluyveri.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52913` contains the seeded identifier with reason `attested rule: Myxozyma kluyveri, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6843` matches the YAML identity: parent `NCBITaxon:54096`, rank `SPECIES`, and related synonym `Myxozyma kluyveri Van der Walt, Spenc.-Mart., Y. Yamada & P.D.G. Richards, 1989`.
- All 13 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6843` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:38304`, where `NCBITaxon:54099` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0705278` / `Myxozyma kluyveri NRRL Y-17277`, linked to project `Gp0831313` and no native analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found 9 type-material rows for `NCBITaxon:54099`, covering variants of `ATCC 76214`, `CBS 7332`, `JCM 7661`, and `NRRL Y-17277`.
- Exact StrainInfo has 3 direct records and 10 deposit rows for `NCBITaxon:54099`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:54099`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:54099`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from exact StrainInfo or type-material side inventories.

## Additional Notes

- None.

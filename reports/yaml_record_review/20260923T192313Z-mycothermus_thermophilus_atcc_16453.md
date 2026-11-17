# YAML Record Review

- Target: `data/taxa/eukaryota/mycothermus_thermophilus_atcc_16453.yaml`
- Taxon: `NCBITaxon:686564` (`Mycothermus thermophilus ATCC 16453`)
- Verdict: pass

## Target

- The record is the seeded strain `NCBITaxon:686564`, label `Mycothermus thermophilus ATCC 16453`.
- It is grounded exactly under `NCBITaxon:85995` (`Mycothermus thermophilus`) with rank `STRAIN`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 17 lineage entries from `root` through `Mycothermus thermophilus`.

## Validation

- `just validate data/taxa/eukaryota/mycothermus_thermophilus_atcc_16453.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mycosphaerellaceae_sp.yaml data/taxa/eukaryota/mycosphaerelloides_madeirae.yaml data/taxa/eukaryota/mycothermus_thermophilus.yaml data/taxa/eukaryota/mycothermus_thermophilus_atcc_16453.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56394` contains the seeded identifier with reason `attested rule: Mycothermus thermophilus ATCC 16453, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:161309` matches the YAML identity: parent `NCBITaxon:85995`, rank `STRAIN`, and exact synonym `Scytalidium thermophilum ATCC 16453`.
- All 17 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:161309` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41330`, where `NCBITaxon:686564` has `organism_count` 1.
- Native GOLD has one exact current-taxid organism row, `Go0017846` / `Scytalidium thermophilum ATCC 16453`, with no linked native projects or analyses.

## Completeness

- An exact ignored-file-inclusive scan of `data/raw/ncbi_type_material.tsv` found no rows for `NCBITaxon:686564`.
- Exact StrainInfo, BacDive, generated raw strain rows, generated StrainInfo rows, and all checked auxiliary source rows were empty for `NCBITaxon:686564`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no current-ID rows for `NCBITaxon:686564`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strain records for `ATCC 16453`.

## Additional Notes

- Species-level type-material side rows include `ATCC 16453`; there are no exact strain-level type-material rows for `NCBITaxon:686564`.

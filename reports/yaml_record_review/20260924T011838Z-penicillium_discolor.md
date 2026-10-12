# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_discolor.yaml`
- Taxon: `NCBITaxon:74830` (`Penicillium discolor`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:74830`, label `Penicillium discolor`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_discolor.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_dipodomyus.yaml data/taxa/eukaryota/penicillium_discolor.yaml data/taxa/eukaryota/penicillium_doidgeae.yaml data/taxa/eukaryota/penicillium_donkii.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53270` contains the seeded identifier with reason `attested rule: Penicillium discolor, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:10644` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:10644` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:42251`, where `NCBITaxon:74830` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found 1 organism row, 2 project rows, and 0 analysis rows for `NCBITaxon:74830`, all centered on organism `Go0583235` (`Penicillium discolor ITEM 17420`).
- Exact `data/raw/ncbi_type_material.tsv` scanning found 16 rows on lines 261884-261899: 12 `culture-from-holotype` spellings centered on CBS 474.84, IBT 21523, and IBT 5738; and 4 `holotype` spellings centered on IMI 285513.
- Exact StrainInfo side evidence has 25 direct `NCBITaxon:74830` records and 26 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:74830`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- The native GOLD organism is fully accounted for by the generated GOLD aggregate row with `organism_count: 1`; its native projects do not add separate organism assertions.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

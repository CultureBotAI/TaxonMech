# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fructuariae_cellae.yaml`
- Taxon: `NCBITaxon:2819925` (`Penicillium fructuariae-cellae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2819925`, label `Penicillium fructuariae-cellae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fructuariae_cellae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_flaviroseum.yaml data/taxa/eukaryota/penicillium_formosanum.yaml data/taxa/eukaryota/penicillium_freii.yaml data/taxa/eukaryota/penicillium_fructuariae_cellae.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63292` contains the seeded identifier with reason `attested rule: Penicillium fructuariae-cellae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:560369` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:560369` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:27215`, where `NCBITaxon:2819925` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found 1 organism row, 2 project rows, and 0 analysis rows for `NCBITaxon:2819925`, centered on organism `Go0584902` (`Penicillium fructuariae-cellae ITEM 18276`).
- Exact `data/raw/ncbi_type_material.tsv` scanning found 5 `culture-from-holotype` rows on lines 127727-127731, centered on CBS 145110, ITEM 18276, and P3.
- Exact StrainInfo side evidence was empty for `NCBITaxon:2819925`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2819925`.
- The native GOLD organism is fully accounted for by the generated GOLD aggregate row with `organism_count: 1`; its native projects do not add separate organism assertions.
- The record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

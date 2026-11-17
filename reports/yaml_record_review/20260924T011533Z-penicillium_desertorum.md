# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_desertorum.yaml`
- Taxon: `NCBITaxon:1303715` (`Penicillium desertorum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1303715`, label `Penicillium desertorum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_desertorum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_desertorum.yaml data/taxa/eukaryota/penicillium_diabolicalicense.yaml data/taxa/eukaryota/penicillium_digitatum.yaml data/taxa/eukaryota/penicillium_dipodomyicola.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59301` contains the seeded identifier with reason `attested rule: Penicillium desertorum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:308120` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:308120` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7430`, where `NCBITaxon:1303715` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:1303715`, centered on organism `Go0679370` / project `Gp0781358` (`Penicillium desertorum IBT 17660`).
- Exact `data/raw/ncbi_type_material.tsv` scanning found 13 rows on lines 21027-21039: 9 `culture-from-holotype` spellings centered on CBS 131543, DTO 148I6, and IBT 16321; and 4 `holotype` spellings centered on CBS H-21056.
- Exact StrainInfo side evidence was empty for `NCBITaxon:1303715`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1303715`.
- The native GOLD organism/project/analysis chain is fully accounted for by the single generated GOLD aggregate row with `organism_count: 1`.
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

# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_elizabethiae.yaml`
- Taxon: `NCBITaxon:3080683` (`Penicillium elizabethiae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:3080683`, label `Penicillium elizabethiae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_elizabethiae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_ehrlichii.yaml data/taxa/eukaryota/penicillium_eickeri.yaml data/taxa/eukaryota/penicillium_elizabethiae.yaml data/taxa/eukaryota/penicillium_euglaucum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:63545` contains the seeded identifier with reason `attested rule: Penicillium elizabethiae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:595695` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonyms `Penicillium echinatum E. Dale ex Biourge, 1923` and `Penicillium echinulatum Biourge, 1923`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:595695` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:31211`, where `NCBITaxon:3080683` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:3080683`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 22 rows on lines 165171-165192, all `culture-from-holotype` spellings centered on BCCM/MUCL 29170, CBS H-22052, DTO 189-B8, IBT 21955, MUCL 29170, and NRRL 917.
- Exact StrainInfo side evidence found one deposit for MUCL 29170 but no direct records for `NCBITaxon:3080683`.

## Completeness

- BacDive, generated StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:3080683`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

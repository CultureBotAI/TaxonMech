# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_decaturense.yaml`
- Taxon: `NCBITaxon:116971` (`Penicillium decaturense`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:116971`, label `Penicillium decaturense`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_decaturense.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_cyclopium.yaml data/taxa/eukaryota/penicillium_daleae.yaml data/taxa/eukaryota/penicillium_decaturense.yaml data/taxa/eukaryota/penicillium_decumbens.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53827` contains the seeded identifier with reason `attested rule: Penicillium decaturense, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:21640` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:21640` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3669`, where `NCBITaxon:116971` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:116971`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 2 rows on lines 11055-11056, both `culture-from-type-material` spellings centered on CBS 117509.
- Exact StrainInfo side evidence was empty for `NCBITaxon:116971`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID, merged-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:116971`.
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

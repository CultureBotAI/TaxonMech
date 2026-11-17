# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_flaviroseum.yaml`
- Taxon: `NCBITaxon:2072478` (`Penicillium flaviroseum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2072478`, label `Penicillium flaviroseum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_flaviroseum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_flaviroseum.yaml data/taxa/eukaryota/penicillium_formosanum.yaml data/taxa/eukaryota/penicillium_freii.yaml data/taxa/eukaryota/penicillium_fructuariae_cellae.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62248` contains the seeded identifier with reason `attested rule: Penicillium flaviroseum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:515679` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:515679` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:19790`, where `NCBITaxon:2072478` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2072478`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 7 rows on lines 82705-82711: 5 `culture-from-holotype` spellings centered on CBS 144479, CGMCC 3.18805, and NN072483; and 2 `holotype` spellings centered on HMAS 247727.
- Exact StrainInfo side evidence was empty for `NCBITaxon:2072478`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2072478`.
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

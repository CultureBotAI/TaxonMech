# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_dipodomyicola.yaml`
- Taxon: `NCBITaxon:254876` (`Penicillium dipodomyicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:254876`, label `Penicillium dipodomyicola`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_dipodomyicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_desertorum.yaml data/taxa/eukaryota/penicillium_diabolicalicense.yaml data/taxa/eukaryota/penicillium_digitatum.yaml data/taxa/eukaryota/penicillium_dipodomyicola.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54783` contains the seeded identifier with reason `attested rule: Penicillium dipodomyicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:51699` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium griseofulvum var. dipodomyicola`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:51699` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23187`, where `NCBITaxon:254876` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:254876`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 13 rows on lines 100800-100812: 9 `culture-from-holotype` spellings centered on CBS 173.87, IBT 21521, NRRL 13487, and NRRL A-27016; and 4 `holotype` spellings centered on IMI 296935.
- Exact StrainInfo side evidence has 7 direct `NCBITaxon:254876` records and 7 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:254876`.
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

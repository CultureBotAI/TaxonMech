# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_freii.yaml`
- Taxon: `NCBITaxon:48697` (`Penicillium freii`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:48697`, label `Penicillium freii`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_freii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_flaviroseum.yaml data/taxa/eukaryota/penicillium_formosanum.yaml data/taxa/eukaryota/penicillium_freii.yaml data/taxa/eukaryota/penicillium_fructuariae_cellae.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52783` contains the seeded identifier with reason `attested rule: Penicillium freii, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:6215` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:6215` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36930`, where `NCBITaxon:48697` has `organism_count` 2.
- The local native GOLD exact current-taxid scan found 2 organism rows, 2 project rows, and 2 analysis rows for `NCBITaxon:48697`, covering `Penicillium freii DAOM 242723` and `Penicillium freii IBT 34325`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 4 `type-material` rows on lines 221688-221691, centered on CBS 476.84 and IMI 285515.
- Exact StrainInfo side evidence has 28 direct `NCBITaxon:48697` records and 31 deposits across those records.
- Generated `data/straininfo/related_records.tsv.gz` contains 2 exact `NCBITaxon:48697` overlay rows for local strain `kgmicrobe.strain:bacdive_7970`, both matching CBS 630.66 to StrainInfo strain `319112` / deposit `471908`.

## Completeness

- BacDive exact rows, raw strain rows, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:48697`.
- The two native GOLD organisms are fully accounted for by the generated GOLD aggregate row with `organism_count: 2`.
- The two generated StrainInfo `related_records` rows are relation overlays only; no generated StrainInfo assemblies or raw strain inventory rows were present for `NCBITaxon:48697`, and the record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo assembly rows for this taxon.

## Additional Notes

- None.

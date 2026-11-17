# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fuscoglaucum.yaml`
- Taxon: `NCBITaxon:463681` (`Penicillium fuscoglaucum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:463681`, label `Penicillium fuscoglaucum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fuscoglaucum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fuscoglaucum.yaml data/taxa/eukaryota/penicillium_fuscum.yaml data/taxa/eukaryota/penicillium_gallaicum.yaml data/taxa/eukaryota/penicillium_glabrum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:55743` contains the seeded identifier with reason `attested rule: Penicillium fuscoglaucum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:103943` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:103943` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:36290`, where `NCBITaxon:463681` has `organism_count` 2.
- The local native GOLD exact current-taxid scan found 2 organism rows, 2 project rows, and 2 analysis rows for `NCBITaxon:463681`, covering `Penicillium fuscoglaucum VS AB I KN 5` and `Penicillium fuscoglaucum S/N-202-OC-P2`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 13 rows on lines 217507-217519: 2 `culture-from-isotype` spellings centered on CBS 261.29, 2 `isotype` spellings centered on CBS H-15446, and 9 `type-material` spellings centered on CBS 122423, IMI 092259, LSHB P81, MUCL 28651, and NRRL 892.
- Exact StrainInfo side evidence found one deposit for MUCL 28651 but no direct records for `NCBITaxon:463681`.

## Completeness

- BacDive, generated StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:463681`.
- The two native GOLD organisms are fully accounted for by the generated GOLD aggregate row with `organism_count: 2`.
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

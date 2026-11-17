# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_digitatum.yaml`
- Taxon: `NCBITaxon:36651` (`Penicillium digitatum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36651`, label `Penicillium digitatum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_digitatum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_desertorum.yaml data/taxa/eukaryota/penicillium_diabolicalicense.yaml data/taxa/eukaryota/penicillium_digitatum.yaml data/taxa/eukaryota/penicillium_dipodomyicola.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52346` contains the seeded identifier with reason `attested rule: Penicillium digitatum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4089` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Monilia digitata`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4089` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33431`, where `NCBITaxon:36651` has `organism_count` 2.
- The local native GOLD exact current-taxid scan found 2 organism rows, 2 project rows, and 2 analysis rows for `NCBITaxon:36651`, covering `Penicillium digitatum PdW03` and `Penicillium digitatum DSM 62840`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 8 rows on lines 194900-194907, all `culture-from-epitype` spellings under `Monilia digitata` centered on CBS 112082 and IBT 13068.
- Exact StrainInfo side evidence has 118 direct `NCBITaxon:36651` records and 181 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:36651`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.
- The two native GOLD organisms are fully accounted for by the generated GOLD aggregate row with `organism_count: 2`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

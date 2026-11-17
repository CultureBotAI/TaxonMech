# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fellutanum.yaml`
- Taxon: `NCBITaxon:70095` (`Penicillium fellutanum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:70095`, label `Penicillium fellutanum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fellutanum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_expansum.yaml data/taxa/eukaryota/penicillium_expansum_nrrl_62431.yaml data/taxa/eukaryota/penicillium_ezekielii.yaml data/taxa/eukaryota/penicillium_fellutanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53200` contains the seeded identifier with reason `attested rule: Penicillium fellutanum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9770` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9770` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41617`, where `NCBITaxon:70095` has `organism_count` 2.
- The local native GOLD exact current-taxid scan found 2 organism rows, 3 project rows, and 1 analysis row for `NCBITaxon:70095`, covering `Penicillium fellutanum ATCC 48694` and `Penicillium fellutanum ATCC 20841`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 2 `culture-from-neotype` rows on lines 258656-258657, centered on NRRL 746.
- Exact StrainInfo side evidence has 33 direct `NCBITaxon:70095` records and 67 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:70095`.
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

# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_flavigenum.yaml`
- Taxon: `NCBITaxon:254877` (`Penicillium flavigenum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:254877`, label `Penicillium flavigenum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_flavigenum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fennelliae.yaml data/taxa/eukaryota/penicillium_fimorum.yaml data/taxa/eukaryota/penicillium_fimosum.yaml data/taxa/eukaryota/penicillium_flavigenum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54784` contains the seeded identifier with reason `attested rule: Penicillium flavigenum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:51700` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:51700` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23188`, where `NCBITaxon:254877` has `organism_count` 2.
- The local native GOLD exact current-taxid scan found 2 organism rows, 3 project rows, and 1 analysis row for `NCBITaxon:254877`, covering `Penicillium flavigenum IBT 14082` and `Penicillium flavigenum ITEM 17421`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 9 rows on lines 100813-100821: 2 `culture-from-holotype` spellings centered on CBS 419.89 and 7 `type-material` spellings centered on IBT 21526, IBT 3091, IBT V1035, and IMI 293207.
- Exact StrainInfo side evidence has 12 direct `NCBITaxon:254877` records and 17 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:254877`.
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

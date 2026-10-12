# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_canescens.yaml`
- Taxon: `NCBITaxon:5083` (`Penicillium canescens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:5083`, label `Penicillium canescens`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_canescens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_burgense.yaml data/taxa/eukaryota/penicillium_bussumense.yaml data/taxa/eukaryota/penicillium_cairnsense.yaml data/taxa/eukaryota/penicillium_canescens.yaml` exited successfully for the four-file batch.

## Identity and Grounding

- `curation/seed_scope.tsv:51933` contains the seeded identifier with reason `attested rule: Penicillium canescens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2224` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2224` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:37458`, where `NCBITaxon:5083` has `organism_count` 7.
- The native GOLD exact current-taxid scan found seven organism rows, eight project rows, and seven analysis rows linked by `AP PROJECT GOLD IDS` for `NCBITaxon:5083`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-neotype spellings centered on `NRRL 910` and two neotype spellings centered on `CBS 300.48`.
- Exact StrainInfo side evidence has 62 direct `NCBITaxon:5083` records and 109 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:5083`.
- The sole merged-ID side row maps old `NCBITaxon:1771995` to current `NCBITaxon:5083`, and the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

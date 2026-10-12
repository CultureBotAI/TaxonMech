# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_decumbens.yaml`
- Taxon: `NCBITaxon:69771` (`Penicillium decumbens`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69771`, label `Penicillium decumbens`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_decumbens.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_cyclopium.yaml data/taxa/eukaryota/penicillium_daleae.yaml data/taxa/eukaryota/penicillium_decaturense.yaml data/taxa/eukaryota/penicillium_decumbens.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53181` contains the seeded identifier with reason `attested rule: Penicillium decumbens, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9668` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9668` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41539`, where `NCBITaxon:69771` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:69771`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 6 rows on lines 258089-258094, all `culture-from-neotype` spellings centered on CBS 230.81, FRR 741, and NRRL 741.
- Exact StrainInfo side evidence has 55 direct `NCBITaxon:69771` records and 104 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69771`.
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

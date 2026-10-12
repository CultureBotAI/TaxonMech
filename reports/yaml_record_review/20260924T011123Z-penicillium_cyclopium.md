# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_cyclopium.yaml`
- Taxon: `NCBITaxon:60167` (`Penicillium cyclopium`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:60167`, label `Penicillium cyclopium`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_cyclopium.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_cyclopium.yaml data/taxa/eukaryota/penicillium_daleae.yaml data/taxa/eukaryota/penicillium_decaturense.yaml data/taxa/eukaryota/penicillium_decumbens.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53011` contains the seeded identifier with reason `attested rule: Penicillium cyclopium, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:7579` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium verrucosum var. cyclopium`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:7579` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:39769`, where `NCBITaxon:60167` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:60167`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 10 rows on lines 240994-241003, all `culture-from-type-material` spellings centered on ATCC 8731, CBS 144.45, CECT 2264, DTO 163-I1, and NRRL 1888.
- Exact StrainInfo side evidence has 22 direct `NCBITaxon:60167` records and 47 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:60167`.
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

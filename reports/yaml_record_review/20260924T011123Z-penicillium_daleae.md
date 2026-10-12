# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_daleae.yaml`
- Taxon: `NCBITaxon:63821` (`Penicillium daleae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:63821`, label `Penicillium daleae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_daleae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_cyclopium.yaml data/taxa/eukaryota/penicillium_daleae.yaml data/taxa/eukaryota/penicillium_decaturense.yaml data/taxa/eukaryota/penicillium_decumbens.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53068` contains the seeded identifier with reason `attested rule: Penicillium daleae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8021` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium dalea`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8021` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40166`, where `NCBITaxon:63821` has `organism_count` 8.
- The local native GOLD exact current-taxid scan found 8 organism rows, 0 project rows, and 0 analysis rows for `NCBITaxon:63821`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 28 rows on lines 243570-243597: 6 isotype spellings centered on CBS 114839, CBS 114840, and CBS 115582; 2 neotype spellings centered on CBS 228.60; and 20 type-material spellings centered on ATCC 10435, CBS 211.28, DSM 2449, FRR 2025, IFO 6087, IFO 9072, IMI 034910, IMI 34910, MUCL 29234, and NRRL 2025.
- Exact StrainInfo side evidence has 34 direct `NCBITaxon:63821` records and 60 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:1177847` and `NCBITaxon:2022591` merged into current `NCBITaxon:63821`.

## Completeness

- BacDive, retained retired old-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:63821`.
- The two merged IDs are NCBI old-ID side evidence only: neither appeared as retained retired rows with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
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

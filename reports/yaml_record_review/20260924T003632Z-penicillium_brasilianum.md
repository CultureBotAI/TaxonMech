# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_brasilianum.yaml`
- Taxon: `NCBITaxon:104259` (`Penicillium brasilianum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:104259`, label `Penicillium brasilianum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_brasilianum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_bilaiae.yaml data/taxa/eukaryota/penicillium_boreae.yaml data/taxa/eukaryota/penicillium_brasilianum.yaml data/taxa/eukaryota/penicillium_brevicompactum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53675` contains the seeded identifier with reason `attested rule: Penicillium brasilianum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:18630` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, three related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:18630` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:616`, where `NCBITaxon:104259` has `organism_count` 2.
- The native GOLD exact current-taxid scan found two organism rows, two project rows, and two analysis rows linked by `AP PROJECT GOLD IDS` for `NCBITaxon:104259`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-holotype spellings centered on `CBS 253.55`, plus six type-material spellings centered on `ATCC 12072`, `FRR 3466`, and `QM 6947`.
- Exact StrainInfo side evidence has eight direct `NCBITaxon:104259` records and 23 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, and checked auxiliary source rows were empty for `NCBITaxon:104259`.
- Two merged-ID side rows map old IDs `NCBITaxon:1492127` and `NCBITaxon:557291` to current `NCBITaxon:104259`; the YAML correctly uses the current identifier.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

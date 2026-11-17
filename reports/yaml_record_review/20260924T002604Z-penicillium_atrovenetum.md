# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_atrovenetum.yaml`
- Taxon: `NCBITaxon:69764` (`Penicillium atrovenetum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69764`, label `Penicillium atrovenetum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_atrovenetum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_atrofulvum.yaml data/taxa/eukaryota/penicillium_atrolazulinum.yaml data/taxa/eukaryota/penicillium_atrosanguineum.yaml data/taxa/eukaryota/penicillium_atrovenetum.yaml` scanned the four-file batch and reported 4 scanned records, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53177` contains the seeded identifier with reason `attested rule: Penicillium atrovenetum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9664` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9664` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41535`, where `NCBITaxon:69764` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:69764`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found two culture-from-type-material spellings centered on `NRRL 2571` and two neotype spellings centered on `CBS 241.56`.
- Exact StrainInfo side evidence has three direct `NCBITaxon:69764` records and 12 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69764`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

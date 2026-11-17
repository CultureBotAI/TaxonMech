# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fennelliae.yaml`
- Taxon: `NCBITaxon:1167480` (`Penicillium fennelliae`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1167480`, label `Penicillium fennelliae`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fennelliae.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fennelliae.yaml data/taxa/eukaryota/penicillium_fimorum.yaml data/taxa/eukaryota/penicillium_fimosum.yaml data/taxa/eukaryota/penicillium_flavigenum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:58091` contains the seeded identifier with reason `attested rule: Penicillium fennelliae, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:257888` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:257888` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:3559`, where `NCBITaxon:1167480` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1167480`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 15 `type-material` rows on lines 10848-10862, centered on ATCC 22050, ATCC 52492, BCCM/IHEM 4389, CBS 711.68, FRR 521, IHEM 4389, IMI 151747, and MUCL 31322.
- Exact StrainInfo side evidence has 4 direct `NCBITaxon:1167480` records and 13 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1167480`.
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

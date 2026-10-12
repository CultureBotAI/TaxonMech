# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_egyptiacum.yaml`
- Taxon: `NCBITaxon:1303716` (`Penicillium egyptiacum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1303716`, label `Penicillium egyptiacum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_egyptiacum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_dunedinense.yaml data/taxa/eukaryota/penicillium_echinulatum.yaml data/taxa/eukaryota/penicillium_echinulonalgiovense.yaml data/taxa/eukaryota/penicillium_egyptiacum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:59302` contains the seeded identifier with reason `attested rule: Penicillium egyptiacum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:308121` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Eupenicillium egyptiacum`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:308121` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:7431`, where `NCBITaxon:1303716` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1303716`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 22 rows on lines 21040-21061: 2 `culture-from-neotype` spellings centered on CBS 244.32 and 20 `type-material` spellings centered on ATCC 10441, CSIR 707, FRR 2090, IBT 14684, IFO 6094, IFO 8141, IFO 8847, IMI 040580, NRRL 2090, and QM 1875.
- Exact StrainInfo side evidence has 5 direct `NCBITaxon:1303716` records and 17 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:36625` merged into current `NCBITaxon:1303716`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:1303716`.
- The merged ID is NCBI old-ID side evidence only: it did not appear as a retained retired row with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
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

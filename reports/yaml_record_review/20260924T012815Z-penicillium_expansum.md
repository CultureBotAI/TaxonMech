# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_expansum.yaml`
- Taxon: `NCBITaxon:27334` (`Penicillium expansum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:27334`, label `Penicillium expansum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_expansum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_expansum.yaml data/taxa/eukaryota/penicillium_expansum_nrrl_62431.yaml data/taxa/eukaryota/penicillium_ezekielii.yaml data/taxa/eukaryota/penicillium_fellutanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52157` contains the seeded identifier with reason `attested rule: Penicillium expansum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:2742` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Penicillium expansum Link, 1809`, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:2742` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:25478`, where `NCBITaxon:27334` has `organism_count` 10.
- The local native GOLD exact current-taxid scan found 10 organism rows, 24 project rows, and 8 analysis rows for `NCBITaxon:27334`; the 10 native organism rows correspond exactly to the transformed GOLD aggregate's `organism_count: 10`.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 5 `culture-from-neotype` rows on lines 115289-115293, centered on ATCC 7861, CBS 325.48, and CBS 32548.
- Exact StrainInfo side evidence has 207 direct `NCBITaxon:27334` records and 277 deposits across those records.
- Exact merged-ID scanning found retired `NCBITaxon:1112175` merged into current `NCBITaxon:27334`.

## Completeness

- BacDive, retained retired old-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:27334`.
- The GOLD assertion intentionally uses direct rows under this taxon only, matching the YAML note that descendant taxa are not gathered.
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

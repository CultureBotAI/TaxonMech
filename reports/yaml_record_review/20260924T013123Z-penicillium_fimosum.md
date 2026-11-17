# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_fimosum.yaml`
- Taxon: `NCBITaxon:2606547` (`Penicillium fimosum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:2606547`, label `Penicillium fimosum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_fimosum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fennelliae.yaml data/taxa/eukaryota/penicillium_fimorum.yaml data/taxa/eukaryota/penicillium_fimosum.yaml data/taxa/eukaryota/penicillium_flavigenum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:62895` contains the seeded identifier with reason `attested rule: Penicillium fimosum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:536259` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:536259` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:23986`, where `NCBITaxon:2606547` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:2606547`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 4 `culture-from-holotype` rows on lines 105426-105429, centered on CBS 142991 and FMR 15104.
- Exact StrainInfo side evidence was empty for `NCBITaxon:2606547`.
- Exact merged-ID scanning found retired `NCBITaxon:2015329` merged into current `NCBITaxon:2606547`.

## Completeness

- BacDive, StrainInfo, retained retired old-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:2606547`.
- The merged ID is NCBI old-ID side evidence only: it did not appear as a retained retired row with `retired_into` evidence requiring a generated `replaces` entry in the YAML.
- The record correctly has `strain_count: 0`.
- NCBI type-material rows are available side evidence only and do not imply generated strain inventory rows for this record.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

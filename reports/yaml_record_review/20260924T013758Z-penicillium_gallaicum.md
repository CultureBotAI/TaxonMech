# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_gallaicum.yaml`
- Taxon: `NCBITaxon:1131582` (`Penicillium gallaicum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:1131582`, label `Penicillium gallaicum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_gallaicum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_fuscoglaucum.yaml data/taxa/eukaryota/penicillium_fuscum.yaml data/taxa/eukaryota/penicillium_gallaicum.yaml data/taxa/eukaryota/penicillium_glabrum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:57834` contains the seeded identifier with reason `attested rule: Penicillium gallaicum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:245744` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:245744` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:2681`, where `NCBITaxon:1131582` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:1131582`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 2 `culture-from-isotype` rows on lines 8352-8353, centered on CBS 167.81.
- Exact StrainInfo side evidence found one deposit for ATCC 42232 but no direct records for `NCBITaxon:1131582`.

## Completeness

- BacDive, generated StrainInfo, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:1131582`.
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

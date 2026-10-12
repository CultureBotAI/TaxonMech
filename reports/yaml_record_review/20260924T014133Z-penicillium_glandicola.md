# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_glandicola.yaml`
- Taxon: `NCBITaxon:197659` (`Penicillium glandicola`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:197659`, label `Penicillium glandicola`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_glandicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_gladioli.yaml data/taxa/eukaryota/penicillium_glandicola.yaml data/taxa/eukaryota/penicillium_goetzii.yaml data/taxa/eukaryota/penicillium_gorlenkoanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:54439` contains the seeded identifier with reason `attested rule: Penicillium glandicola, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:39276` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Coremium glandicola`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:39276` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:18276`, where `NCBITaxon:197659` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:197659`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 2 `type-material` rows on lines 76033-76034 under `Coremium glandicola`, centered on CBS 498.75.
- Exact StrainInfo side evidence has 43 direct `NCBITaxon:197659` records and 65 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:197659`.
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

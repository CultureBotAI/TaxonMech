# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_cyaneum.yaml`
- Taxon: `NCBITaxon:69770` (`Penicillium cyaneum`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:69770`, label `Penicillium cyaneum`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_cyaneum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_crystallinum.yaml data/taxa/eukaryota/penicillium_curticaule.yaml data/taxa/eukaryota/penicillium_cvjetkovicii.yaml data/taxa/eukaryota/penicillium_cyaneum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53180` contains the seeded identifier with reason `attested rule: Penicillium cyaneum, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:9667` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, exact synonym `Citromyces cyaneus`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:9667` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:41538`, where `NCBITaxon:69770` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:69770`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found no rows for `NCBITaxon:69770`.
- Exact StrainInfo side evidence has 11 direct `NCBITaxon:69770` records and 25 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, and checked auxiliary source rows were empty for `NCBITaxon:69770`.
- Exact StrainInfo side evidence did not correspond to BacDive-derived local strain inventory rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

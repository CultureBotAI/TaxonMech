# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_curticaule.yaml`
- Taxon: `NCBITaxon:639300` (`Penicillium curticaule`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:639300`, label `Penicillium curticaule`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_curticaule.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_crystallinum.yaml data/taxa/eukaryota/penicillium_curticaule.yaml data/taxa/eukaryota/penicillium_cvjetkovicii.yaml data/taxa/eukaryota/penicillium_cyaneum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:56196` contains the seeded identifier with reason `attested rule: Penicillium curticaule, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:147333` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, two related synonyms, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:147333` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40180`, where `NCBITaxon:639300` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:639300`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found nine culture-from-holotype spellings centered on `CBS 135127`, `CV 2842`, `DAOM 241159`, and `DTO 180-D3`, plus three type-material spellings centered on `CV 188`.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, exact StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:639300`.
- With no BacDive or StrainInfo exact matches, there were no generated rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/raw/strain_*`; the record correctly has `strain_count: 0`.

## Findings

- No blocking, major, or minor findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes BacDive or StrainInfo rows for this taxon.

## Additional Notes

- None.

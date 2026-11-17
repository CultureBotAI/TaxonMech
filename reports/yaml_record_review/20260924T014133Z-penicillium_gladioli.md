# YAML Record Review

- Target: `data/taxa/eukaryota/penicillium_gladioli.yaml`
- Taxon: `NCBITaxon:36654` (`Penicillium gladioli`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:36654`, label `Penicillium gladioli`.
- It is grounded exactly under `NCBITaxon:5073` (`Penicillium`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 15 lineage entries from `root` through `Penicillium`.

## Validation

- `just validate data/taxa/eukaryota/penicillium_gladioli.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/penicillium_gladioli.yaml data/taxa/eukaryota/penicillium_glandicola.yaml data/taxa/eukaryota/penicillium_goetzii.yaml data/taxa/eukaryota/penicillium_gorlenkoanum.yaml` exited successfully for the four-file batch with zero error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:52349` contains the seeded identifier with reason `attested rule: Penicillium gladioli, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:4092` matches the YAML identity: parent `NCBITaxon:5073`, rank `SPECIES`, one related synonym, genetic code `1`, and the 2026-09-13 taxonomy snapshot.
- All 15 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:4092` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:33437`, where `NCBITaxon:36654` has `organism_count` 1.
- The local native GOLD exact current-taxid scan found no organism, project, or analysis rows for `NCBITaxon:36654`; the generated transformed GOLD aggregate is the only GOLD evidence table row for the YAML assertion.
- Exact `data/raw/ncbi_type_material.tsv` scanning found 4 rows on lines 194964-194967: 2 `culture-from-type-material` spellings centered on NRRL 939 and 2 `neotype` spellings centered on CBS 332.48.
- Exact StrainInfo side evidence has 8 direct `NCBITaxon:36654` records and 36 deposits across those records.

## Completeness

- BacDive, retained retired old-ID, merged-ID side inventory, generated StrainInfo, and checked auxiliary source rows were empty for `NCBITaxon:36654`.
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

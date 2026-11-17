# YAML Record Review

- Target: `data/taxa/eukaryota/mortierella_strangulata.yaml`
- Taxon: `NCBITaxon:64569` (`Mortierella strangulata`)
- Verdict: pass

## Target

- The record is the seeded species `NCBITaxon:64569`, label `Mortierella strangulata`.
- It is grounded exactly under `NCBITaxon:4855` (`Mortierella`) with rank `SPECIES`, domain `EUKARYOTA`, and genetic code `1`.
- The YAML carries 12 lineage entries from `root` through `Mortierella`.

## Validation

- `just validate data/taxa/eukaryota/mortierella_strangulata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/mortierella_sp.yaml ... mortierella_turficola.yaml` scanned the four-file batch and reported 0 files with errors and 0 total error rows.

## Identity and Grounding

- `curation/seed_scope.tsv:53096` contains the seeded identifier with reason `attested rule: Mortierella strangulata, 2 sources incl. NCBI`.
- `data/raw/ncbitaxon_taxa.tsv:8190` matches the YAML identity: parent `NCBITaxon:4855`, rank `SPECIES`, no exact synonyms, and related synonym `Mortierella strangulata Tiegh., 1875`.
- All 12 YAML lineage entries matched the NCBI lineage cache in the bounded scan, with no missing or mismatched ancestors.

## Evidence

- The NCBI source attestation matches `data/raw/ncbitaxon_taxa.tsv:8190` and the 2026-09-13 snapshot note.
- The GOLD source attestation is backed by `data/raw/gold_organisms.tsv:40340`, where `NCBITaxon:64569` has `organism_count` 2.
- Native GOLD has one exact current-taxid organism row, `Go0583313` / `Mortierella strangulata FSU 9849`, linked to project `Gp0586902`; no native analysis row linked to that project.
- `data/raw/ncbi_type_material.tsv:244468-244469` has `CBS 455.67` neotype aliases.

## Completeness

- Exact StrainInfo has two direct records and three deposit rows for `NCBITaxon:64569`, but no generated `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz` rows.
- BacDive exact rows, generated raw strain rows, and all checked auxiliary source rows were empty for `NCBITaxon:64569`.
- A complete ignored-file-inclusive `rg` scan of `data/raw/ncbi_merged_ids.tsv` found no rows for `NCBITaxon:64569`.
- The record has no `replaces` entries, which is consistent with the absence of local retired-ID provenance.

## Findings

- No blocking findings.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run the standard validators if any future curation materializes local strains from the StrainInfo exact-match side inventory.

## Additional Notes

- The transformed GOLD aggregate asserts two organisms, while the local native exact current-taxid scan currently exposes one organism JSONL row.
- `CBS 455.67` appears in NCBI type material, StrainInfo, and the native GOLD culture collection ID for `Mortierella strangulata FSU 9849`.
